var fileInput = document.getElementById("file");
// listening on when someone selects a file
fileInput .onchange = function(e) {
  e.preventDefault();

  // get the file someone selected
  var file = fileInput.files && fileInput.files[0];

  // create an image element with that selected file
  var img = new Image();
  img.src = window.URL.createObjectURL(file);

  // as soon as the image has been loaded
  img.onload = function() {
    var width = img.naturalWidth,
      height = img.naturalHeight;

    // unload it
    window.URL.revokeObjectURL(img.src);

    // check its dimensions
    if (width <= 563 && height <= 751) {
      // it fits 
    } else {
      // it doesn't fit, unset the value 
      // post an error
      fileInput.value = ""
      alert("only 564x752 (3:4) images")
    }
  };
};