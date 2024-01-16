# Generated by Django 4.2.5 on 2023-10-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_Name', models.CharField(blank='true', max_length=50, null='true')),
                ('Prod_Name', models.CharField(blank='true', max_length=50, null='true')),
                ('Prod_Desc', models.CharField(blank='true', max_length=50, null='true')),
                ('Price', models.IntegerField(blank='true', null='true')),
                ('Prod_Image', models.ImageField(blank='true', null='true', upload_to='Product_Images')),
            ],
        ),
    ]
