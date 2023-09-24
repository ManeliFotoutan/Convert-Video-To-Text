# Import necessary libraries
import os
from flask import Flask, request, jsonify
import speech_recognition as sr
import moviepy.editor as mp
import tempfile
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

        # Create a temporary directory to store the uploaded video and converted audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            video_temp_path = temp_file.name
            uploaded_video.save(video_temp_path)

            # Convert video to audio and save it as a WAV file
            converted_audio_file_path = os.path.join(temp_dir, "converted_mp3.wav")
            clip = mp.VideoFileClip(video_temp_path)
            clip.audio.write_audiofile(converted_audio_file_path)

            # Initialize the speech recognition recognizer
            r = sr.Recognizer()

            # Load the converted audio file
            audio = sr.AudioFile(converted_audio_file_path)

            # Recognize the speech in the audio file
            with audio as source:
                r.adjust_for_ambient_noise(source)
                audio_file = r.record(source, duration=50)
                result = r.recognize_google(audio_file)

            return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
