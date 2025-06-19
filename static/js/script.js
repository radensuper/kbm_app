// C:\app\kbm_app\static\js\script.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript berhasil dimuat dan dijalankan!');

    // Contoh interaktivitas: alert saat mengklik header
    const header = document.querySelector('header');
    if (header) {
        header.addEventListener('click', function() {
            alert('Anda mengklik header!');
        });
    }

    // Contoh: Menampilkan pesan waktu
    const footer = document.querySelector('footer p');
    if (footer) {
        const currentYear = new Date().getFullYear();
        footer.textContent = `© ${currentYear} TMK| Aplikasi KBM. Allright Reserve. Versi 1.0.`;
    }
});