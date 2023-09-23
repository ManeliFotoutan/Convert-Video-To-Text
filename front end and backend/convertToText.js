const myForm = document.getElementById("video-form");
const inpFile = document.getElementById("video-input");

myForm.addEventListener("submit",e => {
  e.preventDefault();

  const endpoint = "http://localhost:8000/convert-video-to-text"; // Update with your Flask app's URL
  const formData = new FormData();

  console.log(inpFile.files);

  formData.append("inpFile",inpFile.files[0]);

  fetch(endpoint,{
    method:"post",
    body:formData
  })

  .then(response => response.json()) // Adjust as needed based on your server's response format
  .then(data => {
    // Handle the response data
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
});
