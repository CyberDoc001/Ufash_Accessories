# UFASH ACCESSORIES - POS & E-Commerce Platform

A professional, feature-rich Point of Sale (POS) and e-commerce platform for selling phone accessories, laptop accessories, and computer peripherals. Built with Django, Python, and PostgreSQL.

## 🎯 About UFASH ACCESSORIES

UFASH ACCESSORIES is a complete business management system specializing in:
- **Phone Accessories:** Power banks, chargers, cables, pouches
- **Laptop Accessories:** Chargers, skins, cooling pads, stands
- **Computer Peripherals:** Mouse, keyboards, USB hubs, flash drives
- **Storage Solutions:** Memory cards, flash drives

## ✨ Features

### Product Management
- Add, edit, and manage products with SKU tracking
- Organize products by categories
- Track pricing and quantities in real-time
- Product image support
- Minimum stock threshold configuration

### Product Search & Discovery
- Search products by name or SKU
- Filter by categories
- Fast and responsive search functionality
- Organized product display

### Shopping Cart & Checkout
- Add products to cart with quantity selection
- Real-time stock validation
- Seamless checkout process
- Cart management

### Sales & Transactions
- Complete checkout and transaction processing
- Automatic receipt generation
- Print-friendly receipt format
- Sales history tracking

### Sales Analytics & Reporting
- Daily sales reports with total revenue
- Filter by time period (Today, Week, Month, All Time)
- Track total items sold
- View detailed transaction history
- Daily sales dashboard

### Restock Management
- Automatic alerts when stock falls below minimum threshold
- Active alert management
- Resolve alerts when restocking is complete
- Alert status tracking
- Restock alert dashboard

### User Management
- User registration and authentication
- Secure login system
- User profiles
- Account management

### Professional UI/UX
- Bootstrap 5 responsive design
- Professional color scheme (Gold & Dark theme)
- Mobile-friendly interface
- Intuitive navigation

## 🛠️ Tech Stack

- **Backend:** Django 6.0.5
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Icons:** Bootstrap Icons

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ufash-accessories.git
cd ufash-accessories
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your configuration
nano .env
```

Update the following in `.env`:
- `DB_NAME`: Your PostgreSQL database name
- `DB_USER`: Your PostgreSQL username
- `DB_PASSWORD`: Your PostgreSQL password
- `SECRET_KEY`: A secure Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Your domain names

### 5. Setup PostgreSQL Database
```bash
# Create database and user
createdb ufash_db
createuser ufash_user -W

# Grant privileges
psql -d ufash_db -c "GRANT ALL PRIVILEGES ON DATABASE ufash_db TO ufash_user;"
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Load Sample Data (Optional)
```bash
python manage.py shell < load_sample_data.py
```

### 9. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 10. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 📁 Project Structure

```
ufash-accessories/
├── inventory/                 # Main app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── forms.py              # Django forms
│   ├── urls.py               # App URL routing
│   ├── admin.py              # Django admin config
│   └── migrations/           # Database migrations
├── pos_system/               # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project URL routing
│   ├── wsgi.py               # WSGI config
│   └── asgi.py               # ASGI config
├── templates/                # HTML templates
├── static/                   # CSS, JS, images
├── manage.py                 # Django management
└── requirements.txt          # Python dependencies
```

## 🔧 Configuration

### Database Setup (PostgreSQL)
- Install PostgreSQL
- Create database: `createdb ufash_db`
- Create user: `createuser ufash_user`
- Update `.env` with credentials

### Static Files
Static files are served from the `static/` directory. Collect them in production:
```bash
python manage.py collectstatic --noinput
```

## 📊 Admin Panel

Access the Django admin at `/admin/` with your superuser credentials to:
- Manage products and categories
- View sales transactions
- Manage restock alerts
- View user accounts

## 🔐 Security

- Never commit `.env` file (use `.env.example` instead)
- Always set `DEBUG=False` in production
- Use strong `SECRET_KEY`
- Keep dependencies updated
- Use environment variables for sensitive data

## 📝 Documentation

For detailed guides, see:
- [Authentication Guide](AUTHENTICATION_GUIDE.md)
- [Installation Guide](INSTALLATION.md)
- [PostgreSQL Setup](POSTGRESQL_SETUP.md)
- [Migration Guide](MIGRATION_GUIDE.md)
- [Architecture](ARCHITECTURE.txt)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💬 Support

