from django.apps import apps as django_apps
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import MALE, FEMALE
from .consent_object_validator import ConsentObjectValidator

edc_protocol = django_apps.get_app_config('edc_protocol')

v1 = Consent(
    'flourish_child.childdummysubjectconsent',
    version='1',
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,
    age_min=30,
    age_is_adult=30,
    age_max=110,
    gender=[MALE, FEMALE])

v2 = Consent(
    'flourish_child.childdummysubjectconsent',
    version='2',
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,
    age_min=30,
    age_is_adult=30,
    age_max=110,
    gender=[MALE, FEMALE])

site_consents.validator_cls = ConsentObjectValidator

site_consents.register(v1)
site_consents.register(v2)
