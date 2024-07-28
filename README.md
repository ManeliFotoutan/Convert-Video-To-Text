# Video to Text Converter

This repository contains a Flask application that converts an uploaded video file to text by extracting its audio and using speech recognition.

## Features

- Upload a video file through the web interface.
- Convert the video's audio to text using Google's speech recognition.
- Handle multiple directories for saving the uploaded video and converted audio files.

## Requirements

- Python 3.x
- Flask
- moviepy
- SpeechRecognition

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/video-to-text-converter.git
    cd video-to-text-converter
    ```

2. Install the required packages:

    ```bash
    pip install flask moviepy SpeechRecognition
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8001`.

3. Upload a video file through the web interface.

4. The application will process the video, convert its audio to text, and display the transcribed text.

## Code Overview

The main application code is contained in `app.py`. 

- The root route (`/`) handles both GET and POST requests.
- When a video is uploaded, it checks for available directories to save the video file.
- The video is saved, its audio is extracted, and speech recognition is performed on the audio.
- The resulting text is displayed on a template (`video_to_text.html`).

## Directory Configuration

The application attempts to save the uploaded video file in the following directories:

1. `C:\Users\User`
2. `D:\`
3. `F:\`

If the first directory does not exist, it checks the second, and then the third.

## Portable Version
A portable version of the application is also available in a .rar archive. This version includes all necessary dependencies and can be used without installation. Extract the .rar file and run the application directly.


For any questions or issues, please open an issue on GitHub or contact me at maneli0foroutan@gmail.com.

