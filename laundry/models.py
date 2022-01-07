from django.db import models

# Create your models here.
"""class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name"""



class Laundry(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='uploads/pics')

    def __str__(self):
        return self.name

    @property
    def pictureURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


class OrderItem(models.Model):
    laundry = models.ForeignKey(Laundry, on_delete=models.SET_NULL, null=True)
    #order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.laundry.name

    @property
    def get_total(self):
        total = self.laundry.price * self.quantity
        return total


class Order(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    #date_ordered = models.DateTimeField(auto_now_add=True)
    #is_complete = models.BooleanField(default=False, blank=True)
    #transaction_id = models.CharField(max_length=200, null=True)

    #def __str__(self):
        #return str(self.id)
    customer_name = models.CharField(max_length=250)
    customer_no = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=250)
    choices = (
        ('Pending', 'Pending'),
        ('Ready for delivery', 'Ready for delivery'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=50, choices=choices, default="Pending", blank=True, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    extra_fee = models.IntegerField(default=0, null=True)
    total = models.IntegerField()

    def __str__(self):
        return self.customer_name

    