# Generated by Django 4.2 on 2023-04-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_register',
            fields=[
                ('Userid', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Password', models.CharField(max_length=50)),
                ('Confirmpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
