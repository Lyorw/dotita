// Guardar el título original
var originalTitle = document.title;

// Cambiar el título cuando se pierde el foco de la pestaña
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        document.title = 'No te vayas 😢';
    } else {
        document.title = originalTitle; // Volver al título original
    }
});


// Toggle the menu visibility
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('show'); // Toggles the menu's visibility
});
