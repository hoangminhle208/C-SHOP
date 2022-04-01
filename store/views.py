from operator import ge
from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.urls import register_converter
from .models.product import Product
from store.models import product
from .models.category import Category
from .models.customer import Customer
from django.views import View

# Create your views here.

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    # CHIEN: TẠO THƯ VIỆN DATA RỒI TRUYỀN DỮ LIỆU CỦA PRODUCT VS CATEGORY CHO INDEX.HTML XỬ LÝ
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

def validateCustomer(customer):
    error_message = None;
    if (not customer.first_name):
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 1:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required'
    elif len(customer.last_name) < 1:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.phone:
        error_message = 'Phone Number Required'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(customer.password) < 6:
        error_message = 'Password must be 6 char long'
    elif customer.password == -1:
        error_message = 'Re-enter passwowrd is incorrect'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    elif customer.isExists():
        error_message = 'Email Address Already Registered..'
    return error_message

def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    if postData.get('password_check') == postData.get('password'):
        password = postData.get('password')
    else:
        password = -1
    # validation
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }
    error_message = None
    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone, email=email,
                        password=password)

    error_message = validateCustomer(customer)
    # saving
    if not error_message:
        print(first_name, last_name, phone, email, password)
        
        # Hashing passWord
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'signup.html', data)


# DANG - lấy dữ liệu nhập vào khi tạo tài khoản
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    # Nếu bấm nút đăng ký
    else:
        return registerUser(request)
        
# CHIEN: Class base View
class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'
        print(customer)
        print(email,password)
        return render(request, 'login.html', {'error': error_message})
        

