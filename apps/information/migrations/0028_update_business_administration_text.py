# Data migration: update Business Administration major and famous-person text
# (Zip2 removed, grammar fixed, summary for major description)

from django.db import migrations

MAJOR_SUMMARY = (
    "Elon Musk's path in business administration includes co-founding the online bank X.com in 1999 "
    "and its merger with Confinity, which led to PayPal. After being replaced as CEO, he remained PayPal's "
    "largest shareholder until eBay acquired the company in 2002 for $1.5 billion; Musk received about $175.8 million. "
    "He later bought back the X.com domain and has spoken about building \"X, the everything app.\" "
    "In 2002, after failed attempts to buy rockets in Russia, he founded SpaceX with $100 million of his own money "
    "and became its CEO and Chief Engineer, aiming to build affordable rockets and support goals such as sending payloads to Mars."
)

# For FamousPeople under Business Administration (e.g. Elon Musk): description and action
FAMOUS_DESCRIPTION = (
    "Later in 1999, Musk co-founded X.com, an online financial services and email payment company, with $12 million "
    "of the money he made from the Compaq acquisition. X.com was one of the first federally insured online banks, "
    "and over 200,000 customers joined in its initial months of operation. Although Musk founded the company, "
    "investors regarded him as inexperienced and replaced him with Intuit CEO Bill Harris by the end of the year. "
    "In 2000, X.com merged with the online bank Confinity to avoid competition, as the latter's money-transfer "
    "service PayPal was more popular than X.com's service. Musk then returned as CEO of the merged company. "
    "His preference for Microsoft over Unix-based software caused a rift among the company's employees and eventually "
    "led Confinity co-founder Peter Thiel to resign. With the company suffering from compounding technological issues "
    "and the lack of a cohesive business model, the board ousted Musk and replaced him with Thiel in September 2000. "
    "Under Thiel, the company focused on the money-transfer service and was renamed PayPal in 2001. In 2002, PayPal "
    "was acquired by eBay for $1.5 billion in stock; Musk—PayPal's largest shareholder with 11.72% of shares—received "
    "$175.8 million. In 2017, more than 15 years later, Musk purchased the X.com domain from PayPal for its "
    "\"sentimental value.\" In 2022, Musk discussed a goal of creating \"X, the everything app.\""
)

FAMOUS_ACTION = (
    "In early 2001, Musk became involved with the nonprofit Mars Society and discussed funding plans to place a growth "
    "chamber for plants on Mars. In October of the same year, he traveled to Moscow with Jim Cantrell and Adeo Ressi "
    "to buy refurbished intercontinental ballistic missiles (ICBMs) that could send the greenhouse payloads into space. "
    "He met with NPO Lavochkin and Kosmotras; however, Musk was seen as a novice and the group returned to the United "
    "States empty-handed. In February 2002, the group returned to Russia with Mike Griffin (president of In-Q-Tel) to "
    "look for three ICBMs. They had another meeting with Kosmotras and were offered one rocket for $8 million, which "
    "Musk rejected. He instead decided to start a company that could build affordable rockets. With $100 million of "
    "his own money, Musk founded SpaceX in May 2002 and became the company's CEO and Chief Engineer."
)


def update_business_administration(apps, schema_editor):
    Major = apps.get_model("information", "Major")
    FamousPeople = apps.get_model("information", "FamousPeople")
    majors = Major.objects.filter(name__icontains="Business Administration")
    for major in majors:
        major.description = MAJOR_SUMMARY
        major.save()
        # Update famous people whose bio contains the old Zip2 content (so we don't overwrite other bios)
        for person in FamousPeople.objects.filter(major=major):
            if "Zip2" in (person.description or "") or "zip2" in (person.description or "").lower():
                person.description = FAMOUS_DESCRIPTION
                person.action = FAMOUS_ACTION
                person.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("information", "0027_set_university_theme_colors"),
    ]

    operations = [
        migrations.RunPython(update_business_administration, noop),
    ]
