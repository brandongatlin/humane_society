# Generated by Django 3.0.8 on 2020-08-01 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20200731_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.Human'),
        ),
    ]
