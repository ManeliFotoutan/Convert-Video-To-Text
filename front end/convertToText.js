const videoInput = document.getElementById('video-input');
const videoPlayer = document.getElementById('video-player');
const textOutput = document.getElementById('text-output');
const submitButton = document.getElementById('submit-button');
const startButton = document.getElementById('start-button');
const stopButton = document.getElementById('stop-button');

submitButton.addEventListener('click', convertVideoToText);

function convertVideoToText() {
  const file = videoInput.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const videoData = e.target.result;
      videoPlayer.src = videoData;

      videoPlayer.addEventListener('loadedmetadata', startSpeechRecognition);
    };

    reader.readAsDataURL(file);
  }
}
let recognition;

startButton.addEventListener('click', startSpeechRecognition);
stopButton.addEventListener('click', stopSpeechRecognition);

function startSpeechRecognition() {
  recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = 'en-US';

  recognition.onresult = function (event) {
    const transcript = event.results[event.results.length - 1][0].transcript;
    textOutput.textContent += transcript;
  };

  recognition.start();
}

function stopSpeechRecognition() {
  if (recognition) {
    recognition.stop();
  }
}
function startSpeechRecognition() {
  const track = videoPlayer.audioTracks[0];

  if (track) {
    const audioBlob = track.blobURL;
    const audio = new Audio(audioBlob);
    const recognition = new webkitSpeechRecognition() || new SpeechRecognition();

    recognition.lang = 'en-US'; // Set the language for speech recognition
    recognition.continuous = true; // Enable continuous listening

    recognition.onresult = function (event) {
      const transcript = event.results[event.results.length - 1][0].transcript;
      textOutput.textContent = transcript;
    };

    audio.addEventListener('ended', function () {
      recognition.stop();
    });

    audio.addEventListener('loadeddata', function () {
      recognition.start();
    });

    audio.addEventListener('error', function () {
      console.log('Error loading audio.');
    });

    audio.play()
      .catch(function (error) {
        console.log('Error playing audio:', error);
      });
  }
}