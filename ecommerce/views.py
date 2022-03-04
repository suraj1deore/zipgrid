from fileinput import filename
from django.shortcuts import render, redirect
from .models import Order, Product, Category,Brand
from .forms import OrderForm



# We had to write this function because all backends records that we saved should display on frontend
def home(request):
	orders = Order.objects.all()
	brand = Brand.objects.all()

	total_customers = brand.count()

# We had to write this function to check the status wheather the product is Delivered or Pending
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'brand':brand,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'dashboard.html', context)



# We had to write this function to display all Products details
def products(request):
	products = Product.objects.all()
	
	return render(request, 'products.html',{'products':products })



# We had to write this function to Create any orders by admin
def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)


#We had to write this function to update any previous order
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)



#We had to write this function to delete any previous order
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'delete.html', context)