For support, email support@ufashaccessories.com or open an issue in the repository.

## 👥 Authors

- **UFASH Team** - Initial work

## 🙏 Acknowledgments

- Bootstrap Framework
- Django Community
- PostgreSQL Documentation

---

**Last Updated:** June 2026
- Intuitive navigation

## Technology Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Language**: Python 3

## Installation & Setup

### 1. Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- pip package manager

### 2. Clone and Setup

```bash
# Navigate to project directory
cd "POS APP"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Database

Edit `pos_system/settings.py` to configure PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pos_system',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Access the application at: `http://localhost:8000`

Admin panel: `http://localhost:8000/admin`

## Project Structure

```
POS APP/
├── pos_system/              # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL configuration
│   └── wsgi.py             # WSGI application
├── inventory/              # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── forms.py            # Form definitions
│   ├── urls.py             # App URLs
│   ├── admin.py            # Admin configuration
│   └── migrations/         # Database migrations
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── inventory/          # App templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript
├── media/                  # User uploads
├── manage.py               # Django management
└── requirements.txt        # Python dependencies
```

## Database Models

### Category
- name (CharField)
- description (TextField)
- created_at, updated_at (DateTime)

### Product
- name (CharField)
- category (ForeignKey)
- sku (CharField - Unique)
- price (DecimalField)
- quantity (IntegerField)
- minimum_stock (IntegerField)
- description (TextField)
- is_active (BooleanField)

### Sale
- sale_date (DateField)
- sale_time (TimeField)
- total_amount (DecimalField)
- items_count (IntegerField)

### SaleItem
- sale (ForeignKey)
- product (ForeignKey)
- quantity (IntegerField)
- unit_price (DecimalField)
- subtotal (DecimalField)

### RestockAlert
- product (ForeignKey)
- status (CharField)
- current_stock (IntegerField)
- minimum_stock (IntegerField)
- created_at, resolved_at (DateTime)

## URL Mapping

| URL | Name | Description |
|-----|------|-------------|
| `/` | dashboard | Main dashboard |
| `/catalog/` | catalog | Product catalog with search |
| `/product/add/` | add_product | Add new product |
| `/product/<id>/edit/` | edit_product | Edit product |
| `/product/<id>/add-to-cart/` | add_to_cart | Add to shopping cart |
| `/cart/` | cart | Shopping cart view |
| `/cart/<id>/remove/` | remove_from_cart | Remove from cart |
| `/checkout/` | checkout | Process checkout |
| `/receipt/<id>/` | receipt | View receipt |
| `/sales-report/` | sales_report | Daily sales report |
| `/restock-alerts/` | restock_alerts | Active alerts |
| `/categories/` | categories | Manage categories |

## Usage Guide

### Adding a Product
1. Navigate to Dashboard → Add Product
2. Fill in product details (name, SKU, price, quantity)
3. Set minimum stock level for restock alerts
4. Click "Add Product"

### Making a Sale
1. Go to Catalog
2. Search or browse products
3. Select quantity and add to cart
4. Review cart and proceed to checkout
5. Complete checkout to generate receipt

### Managing Stock
1. Check Restock Alerts section for low stock items
2. Edit product to update quantity
3. Mark alerts as resolved after restocking

### Viewing Reports
1. Navigate to Sales Report
2. Select time period (Today, Week, Month, All Time)
3. View revenue and transaction details

## Professional Features

✓ **Database Integrity** - Foreign key constraints, data validation
✓ **Performance** - Database indexes on frequently searched fields
✓ **Security** - CSRF protection, input validation
✓ **Scalability** - Efficient queries with select_related/prefetch_related
✓ **Admin Panel** - Complete administrative interface
✓ **Responsive Design** - Mobile-friendly UI
✓ **Error Handling** - Comprehensive error messages

## Future Enhancements

- User authentication and roles
- Multi-store support
- Payment gateway integration
- Advanced analytics and reporting
- Barcode/QR code support
- Inventory export (CSV/PDF)
- Real-time notifications
- API endpoints for mobile apps

## Support

For issues or questions, please check the code comments or refer to Django documentation at https://docs.djangoproject.com

## License

This project is provided as-is for UFASH ACCESSORIES business use.

---

**Built with ❤️ using Django | UFASH ACCESSORIES - Premium Phone & Laptop Accessories Store**
