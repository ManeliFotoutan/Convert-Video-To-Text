# Import necessary libraries
import os
from flask import Flask, request, jsonify
import speech_recognition as sr
import moviepy.editor as mp
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app

# Define the index route to serve your HTML page
@app.route('/')
def index():
    return open('convertToText.html').read()

# Define the route for converting video to text
@app.route('/convert-video-to-text', methods=['POST'])
def convert_video_to_text():
    try:
        # Get the uploaded video file from the request
        uploaded_video = request.files['inpFile']

        # Specify the first directory where you want to save the uploaded video file (e.g., desktop_directory)
        desktop_directory = 'C:\\Users\\User'
        video_path_on_desktop = os.path.join(desktop_directory, uploaded_video.filename)

        # Specify the second directory where you want to save the uploaded video file (e.g., desktop_directory2)
        desktop_directory2 = 'D:\\'

        # Specify the third directory as a fallback option (e.g., desktop_directory3)
        desktop_directory3 = 'F:\\'

        # Check if the first directory exists, if not, check the second directory, and then the third directory
        if not os.path.exists(desktop_directory):
            if not os.path.exists(desktop_directory2):
                desktop_directory = desktop_directory3
            else:
                desktop_directory = desktop_directory2

        # Save the uploaded video to the selected directory
        video_path_on_desktop = os.path.join(desktop_directory, uploaded_video.filename)
        uploaded_video.save(video_path_on_desktop)

        # Generate a unique filename for the converted audio
        audio_filename = os.path.splitext(uploaded_video.filename)[0] + "_converted_audio.wav"
        audio_path = os.path.join(desktop_directory, audio_filename)

        # Initialize the speech recognition recognizer
        r = sr.Recognizer()

        # Convert video to audio and recognize the speech in the audio
        with mp.VideoFileClip(video_path_on_desktop) as clip:
            audio = clip.audio.to_audiofile(audio_path)
            with sr.AudioFile(audio_path) as source:
                r.adjust_for_ambient_noise(source)
                audio_file = r.record(source)
                result = r.recognize_google(audio_file)

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
