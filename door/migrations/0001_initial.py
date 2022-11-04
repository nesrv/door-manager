# Generated by Django 4.1.2 on 2022-11-03 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Door",
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
                ("name", models.CharField(max_length=50, verbose_name="Company name")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                ("url", models.URLField(null=True, verbose_name="Link")),
            ],
            options={
                "verbose_name": "Registered door",
                "verbose_name_plural": "Registered doors",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=100)),
                ("login", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                ("password", models.CharField(blank=True, max_length=100)),
                ("description", models.TextField(blank=True)),
                ("photo", models.ImageField(upload_to="photos/")),
                ("time_created", models.DateTimeField(auto_now_add=True)),
                ("time_update", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "door",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="door.door",
                        verbose_name="What door has access to",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registered user",
                "verbose_name_plural": "Registered users",
                "ordering": ("id", "name"),
            },
        ),
        migrations.CreateModel(
            name="History",
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
                    "time_opening",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "door",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="door.door"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="door.user"
                    ),
                ),
            ],
            options={"ordering": ("-time_opening",)},
        ),
        migrations.CreateModel(
            name="ErrorLog",
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
                ("error_name", models.CharField(max_length=200)),
                ("time_error", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "door",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="door.door"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="door.user"
                    ),
                ),
            ],
        ),
    ]
