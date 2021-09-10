# Generated by Django 3.1.5 on 2021-09-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Typenummer', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Lijn', models.CharField(max_length=20)),
                ('Code', models.CharField(max_length=20, null=True)),
                ('Categorie', models.CharField(max_length=60)),
                ('kW', models.CharField(max_length=20, null=True)),
                ('Voltage', models.CharField(max_length=20, null=True)),
                ('Afmetingen', models.CharField(max_length=30, null=True)),
                ('Breedte', models.CharField(max_length=30, null=True)),
                ('Diepte', models.CharField(max_length=30, null=True)),
                ('Hoogte', models.CharField(max_length=30, null=True)),
                ('Aansluiting', models.CharField(max_length=30, null=True)),
                ('Inhoud', models.CharField(max_length=30, null=True)),
                ('Prijs', models.IntegerField()),
                ('Extra', models.CharField(max_length=500, null=True)),
                ('Bedrijf', models.CharField(max_length=30)),
            ],
        ),
    ]
