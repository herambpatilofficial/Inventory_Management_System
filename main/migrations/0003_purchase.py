# Generated by Django 4.0.3 on 2023-05-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_unit_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('pur_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vendor')),
            ],
            options={
                'verbose_name_plural': 'Purchase',
            },
        ),
    ]
