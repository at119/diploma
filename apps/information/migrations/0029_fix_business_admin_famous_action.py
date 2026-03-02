# Data migration: fix Business Administration famous people when Zip2 is in the action (Notable achievement) field

from django.db import migrations

FAMOUS_DESCRIPTION = (
)

FAMOUS_ACTION = (
)


def fix_famous_action(apps, schema_editor):
    Major = apps.get_model("information", "Major")
    FamousPeople = apps.get_model("information", "FamousPeople")
    majors = Major.objects.filter(name__icontains="Business Administration")
    for major in majors:
        for person in FamousPeople.objects.filter(major=major):
            desc = person.description or ""
            action = person.action or ""
            # Zip2 content can be in description OR in action (Notable achievement)
            if "Zip2" in desc or "zip2" in desc.lower() or "Zip2" in action or "zip2" in action.lower():
                person.description = FAMOUS_DESCRIPTION
                person.action = FAMOUS_ACTION
                person.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0028_update_business_administration_text"),
    ]

    operations = [
        migrations.RunPython(fix_famous_action, noop),
    ]
