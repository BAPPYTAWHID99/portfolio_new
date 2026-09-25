// Modern Matrix Portfolio JavaScript

// Enhanced AOS initialization
AOS.init({
    duration: 1200,
    once: true,
    offset: 50,
    easing: 'ease-out-cubic'
});

// Enhanced Matrix Rain Effect
class MatrixRain {
    constructor() {
        this.canvas = document.getElementById('matrix-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン<>{}[]()';
        this.charArray = this.chars.split('');
        this.drops = [];
        this.fontSize = 16;
        this.colors = ['#00FF00', '#00ff41', '#00ffff'];
        
        this.init();
        this.animate();
        
        // Resize handler
        window.addEventListener('resize', () => this.init());
    }
    
    init() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        
        this.columns = Math.floor(this.canvas.width / this.fontSize);
        this.drops = [];
        
        for (let i = 0; i < this.columns; i++) {
            this.drops[i] = {
                y: Math.random() * -500,
                speed: Math.random() * 3 + 1,
                color: this.colors[Math.floor(Math.random() * this.colors.length)]
            };
        }
    }
    
    animate() {
        this.ctx.fillStyle = 'rgba(10, 10, 10, 0.08)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.ctx.font = this.fontSize + 'px monospace';
        
        for (let i = 0; i < this.drops.length; i++) {
            const drop = this.drops[i];
            const text = this.charArray[Math.floor(Math.random() * this.charArray.length)];
            
            // Gradient effect
            const gradient = this.ctx.createLinearGradient(0, drop.y - 20, 0, drop.y + 20);
            gradient.addColorStop(0, 'transparent');
            gradient.addColorStop(0.5, drop.color);
            gradient.addColorStop(1, 'transparent');
            
            this.ctx.fillStyle = gradient;
            this.ctx.fillText(text, i * this.fontSize, drop.y);
            
            drop.y += drop.speed;
            
            if (drop.y > this.canvas.height && Math.random() > 0.98) {
                drop.y = Math.random() * -100;
                drop.speed = Math.random() * 3 + 1;
                drop.color = this.colors[Math.floor(Math.random() * this.colors.length)];
            }
        }
        
        requestAnimationFrame(() => this.animate());
    }
}

// Enhanced Navigation Scroll Effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Smooth scrolling with easing
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Enhanced Project Filtering with Animations
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');
            
            // Update active button with animation
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.style.transform = 'scale(1)';
            });
            this.classList.add('active');
            this.style.transform = 'scale(1.1)';
            
            // Filter projects with stagger animation
            projectCards.forEach((card, index) => {
                setTimeout(() => {
                    if (filter === 'all' || card.getAttribute('data-category') === filter) {
                        card.style.display = 'block';
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(30px) scale(0.9)';
                        
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'translateY(0) scale(1)';
                        }, 50);
                    } else {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(-30px) scale(0.9)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                }, index * 100);
            });
        });
    });
}

// Enhanced Skill Bar Animations
function animateSkillBars() {
    const skillBars = document.querySelectorAll('.skill-progress');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    const bar = entry.target;
                    const percentage = bar.getAttribute('data-percentage');
                    bar.style.setProperty('--skill-width', percentage + '%');
                    bar.style.width = percentage + '%';
                    
                    // Add pulse effect
                    bar.style.animation = 'skillLoad 2s ease-out, pulse 2s infinite';
                }, index * 200);
            }
        });
    }, { threshold: 0.3 });
    
    skillBars.forEach(bar => observer.observe(bar));
}

// Enhanced Contact Form with Better UX
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        // Add input focus effects
        const inputs = contactForm.querySelectorAll('.matrix-input');
        inputs.forEach(input => {
            input.addEventListener('focus', function() {
                this.parentElement.style.transform = 'scale(1.02)';
            });
            
            input.addEventListener('blur', function() {
                this.parentElement.style.transform = 'scale(1)';
            });
        });
        
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Enhanced loading state
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Transmitting...';
            submitBtn.disabled = true;
            submitBtn.style.background = 'linear-gradient(45deg, #ffaa00, #ff6600)';
            
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showNotification('Message transmitted successfully! 🚀', 'success');
                    this.reset();
                    // Success animation
                    submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
                    submitBtn.style.background = 'linear-gradient(45deg, #00ff41, #00ffff)';
                } else {
                    showNotification('Transmission failed. Please retry. ⚠️', 'error');
                }
            })
            .catch(error => {
                showNotification('Network error. Please check connection. 🌐', 'error');
            })
            .finally(() => {
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.background = '';
                }, 2000);
            });
        });
    }
}

