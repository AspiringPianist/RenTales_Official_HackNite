import subprocess
import requests
import base64
from multiline_script_convert import Parser
from reorganize import ScriptWriter
from request import ImageGen
from base_generator import StoryGen
from pillow_bg import clear_bg
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module using relative import
from config.options import renpath, path_to_intermediate_scripts
#prompt = input()
# Generating the base story and then building a human readable script
prompt = ''
with open('./python_scripts/prompt.txt', 'r') as f:
    prompt = f.read()
print('prompt is: ', prompt)
storygen = StoryGen(prompt)
print('Generating Base Story..')
storygen.generate_base()
print('Generated Base Story!')
print('Now generating script..')
storygen.generate_story()
print('Generated script!!')

# Parsing story to RenPy compatible format and analyzing mood for music simulatneously
parser = Parser()
print('Parsing the script')
parser.read_script(f'{path_to_intermediate_scripts}/output.txt', f'{path_to_intermediate_scripts}/script2.rpy')
print(f'Written raw script to {path_to_intermediate_scripts}/script2.rpy')
# Reordering and syntax correction
scriptwriter = ScriptWriter(f'{path_to_intermediate_scripts}/script2.rpy',parser.character_map, parser.scene_description)
scriptwriter.scan_scenes()
scriptwriter.generate_scenes()
scriptwriter.generate_chars()
scriptwriter.code()
print(f'Written final script to {renpath}/script.rpy')

#Image Generation of Backgrounds and Characters
image_gen = ImageGen(scriptwriter.bg_prompts, scriptwriter.char_prompts)
image_gen.generate(0)
print('Backgrounds generated')
image_gen.generate(1)

# Background removal using rembg
for i in parser.character_map.values():
    clear_bg(f'{renpath}/images/{i}.png', f'{renpath}/images/{i}.png')
print('Characters generated')

# Game is Ready to Play
print('Game Ready to play!')
