# RenTales_Official_HackNite

![RenTales Logo](https://github.com/AspiringPianist/RenTales_Official_HackNite/blob/main/RenTales_logo.png)

## Track and Contributors
**Track**: Machine Learning  
**Contributors**: [Unnath Chittimalla](https://github.com/AspiringPianist), [Prakrititz Borah](https://github.com/SweetBunny123), and [Santhosh Vodnala](https://github.com/vodnalasanthosh47)

## Problem Statement
Explain the problem statement here.

## Features
- RenTales allows users to generate a fully fledged visual novel by inputting a single prompt or story idea.
- View generated visual novels on our website.
- Context-Aware music and scene generation based on mood predicted by the BERT model.
- Automatic generation of character and background images based on the script.
- Play the generated visual novel through Ren'Py.
- Use of automatic1111's stable diffusion model for anime-style images.
- User-friendly interface with dialogues, character images, and backgrounds.
- Models used: Llama2:7b (base story idea) and tuned Llama2:7b for human-readable scripts.
- Script parser for .rpy script conversion.
- No need for API_TOKEN; everything runs offline.
- User-friendly GUI with animated loading screen using pygame and tkinter.

## Tech Stack
- **IDE**: VSCode
- **Models**: Ollama, HuggingFace (transformers, accelerate)
- **Languages**: HTML, CSS, JavaScript, Python
- **Libraries**: rembg, requests, subprocess, os, pyGame, tkinter
- **Tools**: Nvidia CUDA, ngrok, renpy
- **Others**: Stable Diffusion (gradio by automatic1111), LangChain, Batch Files
- **Models**: Llama2, BERT, Stable Diffusion, rembg

## SetUp Instructions

Before you begin, ensure that you have the following prerequisites installed:

1. **Ren'Py:** You can download and install Ren'Py from [here](https://www.renpy.org/).

2. **Ollama:** Install Ollama from [here](https://ollama.com/download).

3. **Stable Diffusion:** 
   - Download Stable Diffusion Web UI from [here](https://github.com/AUTOMATIC1111/stable-diffusion-webui). Follow their instructions according to your GPU for installation.
   - After installing Stable Diffusion, copy and replace the two files from the Stable Diffusion config folder to the following path: `<path_to_stable_diffusion_installation>`. Replace the following files: `webui-user.sh`, `weui-user.bat`.

Once you have installed the prerequisites, follow these steps to run the system:

1. **Download Checkpoint for the Model:** 
   - Download the checkpoint for our Stable Diffusion model from [here](#) (provide the private link here).
   - Copy the downloaded file to the directory: `<path_to_stable_diffusion_installation>/webui/models/Stable-Diffusion`.

   
## How To Run

Before running the application, please follow these setup instructions:

1. **Watch Setup Video:**
   - You can follow the detailed setup instructions provided in our YouTube video [here](#).
   - Execution Guide - [here](https://drive.google.com/drive/folders/1qpPppVIIUma3lo8qwJSGwbsdhqbNbR8q?usp=sharing)

2. **Additional Resources:**
   - For more information and additional system requirements, visit our website [here](https://aspiringpianist.github.io/RenTales_Website) (insert link to the website).

3. **First Time Generating:**
   - Generating for the first time may take some time.

4. **Using the Application:**
   - If the home.py script is functioning correctly:
       1. Click on the "New Story" button to open a prompt window.
       2. Enter your prompt in the prompt window and click on the "Generate" button.
       3. The Pygame window may freeze during the generation process (you may close the Pygame window).
   
5. **Enter Ren'Py Path:**
   - Open Ren'Py and create a new project.
   - Navigate to your project settings:
     - Continue -> Enter your project name -> Change the resolution -> Custom -> Width = 1024, Height = 576
     - In the "Window" section, make sure the story name is highlighted.
     - Under "Open Directory," click on "Game" and copy the path of the game folder.
   - Paste the copied path when prompted.

6. **Monitoring Model State:**
   - After pasting the Ren'Py path, you can monitor the current state of the model in the terminal.

7. **Generation Time:**
   - Generating a story may take around 10 - 15 minutes on a GPU with at least 4GB VRAM.


    
4. **Start the Application:**
    - Launch Ren'Py and navigate to the project directory. Copy it's path of ../game folder.
    - Now, from the stable-diffusion folder, run webui.sh (linux and mac) or if on windows, run webui.bat (or run.bat in the parent folder)(This  will setup our image generation model ready for usage)
    - Navigate to the folder where you cloned this repo and execute the following commands 
    - python ./config./setup.py
    - python ./gui/home.py
    - Enter your prompt
    - The terminal will prompt you for the renpath, paste the path you copied earlier.
    - Sit back and relax for 10-15 minutes while your novel is generating!
  
## Applications

- Content Creation (YouTube Shorts)
- Entertainment
- Story Generation Assistance
- Inspiration for Visual Novel Game Developers (Economically)
- Immersive Teaching Experiences
- Storytelling Platforms

## Further Improvements

- Dynamic Character Expression Changes using Faster Image-to-Image Models
- Text-To-Speech Integration for Immersive Storytelling
- Theme Selection (Disney, Anime, Fantasy)
- Different Checkpoints for Different Art Styles and Music, with Different Story Generation Models Particularly for Each Genre (Horror, Comedy, Sci-Fi)


## Demo Videos
Links to [demo videos](https://drive.google.com/drive/folders/1iAEZLaPksLB9BPQew3vxZBeCaWcDnRlo?usp=drive_link) here.
