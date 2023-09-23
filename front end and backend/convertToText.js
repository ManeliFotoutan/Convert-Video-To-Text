
const videoInput = document.getElementById('video-input');
const videoPlayer = document.getElementById('video-player');
const textOutput = document.getElementById('text-output');
const videoForm = document.getElementById('video-form');
const submitAnchor = document.getElementById('submit-button'); // Update this line

submitAnchor.addEventListener('click', function (event) { // Update this line
  event.preventDefault(); // Prevent the default link behavior
  videoForm.submit();
});

videoForm.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  convertVideoToText();
});

function convertVideoToText() {
  const file = videoInput.files[0];

  if (file) {
    const formData = new FormData();
    formData.append('video-player', file);

    fetch('/convert-video-to-text', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      // Update the text output with the result
      textOutput.textContent = data.result;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
}

let recognition;

function startSpeechRecognition() {
  const track = videoPlayer.audioTracks[0];

  if (track) {
    const audioBlob = track.blobURL;
    const audio = new Audio(audioBlob);
    recognition = new webkitSpeechRecognition() || new SpeechRecognition();

    recognition.lang = 'en-US'; // Set the language for speech recognition
    recognition.continuous = true; // Enable continuous listening

    recognition.onresult = function (event) {
      const transcript = event.results[event.results.length - 1][0].transcript;
      textOutput.textContent = transcript;
    };

    audio.addEventListener('ended', function () {
      stopSpeechRecognition();
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

function stopSpeechRecognition() {
  if (recognition) {
    recognition.stop();
  }
}

videoForm.addEventListener('change', function () {
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
});
