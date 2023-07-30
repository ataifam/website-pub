
document.addEventListener("DOMContentLoaded", () => {
    if(document.getElementById("slideHolder") != null) mySlides()

    document.querySelectorAll(".interests").forEach(el => {
        el.onmouseover = (el) => {
            info(el.target.id)
            hoverPicture(el.target.id)
        }
        el.onmouseout = (el) => {
            info(el.target.id)
        }
    })

    window.onscroll = () => {
        if(document.querySelector("#bottom-content") != null) document.querySelector("#bottom-content").style.animationPlayState = "running"
    }
})

function hoverPicture(photoName) {
    let buttonImg = "https://adamswebserverbucket.s3.us-east-2.amazonaws.com/main/images/"+photoName+".png"
    document.getElementById("interest").src = buttonImg
}

const slidingPhotos = ["https://adamswebserverbucket.s3.us-east-2.amazonaws.com/main/images/aaphoto.jpg", "https://adamswebserverbucket.s3.us-east-2.amazonaws.com/main/images/awards.png", "https://adamswebserverbucket.s3.us-east-2.amazonaws.com/main/images/cephoto.jpg"]
var slidecenter = 1

function mySlides() {
    if (slidecenter == 3) slidecenter = 0
    document.getElementById("slideHolder").src = slidingPhotos[slidecenter++]
    setTimeout(() => mySlides(), 4000);
}

let infoTexts = {
    tech: 'Adam is consistently keeping up with new, emerging technologies through his participation in clubs at UMD.',
    wrestling: 'Adam wrestled for over 7 years, 4 of those on his high school\'s varsity team.',
    advocacy: 'In Adam\'s senior year of high school, he served on his county\'s public school student advisory council.',
    govt: 'Adam served as an intern for the County Executive. He built upon his soft skills while assisting with administrative processes.',
    dydx: 'Adam is pursuing a minor in Mathematics at the UMD.'
}

function info(currElement) {
    let documentObj = document.querySelector("#moreInfo").style
    let state = documentObj.visibility
    if (state == "visible" || state == "show") {
        document.querySelector(".infoText").style.opacity = 0
        documentObj.visibility = "hidden"
    }
    else {
        document.querySelector("#moreInfo").innerHTML = infoTexts[currElement]
        let element = document.getElementById("moreInfo").classList
        element.remove("infoText")
        void document.getElementById("moreInfo").offsetWidth
        element.add("infoText")
        document.querySelector(".infoText").style.opacity = 0
        documentObj.visibility = "visible"
        document.querySelector(".infoText").style.animationPlayState = "running"
    }
}
