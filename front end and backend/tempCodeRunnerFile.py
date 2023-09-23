import os
from flask import Flask, request, jsonify
import speech_recognition as sr
import moviepy.editor as mp
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return open('convertToText.html').read()

@app.route('/convert-video-to-text', methods=['POST'])
def convert_video_to_text():
    try:
        # Get the uploaded video file from the request
        uploaded_video = request.files['video']

        # Create a temporary directory to store the uploaded video and converted audio
        with tempfile.TemporaryDirectory() as temp_dir:
            video_temp_path = os.path.join(temp_dir, 'uploaded_video.mp4')
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

if __name__ == '__main__':
    app.run(debug=True)
