# Generated by Django 4.2.1 on 2023-05-22 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prodotto',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Utente',
            new_name='User',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('prodotti', models.ManyToManyField(to='ecommerce.product')),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.user')),
            ],
        ),
    ]
