# Data migration: update university-related info (deadlines, descriptions) from 2024 to 2026

from django.db import migrations


def update_to_2026(apps, schema_editor):
    import datetime

    Admission = apps.get_model("information", "Admission")
    University = apps.get_model("information", "University")
    Major = apps.get_model("information", "Major")
    About = apps.get_model("information", "About")
    Professor = apps.get_model("information", "Professor")
    FamousPeople = apps.get_model("information", "FamousPeople")

    # 1. Admission deadlines: set year to 2026 (keep month/day; handle Feb 29 -> Feb 28 for 2026)
    for adm in Admission.objects.all():
        old = adm.deadline
        try:
            adm.deadline = old.replace(year=2026)
        except ValueError:
            # Feb 29, 2024 -> Feb 28, 2026 (2026 is not a leap year)
            adm.deadline = datetime.date(2026, old.month, 28 if (old.month == 2 and old.day == 29) else old.day)
        adm.save()

    # 2. Replace 2024 with 2026 in text fields
    for uni in University.objects.all():
        if uni.detail and "2024" in uni.detail:
            uni.detail = uni.detail.replace("2024", "2026")
            uni.save()

    for major in Major.objects.all():
        if major.description and "2024" in (major.description or ""):
            major.description = major.description.replace("2024", "2026")
            major.save()

    for about in About.objects.all():
        if about.content and "2024" in about.content:
            about.content = about.content.replace("2024", "2026")
            about.save()

    for prof in Professor.objects.all():
        updated = False
        if prof.description and "2024" in (prof.description or ""):
            prof.description = prof.description.replace("2024", "2026")
            updated = True
        if prof.degree and "2024" in (prof.degree or ""):
            prof.degree = prof.degree.replace("2024", "2026")
            updated = True
        if updated:
            prof.save()

    for person in FamousPeople.objects.all():
        updated = False
        if person.description and "2024" in (person.description or ""):
            person.description = person.description.replace("2024", "2026")
            updated = True
        if person.action and "2024" in (person.action or ""):
            person.action = person.action.replace("2024", "2026")
            updated = True
        if updated:
            person.save()


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0029_fix_business_admin_famous_action"),
    ]

    operations = [
        migrations.RunPython(update_to_2026, noop_reverse),
    ]
