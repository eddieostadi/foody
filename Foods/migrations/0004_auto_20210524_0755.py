# Generated by Django 3.1.7 on 2021-05-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0003_auto_20210519_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialdiet',
            name='diet',
            field=models.CharField(choices=[('Vegan', 'vegan'), ('Vegetarian', 'vegetarian'), ('wheat/gluten-free', 'wheat/gluten-free'), ('Diary Free', 'diary free'), ('Nut', 'nut'), ('Seafood', 'seafood')], max_length=20, null=True),
        ),
    ]
