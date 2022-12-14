# Generated by Django 4.2.dev20220624125221 on 2022-09-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonType', models.CharField(max_length=7)),
                ('FIRST_NAME', models.CharField(max_length=30)),
                ('LAST_NAME', models.CharField(max_length=30)),
                ('EMAIL', models.EmailField(max_length=50)),
                ('CONTACT', models.CharField(max_length=20)),
                ('NID', models.CharField(max_length=20)),
                ('PASSWORD', models.CharField(max_length=50)),
                ('CONFIRM_PASSWORD', models.CharField(max_length=50)),
            ],
        ),
    ]
