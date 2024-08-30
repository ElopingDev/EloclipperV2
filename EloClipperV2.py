import ffmpeg
import subprocess

def userInput():
    start_time = input(f'Enter the start time (hh:mm:ss)\n')
    end_time = input(f'Enter the end time (hh:mm:ss)\n')
    presets = ['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow']

    print(f'Choose a quality preset :\n{presets}\n')
    preset_choice = input(f'Enter your selected quality preset\n')
    if preset_choice not in presets:
        raise ValueError("Invalid quality preset.\n")
    return start_time, end_time, preset_choice

def cut_video(input_file, output_file, start_time, end_time, preset_choice,):
    #very gay command construct
    export_command = [
        'ffmpeg', '-i', input_file,
        '-ss', start_time,
        '-to', end_time,
        '-c:v', 'libx264',
        '-preset', preset_choice,
        '-c:a', 'aac',
        output_file
    ]

    try:
        subprocess.run(export_command, check=True)
        print("Video successfully cut and saved.\n")
    except subprocess.CalledProcessError as e:
        print("An error occurred. Please report this.\n", e)

def main():
    input_file = input(r"Enter the path to the video you wanna cut. (You can also drag and drop the file here): ")
    print('\n')
    output_file = input(r"Enter the output file name. (Must end with .mp4): ")
    print('\n')


    # Clean up the input and output file paths cus its gay
    input_file = input_file.strip('"')
    output_file = output_file.strip('"')

    start_time, end_time, preset_choice = userInput()

    cut_video(input_file, output_file, start_time, end_time, preset_choice,)

if __name__ == '__main__':
    main()
