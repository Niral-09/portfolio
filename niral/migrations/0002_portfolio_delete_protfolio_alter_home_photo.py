# Generated by Django 4.1.2 on 2022-10-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Protfolio',
        ),
        migrations.AlterField(
            model_name='home',
            name='photo',
            field=models.ImageField(upload_to='photo/'),
        ),
    ]
