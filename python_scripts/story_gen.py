import subprocess
import requests
import base64
from multiline_script_convert import Parser
from reorganize import ScriptWriter
from request import ImageGen
from base_generator import StoryGen
from pillow_bg import clear_bg
from ..config.options import renpath, path_to_intermediate_scripts

#prompt = input()
# Generating the base story and then building a human readable script
prompt = 'a script on the adventures of harry potter and his friends'
storygen = StoryGen(prompt)
storygen.generate_base()
storygen.generate_story()

# Parsing story to RenPy compatible format and analyzing mood for music simulatneously
parser = Parser()
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