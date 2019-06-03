from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import URLValidator


class resume(models.Model):
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
    #     "highlights": null,
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
    label = models.CharField(max_length=10, blank=True)
    # picture = models.ImageField(null=True, upload_to='media')
    email = models.EmailField(max_length=100, unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    degree = models.CharField(max_length=25, blank=True)
    website = models.TextField(validators=[URLValidator()])
    # Summary
    summary = models.CharField(max_length=500, blank=True)
    # "highlights": [
    #     "Bullet-point list items that you would like to include along with (or instead of) a summary paragraph."
    # ],
    highlights = models.CharField(max_length=500, blank=True)
    # Location
    address = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country_code = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=10, blank=True)
    # Profiles *array
    network = models.CharField(max_length=20, blank=True)
    username = models.CharField(max_length=20, blank=True)
    url = models.TextField(validators=[URLValidator()])
    # Work *array
    work_company = models.CharField(max_length=100, blank=True)
    work_position = models.CharField(max_length=100, blank=True)
    worl_website = models.TextField(validators=[URLValidator()])
    work_start_date = models.DateField()
    work_end_date = models.DateField()
    work_summary = models.CharField(max_length=500, blank=True)
    work_highlights = models.CharField(max_length=200, blank=True)
    # Education *array
    institution = models.CharField(max_length=100, blank=True)
    education_area = models.CharField(max_length=100, blank=True)
    study_type = models.CharField(max_length=100, blank=True)
    education_start_date = models.DateField()
    education_end_date = models.DateField()
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
    skill_name = models.CharField(max_length=100, blank=True)
    keywords = models.CharField(max_length=20, blank=True)
  # User specific
    owner = models.ForeignKey(
        User, related_name="resume", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
