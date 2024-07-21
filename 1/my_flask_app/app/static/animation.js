// GSAP Animations

// Background animation on load
document.addEventListener('DOMContentLoaded', function() {
    gsap.to('.background', { duration: 2, opacity: 1 });

    // Content animation on load
    gsap.from('.content', { duration: 1, y: 50, opacity: 0, ease: 'power1.out' });
});

// Button click animations
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', function() {
        gsap.fromTo(this, { scale: 1 }, { scale: 1.2, duration: 0.2, yoyo: true, repeat: 1, ease: 'power1.inOut' });
    });
});

// Background animation on clicks
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function() {
        gsap.to('.background', { duration: 1, backgroundColor: getRandomColor(), ease: 'power1.inOut' });
    });
});

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
