  const track = document.getElementById("image-track");
  // Set the initial percentage to -1 to make the images move towards the left by default
  track.dataset.percentage = -1;
  const velocity = 0.003;

  const handleOnDown = e => track.dataset.mouseDownAt = e.clientX;

  const handleOnUp = () => {
    track.dataset.mouseDownAt = "0";  
    track.dataset.d = track.dataset.percentage;
  }

  const handleOnMove = e => {
    if(track.dataset.mouseDownAt === "0") return;
    
    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
          maxDelta = window.innerWidth / 2;
    
    const percentage = (mouseDelta / maxDelta) * -100,
          nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
          // nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);
          nextPercentage = (nextPercentageUnconstrained%100);
          /*
            | | | | |  | | | | | | 
          */
    track.dataset.percentage = nextPercentage;
    
    track.animate({
      transform: `translate(${nextPercentage}%, -50%)`
    }, { duration: 1200, fill: "forwards" });
    
    for(const image of track.getElementsByClassName("image")) {
      image.animate({

        objectPosition: `${100 + nextPercentage}% center`
      }, { duration: 1200, fill: "forwards" });
    }
  }
  let index = 0,
      interval =1000;

  const rand = (min, max) => 
    Math.floor(Math.random() * (max - min + 1)) + min;

  const animate = star => {
    star.style.setProperty("--star-left", `${rand(-10, 100)}%`);
    star.style.setProperty("--star-top", `${rand(-40, 80)}%`);

    star.style.animation = "none";
    star.offsetHeight;
    star.style.animation = "";
  }

  for(const star of document.getElementsByClassName("magic-star")) {
    setTimeout(() => {
      animate(star);
      
      setInterval(() => animate(star), 1000);
    }, index++ * (interval / 3))
  }


  /* -- Had to add extra lines for touch events -- */

  window.onmousedown = e => handleOnDown(e);

  window.ontouchstart = e => handleOnDown(e.touches[0]);

  window.onmouseup = e => handleOnUp(e);

  // window.ontouchend = e => handleOnUp(e.touches[0]);

  window.onmousemove = e => handleOnMove(e);

  window.ontouchmove = e => handleOnMove(e.touches[0]);