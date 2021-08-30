# Generated by Django 3.2 on 2021-08-30 16:39

from django.db import migrations


def create_employee_yeargroup(apps, schema_editor):
    Yeargroup = apps.get_model("base", "Yeargroup")
    db_alias = schema_editor.connection.alias
    if not Yeargroup.objects.using(db_alias).filter(slug='employee').exists():
        Yeargroup.objects.using(db_alias).create(slug='employee', name='Employee')


class Migration(migrations.Migration):
    """This migration is used to create an "employee" yeargroup which is required for the REGISTRATION_LDAP code."""

    dependencies = [
        ('base', '0012_delete_passwdentry'),
    ]

    operations = [
        migrations.RunPython(create_employee_yeargroup)
    ]
