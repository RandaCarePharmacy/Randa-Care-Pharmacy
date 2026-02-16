from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Drug(models.Model):
    CATEGORY_CHOICES = [
        ('OTC', 'Over the Counter'),
        ('RX', 'Prescription'),
        ('CONTROLLED', 'Controlled Drug')
    ]

    name = models.CharField(max_length=200)
    strength = models.CharField(max_length=50)
    dosage_form = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    batch_number = models.CharField(max_length=100)
    expiry_date = models.DateField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    reorder_level = models.IntegerField(default=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
