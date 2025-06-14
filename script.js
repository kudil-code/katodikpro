// Tunggu DOM selesai loading
document.addEventListener('DOMContentLoaded', function() {
    // Load menu dari file JSON
    loadMenu();
    
    // Setup mobile menu toggle
    setupMobileMenu();
    
    // Setup contact form
    setupContactForm();
});

// Function untuk load menu dari menu.json
async function loadMenu() {
    try {
        // Fetch data menu dari file JSON
        const response = await fetch('menu.json');
        const menuData = await response.json();
        
        // Ambil semua element nav-menu di halaman
        const navMenus = document.querySelectorAll('.nav-menu');
        
        // Loop untuk setiap nav-menu
        navMenus.forEach(navMenu => {
            // Clear existing content
            navMenu.innerHTML = '';
            
            // Create menu items dari JSON data
            menuData.forEach(item => {
                // Buat element li
                const li = document.createElement('li');
                // Buat element a (link)
                const a = document.createElement('a');
                a.href = item.url; // Set URL dari JSON
                a.textContent = item.name; // Set text dari JSON
                
                // Tambahkan class active jika URL matches current page
                if (window.location.pathname.includes(item.url)) {
                    a.classList.add('active');
                }
                
                // Append a ke li, dan li ke nav-menu
                li.appendChild(a);
                navMenu.appendChild(li);
            });
        });
    } catch (error) {
        // Log error jika gagal load menu
        console.error('Error loading menu:', error);
        // Fallback menu jika JSON gagal load
        createFallbackMenu();
    }
}

// Function untuk create fallback menu jika JSON gagal
function createFallbackMenu() {
    // Default menu items
    const defaultMenu = [
        { name: 'Beranda', url: 'index.html' },
        { name: 'Produk', url: 'products.html' },
        { name: 'Studi Kasus', url: 'case_studies.html' },
        { name: 'Sumber Daya', url: 'resources.html' }
    ];
    
    // Ambil semua nav-menu elements
    const navMenus = document.querySelectorAll('.nav-menu');
    
    // Create menu dari default items
    navMenus.forEach(navMenu => {
        defaultMenu.forEach(item => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = item.url;
            a.textContent = item.name;
            li.appendChild(a);
            navMenu.appendChild(li);
        });
    });
}

// Function untuk setup mobile menu toggle
function setupMobileMenu() {
    // Ambil hamburger button dan nav menu
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    
    // Check jika elements exist
    if (hamburger && navMenu) {
        // Add click event listener ke hamburger
        hamburger.addEventListener('click', function() {
            // Toggle class 'active' pada nav menu
            navMenu.classList.toggle('active');
            
            // Animate hamburger icon
            this.classList.toggle('active');
        });
        
        // Close menu ketika click menu item di mobile
        const menuLinks = navMenu.querySelectorAll('a');
        menuLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Remove active class
                navMenu.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });
        
        // Close menu ketika click di luar menu
        document.addEventListener('click', function(event) {
            // Check jika click bukan di hamburger atau menu
            if (!hamburger.contains(event.target) && !navMenu.contains(event.target)) {
                // Remove active class
                navMenu.classList.remove('active');
                hamburger.classList.remove('active');
            }
        });
    }
}

// Function untuk setup contact form
function setupContactForm() {
    // Ambil contact form element
    const contactForm = document.getElementById('contactForm');
    
    // Check jika form exist
    if (contactForm) {
        // Add submit event listener
        contactForm.addEventListener('submit', function(e) {
            // Prevent default form submission
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            
            // Simulate form submission (dalam real app, kirim ke server)
            console.log('Form submitted with data:');
            for (let [key, value] of formData.entries()) {
                console.log(key + ': ' + value);
            }
            
            // Show success message
            alert('Terima kasih! Pesan Anda telah terkirim. Kami akan segera menghubungi Anda.');
            
            // Reset form
            this.reset();
        });
    }
}

// Function untuk smooth scroll (jika ada anchor links)
function setupSmoothScroll() {
    // Ambil semua links dengan hash
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            // Prevent default anchor click
            e.preventDefault();
            
            // Get target element
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            // Smooth scroll ke target
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Call smooth scroll setup
setupSmoothScroll();

// Function untuk animate elements saat scroll (optional enhancement)
function setupScrollAnimations() {
    // Elements yang akan di-animate
    const animateElements = document.querySelectorAll('.feature, .benefit, .case-study');
    
    // Intersection Observer untuk trigger animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Check jika element visible
            if (entry.isIntersecting) {
                // Add animation class
                entry.target.classList.add('animate-in');
                // Stop observing element yang sudah animated
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1, // Trigger ketika 10% visible
        rootMargin: '0px 0px -50px 0px' // Trigger sedikit sebelum element fully visible
    });
    
    // Observe each element
    animateElements.forEach(element => {
        observer.observe(element);
    });
}

// Call scroll animations setup
setupScrollAnimations();