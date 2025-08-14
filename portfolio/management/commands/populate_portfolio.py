from django.core.management.base import BaseCommand
from portfolio.models import SiteConfiguration, Project, Skill, BlogPost
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Populate the portfolio with Bappy Tawhid\'s CV data'

    def handle(self, *args, **options):
        self.stdout.write('Populating portfolio with CV data...')
        
        # Create or update site configuration
        site_config, created = SiteConfiguration.objects.get_or_create(pk=1)
        
        # Always update the configuration with current data
        site_config.site_title = 'BAPPY  TAWHID'
        site_config.site_subtitle = 'Software Engineer & Data Analyst'
        site_config.hero_text = 'Welcome to the Matrix > Initializing...'
        site_config.about_text = '''I'm a results-driven Software Engineer and Data Analyst with expertise in designing, developing, and optimizing scalable web applications. 

🎓 Education:
• Bachelor of Science in Computer Science & Engineering
• Specialized in Software Engineering and Data Analytics

💻 Technical Stack:
• Languages: Java, Groovy, Python, JavaScript, C++, C#, R
• Frameworks: Spring Boot, Grails, Django, Bootstrap
• Databases: Oracle, MySQL, PostgreSQL
• Tools: Git, Docker, Jaspersoft Studio, REST APIs

🏢 Professional Experience:
• Senior Software Engineer at Walton Digi-Tech Industries Limited
• Developing enterprise-grade financial systems and ERP solutions
• Creating innovative solutions that automate business processes
• Leading cross-functional teams to deliver high-quality products

I'm passionate about building efficient, user-friendly solutions using modern technologies and best coding practices. Continuously learning and adapting to emerging trends to stay at the forefront of technological advancement.'''
        site_config.email = 'bappytawhid1999@gmail.com'
        site_config.github_url = 'https://github.com/bappytawhid'
        site_config.linkedin_url = 'https://linkedin.com/in/bapptytawhid'
        site_config.save()
        
        if created:
            self.stdout.write(self.style.SUCCESS('Site configuration created'))
        else:
            self.stdout.write(self.style.SUCCESS('Site configuration updated'))

        # Create projects
        projects_data = [
            {
                'title': 'PAI PAI POS System',
                'short_description': 'Enterprise POS and ERP platform for retail operations with complete inventory, sales, purchase, and accounts management.',
                'description': '''🏢 PAI PAI POS - Enterprise-Grade Retail Solution

A comprehensive Enterprise POS and ERP platform developed for Walton Digitech Ltd. This system revolutionizes retail operations by providing a unified solution for all business processes.

🚀 Key Features:
• Complete sales and purchase management with real-time processing
• Advanced inventory tracking and control with automated reorder points
• Subscription management for recurring revenue streams
• Internal requisitions system for streamlined operations
• Comprehensive accounting module with financial reporting
• Advanced MIS reporting and business intelligence
• Multi-location support with centralized management

💡 Technical Highlights:
• Built using modern enterprise architecture patterns
• Scalable microservices design for high availability
• Real-time data synchronization across all modules
• Advanced security with role-based access control
• Integration with external payment gateways and APIs

📊 Impact:
Processing thousands of transactions daily, this system serves as the backbone for Walton's retail operations, significantly improving operational efficiency and customer satisfaction.''',
                'category': 'web',
                'technologies': 'Spring Boot, Grails, Java, Groovy, Oracle Database, Jaspersoft Studio, REST APIs',
                'featured': True,
            },
            {
                'title': 'PAI PAI ERP System',
                'short_description': 'Complete Enterprise Resource Planning system with comprehensive business modules for finance, HR, manufacturing, and operations.',
                'description': '''🏭 PAI PAI ERP - Complete Enterprise Resource Planning Solution

A comprehensive Enterprise Resource Planning (ERP) system designed to manage all aspects of business operations from finance and HR to manufacturing and supply chain management.

🚀 Core Modules:
• Financial Management - General ledger, accounts payable/receivable, budgeting
• Human Resources - Employee management, payroll, attendance, performance tracking
• Manufacturing - Production planning, work orders, bill of materials, quality control
• Supply Chain - Procurement, vendor management, purchase orders, contracts
• Inventory Management - Stock control, warehouse management, asset tracking
• Customer Relationship Management - Lead tracking, sales pipeline, customer service
• Business Intelligence - Real-time dashboards, advanced analytics, custom reports

💡 Advanced Features:
• Multi-company and multi-currency support
• Workflow automation and approval processes
• Role-based security with granular permissions
• Integration with external systems via REST APIs
• Mobile-responsive interface for remote access
• Advanced reporting with drill-down capabilities
• Automated notifications and alerts

🔧 Technical Architecture:
• Microservices-based architecture for scalability
• Cloud-ready deployment with containerization
• Real-time data processing and synchronization
• Advanced caching for optimal performance
• Automated backup and disaster recovery
• RESTful API for third-party integrations

📊 Business Impact:
• Streamlined business processes across all departments
• Reduced operational costs by 35%
• Improved data accuracy and real-time visibility
• Enhanced decision-making with comprehensive analytics
• Increased productivity through automation''',
                'category': 'web',
                'technologies': 'Spring Boot, Grails, Java, Groovy, Oracle Database, Microservices, REST APIs, Business Intelligence',
                'featured': True,
            },
            {
                'title': 'Walton Digi Provident Fund System',
                'short_description': 'Autonomous financial management system with core banking integration for provident fund operations.',
                'description': '''💰 Provident Fund Management System

An autonomous accounting and fund management software designed to handle all core provident fund operations with seamless integration to banking systems.

🏦 Core Features:
• Automated provident fund calculations with multiple schemes
• Seamless core banking policy integration
• Comprehensive compliance management and audit trails
• Employee contribution tracking with detailed history
• Automated interest calculation and distribution
• Advanced reporting system with customizable reports
• Multi-branch support with centralized administration

🔧 Technical Architecture:
• Microservices architecture for scalability
• RESTful APIs for third-party integrations
• Automated backup and disaster recovery
• Real-time transaction processing
• Advanced security with encryption

✅ Business Impact:
• Eliminated manual calculation errors
• Reduced processing time by 80%
• Ensured 100% compliance with banking regulations
• Improved transparency in fund management''',
                'category': 'web',
                'technologies': 'Spring Boot, Grails, Java, Groovy, Oracle Database, REST APIs, Banking APIs',
                'featured': True,
            },
            {
                'title': 'Walton Profit Participation Fund System',
                'short_description': 'Automated profit distribution system with advanced financial processing and third-party integrations.',
                'description': '''📈 Profit Participation Fund System

A sophisticated profit distribution system that automates complex financial processes while ensuring compliance with company-specific policies and regulations.

💼 Key Capabilities:
• Automated profit calculation with configurable formulas
• Company-specific policy implementation and enforcement
• Real-time transaction validation and processing
• Comprehensive third-party system integration via REST APIs
• Advanced financial reporting with drill-down capabilities
• Complete audit trail and compliance tracking
• Role-based access control with approval workflows

🔐 Security & Compliance:
• End-to-end encryption for sensitive financial data
• Multi-level approval workflows
• Comprehensive audit logging
• Regulatory compliance reporting
• Data retention policies

⚡ Performance Benefits:
• Reduced manual processing delays from days to minutes
• Improved operational efficiency by 90%
• Enhanced transparency in profit distribution
• Automated validation prevents calculation errors''',
                'category': 'web',
                'technologies': 'Spring Boot, Grails, Java, Groovy, REST APIs, Oracle Database, Financial APIs',
                'featured': True,
            },
            {
                'title': 'Matrix Portfolio Website',
                'short_description': 'Modern Django-based portfolio with cyberpunk Matrix theme, animations, and responsive design.',
                'description': '''🌐 Matrix-Themed Portfolio Website

A futuristic personal portfolio website built with Django, featuring a Matrix-inspired cyberpunk interface with smooth animations and responsive design.

✨ Design Features:
• Matrix-themed UI with glowing green accents
• Animated background with Matrix rain effect
• Cyberpunk aesthetic with modern typography
• Smooth hover effects and transitions
• Responsive design for all devices
• Dark theme optimized for developer audience

🛠️ Technical Features:
• Django backend with class-based views
• SQLite database for content management
• Bootstrap 5 for responsive grid system
• Custom CSS animations and effects
• Contact form with server-side validation
• Admin panel for easy content updates
• SEO optimized structure and meta tags

📱 User Experience:
• Fast loading with optimized assets
• Intuitive navigation with smooth scrolling
• Interactive elements with visual feedback
• Mobile-first responsive design
• Accessibility features included''',
                'category': 'web',
                'technologies': 'Django, Python, HTML5, CSS3, JavaScript, Bootstrap, SQLite, FontAwesome',
                'featured': False,
            },
            {
                'title': 'Data Analytics Dashboard',
                'short_description': 'Interactive business intelligence dashboard with real-time data visualization and reporting.',
                'description': '''📊 Business Intelligence Dashboard

A comprehensive data analytics platform that transforms raw business data into actionable insights through interactive visualizations and real-time reporting.

📈 Analytics Features:
• Real-time data processing and visualization
• Interactive charts and graphs with drill-down capabilities
• Customizable dashboards for different user roles
• Automated report generation and scheduling
• Data export functionality in multiple formats
• Mobile-responsive design for on-the-go access

🔍 Data Sources:
• Integration with multiple databases
• API connections to external systems
• Real-time data streaming capabilities
• Historical data analysis and trending
• Predictive analytics using machine learning

🎯 Business Value:
• Improved decision-making with real-time insights
• Reduced time to generate reports by 75%
• Enhanced data accuracy and consistency
• Better understanding of business trends and patterns''',
                'category': 'ai',
                'technologies': 'Python, R, Pandas, Matplotlib, Plotly, Django, PostgreSQL, REST APIs',
                'featured': True,
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            # Always update the project with current data
            for key, value in project_data.items():
                setattr(project, key, value)
            project.save()
            
            if created:
                self.stdout.write(f'Created project: {project.title}')
            else:
                self.stdout.write(f'Updated project: {project.title}')

        # Create skills
        skills_data = [
            # Programming Languages
            {'name': 'Java', 'category': 'backend', 'proficiency': 90, 'icon_class': 'fab fa-java'},
            {'name': 'Groovy', 'category': 'backend', 'proficiency': 85, 'icon_class': 'fas fa-code'},
            {'name': 'Python', 'category': 'backend', 'proficiency': 80, 'icon_class': 'fab fa-python'},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 75, 'icon_class': 'fab fa-js'},
            {'name': 'C++', 'category': 'other', 'proficiency': 70, 'icon_class': 'fas fa-code'},
            {'name': 'C#', 'category': 'backend', 'proficiency': 65, 'icon_class': 'fas fa-code'},
            {'name': 'R', 'category': 'ai', 'proficiency': 75, 'icon_class': 'fab fa-r-project'},
            {'name': 'SQL', 'category': 'database', 'proficiency': 90, 'icon_class': 'fas fa-database'},
            
            # Frontend Technologies
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 90, 'icon_class': 'fab fa-html5'},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 85, 'icon_class': 'fab fa-css3-alt'},
            {'name': 'Bootstrap', 'category': 'frontend', 'proficiency': 80, 'icon_class': 'fab fa-bootstrap'},
            {'name': 'jQuery', 'category': 'frontend', 'proficiency': 75, 'icon_class': 'fas fa-code'},
            {'name': 'Responsive Design', 'category': 'frontend', 'proficiency': 85, 'icon_class': 'fas fa-mobile-alt'},
            
            # Backend Frameworks
            {'name': 'Spring Boot', 'category': 'backend', 'proficiency': 90, 'icon_class': 'fas fa-leaf'},
            {'name': 'Grails', 'category': 'backend', 'proficiency': 95, 'icon_class': 'fas fa-cogs'},
            {'name': 'Django', 'category': 'backend', 'proficiency': 75, 'icon_class': 'fab fa-python'},
            {'name': 'REST APIs', 'category': 'backend', 'proficiency': 90, 'icon_class': 'fas fa-exchange-alt'},
            {'name': 'Microservices', 'category': 'backend', 'proficiency': 80, 'icon_class': 'fas fa-cubes'},
            
            # Databases
            {'name': 'Oracle Database', 'category': 'database', 'proficiency': 90, 'icon_class': 'fas fa-database'},
            {'name': 'MySQL', 'category': 'database', 'proficiency': 80, 'icon_class': 'fas fa-database'},
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 75, 'icon_class': 'fas fa-database'},
            {'name': 'SQLite', 'category': 'database', 'proficiency': 80, 'icon_class': 'fas fa-database'},
            
            # DevOps & Tools
            {'name': 'Git', 'category': 'devops', 'proficiency': 85, 'icon_class': 'fab fa-git-alt'},
            {'name': 'GitHub', 'category': 'devops', 'proficiency': 85, 'icon_class': 'fab fa-github'},
            {'name': 'Docker', 'category': 'devops', 'proficiency': 70, 'icon_class': 'fab fa-docker'},
            {'name': 'Linux', 'category': 'devops', 'proficiency': 75, 'icon_class': 'fab fa-linux'},
            {'name': 'AWS', 'category': 'devops', 'proficiency': 65, 'icon_class': 'fab fa-aws'},
            
            # Data Analysis & AI
            {'name': 'Pandas', 'category': 'ai', 'proficiency': 80, 'icon_class': 'fas fa-chart-line'},
            {'name': 'NumPy', 'category': 'ai', 'proficiency': 75, 'icon_class': 'fas fa-calculator'},
            {'name': 'Matplotlib', 'category': 'ai', 'proficiency': 70, 'icon_class': 'fas fa-chart-bar'},
            {'name': 'Data Visualization', 'category': 'ai', 'proficiency': 80, 'icon_class': 'fas fa-chart-pie'},
            {'name': 'Machine Learning', 'category': 'ai', 'proficiency': 70, 'icon_class': 'fas fa-brain'},
            
            # Other Skills
            {'name': 'Jaspersoft Studio', 'category': 'other', 'proficiency': 85, 'icon_class': 'fas fa-chart-bar'},
            {'name': 'OOP', 'category': 'other', 'proficiency': 90, 'icon_class': 'fas fa-object-group'},
            {'name': 'Data Structures & Algorithms', 'category': 'other', 'proficiency': 80, 'icon_class': 'fas fa-sitemap'},
            {'name': 'Agile Methodology', 'category': 'other', 'proficiency': 85, 'icon_class': 'fas fa-sync-alt'},
            {'name': 'System Design', 'category': 'other', 'proficiency': 80, 'icon_class': 'fas fa-drafting-compass'},
            {'name': 'Financial Systems', 'category': 'other', 'proficiency': 90, 'icon_class': 'fas fa-dollar-sign'},
        ]

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            # Always update the skill with current data
            skill.category = skill_data['category']
            skill.proficiency = skill_data['proficiency']
            skill.icon_class = skill_data['icon_class']
            skill.save()
            
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
            else:
                self.stdout.write(f'Updated skill: {skill.name}')

        # Create sample blog posts
        blog_posts = [
            {
                'title': 'Building Enterprise-Grade Financial Systems with Spring Boot and Grails',
                'slug': 'building-enterprise-financial-systems-spring-boot-grails',
                'excerpt': 'A comprehensive guide to developing robust financial systems using Spring Boot and Grails framework, focusing on scalability, security, and compliance requirements in enterprise environments.',
                'content': '''# Building Enterprise-Grade Financial Systems

In my experience developing financial systems at Walton Digi-Tech Industries, I've learned that building enterprise-grade applications requires careful consideration of architecture, security, and scalability.

## 🏗️ System Architecture Principles

### 1. Security First Approach
- **Multi-layer Authentication**: Implement OAuth 2.0 with JWT tokens
- **Data Encryption**: AES-256 encryption for sensitive financial data
- **Audit Trails**: Complete logging of all financial transactions
- **Role-based Access**: Granular permissions for different user roles

### 2. Compliance and Regulatory Requirements
- **Financial Regulations**: Adherence to banking and financial compliance
- **Data Retention**: Automated backup and archival policies
- **Reporting Standards**: Standardized financial reporting formats
- **Audit Support**: Real-time audit trail generation

### 3. Scalability and Performance
- **Microservices Architecture**: Decomposed services for better scaling
- **Database Optimization**: Query optimization and connection pooling
- **Caching Strategies**: Redis for session management and data caching
- **Load Balancing**: Horizontal scaling with load distribution

## 🛠️ Technology Stack Deep Dive

### Backend Framework
```groovy
// Spring Boot Configuration
@SpringBootApplication
@EnableJpaRepositories
@EnableTransactionManagement
class FinancialSystemApplication {
    static void main(String[] args) {
        SpringApplication.run(FinancialSystemApplication, args)
    }
}
```

### Database Design
- **Oracle Database**: Primary database for ACID compliance
- **Connection Pooling**: HikariCP for optimal performance
- **Transaction Management**: Declarative transactions with Spring

### Integration Layer
- **REST APIs**: Standardized API design with proper versioning
- **Message Queues**: Asynchronous processing for heavy operations
- **Third-party Integration**: Secure API gateways for external systems

## 📊 Real-world Implementation Results

After implementing these principles in our financial systems:
- **99.9% Uptime**: Achieved through robust architecture
- **Sub-second Response**: Optimized queries and caching
- **Zero Data Loss**: Comprehensive backup and recovery strategies
- **100% Compliance**: Met all regulatory requirements

This approach has proven successful in processing thousands of daily transactions while maintaining the highest standards of security and reliability.''',
                'published': True,
            },
            {
                'title': 'Data Analytics in Enterprise Applications: From Raw Data to Business Insights',
                'slug': 'data-analytics-enterprise-applications-insights',
                'excerpt': 'Exploring how to implement effective data analytics solutions in enterprise environments, transforming raw business data into actionable insights for strategic decision-making.',
                'content': '''# Data Analytics in Enterprise Applications

In today's data-driven business environment, the ability to extract meaningful insights from raw data is crucial for competitive advantage. Here's how I've implemented analytics solutions in enterprise applications.

## 🎯 Strategic Approach to Data Analytics

### 1. Data Collection and Integration
- **Multiple Data Sources**: Integrating databases, APIs, and file systems
- **Real-time Streaming**: Live data processing for immediate insights
- **Data Quality**: Validation and cleansing processes
- **Historical Data**: Maintaining data lineage and versioning

### 2. Analytics Pipeline Architecture
```python
# Data Processing Pipeline Example
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

class DataAnalyticsPipeline:
    def __init__(self, db_connection):
        self.engine = create_engine(db_connection)
    
    def extract_data(self, query):
        return pd.read_sql(query, self.engine)
    
    def transform_data(self, df):
        # Data cleaning and transformation
        df['processed_date'] = pd.to_datetime(df['date'])
        return df.dropna()
    
    def generate_insights(self, df):
        # Business logic for insights
        return df.groupby('category').agg({
            'revenue': 'sum',
            'transactions': 'count'
        })
```

### 3. Visualization and Reporting
- **Interactive Dashboards**: Real-time business intelligence
- **Automated Reports**: Scheduled report generation
- **Mobile Analytics**: Responsive design for mobile access
- **Export Capabilities**: Multiple format support (PDF, Excel, CSV)

## 🔍 Implementation Case Studies

### Financial Performance Analytics
**Challenge**: Need for real-time financial performance tracking
**Solution**: 
- Created automated dashboard showing KPIs
- Implemented predictive analytics for revenue forecasting
- Developed exception reporting for anomaly detection

**Results**:
- 75% reduction in report generation time
- 90% improvement in decision-making speed
- 60% increase in data accuracy

### Customer Behavior Analytics
**Challenge**: Understanding customer patterns for business growth
**Solution**:
- Implemented customer segmentation algorithms
- Created behavior tracking and analysis
- Developed retention prediction models

## 📈 Best Practices and Lessons Learned

### Performance Optimization
- **Database Indexing**: Strategic index creation for faster queries
- **Data Partitioning**: Organizing large datasets efficiently
- **Caching Strategies**: Memory-based caching for frequently accessed data

### Security and Compliance
- **Data Privacy**: GDPR and privacy regulation compliance
- **Access Control**: Role-based data access permissions
- **Audit Logging**: Complete tracking of data access and modifications

The key to successful data analytics implementation is starting with clear business objectives and building a robust, scalable infrastructure that can grow with your organization's needs.''',
                'published': True,
            },
            {
                'title': 'Microservices Architecture: Lessons from Production Deployment',
                'slug': 'microservices-architecture-production-lessons',
                'excerpt': 'Real-world insights and practical lessons learned from implementing and maintaining microservices architecture in enterprise production environments.',
                'content': '''# Microservices Architecture: Production Lessons

The journey from monolithic to microservices architecture is complex but rewarding. Here are the practical lessons I've learned from implementing microservices in enterprise production environments.

## 🏗️ Architecture Evolution

### Starting Point: Monolithic Challenges
- **Deployment Bottlenecks**: Single point of failure during deployments
- **Technology Lock-in**: Difficulty adopting new technologies
- **Team Coordination**: Multiple teams working on same codebase
- **Scaling Limitations**: Unable to scale individual components

### Microservices Solution
```java
// Example Microservice Structure
@RestController
@RequestMapping("/api/v1/payments")
public class PaymentService {
    
    @Autowired
    private PaymentRepository paymentRepository;
    
    @PostMapping
    public ResponseEntity<Payment> processPayment(@RequestBody PaymentRequest request) {
        // Payment processing logic
        Payment payment = paymentService.process(request);
        return ResponseEntity.ok(payment);
    }
}
```

## 🛠️ Implementation Strategy

### 1. Service Decomposition
- **Domain-Driven Design**: Services aligned with business domains
- **Data Ownership**: Each service owns its data
- **API Contracts**: Well-defined interfaces between services
- **Autonomous Teams**: Independent development and deployment

### 2. Infrastructure Requirements
- **Service Discovery**: Consul/Eureka for service registration
- **Load Balancing**: Nginx/HAProxy for traffic distribution
- **API Gateway**: Centralized routing and cross-cutting concerns
- **Monitoring**: Distributed tracing and centralized logging

### 3. Communication Patterns
```groovy
// Asynchronous Communication Example
@EventListener
class OrderEventHandler {
    
    @Async
    void handleOrderCreated(OrderCreatedEvent event) {
        // Process order asynchronously
        inventoryService.reserveItems(event.orderItems)
        paymentService.processPayment(event.paymentInfo)
    }
}
```

## 🚀 Production Deployment Experience

### Challenges Encountered
1. **Data Consistency**: Implementing eventual consistency patterns
2. **Service Communication**: Managing network latency and failures
3. **Testing Complexity**: Integration testing across multiple services
4. **Operational Overhead**: Increased monitoring and maintenance

### Solutions Implemented
- **Circuit Breaker Pattern**: Hystrix for fault tolerance
- **Event Sourcing**: Maintaining data consistency across services
- **Contract Testing**: Pact for API contract verification
- **Centralized Logging**: ELK stack for distributed logging

## 📊 Results and Metrics

### Performance Improvements
- **Deployment Frequency**: From monthly to daily deployments
- **Time to Market**: 50% reduction in feature delivery time
- **System Reliability**: 99.9% uptime with isolated failures
- **Team Productivity**: 40% increase in development velocity

### Lessons Learned
1. **Start Small**: Begin with one service and gradually extract more
2. **Invest in Tooling**: Proper monitoring and deployment tools are essential
3. **Team Structure**: Organize teams around services, not technologies
4. **Cultural Change**: Microservices require organizational transformation

## 🔮 Future Considerations

- **Service Mesh**: Implementing Istio for advanced traffic management
- **Serverless Integration**: Hybrid approach with AWS Lambda
- **Kubernetes**: Container orchestration for better resource management

The key to successful microservices adoption is understanding that it's not just a technical transformation, but an organizational one that requires proper planning, tooling, and cultural change.''',
                'published': True,
            },
        ]

        for post_data in blog_posts:
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'Created blog post: {post.title}')
            else:
                self.stdout.write(f'Blog post already exists: {post.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated portfolio with CV data!')
        )
