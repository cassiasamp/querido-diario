from datetime import date

from gazette.spiders.base.doem import DoemGazetteSpider


class BaMascoteSpider(DoemGazetteSpider):
    TERRITORY_ID = "2920908"
    name = "ba_mascote"
    state_city_url_part = "ba/mascote"
    start_date = date(2010, 1, 4)
