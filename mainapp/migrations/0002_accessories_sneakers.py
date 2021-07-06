# Generated by Django 3.2.5 on 2021-07-03 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='изображение')),
                ('description', models.TextField(null=True, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='цена')),
                ('sneakers_model', models.CharField(max_length=255, verbose_name='модель')),
                ('color', models.CharField(max_length=255, verbose_name='цвет')),
                ('size', models.CharField(max_length=255, verbose_name='размер')),
                ('gender_m', models.CharField(max_length=255, verbose_name='мужские')),
                ('gender_w', models.CharField(max_length=255, verbose_name='женские')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='изображение')),
                ('description', models.TextField(null=True, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='цена')),
                ('socks_m', models.CharField(max_length=255, verbose_name='носки мужские')),
                ('socks_w', models.CharField(max_length=255, verbose_name='носки женские')),
                ('laces', models.CharField(max_length=255, verbose_name='шнурки')),
                ('clean_staff', models.CharField(max_length=255, verbose_name='средства для ухода')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
