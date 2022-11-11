# Generated by Django 3.1.7 on 2021-02-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "1013_migrate_tag_colour"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savedviewfilterrule",
            name="rule_type",
            field=models.PositiveIntegerField(
                choices=[
                    (0, "title contains"),
                    (1, "content contains"),
                    (2, "ASN is"),
                    (3, "correspondent is"),
                    (4, "document type is"),
                    (5, "is in inbox"),
                    (6, "has tag"),
                    (7, "has any tag"),
                    (8, "created before"),
                    (9, "created after"),
                    (10, "created year is"),
                    (11, "created month is"),
                    (12, "created day is"),
                    (13, "added before"),
                    (14, "added after"),
                    (15, "modified before"),
                    (16, "modified after"),
                    (17, "does not have tag"),
                    (18, "does not have ASN"),
                    (19, "title or content contains"),
                ],
                verbose_name="rule type",
            ),
        ),
    ]
