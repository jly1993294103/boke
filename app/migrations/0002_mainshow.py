# Generated by Django 2.1.1 on 2018-11-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
                ('categoryid', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=300)),
                ('childcid1', models.CharField(max_length=50)),
                ('productid1', models.CharField(max_length=20)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=20)),
                ('marketprice1', models.CharField(max_length=20)),
                ('img2', models.CharField(max_length=300)),
                ('childcid2', models.CharField(max_length=50)),
                ('productid2', models.CharField(max_length=20)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=20)),
                ('marketprice2', models.CharField(max_length=20)),
                ('img3', models.CharField(max_length=300)),
                ('childcid3', models.CharField(max_length=50)),
                ('productid3', models.CharField(max_length=20)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=20)),
                ('marketprice3', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]
