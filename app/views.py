from django.shortcuts import render, redirect
from .models import Supplier, Product, Car, Customer
from django.contrib.auth import authenticate, login, logout

'''# Landing afrer login

def landingview(request):
    return render(request, 'landingpage.html')
'''

# Login and logout

def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')
    
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

# Product view´s

def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render (request,"productlist.html",context)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
    
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def edit_product_get(request, id):
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)

def edit_product_post(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)

# Supplier view´s

def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request,"supplierlist.html",context)

def addsupplier(request):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            a = request.POST['companyname']
            b = request.POST['contactname']
            c = request.POST['address']
            d = request.POST['phone']
            e = request.POST['email']
            f = request.POST['country']
            Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
            return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)

def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__contains = search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html",context)

# Car Views
def carlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        carlist = Car.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'cars': carlist, 'suppliers': supplierlist}
        return render (request,"carlist.html",context)


def add_car(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['model']
        b = request.POST['license_number']
        c = request.POST['supplier']
        
        Car(model=a, license_number=b, supplier=Supplier.objects.get(id=c)).save()
        return redirect(request.META['HTTP_REFERER'])
    
def cars_by_supplier(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.get(id=id)
        cars = Car.objects.filter(supplier=supplier)
        supplierlist = Supplier.objects.all()
        context = {'cars': cars, 'suppliers': supplierlist, 'selected_supplier': supplier}
        return render(request, 'carlist.html', context)
    
def edit_car_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        car = Car.objects.get(id=id)
        supplierlist = Supplier.objects.all()
        context = {'car': car, 'suppliers': supplierlist}
        return render(request, "edit_car.html", context)

def edit_car_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        car = Car.objects.get(id=id)
        car.model = request.POST['model']
        car.license_number = request.POST['license_number']
        car.supplier = Supplier.objects.get(id=request.POST['supplier'])
        car.save()
        return redirect(carlistview)

def confirm_delete_car(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        car = Car.objects.get(id=id)
        context = {'car': car}
        return render(request, "confirmdelcar.html", context)

def delete_car(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Car.objects.get(id=id).delete()
        return redirect(carlistview)
    
# Customer Views

def customerlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customerlist = Customer.objects.all()
        context = {'customers': customerlist}
        return render(request, "customerlist.html", context)

def add_customer(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        if request.method == 'POST':
            a = request.POST['name']
            b = request.POST['email']
            c = request.POST['phone']
            d = request.POST['address']
            Customer(name=a, email=b, phone=c, address=d).save()
            return redirect('customer_list')
        else:
            return render(request, 'customerlist.html')

def confirm_delete_customer(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customer = Customer.objects.get(id=id)
        context = {'customer': customer}
        return render(request, "confirmdelcustomer.html", context)

def delete_customer(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Customer.objects.get(id=id).delete()
        return redirect(customerlistview)