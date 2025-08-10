# Matrix Portfolio - Django Web Application

A modern, futuristic personal portfolio website built with Django, featuring a Matrix-inspired interface with smooth animations, responsive design, and a striking cyberpunk aesthetic.

![Matrix Portfolio](https://via.placeholder.com/800x400/000000/ff073d?text=Matrix+Portfolio)

## 🚀 Features

### 🎨 Design & UI
- **Matrix-themed Interface**: Dark background with neon red ("redium") accents
- **Animated Background**: Matrix rain effect with customizable characters
- **Smooth Animations**: Entrance effects, hover animations, and transitions
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern Typography**: N-dot style font (Space Mono) for authentic feel

### 📱 Sections
- **Home**: Animated hero section with call-to-action buttons
- **About**: Personal information, skills, and experience timeline
- **Projects**: Gallery with filtering, categories, and detailed views
- **Skills**: Interactive progress bars and categorized skill sets
- **Contact**: Functional contact form with Django backend
- **Blog**: Article listing and detailed blog post views

### ⚡ Functionality
- **Django Admin**: Full content management system
- **Email Integration**: Contact form sends notifications
- **Image Handling**: Project and blog post images with Pillow
- **SEO Optimized**: Proper meta tags and semantic HTML
- **Performance**: Optimized CSS/JS and lazy loading

## 🛠️ Tech Stack

### Backend
- **Django 5.2.4** - Web framework
- **Python 3.13+** - Programming language
- **SQLite** - Database (easily configurable to PostgreSQL/MySQL)
- **Pillow** - Image processing

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom Matrix styling + animations
- **JavaScript** - Interactive features and effects
- **Bootstrap 5.3.0** - Responsive grid system
- **Font Awesome 6.4.0** - Icons
- **AOS Library** - Scroll animations

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django pillow
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
portfolio/
├── portfolio_site/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/               # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # Class-based views
│   ├── forms.py            # Contact form
│   ├── admin.py            # Admin configuration
│   └── urls.py             # URL routing
├── templates/              # HTML templates
│   ├── base.html           # Base template with navigation
│   └── portfolio/          # App-specific templates
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Matrix-themed CSS
│   ├── js/
│   │   └── script.js       # Interactive JavaScript
│   └── images/             # Static images
├── media/                  # User uploads
├── venv/                   # Virtual environment
└── manage.py               # Django management script
```

## 🎯 Usage

### Content Management

1. **Access Admin Panel**
   - Navigate to `/admin/`
   - Login with superuser credentials

2. **Add Content**
   - **Site Configuration**: Basic site information and social links
   - **Projects**: Portfolio projects with images and descriptions
   - **Skills**: Technical skills with proficiency levels
   - **Blog Posts**: Articles with images and content
   - **Contact Messages**: View submitted contact forms

3. **Customize Design**
   - Edit `static/css/style.css` for styling changes
   - Modify `static/js/script.js` for interaction updates
   - Update templates in `templates/portfolio/` for layout changes

### Key Models

- **Project**: Portfolio projects with categories, technologies, and links
- **Skill**: Technical skills organized by categories with proficiency levels
- **BlogPost**: Blog articles with images, excerpts, and publication status
- **Contact**: Contact form submissions with read status
- **SiteConfiguration**: Global site settings and social media links

## 🎨 Customization

### Color Scheme
The Matrix theme uses CSS custom properties for easy customization:

```css
:root {
    --matrix-black: #000000;
    --matrix-red: #ff073d;          /* Primary accent color */
    --matrix-red-glow: #ff073d88;   /* Glow effects */
    --matrix-green: #00ff41;        /* Secondary accent */
    --matrix-white: #ffffff;
    --matrix-gray: #333333;
    --matrix-dark-gray: #1a1a1a;
}
```

### Typography
The portfolio uses Space Mono font for the authentic Matrix/terminal feel:

```css
--n-dot-font: 'Space Mono', monospace;
```

### Animations
Key animation classes for consistency:
- `.matrix-btn` - Animated buttons with hover effects
- `.skill-progress` - Animated progress bars
- `.project-card` - Hover animations for project cards
- Matrix rain background animation

## 🔧 Configuration

### Django Settings
Key settings in `portfolio_site/settings.py`:

- **Debug Mode**: Set `DEBUG = False` for production
- **Allowed Hosts**: Add your domain to `ALLOWED_HOSTS`
- **Static Files**: Configure `STATIC_ROOT` for production
- **Media Files**: Set up `MEDIA_ROOT` for file uploads
- **Email Backend**: Configure for contact form notifications

### Environment Variables
For production, use environment variables:

```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
```

## 📱 Responsive Design

The portfolio is fully responsive with breakpoints:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: < 768px

## 🚀 Deployment

### Prerequisites for Production
1. Set `DEBUG = False`
2. Configure `ALLOWED_HOSTS`
3. Set up static file serving
4. Configure database (PostgreSQL recommended)
5. Set up email backend for contact form

### Recommended Deployment Platforms
- **Heroku**: Easy deployment with Git integration
- **DigitalOcean**: App Platform or Droplets
- **AWS**: Elastic Beanstalk or EC2
- **PythonAnywhere**: Django-friendly hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- Portfolio: [Your Portfolio URL]
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Matrix movie franchise for design inspiration
- Django community for the excellent framework
- Font Awesome for the icon library
- AOS library for scroll animations
- Google Fonts for Space Mono typeface

## 📞 Support

If you have any questions or need help with setup, feel free to:
- Open an issue on GitHub
- Contact via the portfolio contact form
- Email directly at your.email@example.com

---

**Built with 💖 and lots of ☕ by [Your Name]**
