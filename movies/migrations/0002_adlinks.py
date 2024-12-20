# Generated by Django 4.2.3 on 2023-07-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdLinks',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=False, null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('link_name', models.CharField(blank=True, max_length=500, null=True)),
                ('link_address', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
