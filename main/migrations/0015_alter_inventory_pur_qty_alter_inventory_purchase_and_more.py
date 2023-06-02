# Generated by Django 4.0.3 on 2023-05-20 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_purchase_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='pur_qty',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='purchase',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.purchase'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='sale',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.sale'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='sale_qty',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total_amt',
            field=models.FloatField(editable=False),
        ),
    ]
