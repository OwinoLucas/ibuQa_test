from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length = 100)
    amount = models.IntegerField(max_length = 10)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ["-pk"]
