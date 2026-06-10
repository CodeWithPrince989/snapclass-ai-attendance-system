document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Navigation on Scroll
    const navbar = document.querySelector('nav');
    
    const handleScroll = () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check once on load

    // 2. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Once it is revealed, we can unobserve to avoid repeat triggers
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1, // Trigger when 10% of the element is visible
        rootMargin: '0px 0px -50px 0px' // Trigger slightly before it hits viewport center
    });

    revealElements.forEach(element => {
        revealOnScroll.observe(element);
    });

    // 3. Staggered transition delay for grid items
    // Add staggered delays for features-grid, timeline, and tech-grid to make animations look organic
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.transitionDelay = `${index * 0.1}s`;
    });

    const techItems = document.querySelectorAll('.tech-item');
    techItems.forEach((item, index) => {
        item.style.transitionDelay = `${index * 0.05}s`;
    });

    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach((item, index) => {
        item.style.transitionDelay = `${index * 0.15}s`;
    });

    const statItems = document.querySelectorAll('.stat-item');
    statItems.forEach((item, index) => {
        item.style.transitionDelay = `${index * 0.1}s`;
    });
});
