# Generated by Django 3.0.8 on 2020-08-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20200731_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
