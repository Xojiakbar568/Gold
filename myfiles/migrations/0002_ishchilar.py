# Generated by Django 4.0 on 2022-08-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ishchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('fam', models.CharField(max_length=30)),
                ('yosh', models.IntegerField()),
                ('foto', models.ImageField(upload_to='media')),
            ],
        ),
    ]
