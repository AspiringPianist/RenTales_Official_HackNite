import shutil
import os
# Run this script from the parent directory i.e ..RenTales/
current_dir = os.path.abspath(os.getcwd())
current_dir = current_dir.replace('\\', '/')
#renpath = f'C:/Users/Prakrititz Borah/Downloads/RenTales_Official_HackNite-main/RenTales_Official_HackNite-main/story/game'
renpath = input('enter renpath: ').replace('\\', '/').replace('"', '')
path_to_intermediate_scripts = f'{current_dir}/renpy_intermediate_scripts'
print(path_to_intermediate_scripts)
def copy_audio_files(src_path, dest_path):
    # Copy the entire source directory to the destination directory
    shutil.copytree(src_path, dest_path)
for mood in ['positive', 'negative', 'neutral']:
    src_path = f'{current_dir}/audio/'+mood
    print(src_path)
    dest_path = f'{renpath}/audio/'+mood
    print(dest_path)
    copy_audio_files(src_path, dest_path)

# Example usage
# src_path = f'{current_dir}/audio_orig'
# dest_path = f'{renpath}'
