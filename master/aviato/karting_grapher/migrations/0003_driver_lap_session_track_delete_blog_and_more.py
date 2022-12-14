# Generated by Django 4.1 on 2022-08-22 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("karting_grapher", "0002_blog_alter_karting_data_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver",
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
                ("driver_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Lap",
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
                ("laptime", models.DecimalField(decimal_places=3, max_digits=6)),
                ("lap_of_session", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Session",
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
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="karting_grapher.driver",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Track",
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
            ],
        ),
        migrations.DeleteModel(name="Blog",),
        migrations.DeleteModel(name="Karting_Data",),
        migrations.AddField(
            model_name="session",
            name="track_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="karting_grapher.track"
            ),
        ),
        migrations.AddField(
            model_name="lap",
            name="session_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="karting_grapher.session",
            ),
        ),
    ]
