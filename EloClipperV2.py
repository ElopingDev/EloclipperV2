import ffmpeg
import subprocess

def userInput():
    start_time = input(f'Enter the start time (hh:mm:ss)\n')
    end_time = input(f'Enter the end time (hh:mm:ss)\n')
    crf_value = input(f'Enter the quality value (CRF), lower value means higher quality but larger file size and vice versa. (default: 23): ')

    if not crf_value:
        crf_value = 23  # Use default if no input
    else:
        crf_value = int(crf_value)

    return start_time, end_time, crf_value

def cut_video(input_file, output_file, start_time, end_time, crf_value):
    #very gay command construct
    export_command = [
        'ffmpeg', '-i', input_file,
        '-ss', start_time,
        '-to', end_time,
        '-c:v', 'libx264',
        '-crf', str(crf_value),
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

    start_time, end_time, crf_value = userInput()

    cut_video(input_file, output_file, start_time, end_time, crf_value)

if __name__ == '__main__':
    main()
