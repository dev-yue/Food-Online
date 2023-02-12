# Generated by Django 4.1.5 on 2023-02-12 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0005_openinghour"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="openinghour",
            options={"ordering": ("day", "-from_hour")},
        ),
        migrations.AlterUniqueTogether(
            name="openinghour",
            unique_together={("vendor", "day", "from_hour", "to_hour")},
        ),
    ]
