# Generated by Django 5.1.6 on 2025-02-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0007_rename_descricao_link_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='name',
            new_name='nome',
        ),
    ]
