from lgsf.scrapers.councillors import CMISCouncillorScraper


class Scraper(CMISCouncillorScraper):
    base_url = "http://ealing.cmis.uk.com/ealing/Councillors.aspx"
