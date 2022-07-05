var videos = document.getElementsByClassName("project-video");
for (i = 0; i < videos.length; i++) {
    videos[i].addEventListener("click", function() {
    let defaultClass = "project-video";
    let fullscreenClass = "project-video-fullscreen";
    if (this.classList.contains(fullscreenClass)) {
            this.className = defaultClass;
    } else {
        this.className = fullscreenClass;
    }
    });
    videos[i].addEventListener("mouseover", function() {
        this.play();
    });
    videos[i].addEventListener("mouseout", function() {
        this.pause();
    });
}