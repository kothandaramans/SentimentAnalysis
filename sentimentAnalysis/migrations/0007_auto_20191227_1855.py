# Generated by Django 3.0 on 2019-12-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentimentAnalysis', '0006_auto_20191227_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
