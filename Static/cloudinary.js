
var myWidget = cloudinary.createUploadWidget(
  {
    cloudName: 'dnw6jobbe',
    uploadPreset: '181898929544979',
    sources: ['local', 'url'],
    defaultSource: 'local',
    multiple: false,
    resourceType: 'auto',
    maxFileSize: 1024 * 1024, 
    maxImageWidth: 1000,
    maxImageHeight: 1000,
    uploadSignatureTimestamp: Math.round(Date.now() / 1000),
    uploadSignature: 'QgYpHWY7RBAuT3DjYrsst_lGZRQ',
  },
  function (error, result) {
    if (!error && result && result.event === 'success') {
      // Handle successful upload
      console.log('Upload success:', result.info);
    }
  }
);

document.getElementById('myFile').addEventListener('click', function () {
  myWidget.open();
}, false);
