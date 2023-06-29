
const trendingTopics = document.querySelectorAll(".trendingtopics li");

trendingTopics.forEach((topic) => {
  const topicText = topic.textContent.slice(1); 
  const imageUrl = `https://res.cloudinary.com/dowrygm9b/image/upload/${icebath}.jpg`;
  topic.style.backgroundImage = `url(${imageUrl})`;
});
