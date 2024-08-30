# Video Clipper

This Python script is the second version of a previous program i made, but i unfortunately lost the source code.
This script provides an easy way to trim and cut videos using `ffmpeg`. You can specify the start and end times, as well as choose a quality preset to adjust the compression speed and output size.

## Features

- **User Input**: Easily input start and end times in `hh:mm:ss` format.
- **Quality Presets**: Choose from various `ffmpeg` quality presets, ranging from `ultrafast` to `veryslow`.
- **Cross-Platform**: Works on Windows, macOS, and Linux, as long as `ffmpeg` is installed.

## Requirements

- Python 3.x
- `ffmpeg` installed and accessible via the command line.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/video-cutter-utility.git
    cd video-cutter-utility
    ```

2. **Install Python Dependencies**:

    This script doesn't require any external Python libraries. Just make sure `ffmpeg` is installed on your system.

3. **Install `ffmpeg`**:

    - **Windows**: [Download `ffmpeg`](https://ffmpeg.org/download.html) and add it to your PATH or put it in the script's folder.
    - **macOS**: Use Homebrew:
      
      ```bash
      brew install ffmpeg
      ```
    - **Linux**: Install via your package manager, e.g., on Ubuntu:
      
      ```bash
      sudo apt-get install ffmpeg
      ```

## Usage

1. **Run the Script**:

    ```bash
    python EloclipperV2.py
    ```

2. **Input Details**:

    - Enter the path to the video file (you can drag and drop the file into the terminal).
    - Enter the output file name (must end with `.mp4`).
    - Specify the start and end times in `hh:mm:ss` format.
    - Choose a quality preset from the available options.

3. **Example**:

    ```plaintext
    Enter the path to the video you wanna cut. (You can also drag and drop the file here): "C:\Videos\input_video.mp4"
    
    Enter the output file name. (Must end with .mp4): "C:\Videos\output_video.mp4"
    
    Enter the start time (hh:mm:ss): 00:01:00
    Enter the end time (hh:mm:ss): 00:05:00
    
    Choose a quality preset :
    ['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow']
    
    Enter your selected quality preset: medium
    ```

    The script will trim the video and save the output file with the specified name.

## Script Details

### Functions

- **`userInput()`**:
  - Prompts the user to input start and end times and select a quality preset.
  - Validates the quality preset.

- **`cut_video(input_file, output_file, start_time, end_time, preset_choice)`**:
  - Constructs and runs the `ffmpeg` command to cut the video.
  - Handles errors during the process.

- **`main()`**:
  - Handles user input and cleans up file paths.
  - Calls the necessary functions to perform the video cut.


## Contributions

Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or create a pull request.

## Support

If you encounter any issues or have questions, feel free to [open an issue](https://github.com/ElopingDev/EloClipperV2/issues).

## Acknowledgements

- [FFmpeg](https://ffmpeg.org/) - The powerful multimedia framework used in this project.
