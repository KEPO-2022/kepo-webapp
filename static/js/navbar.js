const navMenu = document.querySelector("nav ul");
const icon2 = document.getElementById("icon");

function change(iconID) {
  if (document.getElementById(iconID).className == "fa fa-ellipsis-h") {
    document.getElementById(iconID).className = "fa fa-times";
  } else {
    document.getElementById(iconID).className = "fa fa-ellipsis-h";
  }
}

function showMenu() {
  navMenu.classList.toggle("responsive");
}
