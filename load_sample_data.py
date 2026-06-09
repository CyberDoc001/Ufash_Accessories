"""
UFASH ACCESSORIES - Sample data loader
Run: python manage.py shell < load_sample_data.py
"""

from inventory.models import Category, Product
from decimal import Decimal

# Clear existing data
Category.objects.all().delete()
Product.objects.all().delete()

# Create Categories
categories_data = [
    {'name': 'Power Banks', 'description': 'High-capacity portable power banks for all devices'},
    {'name': 'Chargers', 'description': 'Quality fast chargers for phones and laptops'},
    {'name': 'Cables & Cords', 'description': 'Durable charging and data cables'},
    {'name': 'Pouches & Cases', 'description': 'Protective pouches and carrying cases'},
    {'name': 'Laptop Accessories', 'description': 'Laptop chargers, skins, and cooling pads'},
    {'name': 'Computer Peripherals', 'description': 'Mouse, keyboards, and USB devices'},
    {'name': 'Storage Devices', 'description': 'Flash drives and memory cards'},
]

categories = {}
for cat_data in categories_data:
    category = Category.objects.create(**cat_data)
    categories[cat_data['name']] = category
    print(f"Created category: {cat_data['name']}")

# Create Products for UFASH ACCESSORIES
products_data = [
    # Power Banks
    {
        'name': '20000mAh Power Bank',
        'category': 'Power Banks',
        'sku': 'PB-20K-001',
        'price': Decimal('1299.99'),
        'quantity': 45,
        'minimum_stock': 10,
        'description': 'Ultra-fast charging 20000mAh power bank with dual USB ports'
    },
    {
        'name': '10000mAh Compact Power Bank',
        'category': 'Power Banks',
        'sku': 'PB-10K-001',
        'price': Decimal('699.99'),
        'quantity': 60,
        'minimum_stock': 15,
        'description': 'Slim and portable 10000mAh power bank'
    },
    {
        'name': '30000mAh Heavy Duty Power Bank',
        'category': 'Power Banks',
        'sku': 'PB-30K-001',
        'price': Decimal('1999.99'),
        'quantity': 30,
        'minimum_stock': 8,
        'description': 'Heavy-duty 30000mAh power bank with LCD display'
    },
    
    # Chargers
    {
        'name': '65W USB-C Fast Charger',
        'category': 'Chargers',
        'sku': 'CHG-65W-001',
        'price': Decimal('1899.99'),
        'quantity': 50,
        'minimum_stock': 12,
        'description': 'Fast-charging 65W USB-C charger for laptops and phones'
    },
    {
        'name': '18W Quick Charger',
        'category': 'Chargers',
        'sku': 'CHG-18W-001',
        'price': Decimal('599.99'),
        'quantity': 80,
        'minimum_stock': 20,
        'description': 'Quick charge 18W charger with compact design'
    },
    {
        'name': '20W Dual Port Charger',
        'category': 'Chargers',
        'sku': 'CHG-20W-001',
        'price': Decimal('749.99'),
        'quantity': 70,
        'minimum_stock': 15,
        'description': 'Dual port 20W charger for simultaneous charging'
    },
    {
        'name': '140W Laptop Charger (Universal)',
        'category': 'Chargers',
        'sku': 'CHG-140W-LAP',
        'price': Decimal('2499.99'),
        'quantity': 25,
        'minimum_stock': 5,
        'description': 'Universal 140W laptop charger for most brands'
    },
    
    # Cables & Cords
    {
        'name': 'USB-C Charging Cable (2m)',
        'category': 'Cables & Cords',
        'sku': 'CORD-USB-C-2M',
        'price': Decimal('299.99'),
        'quantity': 150,
        'minimum_stock': 40,
        'description': '2-meter durable USB-C charging and data cable'
    },
    {
        'name': 'Lightning Cable (1m)',
        'category': 'Cables & Cords',
        'sku': 'CORD-LIGHT-1M',
        'price': Decimal('349.99'),
        'quantity': 120,
        'minimum_stock': 30,
        'description': '1-meter lightning cable for iPhone/iPad'
    },
    {
        'name': 'Micro USB Cable (2m)',
        'category': 'Cables & Cords',
        'sku': 'CORD-MICRO-2M',
        'price': Decimal('199.99'),
        'quantity': 180,
        'minimum_stock': 50,
        'description': '2-meter micro USB cable with reinforced connectors'
    },
    {
        'name': '3-in-1 Charging Cable',
        'category': 'Cables & Cords',
        'sku': 'CORD-3IN1-001',
        'price': Decimal('499.99'),
        'quantity': 90,
        'minimum_stock': 20,
        'description': 'Universal 3-in-1 cable (USB-C, Lightning, Micro USB)'
    },
    
    # Pouches & Cases
    {
        'name': 'Neoprene Phone Pouch',
        'category': 'Pouches & Cases',
        'sku': 'POUCH-NEO-001',
        'price': Decimal('399.99'),
        'quantity': 100,
        'minimum_stock': 25,
        'description': 'Protective neoprene pouch for phones up to 6.5"'
    },
    {
        'name': 'Travel Organizer Pouch',
        'category': 'Pouches & Cases',
        'sku': 'POUCH-ORG-001',
        'price': Decimal('699.99'),
        'quantity': 70,
        'minimum_stock': 15,
        'description': 'Multi-compartment travel organizer for accessories'
    },
    {
        'name': 'Waterproof Electronics Pouch',
        'category': 'Pouches & Cases',
        'sku': 'POUCH-WP-001',
        'price': Decimal('599.99'),
        'quantity': 55,
        'minimum_stock': 12,
        'description': 'IPX8 waterproof pouch for phones and small devices'
    },
    
    # Laptop Accessories
    {
        'name': 'Laptop Skin (Matte Black)',
        'category': 'Laptop Accessories',
        'sku': 'SKIN-LAP-BK',
        'price': Decimal('399.99'),
        'quantity': 100,
        'minimum_stock': 20,
        'description': 'Premium matte black protective laptop skin'
    },
    {
        'name': 'Laptop Cooling Pad',
        'category': 'Laptop Accessories',
        'sku': 'COOL-LAP-001',
        'price': Decimal('1299.99'),
        'quantity': 40,
        'minimum_stock': 8,
        'description': 'USB-powered laptop cooling pad with dual fans'
    },
    {
        'name': 'Laptop Stand (Aluminum)',
        'category': 'Laptop Accessories',
        'sku': 'STAND-LAP-AL',
        'price': Decimal('1599.99'),
        'quantity': 35,
        'minimum_stock': 7,
        'description': 'Adjustable aluminum laptop stand for ergonomic viewing'
    },
    
    # Computer Peripherals
    {
        'name': 'Wireless Mouse (2.4GHz)',
        'category': 'Computer Peripherals',
        'sku': 'MOUSE-W-001',
        'price': Decimal('599.99'),
        'quantity': 85,
        'minimum_stock': 15,
        'description': 'Ergonomic wireless mouse with USB receiver'
    },
    {
        'name': 'Mechanical Keyboard (RGB)',
        'category': 'Computer Peripherals',
        'sku': 'KB-MECH-RGB',
        'price': Decimal('2499.99'),
        'quantity': 30,
        'minimum_stock': 5,
        'description': 'RGB mechanical keyboard with customizable backlighting'
    },
    {
        'name': 'USB Hub (7 Ports)',
        'category': 'Computer Peripherals',
        'sku': 'HUB-USB-7',
        'price': Decimal('799.99'),
        'quantity': 50,
        'minimum_stock': 10,
        'description': '7-port USB hub with fast charging'
    },
    
    # Storage Devices
    {
        'name': '64GB USB Flash Drive',
        'category': 'Storage Devices',
        'sku': 'FLASH-64GB-001',
        'price': Decimal('499.99'),
        'quantity': 120,
        'minimum_stock': 30,
        'description': 'Fast 64GB USB 3.0 flash drive'
    },
    {
        'name': '128GB USB Flash Drive',
        'category': 'Storage Devices',
        'sku': 'FLASH-128GB-001',
        'price': Decimal('899.99'),
        'quantity': 90,
        'minimum_stock': 20,
        'description': 'Ultra-fast 128GB USB 3.1 flash drive'
    },
    {
        'name': '32GB Memory Card (microSD)',
        'category': 'Storage Devices',
        'sku': 'CARD-MICRO-32GB',
        'price': Decimal('299.99'),
        'quantity': 150,
        'minimum_stock': 40,
        'description': '32GB Class 10 microSD card with adapter'
    },
]

for prod_data in products_data:
    category = categories[prod_data.pop('category')]
    product = Product.objects.create(category=category, **prod_data)
    print(f"Created product: {product.name} ({product.sku})")

print("\n✓ UFASH ACCESSORIES sample data loaded successfully!")
print(f"Created {len(categories)} categories")
print(f"Created {len(products_data)} products")
