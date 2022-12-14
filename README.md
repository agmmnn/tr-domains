<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/16024979/207469449-f9f36114-6e4d-4549-bf18-bd90a0e4efde.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/16024979/207469461-8eb4332a-d530-455f-9832-4bad74acf5b9.png">
  <img alt=".tr domains list" src="https://user-images.githubusercontent.com/16024979/207469461-8eb4332a-d530-455f-9832-4bad74acf5b9.png">
</picture>

List of .tr domains.

_[.tr](https://en.wikipedia.org/wiki/.tr) is the Internet country code top-level domain (ccTLD) for [Turkey](https://www.cia.gov/the-world-factbook/countries/turkey-turkiye/). [nic.tr](https://icannwiki.org/NIC.TR) is the only second-level domain name, other second-level domains are prohibited. For easier classification, only third-level domain names are given, such as .com.tr, .gov.tr._ In this case it is easier to use the subdomain enumeration tools.

## Gathering Data

### Enumeration Pipeline [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agmmnn/tr-domains/blob/master/tr-domain-enumeration-pipeline.ipynb)

1. Domain enumeration with [OWASP/Amass](https://github.com/OWASP/Amass) and [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)
1. Merge lists, clean non-root domains
1. Validating the domain list with [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx)
1. Generating json file and url list from httpx output

### Data Content

- `.json` result of httpx query. It contains information such as timestamp, hash, webserver, host informations and so on.
- `.txt` files contains only urls.

## Domains

### Official Related or Document Required

| Domain      | Reserved for                                                                               | Full Output                       | Only Urls                       |
| ----------- | ------------------------------------------------------------------------------------------ | --------------------------------- | ------------------------------- |
| `gov.tr`    | the Government of Turkey and state institutions/organizations                              | [.json](/data_docreq/gov.tr.json) | [.txt](/data_docreq/gov.tr.txt) |
| `bel.tr`    | provincial, district, and town municipal organizations and governments                     | [.json](/data_docreq/bel.tr.json) | [.txt](/data_docreq/bel.tr.txt) |
| `pol.tr`    | the General Directorate of Security and police                                             | [.json](/data_docreq/pol.tr.json) | [.txt](/data_docreq/pol.tr.txt) |
| `edu.tr`    | higher education institutions approved by the Council of Higher Education                  | [.json](/data_docreq/edu.tr.json) | [.txt](/data_docreq/edu.tr.txt) |
| `k12.tr`    | schools approved by the Ministry of National Education                                     | [.json](/data_docreq/k12.tr.json) | [.txt](/data_docreq/k12.tr.txt) |
| `av.tr`     | freelance lawyers, law firms and attorney partnerships                                     | [.json](/data_docreq/av.tr.json)  | [.txt](/data_docreq/av.tr.txt)  |
| `dr.tr`     | medical doctors, medical partnerships, hospitals, and healthcare services                  | [.json](/data_docreq/dr.tr.json)  | [.txt](/data_docreq/dr.tr.txt)  |
| `tsk.tr`    | the Turkish Armed Forces                                                                   | -                                 | -                               |
| `gov.ct.tr` | the Government of Turkish Republic of Northern Cyprus and state institutions/organizations | [.json](/data_docreq/gov.tr.json) | [.txt](/data_docreq/gov.tr.txt) |

### No Document Required

| Domain    | Definition                                                                               | Full Output                       | Only Urls                       |
| --------- | ---------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------- |
| `com.tr`  |                                                                                          | [.json](/data_nodoc/com.tr.json)  | [.txt](/data_nodoc/com.tr.txt)  |
| `net.tr`  | network operators/providers, as well as internet-related access services                 | [.json](/data_nodoc/net.tr.json)  | [.txt](/data_nodoc/net.tr.txt)  |
| `org.tr`  | nonprofit entities such as foundations, associations, and non-governmental organizations | [.json](/data_nodoc/org.tr.json)  | [.txt](/data_nodoc/org.tr.txt)  |
| `biz.tr`  | commercial entities                                                                      | [.json](/data_nodoc/biz.tr.json)  | [.txt](/data_nodoc/biz.tr.txt)  |
| `info.tr` | informational websites                                                                   | [.json](/data_nodoc/info.tr.json) | [.txt](/data_nodoc/info.tr.txt) |
| `tv.tr`   | entities in the television industry                                                      | [.json](/data_nodoc/tv.tr.json)   | [.txt](/data_nodoc/tv.tr.txt)   |
| `gen.tr`  | general use                                                                              | [.json](/data_nodoc/gen.tr.json)  | [.txt](/data_nodoc/gen.tr.txt)  |
| `web.tr`  | general use                                                                              | [.json](/data_nodoc/web.tr.json)  | [.txt](/data_nodoc/web.tr.txt)  |
| `name.tr` | individual/personal use                                                                  | [.json](/data_nodoc/name.tr.json) | [.txt](/data_nodoc/name.tr.txt) |
| `bbs.tr`  | entities providing BBS services                                                          | [.json](/data_nodoc/bbs.tr.json)  | [.txt](/data_nodoc/bbs.tr.txt)  |

### Other Turkish Domains

| Domain                                         | Definition                                                                                                                                                         | Full Output                        | Only Urls                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- | -------------------------------- |
| [`.istanbul`](https://icannwiki.org/.istanbul) | a community-based sponsored top-level domain by [Istanbul Metropolitan Municipality](https://www.ibb.istanbul/en) -[wiki](https://en.wikipedia.org/wiki/.istanbul) | [.json](/data_other/istanbul.json) | [.txt](/data_other/istanbul.txt) |
| [`.ist`](https://icannwiki.org/.ist)           | a community-based sponsored top-level domain by [Istanbul Metropolitan Municipality](https://www.ibb.istanbul/en) -[wiki](https://en.wikipedia.org/wiki/.istanbul) | [.json](/data_other/ist.json)      | [.txt](/data_other/ist.txt)      |

## Useful

### Wikidata Queries

- Metropolitan municipalities in Turkey and their websites: [query](https://query.wikidata.org/#SELECT%20%3Fitem%20%3FitemLabel%20%3Fwebsite%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ2716259.%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%20%3Fwebsite%20.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Ctr%22.%20%7D%0A%7D%0AORDER%20BY%20%3Fitem)
- All museums in Turkey and their websites: [query](https://query.wikidata.org/#%23t%C3%BCrkiyedeki%28Q43%29%20m%C3%BCzeler%28Q33506%29%0ASELECT%20DISTINCT%20%3Fitem%20%3Fname%20%3Fweb%20%3Fcoord%20%3Flat%20%3Flon%0AWHERE%0A%7B%0A%20hint%3AQuery%20hint%3Aoptimizer%20%22None%22%20.%0A%20%3Fitem%20wdt%3AP131%2a%20wd%3AQ43%20.%0A%20%3Fitem%20wdt%3AP31%2Fwdt%3AP279%2a%20wd%3AQ33506%20.%0A%20%3Fitem%20wdt%3AP625%20%3Fcoord%20.%0A%20%3Fitem%20p%3AP625%20%3Fcoordinate%20.%0A%20%3Fcoordinate%20psv%3AP625%20%3Fcoordinate_node%20.%0A%20%3Fcoordinate_node%20wikibase%3AgeoLatitude%20%3Flat%20.%0A%20%3Fcoordinate_node%20wikibase%3AgeoLongitude%20%3Flon%20.%0A%20OPTIONAL%7B%3Fitem%20wdt%3AP856%20%20%3Fweb%20.%7D%0A%20SERVICE%20wikibase%3Alabel%20%7B%0A%20bd%3AserviceParam%20wikibase%3Alanguage%20%22tr%22%20.%0A%20%3Fitem%20rdfs%3Alabel%20%3Fname%0A%20%7D%0A%7D%0AORDER%20BY%20ASC%20%28%3Fname%29)

### Censys Search

- search.censys.io/[services.tls.certificates.leaf_data.names: \*.com.tr](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=services.tls.certificates.leaf_data.names%3A+*.com.tr)
- search.censys.io/[location.country: Turkey](https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q=location.country%3A+Turkey)

### Related Repos

- [cisagov/dotgov-data](https://github.com/cisagov/dotgov-data) - Official list of .gov domains.
- [robbi5/german-gov-domains](https://github.com/robbi5/german-gov-domains) - An incomplete listing of german government domains.

## Contributing

Your contributions are welcome. If you want to contribute to this list send a pull request or just open a new issue.
