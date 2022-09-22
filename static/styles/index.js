
let homeItems = document.getElementsByClassName("home")

// Home Page
homeItems[0].onclick = function() {
            window.location = "/"
}

// Recommendation page
homeItems[1].onclick = function() {
    window.location = "/recommend"
}

// About page
homeItems[2].onclick = function() {
    window.location = "/about"
}




