# pip install requests
import requests
import base64
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module using relative import
from config.options import renpath, path_to_intermediate_scripts
class ImageGen: # Utilizes automatic1111's stable diffusion webui, and a customized checkpoint trained on pixel/anime images.
    def __init__(self, image_prompts, chars):
        self.image_prompts = image_prompts
        self.modifier = ", anime, background"
        self.char_modifier = ",anime, portrait, beautiful, white background"
        self.character_prompts = chars

    def request_and_save_image(self, prompt, steps, output_file, type):
        url = "http://127.0.0.1:7860/sdapi/v1/txt2img"  # Replace with your web UI URL

        if type==0:
            payload = {
                "prompt": prompt,
                "steps": steps,
                "negative_prompt" : 'foreground characters, realistic',
                "width" : 1024,
                "height": 576,
                "sampler_name" : "Euler a",
                "override_settings": {
                    "sd_model_checkpoint": "pixelstyleckpt_strength07.safetensors [11c2aa1997]",
                    "CLIP_stop_at_last_layers": 2,
                }
            }
        elif type==1:
            payload = {
                "prompt": prompt,
                "steps": steps,
                "negative_prompt" : 'unique instance',
                "width" : 256,
                "height": 256,
                "sampler_name" : "Euler a",
                "override_settings": {
                    "sd_model_checkpoint": "pixelstyleckpt_strength07.safetensors [11c2aa1997]",
                    "CLIP_stop_at_last_layers": 2,
                }
            }

        try:
            response = requests.post(url=f'{url}', json=payload)
            response.raise_for_status()  # Check if request was successful
            r = response.json()

            # Decode and save the image
            with open(output_file, 'wb') as f:
                f.write(base64.b64decode(r['images'][0]))

            print(f"Image saved as {output_file}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    # Example usage:
    # image_prompts = ["a bustling caffeteria filled with arroma of freshly baked bread and sizzling bacon", "bright-eyed students, bustling -hallways, endless possibilities awaited at school tomorrow", "teacher gradinng papers, a student asking for help, a principal walking down the hallway", "lady with huge tongue"]
    # for i in range(len(image_prompts)):
    #     request_and_save_image(image_prompts[i]+modifier, 50, f"bg{i}.png")

    def generate(self, type):
        if type == 0:
            for i in range(len(self.image_prompts)):
                print(f'Requesting background {i}')
                self.request_and_save_image(self.image_prompts[i] + self.modifier, 20, f'{renpath}/images/bg_{i}.png', 0)

        elif type == 1:
            for i in range(len(self.character_prompts)):
                print(f'Requesting character {i}')
                self.request_and_save_image(self.character_prompts[i] + self.char_modifier, 20, f'{renpath}/images/char_{i}.png', 1)
