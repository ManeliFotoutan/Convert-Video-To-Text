# Video to Text Converter using Flask

This project is a simple web application that converts video files into text using Flask, MoviePy, and the Google Web Speech API. It takes an uploaded video, extracts the audio, applies basic noise reduction, and then transcribes the speech in the video into text.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (>=3.6)
- Flask
- Flask-CORS
- MoviePy
- Pydub
- SpeechRecognition

You can install the required packages using pip:

pip install flask flask-cors moviepy pydub SpeechRecognition

Usage
Access the web application by opening your web browser and navigating to http://localhost:5000.

Click the "Choose File" button to upload a video file for conversion.

Once the video is uploaded, click the "Convert to Text" button.

The application will process the video, perform noise reduction, and transcribe the speech into text.

The resulting text will be displayed on the web page.

Configuration
You can configure the noise reduction level in the app.py file by adjusting the audio = audio - 20 line. Experiment with different values to optimize noise reduction for your videos.

Troubleshooting
If you encounter any issues or errors, please refer to the error messages displayed on the web page or in the terminal where the Flask application is running.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Flask
MoviePy
Pydub
SpeechRecognition
Feel free to customize this README to include additional information or instructions specific to your project.
