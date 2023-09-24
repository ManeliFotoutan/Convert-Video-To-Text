const myForm = document.getElementById("video-form");
const inpFile = document.getElementById("video-input");
const resultDiv = document.getElementById("result");

myForm.addEventListener("submit", e => {
  e.preventDefault();

  const endpoint = "http://127.0.0.1:5000/convert-video-to-text";
  const formData = new FormData();

  formData.append("inpFile", inpFile.files[0]);

  fetch(endpoint, {
    method: "post",
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response data
      if (data.error) {
        resultDiv.textContent = "Error: " + data.error;
      } else if (data.result) {
        resultDiv.textContent = "Converted Text: " + data.result;
      } else {
        resultDiv.textContent = "No data received from the server.";
      }
    })
    .catch(error => {
      console.error(error);
      resultDiv.textContent = "An error occurred while communicating with the server.";
    });
});





//for vidio
// Get references to the video element and the form
const videoPlayer = document.getElementById('video-player');
const videoForm = document.getElementById('video-form');

// Add an event listener to the form for form submission
videoForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from actually submitting
    
    // Get the selected video file
    const videoInput = document.getElementById('video-input');
    const videoFile = videoInput.files[0];
    
    if (videoFile) {
        // Set the video source to the selected video file and play it
        videoPlayer.src = URL.createObjectURL(videoFile);
        videoPlayer.play();
    }
});
