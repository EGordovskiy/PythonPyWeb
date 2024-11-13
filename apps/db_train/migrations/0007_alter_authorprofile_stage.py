# Generated by Django 4.2.5 on 2024-10-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db_train", "0006_tag_entry_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authorprofile",
            name="stage",
            field=models.IntegerField(
                blank=True, default=0, help_text="Стаж в годах", verbose_name="Стаж"
            ),
        ),
    ]
