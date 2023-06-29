// Get all the thumbs-up icons
var thumbsUpIcons = document.querySelectorAll('.thumbs-up');

// Attach click event listeners to each thumbs-up icon
thumbsUpIcons.forEach(function(icon) {
  var likeCount = 0; // Initialize the like count

  // Create a separate element to display the like count
  var likeCountElement = document.createElement('span');
  likeCountElement.classList.add('like-count');
  likeCountElement.textContent = likeCount;

  // Append the like count element after the thumbs-up icon
  icon.parentNode.appendChild(likeCountElement);

  icon.addEventListener('click', function() {
    // Toggle the "liked" class on the clicked icon
    this.classList.toggle('liked');
    
    // Update the like count and display it
    if (this.classList.contains('liked')) {
      likeCount++;
    } else {
      likeCount--;
    }
    likeCountElement.textContent = likeCount;

    // Perform additional actions when the icon is liked or unliked
    if (this.classList.contains('liked')) {
      // Icon is liked
      console.log('Liked!');
      // Add your code here for handling the liked state
    } else {
      // Icon is unliked
      console.log('Unliked!');
      // Add your code here for handling the unliked state
    }
  });
});
