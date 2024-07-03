# YouTube-Video-Transcriber

This Python script downloads a YouTube video, extracts its audio, and transcribes the audio to text. The transcribed text can be used for summaries, analysis, or any other purpose.

## Features

- Downloads audio from YouTube videos
- Converts audio to text using Google Speech Recognition
- Splits audio into manageable chunks for reliable transcription
- Exports transcribed text to a specified text file

## Requirements

- Python 3.6+
- `ffmpeg`
- For required libraries, see requirements.txt

## Installation

1. Clone the repository:
    ```sh
    git clone [https://github.com/yourusername/yourrepository.git](https://github.com/ilo-bst/YouTube-Video-Transcriber.git)
    cd YouTube-Video-Transcriber
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv yt-venv
    source yt-venv/bin/activate  # For macOS/Linux
    .\yt-venv\Scripts\activate  # For Windows
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure `ffmpeg` is installed on your system:
    ```sh
    brew install ffmpeg  # For macOS using Homebrew
    ```

## Usage

1. Run the script:
    ```sh
    python youtube_to_text.py
    ```

2. Follow the prompts to enter the YouTube video URL and the name for the output text file.

## License

This project is licensed under the MIT License.

## Acknowledgments

- This project uses the `pytube` library for downloading YouTube videos.
- Audio processing is done using `moviepy` and `pydub`.
- Transcription is handled by Google's Web Speech API through the `speechrecognition` library.


