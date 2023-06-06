const menuAccess = document.querySelector(".menu-items")
const menuButton = document.querySelector('.mobile-menu')

menuButton.addEventListener('click', (event) => {
    menuAccess.classList.toggle("open")
})