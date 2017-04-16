from django.db import models

# Create your models here.


class Heater(models.Model):
    name = models.CharField(max_length=40)
    kind = models.CharField(max_length=20)
    img = models.ImageField(upload_to='baseimg/', blank=True, null=True)
    img2 = models.ImageField(upload_to='baseimg/', blank=True, null=True)
    img3 = models.ImageField(upload_to='baseimg/', blank=True, null=True)
    power = models.IntegerField()
    temp = models.IntegerField()
    voltage = models.IntegerField()
    weight = models.IntegerField()
    dimensions = models.CharField(max_length=20)
    price = models.IntegerField()
    caption = models.CharField(max_length=300, default='Описание')


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Heater, unique=False)

    class Meta:
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def augment_quantity(self, quantity):
         self.quantity += int(quantity)
         self.save()
