from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, upload_to="CategoryImg/")
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Categorys"


class Product(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="ProductImg")
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Products"


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to="Files/%Y/%m/%d/")
    created_time = models.DateTimeField(auto_now_add=True)
