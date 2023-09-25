import os
from flask import Flask, request, jsonify
import speech_recognition as sr
import moviepy.editor as mp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return open('convertToText.html').read()

@app.route('/convert-video-to-text', methods=['POST'])
def convert_video_to_text():
    try:
        # Get the uploaded video file from the request
        uploaded_video = request.files['inpFile']

        # Specify the directory where you want to save the uploaded video file
        desktop_directory = 'C:\\Users\\User'  # Change this to your desired directory

        # Save the uploaded video to the selected directory
        video_path_on_desktop = os.path.join(desktop_directory, uploaded_video.filename)
        uploaded_video.save(video_path_on_desktop)

        # Generate a unique filename for the converted audio
        audio_filename = os.path.splitext(uploaded_video.filename)[0] + "_converted_audio.wav"
        audio_path = os.path.join(desktop_directory, audio_filename)

        # Convert video to audio using moviepy
        video = mp.VideoFileClip(video_path_on_desktop)
        audio = video.audio
        audio.write_audiofile(audio_path)

        # Initialize the speech recognition recognizer with PocketSphinx
        r = sr.Recognizer()
        r.energy_threshold = 4000  # Adjust the energy threshold as needed

        # Load the converted audio file
        audio_file = sr.AudioFile(audio_path)

        print("Converting audio to text...")

        # Recognize the speech in the audio file using PocketSphinx
        with audio_file as source:
            r.adjust_for_ambient_noise(source)
            audio_data = r.record(source)
            try:
                result = r.recognize_sphinx(audio_data)
                print("Conversion complete. Recognized text:", result)
                return jsonify({'result': result})
            except sr.UnknownValueError:
                print("PocketSphinx could not understand audio")
                return jsonify({'error': 'PocketSphinx could not understand audio'})
            except sr.RequestError as e:
                print("PocketSphinx error: {0}".format(e))
                return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
