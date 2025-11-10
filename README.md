Ecommerce-mini- Project (Django)

A simple e-commerce web application built using Django, featuring product management, cart system, checkout, order summary, and an admin dashboard.
This project demonstrates full-stack skills, including authentication, database modeling, CRUD operations, and user/admin workflows.

Live Demo
     User Website: https://nandinir9992.pythonanywhere.com/
    
     Admin Dashboard: https://nandinir9992.pythonanywhere.com/admin/

 Features
  User Features
  
  User Signup
  
  Login 
  
  Logout
  
  View products
  
  Add products to cart
  
  Increase/decrease quantity
  
  Remove items from cart
  
  Checkout with shipping address
  
  View order summary


Cart & Checkout
  
  Add multiple items
  
  Cart total auto calculated
  
  Checkout form
  
  Order saved with order items
  
  Shipping address stored


Order Management

  Order details (ID, user, total, status, created date)
  
  Order Items stored separately
  
  Shipping address linked to order


Admin Features
 
  Custom Admin Dashboard:
  
  Total Products
  
  Total Orders
  
  Pending Orders
  
  Total Revenue


Manage products (CRUD)

Manage orders (view + update)

View order items (inline display)

View shipping addresses


Tech Stack

  Backend: Django
  
  Database: SQLite
  
  Frontend: HTML



 Installation & Setup
1. Clone the repository
git clone https://github.com/nandinir9992/ecommerce-mini-project.git
cd ecommerce-mini

2️. Create a virtual environment
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

3️. Install dependencies
pip install django djangorestframework djangorestframework-simplejwt pillow django-cors-headers django-filter

4️. Run migrations
python manage.py makemigrations
python manage.py migrate

5️. Create superuser
python manage.py createsuperuser

6️. Start the server
python manage.py runserver


 browser:
 http://127.0.0.1:8000/login/
 Admin Panel: http://127.0.0.1:8000/admin/

 Default Flow 
   Signup or Login
   Browse products
   Add products to cart
   View cart (update quantity or remove items)
   Checkout page
   Enter shipping address
   Place order → Order Summary

Admin Dashboard
   Total Orders
   Pending Orders
   Total Revenue
   Total Products
   Models Summary
   Product
   Stores product details
   Cart
   Stores user cart
   CartItem
   Stores items inside cart
   Order
   Stores order details (user, total, status)
   OrderItem
   Stores products inside each order
   ShippingAddress
   Stores order shipping details

Testing
   Add product from Django Admin
   Login with user
   Add to cart
   Checkout
   View orders from admin dashboard

Notes
   No React/Angular
   Pure Django template rendering
   Easy to extend for future enhancement
