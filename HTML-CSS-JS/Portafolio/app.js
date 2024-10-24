// Detectar el movimiento del cursor y scroll
let lastScrollPosition = 0;
const header = document.querySelector('.header');

window.addEventListener('scroll', function() {
    // Obtener la posición del scroll actual
    let currentScrollPosition = window.pageYOffset;

    // Si se hace scroll hacia abajo, ocultar el header
    if (currentScrollPosition > lastScrollPosition) {
        header.classList.add('hidden');
    } else {
        header.classList.remove('hidden');
    }

    // Actualizar la posición de scroll
    lastScrollPosition = currentScrollPosition;
});

// Obtener todos los puntos de la línea de tiempo
const timelinePoints = document.querySelectorAll('.timeline-point');

// Recorrer los puntos y agregar eventos hover y salida de cursor
timelinePoints.forEach(point => {
    point.addEventListener('mouseenter', () => {
        // Ocultar todas las secciones de información
        document.querySelectorAll('.timeline-info').forEach(info => {
            info.classList.remove('active');
        });
        
        // Mostrar la información correspondiente al punto
        const infoId = point.getAttribute('data-info');
        document.getElementById(infoId).classList.add('active');
    });

    // Evento para ocultar la información cuando el cursor sale del punto
    point.addEventListener('mouseleave', () => {
        const infoId = point.getAttribute('data-info');
        document.getElementById(infoId).classList.remove('active');
    });
});

// Detectar si el mouse se acerca al top de la pantalla
window.addEventListener('mousemove', function(event) {
    if (event.clientY < 50) { // Si el mouse está cerca del top de la ventana (ajusta los píxeles si es necesario)
        header.classList.remove('hidden');
    }
});



// Scroll suave al hacer clic en los enlaces de navegación
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

function filterProjects(category) {
    // Obtener todas las tarjetas de proyectos
    const cards = document.querySelectorAll('.project-card');

    // Si se selecciona "todos", mostrar todas las tarjetas
    if (category === 'all') {
        cards.forEach(card => card.style.display = 'block');
        return;
    }

    // Mostrar solo las tarjetas que coincidan con la categoría seleccionada
    cards.forEach(card => {
        if (card.classList.contains(category)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}