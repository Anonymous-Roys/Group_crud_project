# Generated by Django 4.0 on 2023-12-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.AutoField(db_column='prdIdpk', primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, db_column='prdName', max_length=255, null=True)),
                ('Description', models.CharField(blank=True, db_column='prdDescription', max_length=255, null=True)),
                ('Price', models.DecimalField(blank=True, db_column='prdPrice', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'tblproduct',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('Id', models.AutoField(db_column='prdBrandIdpk', primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, db_column='prdBrandName', max_length=255, null=True)),
                ('Description', models.CharField(blank=True, db_column='prdBrandDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblproductbrand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('Id', models.AutoField(db_column='prdCategoryIdpk', primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, db_column='prdCategoryName', max_length=255, null=True)),
                ('Description', models.CharField(blank=True, db_column='prdCategoryDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblproductcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('Id', models.AutoField(db_column='prdSubCategoryIdpk', primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, db_column='prdSubCategoryName', max_length=255, null=True)),
                ('Description', models.CharField(blank=True, db_column='prdSubCategoryDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblproductsubcategory',
                'managed': False,
            },
        ),
    ]
