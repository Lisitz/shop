
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order.by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True)
        return products


class LatestProducts:

    objects = LatestProductManager()



#1 Product
#2 Category
#3 Cart Product
#4 Cart
#5 Order
#6 Customer
#7 Specification/features

class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):


    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='изображение')
    description = models.TextField(verbose_name='описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.title


class Sneakers(Product):

    sneakers_model = models.CharField(max_length=255, verbose_name='модель')
    color = models.CharField(max_length=255, verbose_name='цвет')
    size = models.CharField(max_length=255, verbose_name='размер')
    gender_m = models.CharField(max_length=255, verbose_name='мужские')
    gender_w = models.CharField(max_length=255, verbose_name='женские')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Accessories(Product):

    socks_m = models.CharField(max_length=255, verbose_name='носки мужские')
    socks_w = models.CharField(max_length=255, verbose_name='носки женские')
    laces = models.CharField(max_length=255, verbose_name='шнурки')
    clean_staff = models.CharField(max_length=255, verbose_name='средства для ухода')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Всего')

    def __str__(self):
        return "Продукт: {} для корзины".format(self.product.title)

class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Всего')

    def __str__(self):
        return str(self.id)

class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='контактный номер')
    adress = models.CharField(max_length=255, verbose_name='адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)











