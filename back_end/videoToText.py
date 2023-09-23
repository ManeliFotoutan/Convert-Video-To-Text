import speech_recognition as sr
import moviepy.editor as mp
import os

# Specify the file path to your video file
video_file_path = r"F:\cs50\convert video to text\Convert-Video-To-Text\FoxNews.mp4"

# Specify the directory where you want to save the files
output_directory = r"F:\cs50"

# Combine the directory path with the file names
converted_audio_file_path = os.path.join(output_directory, "converted_mp3.wav")
recognized_text_file_path = os.path.join(output_directory, "recognized_text_file.txt")

# Convert video to audio and save it as a WAV file
clip = mp.VideoFileClip(video_file_path)
clip.audio.write_audiofile(converted_audio_file_path)

# Initialize the speech recognition recognizer
r = sr.Recognizer()

# Load the converted audio file
audio = sr.AudioFile(converted_audio_file_path)

print("Converting audio to text...")

# Recognize the speech in the audio file
with audio as source:
    r.adjust_for_ambient_noise(source)
    audio_file = r.record(source, duration=50) 
result = r.recognize_google(audio_file)

# Write the recognized text to a text file in the specified directory
with open(recognized_text_file_path, mode='a') as file:
    file.write("Speech recognized\n")
    file.write(result)
    print("Conversion complete. Recognized text saved to", recognized_text_file_path)