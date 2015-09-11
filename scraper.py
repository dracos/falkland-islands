import scraperwiki
import lxml.html


def area_id(area):
  return 'ocd-division/country:fk/constituency:%s' % area.lower().replace(' ','-')


def scrape_term(t):
    html = scraperwiki.scrape(t['source'])
    root = lxml.html.fromstring(html)
    for a in root.cssselect('a[href*="Symbol_confirmed"]'):
        tds = a.xpath('ancestor::tr/td')
        area = a.xpath('ancestor::table//th[@colspan="6"]/a//text()')[0]
        area = area.replace(' result', '')
        who = tds[1].text_content().strip()
        wikiname = tds[1].xpath('.//a')[0].get('title')
        data = {
            'name': who,
            'wikiname': wikiname,
            'area': area,
            'area_id': area_id(area),
            'party': 'Independent',
            'term': t['id'],
            'source': t['source']
        }
        scraperwiki.sqlite.save(['name', 'term'], data)


terms = [
    {
        'id': 2013,
        'name': '2013 election',
        'start_date': '2013-11-07',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_2013',
    },
    {
        'id': 2009,
        'name': '2009 election',
        'start_date': '2009-11-05',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_2009',
    },
    {
        'id': 2005,
        'name': '2005 election',
        'start_date': '2005-11-17',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_2005',
    },
    {
        'id': 2001,
        'name': '2001 election',
        'start_date': '2001-11-22',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_2001',
    },
    {
        'id': 1997,
        'name': '1997 election',
        'start_date': '1997-10-09',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_1997',
    },
    {
        'id': 1993,
        'name': '1993 election',
        'start_date': '1993-10-14',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_1993',
    },
    {
        'id': 1989,
        'name': '1989 election',
        'start_date': '1989-10-12',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_1989',
    },
    {
        'id': 1985,
        'name': '1985 election',
        'start_date': '1985-10-03',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_1985',
    },
    {
        'id': 1981,
        'name': '1981 election',
        'start_date': '1981-10-01',
        'source': 'https://en.wikipedia.org/wiki/Falkland_Islands_general_election,_1981',
    },
]

scraperwiki.sqlite.save(['id'], terms, 'terms')

for term in terms:
    scrape_term(term)
