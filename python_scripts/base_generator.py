import subprocess

path_to_intermediate_scripts = '../renpy_intermediate_scripts'

class StoryGen:

    def __init__(self, prompt):

        self.prompt = prompt
        self.cmd = 'Give me a title and proper synopsis for a story withot any cliffhangers and full ending about ' + self.prompt
        self.base = ''
        self.out = ''

    def generate_base(self):
        self.cmd = f'ollama run llama2 "{self.cmd}"'
        self.result = subprocess.run(self.cmd, shell=True, stdout= subprocess.PIPE).stdout.decode()
        self.result = self.result.replace('failed to get console mode for stdout: The handle is invalid.', "")
        with open(f'{path_to_intermediate_scripts}/base_story.txt', 'w') as f:
            f.write(self.result)
            f.close()
        print('written base story to base_story.txt!')

    def generate_story(self):
        with open(f'{path_to_intermediate_scripts}/base_story.txt', 'r') as file:
            lines = file.readlines()
            output = ''
            for line in lines:
                    line = line.strip()
                    output+=line
            file.close()
        print(output)
        cmd = f'ollama run story "For dialogues use this format (insert newline) Character : (mood) Dialogue (insert newline). For descriptions use this format (insert newline) (description) (insert newline). You can depict scenes in this way Scene Number - Scene Name. Note that here, Character, Dialogue, description  in the brackets and Scene Name are just placeholders for the actual content. Following the specified script format, generate a very long script of atleast 2000 words with this story - {output}."'
        completed_process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Decode the stdout and stderr outputs
        self.out = completed_process.stdout.decode('utf-8').replace('failed to get console mode for stdout: The handle is invalid.', '')
        stderr_text = completed_process.stderr.decode('utf-8')
        with open(f'{path_to_intermediate_scripts}/output.txt', 'w') as f:
            f.write(self.out+'\n(To be continued)\n')
            f.close()
        print('written story to output.txt!')
