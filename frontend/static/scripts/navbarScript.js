// Obtener los elementos de la barra de navegación
const navItems = document.querySelectorAll('nav a');

// Función para actualizar la clase "active" en la barra de navegación
function updateActiveNavItem() {
  // Obtener la URL actual
  const currentURL = window.location.href;
  
  // Iterar a través de cada enlace en la barra de navegación
  navItems.forEach((item) => {
    // Obtener la URL del enlace
    const url = item.getAttribute('href');
    
    // Comprobar si la URL del enlace está incluida en la URL actual
    if (currentURL.includes(url)) {
      // Quitar la clase "active" de todos los elementos
      navItems.forEach((item) => {
        item.parentElement.classList.remove('active');
      });

      // Agregar la clase "active" al elemento activo
      item.parentElement.classList.add('active');
    }
  });
}

// Llamar a la función para actualizar la clase "active" cuando se cargue la página
window.addEventListener('load', updateActiveNavItem);