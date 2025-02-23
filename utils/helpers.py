from utils.constants import all_countries


def get_full_country_name(country_code):
    return all_countries.get(country_code)
