# Generated by Django 4.2.1 on 2023-05-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_user_isamm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='isAmm',
        ),
        migrations.AddField(
            model_name='order',
            name='totale',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
