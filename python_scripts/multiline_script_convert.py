import random
INDENT = '    '
from sentiment_mood_analyze import SceneAnalyze

def rectify_name(name):
    return name.replace('.', '')
class Parser:
    def __init__(self):
        self.narrator_line = ''
        self.character = ''
        self.character_map = {}
        self.character_index = 0
        self.mood = None
        self.character_dialog = ''
        self.dialogue_continue = False
        self.scene_label = None
        self.narrator_continue = False
        self.char_pos = {}
        self.out = ''
        self.sceneAnalyze = SceneAnalyze()
        self.music = {'positive' : ['AshitakaSekki.mp3',
                    'Atownwithaviewofthesea.mp3',
                    'CastleintheSkyKimiwoNoseteCarryingYou.mp3',
                    'GoodbyeSummer.mp3',
                    'NameofLife.mp3',
                    'NausicaaRequiem.mp3',
                    'PrincessMononoke.mp3',
                    'SpiritedAwayOSTRepriseAgain.mp3'], 'neutral': ['AnimalCrossingNewHorizons.mp3',
                    'NintendoDSMusicStreetPassMiiPlazaTheme.mp3',
                    'NintendoMiiMaker.mp3',
                    'WiiSports.mp3'], 'negative':['EvangelionostLongSlowPain.mp3','ghost_hunt_doukutsu.mp3','ghost_hunt_fuon.mp3','HigurashiNoNakuKoroNiOSTKazashi.mp3','HigurashiNoNakuKoroNiOSTSenkou.mp3','HigurashiNoNakuKoroNiOSTShinjitsu.mp3','ShikiMiniOSTMementoMori.mp3',]}
        self.prev_mood = ''
        self.scene_description = []
        
    def read_script(self, path, output):
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('failed to get console mode for stdout: The handle is invalid.', '')
                line = line.strip()
                if '(insert newline)' in line:
                    line = line.replace('(insert newline)', "")
                if '(insert newline' in line:
                    line = line.replace('(insert newline', '')
                if 'insert newline)' in line:
                    line = line.replace('insert newline)', '')
                if 'insert newline' in line:
                    line = line.replace('insert newline', '')
                if self.is_dialog(line) and 'Narrator' not in line and 'Scene' not in line:
                    self.character, mood_dialog = line.split(':', 2)
                    self.character = rectify_name(self.character.strip())
                    if self.character:
                        self.char_cmd()
                    if '(' in mood_dialog and ')' in mood_dialog:
                        print(line)
                        self.mood, *remaining = mood_dialog.split(')', 2)
                        self.character_dialog = ''.join(remaining)
                        self.mood = self.mood[1:].strip()
                    else:
                        self.character_dialog = mood_dialog.strip()
                        self.mood = None
                    self.dialogue_continue = True
                    continue

                elif self.is_scene(line):
                    if(':' in line):
                        self.scene_label = line.split(':', 2)[1].replace(' ', '_')[1:]
                    elif('-' in line):
                        self.scene_label = line.split('-', 2)[1].replace(' ', '_')[1:]
                    self.scene_label = self.scene_label.replace('\'', '_')
                    self.scene_cmd()
                    self.scene_desc_needed = True

                elif self.is_narrator_line(line):
                    self.narrator_line = line.strip()[1:].strip('Narrator line:')
                    self.narrator_continue = True
                    continue

                if self.dialogue_continue:
                    if line:
                        self.character_dialog += ' ' + line.strip()
                        continue
                    elif not line:
                        self.dialog_cmd()
                        self.dialogue_continue = False
                        continue

                if self.narrator_continue:
                    if line.strip():
                        self.narrator_line += ' ' + line.strip()
                        while self.narrator_line.endswith(')'):
                            self.narrator_line = self.narrator_line[0:-1]
                        continue
                    else:
                        self.narrator_continue = False
                        if self.scene_desc_needed:
                            self.scene_description.append(self.narrator_line)
                            self.scene_desc_needed = False
                        self.narrate_cmd()
                        print('Analyzing Scene mood')
                        mood = self.sceneAnalyze.analyze_sentiment(self.narrator_line)
                        if mood!=self.prev_mood:
                            music = random.choice(self.music[mood])
                            self.out+=INDENT+f'play music "audio/{mood}/{music}" fadein 0.1 fadeout 0.1\n'
                        self.prev_mood = mood
                        continue
        with open(output, 'w') as file:
            file.write(self.out)

    def is_dialog(self, line):
        if ':' in line:
            return True
        return False
    def is_scene(self, line):
        if (':' in line or '-' in line) and 'Scene' in line:
            return True
        return False
    def is_narrator_line(self, line):
        if line.startswith('(') or 'Narrator' in line:
            return True
        return False
    def dialog_cmd(self):
        cmd = ''
        if 'Title' not in self.character or 'Synopsis' not in self.character:
            if self.mood:
                self.character_dialog = self.character_dialog.replace('"', '\'')
                cmd = INDENT + f'show {self.character_map[self.character]} at {self.char_pos[self.character_map[self.character]]} with dissolve\n'
                cmd += INDENT + f'{self.character_map[self.character]} "{self.mood}) {self.character_dialog}"'
            elif not self.mood and self.character!='Title' and self.character!='Synopsis':
                self.character_dialog = self.character_dialog.replace('"', '\'')
                cmd = INDENT + f'show {self.character_map[self.character]} at {self.char_pos[self.character_map[self.character]]} with dissolve\n'
                cmd += INDENT + f'{self.character_map[self.character]} "{self.character_dialog}"'
            self.out += cmd+'\n'
            #print(cmd)
            if self.character!='Title' and self.character!='Synopsis':
                self.out += INDENT + f'hide {self.character_map[self.character]}' +'\n'
                #print(INDENT + f'hide {self.character_map[self.character]}')
    def char_cmd(self):
        if 'Title' not in self.character and 'Synopsis' not in self.character and self.character not in self.character_map:
            self.character_map[self.character] = f'char_{self.character_index}'
            self.out += f'define char_{self.character_index} = Character(_("{self.character}"), color = "c8ffc8", image = "{self.character_map[self.character]}")'+'\n'
            #print(f'define char_{self.character_index} = Character(_("{self.character}"), color = "c8ffc8")')
            self.char_pos[self.character_map[self.character]] = 'left'
            if self.character_index % 2:
                self.char_pos[self.character_map[self.character]] = 'right'
            self.character_index += 1
    def scene_cmd(self):
        if self.scene_label:
            self.out += f'label {self.scene_label}:\n'
            #print(f'label {self.scene_label}:')
    def narrate_cmd(self):
        if self.narrator_line:
            self.narrator_line = self.narrator_line.replace('"', '\'')
            self.out += f'{INDENT}"{self.narrator_line}"\n'
            #print(f'{INDENT}"{self.narrator_line}"')

#Usage
# parser = Parser()
# path = 'output.txt'
# parser.read_script(path, 'script_test.rpy')
