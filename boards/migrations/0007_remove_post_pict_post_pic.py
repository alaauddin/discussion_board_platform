# Generated by Django 4.2 on 2023-07-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0006_rename_pic_post_pict"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="pict",),
        migrations.AddField(
            model_name="post",
            name="pic",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="static/media/"
            ),
        ),
    ]
