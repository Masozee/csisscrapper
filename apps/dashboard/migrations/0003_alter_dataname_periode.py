# Generated by Django 4.2.7 on 2023-11-20 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_datavalue_date_alter_datavalue_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataname',
            name='periode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.option'),
        ),
    ]
