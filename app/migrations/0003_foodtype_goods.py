# Generated by Django 2.1.1 on 2018-11-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=20)),
                ('childtypenames', models.CharField(max_length=50)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=30)),
                ('productlongname', models.CharField(max_length=50)),
                ('isxf', models.BooleanField()),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=20)),
                ('dealerid', models.CharField(max_length=20)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]
