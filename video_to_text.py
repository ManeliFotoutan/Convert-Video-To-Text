from flask import Flask, request, render_template
import os
import moviepy.editor as mp
import speech_recognition as sr

app = Flask(__name__, template_folder='', static_url_path='', static_folder='')

@app.route('/', methods=['GET', 'POST'])
def convert_video_to_text():
    if request.method == 'POST':
        try:
            # Get the uploaded video file from the request
            uploaded_video = request.files['video']
            
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
                audio = clip.audio
                audio.write_audiofile(audio_path)
                with sr.AudioFile(audio_path) as source:
                    r.adjust_for_ambient_noise(source)
                    audio_file = r.record(source)
                    result = r.recognize_google(audio_file)

            return render_template('video_to_text.html', result=result)

        except Exception as e:
            return render_template('video_to_text.html', error=str(e))

    else:
        return render_template('video_to_text.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)
