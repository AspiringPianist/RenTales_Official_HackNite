import shutil
import os
# Run this script from the parent directory i.e ..RenTales/
current_dir = os.path.abspath(os.getcwd())
renpath = f'{current_dir}/audio'
path_to_intermediate_scripts = f'{current_dir}/renpy_intermediate_scripts'
print(path_to_intermediate_scripts)
def copy_audio_files(src_path, dest_path):
    # Copy the entire source directory to the destination directory
    shutil.copytree(src_path, dest_path)
# Example usage
src_path = f'{current_dir}/audio_orig'
dest_path = f'{renpath}'
copy_audio_files(src_path, dest_path)