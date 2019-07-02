from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import URLValidator
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField


class Resume(models.Model):
    # {
    #   "basics": {
    #     "name": "",
    #     "label": "",
    #     "picture": "",
    #     "email": "",
    #     "phone": "",
    #     "degree": "",
    #     "website": "",
    #     "summary": "",
    #     "highlights": "",
    #     "location": {
    #       "address": "",
    #       "postalCode": "",
    #       "city": "",
    #       "countryCode": "",
    #       "region": ""
    #     },
    #     "profiles": [
    #       {
    #         "network": "",
    #         "username": "",
    #         "url": ""
    #       }
    #     ]
    #   },
    # ==================================
    #   "work": [
    #     {
    #       "company": "",
    #       "position": "",
    #       "website": "",
    #       "startDate": "",
    #       "endDate": "",
    #       "summary": "",
    #       "highlights": [
    #         ""
    #       ]
    #     }
    #   ],
    # ==================================
    #   "education": [
    #     {
    #       "institution": "",
    #       "area": "",
    #       "studyType": "",
    #       "startDate": "",
    #       "endDate": "",
    #     }
    #   ],
    # ==================================
    #   "skills": [
    #     {
    #       "name": "",
    #       "keywords": [
    #         ""
    #       ]
    #     }
    #   ]
    # }

    # basic information
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=10, null=True, blank=True)
    # picture = models.ImageField(null=True, upload_to='media')
    email = models.EmailField(max_length=100, null=True, unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex], max_length=17, null=True, blank=True)  # validators should be a list
    degree = models.CharField(max_length=25, null=True, blank=True)
    website = models.TextField(
        validators=[URLValidator()], null=True, blank=True)
    # Summary
    summary = models.CharField(max_length=500, null=True, blank=True)
    # "highlights": [
    #     "Bullet-point list items that you would like to include along with (or instead of) a summary paragraph."
    # ],
    highlights = models.CharField(max_length=500, null=True, blank=True)
    # Location
    address = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=20, null=True, blank=True)
    region = models.CharField(max_length=10, null=True, blank=True)
    # Profiles *array
    # network = models.CharField(max_length=20, null=True, blank=True)
    # username = models.CharField(max_length=20, null=True, blank=True)
    # url = models.TextField(validators=[URLValidator()], null=True, blank=True)
    profiles = ArrayField(
        JSONField(blank=True, null=True), blank=True, null=True)
    # Work *array
    # work_company = models.CharField(max_length=100, null=True, blank=True)
    # work_position = models.CharField(max_length=100, null=True, blank=True)
    # worl_website = models.TextField(
    #     validators=[URLValidator()], null=True, blank=True)
    # work_start_date = models.DateField(null=True, blank=True)
    # work_end_date = models.DateField(null=True, blank=True)
    # work_summary = models.CharField(max_length=500, null=True, blank=True)
    # work_highlights = models.CharField(
    #     max_length=200, null=True, blank=True)
    work = ArrayField(JSONField(blank=True, null=True), blank=True, null=True)
    # Education *array
    # institution = models.CharField(max_length=100, null=True, blank=True)
    # education_area = models.CharField(
    #     max_length=100, null=True, blank=True)
    # study_type = models.CharField(max_length=100, null=True, blank=True)
    # education_start_date = models.DateField(null=True, blank=True)
    # education_end_date = models.DateField(null=True, blank=True)
    education = ArrayField(
        JSONField(blank=True, null=True), blank=True, null=True)
    # skills
  #   "skills": [
  #     {
  #       "name": "A category of job skills (e.g. 'Programming Languages')",
  #       "level": "",
  #       "keywords": [
  #                   "Keywords under this category (e.g. 'Java', 'C++', etc)"
  #                   ]
  #     }
  #   ]
    # skill_name = models.CharField(max_length=100, null=True, blank=True)
    # keywords = models.CharField(max_length=20, null=True, blank=True)
    skills = ArrayField(JSONField(blank=True, null=True),
                        blank=True, null=True)
  # User specific
    owner = models.ForeignKey(
        User, related_name="resumes", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
