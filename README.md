<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/16024979/207469449-f9f36114-6e4d-4549-bf18-bd90a0e4efde.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/16024979/207469461-8eb4332a-d530-455f-9832-4bad74acf5b9.png">
  <img alt=".tr domains list" src="https://user-images.githubusercontent.com/16024979/207469461-8eb4332a-d530-455f-9832-4bad74acf5b9.png">
</picture>

List of `.tr` domains. The number of domains currently in this repo is _`200.515`_.

> _[.tr](https://en.wikipedia.org/wiki/.tr) is the Internet country code top-level domain (ccTLD) for [Turkey](https://www.cia.gov/the-world-factbook/countries/turkey-turkiye/). Second-level domains are prohibited by current policy. [nic.tr](https://icannwiki.org/NIC.TR) is the only second-level domain name. For easier classification, only third-level domain names are given, such as .com.tr, .gov.tr._

## Gathering Data

### Enumeration Pipeline [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agmmnn/tr-domains/blob/master/tr-domains-pipeline.ipynb)

1. Domain enumeration with [OWASP/Amass](https://github.com/OWASP/Amass) and [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)
1. Merge lists, clean non-root domains
1. Validating the domain list with [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx)
1. Generating json file and url list from httpx output

### Data Content

- `.json` result of httpx query. It contains information such as timestamp, hash, webserver, host informations and so on.
- `.txt` files contains only urls.

## Domains

### Official Related or Document Required

| Domain      | Reserved for                                                                               | Full Output                            | Only Urls                            | Count    |
| ----------- | ------------------------------------------------------------------------------------------ | -------------------------------------- | ------------------------------------ | -------- |
| `gov.tr`    | the Government of Turkey and state institutions/organizations                              | [`.json`](/data_docreq/gov.tr.json)    | [`.txt`](/data_docreq/gov.tr.txt)    | _`2582`_ |
| `bel.tr`    | provincial, district, and town municipal organizations and governments                     | [`.json`](/data_docreq/bel.tr.json)    | [`.txt`](/data_docreq/bel.tr.txt)    | _`1231`_ |
| `pol.tr`    | the General Directorate of Security and police                                             | [`.json`](/data_docreq/pol.tr.json)    | [`.txt`](/data_docreq/pol.tr.txt)    | _`165`_  |
| `edu.tr`    | higher education institutions approved by the Council of Higher Education                  | [`.json`](/data_docreq/edu.tr.json)    | [`.txt`](/data_docreq/edu.tr.txt)    | _`318`_  |
| `k12.tr`    | schools approved by the Ministry of National Education                                     | [`.json`](/data_docreq/k12.tr.json)    | [`.txt`](/data_docreq/k12.tr.txt)    | _`927`_  |
| `av.tr`     | freelance lawyers, law firms and attorney partnerships                                     | [`.json`](/data_docreq/av.tr.json)     | [`.txt`](/data_docreq/av.tr.txt)     | _`4116`_ |
| `dr.tr`     | medical doctors, medical partnerships, hospitals, and healthcare services                  | [`.json`](/data_docreq/dr.tr.json)     | [`.txt`](/data_docreq/dr.tr.txt)     | _`41`_   |
| `tsk.tr`\*  | the Turkish Armed Forces                                                                   | -                                      | -                                    | _`16`_   |
| `gov.ct.tr` | the Government of Turkish Republic of Northern Cyprus and state institutions/organizations | [`.json`](/data_docreq/gov.ct.tr.json) | [`.txt`](/data_docreq/gov.ct.tr.txt) | _`181`_  |
|             |                                                                                            |                                        |                                      | _`9577`_ |

> \*have to manually select webpages and subdomains, so it is not included.

### No Document Required

| Domain    | Definition                                                                               | Full Output                           | Only Urls                         | Count      |
| --------- | ---------------------------------------------------------------------------------------- | ------------------------------------- | --------------------------------- | ---------- |
| `com.tr`  | commercial entities                                                                      | [`.json`](/data_nodoc/com.tr.json.7z) | [`.txt`](/data_nodoc/com.tr.txt)  | _`169798`_ |
| `net.tr`  | network operators/providers, as well as internet-related access services                 | [`.json`](/data_nodoc/net.tr.json)    | [`.txt`](/data_nodoc/net.tr.txt)  | _`1600`_   |
| `org.tr`  | nonprofit entities such as foundations, associations, and non-governmental organizations | [`.json`](/data_nodoc/org.tr.json)    | [`.txt`](/data_nodoc/org.tr.txt)  | _`7172`_   |
| `biz.tr`  | commercial entities                                                                      | [`.json`](/data_nodoc/biz.tr.json)    | [`.txt`](/data_nodoc/biz.tr.txt)  | _`911`_    |
| `info.tr` | informational websites                                                                   | [`.json`](/data_nodoc/info.tr.json)   | [`.txt`](/data_nodoc/info.tr.txt) | _`653`_    |
| `tv.tr`   | entities in the television industry                                                      | [`.json`](/data_nodoc/tv.tr.json)     | [`.txt`](/data_nodoc/tv.tr.txt)   | _`238`_    |
| `gen.tr`  | general use                                                                              | [`.json`](/data_nodoc/gen.tr.json)    | [`.txt`](/data_nodoc/gen.tr.txt)  | _`5432`_   |
| `web.tr`  | general use                                                                              | [`.json`](/data_nodoc/web.tr.json)    | [`.txt`](/data_nodoc/web.tr.txt)  | _`2631`_   |
| `name.tr` | individual/personal use                                                                  | [`.json`](/data_nodoc/name.tr.json)   | [`.txt`](/data_nodoc/name.tr.txt) | _`1039`_   |
| `bbs.tr`  | entities providing BBS services                                                          | [`.json`](/data_nodoc/bbs.tr.json)    | [`.txt`](/data_nodoc/bbs.tr.txt)  | _`66`_     |
|           |                                                                                          |                                       |                                   | _`189540`_ |

### Other Turkish Domains

| Domain                                         | Definition                                                                                                                                                         | Full Output                          | Only Urls                          | Count    |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ | ---------------------------------- | -------- |
| [`.istanbul`](https://icannwiki.org/.istanbul) | a community-based sponsored top-level domain by [Istanbul Metropolitan Municipality](https://www.ibb.istanbul/en) -[wiki](https://en.wikipedia.org/wiki/.istanbul) | [`.json`](/data_other/istanbul.json) | [`.txt`](/data_other/istanbul.txt) | _`498`_  |
| [`.ist`](https://icannwiki.org/.ist)           | a community-based sponsored top-level domain by [Istanbul Metropolitan Municipality](https://www.ibb.istanbul/en) -[wiki](https://en.wikipedia.org/wiki/.istanbul) | [`.json`](/data_other/ist.json)      | [`.txt`](/data_other/ist.txt)      | _`916`_  |
|                                                |                                                                                                                                                                    |                                      |                                    | _`1414`_ |

_Total: `200.531`_

## Useful

### Wikidata Queries

- Metropolitan municipalities in Turkey with websites: [query](https://query.wikidata.org/#SELECT%20%3Fitem%20%3FitemLabel%20%3Fwebsite%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ2716259.%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%20%3Fwebsite%20.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Ctr%22.%20%7D%0A%7D%0AORDER%20BY%20%3Fitem)
- All museums in Turkey with websites, coordinates: [query](https://query.wikidata.org/#%23t%C3%BCrkiyedeki%28Q43%29%20m%C3%BCzeler%28Q33506%29%0ASELECT%20DISTINCT%20%3Fitem%20%3Fname%20%3Fweb%20%3Fcoord%20%3Flat%20%3Flon%0AWHERE%0A%7B%0A%20hint%3AQuery%20hint%3Aoptimizer%20%22None%22%20.%0A%20%3Fitem%20wdt%3AP131%2a%20wd%3AQ43%20.%0A%20%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ33506%20.%0A%20%3Fitem%20wdt%3AP625%20%3Fcoord%20.%0A%20%3Fitem%20p%3AP625%20%3Fcoordinate%20.%0A%20%3Fcoordinate%20psv%3AP625%20%3Fcoordinate_node%20.%0A%20%3Fcoordinate_node%20wikibase%3AgeoLatitude%20%3Flat%20.%0A%20%3Fcoordinate_node%20wikibase%3AgeoLongitude%20%3Flon%20.%0A%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%20%3Fweb%20.%7D%0A%20SERVICE%20wikibase%3Alabel%20%7B%0A%20bd%3AserviceParam%20wikibase%3Alanguage%20%22tr%22%20.%0A%20%3Fitem%20rdfs%3Alabel%20%3Fname%0A%20%7D%0A%7D%0AORDER%20BY%20ASC%20%28%3Fname%29)
- All universities in Turkey with websites, coordinates: [query](https://query.wikidata.org/#%23t%C3%BCrkiye%28Q43%29%20%C3%BCniversite%28Q33506%29%0ASELECT%20DISTINCT%20%3Fitem%20%3Fname%20%3Fweb%20%3Fcoord%0AWHERE%0A%7B%0A%20hint%3AQuery%20hint%3Aoptimizer%20%22None%22%20.%0A%20%3Fitem%20wdt%3AP131%2a%20wd%3AQ43%20.%0A%20%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3918%20.%0A%20OPTIONAL%7B%3Fitem%20wdt%3AP625%20%3Fcoord%20.%7D%0A%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%20%3Fweb%20.%7D%0A%20SERVICE%20wikibase%3Alabel%20%7B%0A%20bd%3AserviceParam%20wikibase%3Alanguage%20%22tr%22%20.%0A%20%3Fitem%20rdfs%3Alabel%20%3Fname%0A%20%7D%0A%7D)

### Censys Search

- search.censys.io/[services.tls.certificates.leaf_data.names: \*.com.tr](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.tls.certificates.leaf_data.names%3A+*.com.tr)
- search.censys.io/[location.country: Turkey](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=location.country%3A+Turkey)

### Related Repos

- [cisagov/dotgov-data](https://github.com/cisagov/dotgov-data) - Official list of .gov domains.
- [robbi5/german-gov-domains](https://github.com/robbi5/german-gov-domains) - An incomplete listing of german government domains.
- [anroots/ee-domains](https://github.com/anroots/ee-domains) - List of Estonian top-level internet domains.
- [cygenta/top10million](https://github.com/cygenta/top10million) - A repository of the 10 million live most popular websites.
- [zakird/crux-top-lists](https://github.com/zakird/crux-top-lists) - Cached Chrome top million websites.

### Others

- [Hipo/University Domains List API (filter:turkey)](http://universities.hipolabs.com/search?country=turkey) ([repo](https://github.com/Hipo/university-domains-list))

## Contributing

Your contributions are welcome. If you want to contribute to this list send a pull request or just open a new issue.
