import subprocess
import re
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module using relative import
from config.options import renpath, path_to_intermediate_scripts
class ScriptWriter:
    def __init__(self, path, character_map, scene_description):
        self.path = path
        self.scenes = []
        self.out = ''
        self.bg_prompts = []
        self.bg_cmds = ''
        self.character_map = character_map
        self.char_prompts = []
        self.scene_description = scene_description

    def code(self):
        with open(self.path) as file:
            self.out += self.bg_cmds
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if 'define' in line:
                    #print(line)
                    self.out += (line+'\n')
        self.out += 'label start:\n'
        #print('label start:')
        with open(self.path) as file:
            i = 0
            lines = file.readlines()
            for line in lines:
                if 'label' in line:
                    self.out += line+'\n'+f'    show {self.scenes[i]} with dissolve\n'
                    i+=1
                if 'define' not in line and 'image' not in line and 'label' not in line:
                    #print(line)
                    self.out+=line+'\n'
        with open(renpath+'/script.rpy', 'w') as file:
            file.write(self.out)

    def scan_scenes(self):
        with open(self.path) as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if 'label' in line and 'start' not in line:
                    self.scenes.append(line[5:-1].strip())

    def generate_scenes(self):
        self.bg_cmds = ''
        print('scene_descriptions:')
        print(self.scene_description)
        n = len(self.scene_description)
        for i in range(n):
            if i > len(self.scenes)-1:
                break
            cmd = f'ollama run llama2 "Describe image of {self.scenes[i]}+{self.scene_description[i]} in twenty words at max for stable diffusion"'
            self.bg_prompts.append(subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode().replace('failed to get console mode for stdout: The handle is invalid.', ""))
                                                                                                                
        #Assume we have all images now from model like bg_0, bg_1 and all
        print('prompts: ')
        print(*self.bg_prompts)
        i = 0
        for scene in self.scenes:
            self.bg_cmds += f'image {scene} = "bg_{i}.png"\n'
            i+=1

    def generate_chars(self):
        self.char_cmds = ''
        print(self.character_map)
        for char in self.character_map:
            cmd = f'ollama run llama2 "Describe portrait image of character called {char} in twenty words at max for stable diffusion"'
            self.char_prompts.append(subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode().replace('failed to get console mode for stdout: The handle is invalid.', ""))
        print('char prompts:')
        print(*self.char_prompts)
        i = 0
        for char in self.character_map:
            self.char_cmds += f'image {self.character_map[char]} = "char_{i}.png"'
            i+=1

    def display_scenes(self):
        print(*self.scenes)


#Usage
# scriptwriter = ScriptWriter('script_test.rpy', 'final_test.rpy')
# scriptwriter.code()
# scriptwriter.display_scenes()
# scriptwriter.generate_scenes()
