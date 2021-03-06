# Generated by Django 2.2.4 on 2019-08-21 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikesharing', '0004_auto_20190813_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='internal_note',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='bike',
            name='last_reported',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='bike_type',
            field=models.CharField(choices=[('BI', 'Bike'), ('CB', 'Cargo Bike'), ('EB', 'E-Bike'), ('ES', 'E-Scooter'), ('WH', 'Wheelchair')], default='BI', max_length=2),
        ),
        migrations.AlterField(
            model_name='bike',
            name='state',
            field=models.CharField(choices=[('US', 'Usable'), ('BR', 'Broken'), ('IR', 'In Repair'), ('MI', 'Missing')], default='US', max_length=2),
        ),
        migrations.AlterField(
            model_name='rent',
            name='bike',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='bikesharing.Bike'),
        ),
    ]