// Enhanced Notification System
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.matrix-notification');
    existingNotifications.forEach(notif => notif.remove());
    
    const notification = document.createElement('div');
    notification.className = `matrix-notification ${type}`;
    
    const iconMap = {
        success: 'fa-check-circle',
        error: 'fa-exclamation-triangle',
        info: 'fa-info-circle'
    };
    
    const colorMap = {
        success: ['#00ff41', 'rgba(0, 255, 65, 0.1)'],
        error: ['#ff073d', 'rgba(255, 7, 61, 0.1)'],
        info: ['#00ffff', 'rgba(0, 255, 255, 0.1)']
    };
    
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${iconMap[type]}"></i>
            <span>${message}</span>
            <button class="close-btn" onclick="this.parentElement.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;
    
    const [borderColor, bgColor] = colorMap[type];
    
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 30px;
        background: ${bgColor};
        backdrop-filter: blur(20px);
        border: 2px solid ${borderColor};
        color: ${borderColor};
        padding: 20px 25px;
        border-radius: 15px;
        z-index: 10000;
        font-family: var(--n-dot-font);
        font-size: 14px;
        box-shadow: 0 10px 30px ${borderColor}44;
        transform: translateX(400px);
        transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        max-width: 350px;
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove with warning animation
    setTimeout(() => {
        notification.style.borderColor = '#ffaa00';
        notification.style.animation = 'pulse 0.5s infinite';
    }, 4000);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => notification.remove(), 500);
    }, 5000);
}

// Enhanced Counter Animation with Easing
function animateCounters() {
    const counters = document.querySelectorAll('.counter');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    const counter = entry.target;
                    const target = parseInt(counter.getAttribute('data-target'));
                    const duration = 2000;
                    const startTime = Date.now();
                    
                    const updateCounter = () => {
                        const elapsed = Date.now() - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        
                        // Easing function (ease-out-cubic)
                        const easedProgress = 1 - Math.pow(1 - progress, 3);
                        const current = Math.floor(easedProgress * target);
                        
                        counter.textContent = current;
                        
                        if (progress < 1) {
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target;
                            // Add completion effect
                            counter.style.transform = 'scale(1.2)';
                            setTimeout(() => {
                                counter.style.transform = 'scale(1)';
                            }, 200);
                        }
                    };
                    
                    updateCounter();
                    observer.unobserve(counter);
                }, index * 300);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
}

// Enhanced Navigation Active State
function updateNavigation() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.matrix-nav-link');
    
    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop && pageYOffset < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').slice(1) === current) {
                link.classList.add('active');
            }
        });
    });
}

// Enhanced Parallax Effect
function initParallax() {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const rate = scrolled * -0.3;
        
        const matrixBg = document.querySelector('.matrix-bg');
        if (matrixBg) {
            matrixBg.style.transform = `translateY(${rate}px)`;
        }
        
        // Parallax for profile picture
        const profilePicture = document.querySelector('.profile-picture-container');
        if (profilePicture) {
            const profileRate = scrolled * 0.1;
            profilePicture.style.transform = `translateY(${profileRate}px)`;
        }
    });
}

// Enhanced Typing Effect with Better Spacing
document.addEventListener('DOMContentLoaded', function() {
    const typingElement = document.querySelector('.typing-text');
    if (typingElement) {
        const originalText = typingElement.textContent.trim();
        
        // Use original text without extra spacing to prevent overflow
        const spacedText = originalText;
        
        typingElement.textContent = '';
        typingElement.style.borderRight = 'none';
        
        let i = 0;
        function typeWriter() {
            if (i < spacedText.length) {
                typingElement.textContent += spacedText.charAt(i);
                i++;
                setTimeout(typeWriter, 100); // Slightly slower for better visibility
            } else {
                setTimeout(() => {
                    typingElement.style.borderRight = '3px solid var(--matrix-red)';
                    typingElement.style.animation = 'blink-caret 0.75s step-end infinite';
                }, 500);
            }
        }
        
        setTimeout(typeWriter, 1500);
    }
});

