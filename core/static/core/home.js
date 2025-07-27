document.addEventListener('DOMContentLoaded', function() {
    console.log('🏠 Home page loaded successfully');

    // Initialize Bootstrap Carousel for hero banner
    const heroCarousel = document.getElementById('heroCarousel');
    if (heroCarousel) {
        new bootstrap.Carousel(heroCarousel, {
            interval: 5000,
            wrap: true,
            pause: 'hover'
        });
    }

    // Animate elements on scroll using IntersectionObserver
    const animateElements = document.querySelectorAll('[data-animate]');
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const element = entry.target;
                const animation = element.getAttribute('data-animate');
                element.classList.add('animate-' + animation);
                observer.unobserve(element);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    });

    animateElements.forEach(function(element) {
        observer.observe(element);
    });

    // Product card hover animations
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Category card hover animations
    const categoryCards = document.querySelectorAll('.category-card');
    categoryCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// Newsletter subscription simulation
function subscribeNewsletter(event) {
    event.preventDefault();

    const form = event.target;
    const email = form.querySelector('.newsletter-input').value;
    const button = form.querySelector('.newsletter-btn');

    if (!email) {
        showNotification('Please enter your email address', 'warning');
        return false;
    }

    // Save original button content
    const originalContent = button.innerHTML;

    // Show loading state
    button.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span> Subscribing...';
    button.disabled = true;

    // Simulate API call delay
    setTimeout(function() {
        // Show success state
        button.innerHTML = '<i class="bi bi-check-circle me-2"></i> Subscribed!';
        showNotification('Thank you for subscribing to our newsletter!', 'success');

        // Reset form input
        form.querySelector('.newsletter-input').value = '';

        // Reset button after 3 seconds
        setTimeout(function() {
            button.innerHTML = originalContent;
            button.disabled = false;
        }, 3000);
    }, 2000);

    return false;
}

// Helper function to show notifications (basic alert, replace with your custom UI)
function showNotification(message, type) {
    alert(message); // You can replace this with a modal or toast notification
}

// Add to cart button handler skeleton
document.querySelectorAll('.btn-add-to-cart').forEach(function(button) {
    button.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        if (productId) {
            // Your add to cart logic here — e.g., AJAX call or form submit
            console.log('Add to cart product ID:', productId);
            // For demo:
            alert('Product ' + productId + ' added to cart!');
        }
    });
});

// Wishlist button handler skeleton
document.querySelectorAll('.btn-wishlist').forEach(function(button) {
    button.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        if (productId) {
            // Your wishlist toggle logic here
            console.log('Toggle wishlist for product ID:', productId);
            alert('Wishlist toggled for product ' + productId);
        }
    });
});

// Compare button handler skeleton
document.querySelectorAll('.btn-compare').forEach(function(button) {
    button.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        if (productId) {
            // Your compare toggle logic here
            console.log('Toggle comparison for product ID:', productId);
            alert('Comparison toggled for product ' + productId);
        }
    });
});

console.log('✅ Home page JavaScript initialized successfully');
