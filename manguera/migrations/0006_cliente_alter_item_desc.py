# Generated by Django 4.0.4 on 2022-06-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manguera', '0005_alter_item_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
