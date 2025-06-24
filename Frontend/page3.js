const uploadButton = document.querySelector('.upload-button');
const fileInput = document.getElementById('file-upload');

uploadButton.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (file) {
    alert(`Selected: ${file.name}`);
    // Add PDF to Word conversion logic here (backend or API integration)
  }
});
