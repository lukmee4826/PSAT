# Generated by Django 4.1.13 on 2025-02-15 16:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_requested', models.IntegerField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('requestor', models.CharField(max_length=200)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.medicine')),
            ],
        ),
    ]
