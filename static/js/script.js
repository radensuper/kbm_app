// C:\app\kbm_app\static\js\script.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript untuk dashboard berhasil dimuat!');

    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.querySelector('.sidebar');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }
});