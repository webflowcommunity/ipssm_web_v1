# Generated by Django 4.2.1 on 2023-05-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_alter_event_img_alter_faculty_img_alter_gallery_img_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="contactus",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Email"),
                ),
                ("subject", models.CharField(max_length=250, verbose_name="Subject")),
                ("Message", models.TextField(verbose_name="Message")),
            ],
        ),
        migrations.AlterField(
            model_name="event",
            name="img",
            field=models.ImageField(upload_to="events", verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="faculty",
            name="img",
            field=models.ImageField(upload_to="faculty", verbose_name="Faculty image"),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="img",
            field=models.ImageField(upload_to="gallery", verbose_name="Gallery"),
        ),
        migrations.AlterField(
            model_name="placements",
            name="img",
            field=models.ImageField(upload_to="placements", verbose_name="image"),
        ),
        migrations.AlterField(
            model_name="studentachi",
            name="file",
            field=models.FileField(upload_to="studentpdf", verbose_name="PDF"),
        ),
        migrations.AlterField(
            model_name="teacherachi",
            name="file",
            field=models.FileField(upload_to="studentpdf", verbose_name="PDF"),
        ),
        migrations.AlterField(
            model_name="testmonials",
            name="img",
            field=models.ImageField(upload_to="testmonial", verbose_name="image"),
        ),
    ]
