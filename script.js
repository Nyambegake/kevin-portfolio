document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fill = entry.target.querySelector('.fill');
                const targetWidth = entry.target.getAttribute('data-skill');
                fill.style.width = targetWidth + '%';
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.pillar').forEach(pillar => {
        observer.observe(pillar);
    });
});