// Enhanced Download CV Function
function downloadCV() {
    const link = document.createElement('a');
    link.href = '/static/files/Bappy_Tawhid_CV.pdf';
    link.download = 'Bappy_Tawhid_CV.pdf';
    link.target = '_blank';
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    showNotification('CV download initiated! 📄✨', 'success');
}

function initWeatherWidget() {
    const weatherCard = document.querySelector('.weather-card');
    if (!weatherCard) return;

    const weatherCodes = {
        0: ['☀️', 'Clear sky'],
        1: ['🌤', 'Mostly clear'],
        2: ['⛅', 'Partly cloudy'],
        3: ['☁️', 'Overcast'],
        45: ['🌫', 'Foggy'],
        48: ['🌫', 'Rime fog'],
        51: ['🌦', 'Light drizzle'],
        53: ['🌦', 'Drizzle'],
        55: ['🌧', 'Heavy drizzle'],
        61: ['🌧', 'Light rain'],
        63: ['🌧', 'Rain'],
        65: ['🌧', 'Heavy rain'],
        71: ['🌨', 'Light snow'],
        73: ['🌨', 'Snow'],
        75: ['❄️', 'Heavy snow'],
        80: ['🌦', 'Rain showers'],
        81: ['🌦', 'Rain showers'],
        82: ['⛈', 'Heavy showers'],
        95: ['⛈', 'Thunderstorm'],
        96: ['⛈', 'Storm with hail'],
        99: ['⛈', 'Storm with hail']
    };

    const updateWeather = (weather) => {
        const [icon, weatherStatus] = weatherCodes[weather.weather_code] || ['🌤', 'Current weather'];
        weatherCard.querySelector('[data-weather-icon]').textContent = icon;
        weatherCard.querySelector('[data-weather-city]').textContent = 'Busan';
        weatherCard.querySelector('[data-weather-status]').textContent = `${weatherStatus} · Live data`;
        weatherCard.querySelector('[data-weather-temperature]').textContent = Math.round(weather.temperature_2m);
        weatherCard.querySelector('[data-weather-humidity]').textContent = `${weather.relative_humidity_2m}%`;
        weatherCard.querySelector('[data-weather-wind]').textContent = `${Math.round(weather.wind_speed_10m)} km/h`;
    };

    const url = 'https://api.open-meteo.com/v1/forecast' +
        '?latitude=35.1796' +
        '&longitude=129.0756' +
        '&current=temperature_2m,relative_humidity_2m,wind_speed_10m' +
        '&temperature_unit=celsius' +
        '&wind_speed_unit=kmh' +
        '&timezone=Asia%2FSeoul';

    fetch(url, { signal: AbortSignal.timeout(8000) })
        .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.json();
        })
        .then(data => {
            if (!data.current) throw new Error('Open-Meteo response has no current data');
            updateWeather(data.current);
        })
        .catch(error => {
            console.error('Weather API error:', error);
            weatherCard.querySelector('[data-weather-city]').textContent = 'Busan';
            weatherCard.querySelector('[data-weather-status]').textContent = 'Live data unavailable';
            weatherCard.querySelector('[data-weather-temperature]').textContent = '--';
            weatherCard.querySelector('[data-weather-humidity]').textContent = '--';
            weatherCard.querySelector('[data-weather-wind]').textContent = '--';
        });
}

// Initialize all enhanced functions
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Matrix Rain
    new MatrixRain();
    
    // Initialize all functions
    initProjectFilters();
    animateSkillBars();
    initContactForm();
    initParallax();
    animateCounters();
    initWeatherWidget();
    updateNavigation();
    
    // Add loading animation
    document.body.classList.add('loaded');
    
    // Add mouse cursor effect
    const cursor = document.createElement('div');
    cursor.className = 'cursor-trail';
    cursor.style.cssText = `
        position: fixed;
        width: 20px;
        height: 20px;
        background: radial-gradient(circle, var(--matrix-red), transparent);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        opacity: 0.7;
        transition: transform 0.1s ease;
    `;
    document.body.appendChild(cursor);
    
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX - 10 + 'px';
        cursor.style.top = e.clientY - 10 + 'px';
    });
});
