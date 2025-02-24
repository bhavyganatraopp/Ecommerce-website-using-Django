from django.db import models

# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    product_discreption=models.CharField(max_length=300000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    phone = models.IntegerField(default=0000000000)
    desc = models.CharField(max_length=5000)

    def __self__(self):
        return self.name
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=10000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    address = models.CharField(max_length=5000)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=6)
    phone = models.IntegerField(default=0000000000)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __self__(self):
        return self.update_desc[0:7] + "..."
