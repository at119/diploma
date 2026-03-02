# Data migration: set theme_color for each university by name

from django.db import migrations


# University name substring (case-insensitive) -> hex theme color
UNIVERSITY_THEME_COLORS = [
    ("harvard", "#722F37"),           # burgundy
    ("stanford", "#8C1515"),         # cardinal red
    ("grinnell", "#E35205"),         # orange
    ("grinell", "#E35205"),           # orange (alternate spelling)
    ("reed", "#C41230"),             # red
    ("cornell", "#B31B1B"),          # carnelian red (and white)
    ("princeton", "#008C45"),        # dark green
    ("brown", "#4E3629"),             # brown (Brown University)
    ("new york university", "#57068C"),   # purple (NYU)
    ("university of california", "#002868"),  # blue (and gold)
    ("mit", "#A31F34"),              # cardinal red (and silver gray)
    ("columbia", "#6E9FD4"),         # light blue (Columbia)
    ("northwestern", "#4E2A84"),     # purple
]


def set_theme_colors(apps, schema_editor):
    University = apps.get_model("information", "University")
    for name_part, hex_color in UNIVERSITY_THEME_COLORS:
        University.objects.filter(name__icontains=name_part).update(theme_color=hex_color)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0026_add_university_theme_color"),
    ]

    operations = [
        migrations.RunPython(set_theme_colors, noop),
    ]
