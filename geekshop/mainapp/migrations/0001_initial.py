
# Generated by Django 3.2.11 on 2022-02-03 16:35


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="имя")),
                ("description", models.TextField(blank=True, verbose_name="описание")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="имя")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=7, verbose_name="цена"
                    ),
                ),
                (
                    "color",
                    models.PositiveBigIntegerField(default=0, verbose_name="цвет"),
                ),
                ("description", models.TextField(blank=True, verbose_name="описание")),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="products", verbose_name="картинка"

                    ),
                ),
                (
                    "quantity",
                    models.PositiveBigIntegerField(
                        default=0, verbose_name="количество"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.productcategory",
                    ),
                ),
            ],
        ),
    ]
