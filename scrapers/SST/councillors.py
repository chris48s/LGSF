from lgsf.scrapers.councillors import CMISCouncillorScraper


class Scraper(CMISCouncillorScraper):
    base_url = "https://services.sstaffs.gov.uk/cmis/Councillors.aspx"
