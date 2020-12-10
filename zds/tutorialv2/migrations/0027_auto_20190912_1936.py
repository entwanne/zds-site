# Generated by Django 2.1.11 on 2019-09-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorialv2", "0026_publicationevent_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publicationevent",
            name="state_of_processing",
            field=models.CharField(
                choices=[
                    ("REQUESTED", "Export demandé"),
                    ("RUNNING", "Export en cours"),
                    ("SUCCESS", "Export réalisé"),
                    ("FAILURE", "Export échoué"),
                ],
                db_index=True,
                max_length=20,
            ),
        ),
    ]