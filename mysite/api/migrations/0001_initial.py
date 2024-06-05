# Generated by Django 5.0.6 on 2024-06-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RealEstate",
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
                ("date", models.DateTimeField()),
                ("price", models.IntegerField()),
                ("bedrooms", models.IntegerField()),
                ("bathrooms", models.FloatField()),
                ("sqft_living", models.IntegerField()),
                ("sqft_lot", models.IntegerField()),
                ("floors", models.FloatField()),
                ("waterfront", models.BooleanField()),
                ("view", models.IntegerField()),
                ("condition", models.IntegerField()),
                ("sqft_above", models.IntegerField()),
                ("sqft_basement", models.IntegerField()),
                ("yr_built", models.IntegerField()),
                ("yr_renovated", models.IntegerField(blank=True, null=True)),
                ("street", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("statezip", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=50)),
                ("predict_price", models.FloatField()),
            ],
        ),
    ]
