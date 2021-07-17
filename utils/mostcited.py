#!/usr/bin/env python3
# coding: utf-8

# Find most cited papers.
# It writes to `mostcited.yml`, copy those to the `_data/mostcited.yml` after screening.

import random
import itertools
import yaml
from datetime import date, datetime

from scholarly import scholarly, ProxyGenerator

try:
    # for python newer than 2.7
    from collections import OrderedDict
except ImportError:
    # use backport from pypi
    from ordereddict import OrderedDict

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from yaml.representer import SafeRepresenter

_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG


def dict_representer(dumper, data):
    return dumper.represent_dict(data.iteritems())


def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))


Dumper.add_representer(OrderedDict, dict_representer)
Loader.add_constructor(_mapping_tag, dict_constructor)

Dumper.add_representer(str, SafeRepresenter.represent_str)


def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items()
        )

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


def _format_author_list(authors):
    add_dot = []
    for auth in authors:
        name_parts = auth.split()
        if len(name_parts[0]) == 1 or (
            len(name_parts[0]) == 2 and name_parts[0].isupper()
        ):
            new_auth = ".".join(name_parts[0]) + ". " + " ".join(name_parts[1:])
        else:
            new_auth = auth
        add_dot.append(new_auth)
    return add_dot


def _format_author_string(authors, abbreviate_first_name=True):
    res = authors.split(" and ")
    tmp = []
    for r in res:
        name = r.split(", ")[::-1]
        if len(name) > 2 and len(name[1]) == 1:
            name[1] += "."

        if abbreviate_first_name:
            name[0] = name[0][0] + "."

        tmp.append(" ".join(name))

    return tmp


def format_author_list(authors, abbreviate_first_name=True):
    if isinstance(authors, list):
        return _format_author_list(authors)
    else:
        return _format_author_string(
            authors, abbreviate_first_name=abbreviate_first_name
        )


def date_from_string(s):
    if "," in s:
        month_day = s.split("-")[0]
        year = s.split(",")[1]
    else:
        month_day = "January 1"
        year = s
    return datetime.strptime(month_day + " " + year, "%B %d %Y")


def query_generator(search_term, venue, year, num_results, pg, grace_period=0):
    google_search_query = search_term
    query_year = year

    if venue == "CoRL":
        if year == 2019:
            query_year = 2020
        elif year == 2020:
            query_year = 2021

    while True:
        try:
            search_query = scholarly.search_pubs(
                google_search_query,
                year_low=query_year,
                year_high=query_year + grace_period,
                patents=False,
            )

            results = list(itertools.islice(search_query, num_results))

            print("Search URL: ", search_query._url)

            return results, search_query._url
        except Exception as e:
            print("Trying different proxy!")
            pg.get_next_proxy()


force_update = True
use_OR = False
num_search_top_results = 200
num_output_top_results = 10
use_full_author_list = False  # Requires more google queries

update_specific_venue = False
update_venues = ["ICLR"]
update_years = [2016]
# update_years = list(range(2010, 2020))

min_number_of_days_elapsed = int(365 / 2)

# use the free-proxy library
pg = ProxyGenerator()
# pg.FreeProxies()
# to use thor do: sudo service tor start
pg.Tor_External(
    tor_sock_port=9050, tor_control_port=9051, tor_password="myscholarly_password"
)
scholarly.use_proxy(pg)

data_papers = yaml.load(open("../_data/papers.yml", "r"), Loader=Loader)
data_venues = yaml.load(open("../_data/venues.yml", "r"), Loader=Loader)
data_mostcited = yaml.load(open("../_data/mostcited.yml", "r"), Loader=Loader)

random.shuffle(data_papers)

today = date.today()
today_str = today.strftime("%m/%d/%y")

for award in data_papers:
    venue = award["venue"]
    year = award["year"]
    venue_date = date_from_string(award["date"]).date()

    # ignore venue if too recent (since citation numbers won't be representative)
    elapsed_time = today - venue_date
    if elapsed_time.days < min_number_of_days_elapsed:
        print(f"Venue {venue} {year} was too recent: {elapsed_time.days} days.")
        continue

    if update_specific_venue:
        if venue not in update_venues or year not in update_years:
            print(f"Venue {venue} {year} is not supposed to be updated.")
            continue

    # ignore if the last update was today
    existing_entry = next(
        (
            item
            for item in data_mostcited
            if item["venue"] == venue and item["year"] == year
        ),
        None,
    )
    if existing_entry and not force_update:
        last_updated = datetime.strptime(
            existing_entry["last_updated"], "%m/%d/%y"
        ).date()
        if last_updated >= today:
            print(f"Venue {venue} {year} was updated today. Skipping.")
            continue

    # get the proper search terms for google scholar
    search_terms = next((item for item in data_venues if item["name"] == venue), None)
    if not search_terms:
        continue
    search_terms = search_terms["source"]
    if type(search_terms) is not list:
        search_terms = [search_terms]
    print(
        f"Checking: {venue} {year}.  Search terms: {search_terms}".format(venue, year)
    )

    if use_OR:
        google_search_query = " OR ".join(
            ['source:"{}"'.format(search_term) for search_term in search_terms]
        )

        results, search_query_url = query_generator(
            google_search_query,
            venue=venue,
            year=year,
            num_results=num_search_top_results,
            pg=pg,
        )
    else:
        results = []
        for search_term in search_terms:
            google_search_query = 'source:"{}"'.format(search_term)
            results_tmp, search_query_url = query_generator(
                google_search_query,
                venue=venue,
                year=year,
                num_results=num_search_top_results,
                pg=pg,
            )
            results.extend(results_tmp)

    # add best papers to search results
    # this requires a separate search query -- gscholar doesn't understand OR here (?)
    exclude_awards = ["Test of Time", "Retrospective Most Impactful Paper"]
    search_terms_best_papers = [
        paper["title"]
        for paper in award["awards"]
        if not any([paper["award"].startswith(x) for x in exclude_awards])
    ]
    for query in search_terms_best_papers:
        best_paper_results, _ = query_generator(
            '"{}"'.format(query),
            venue="",
            year=year,
            grace_period=1,  # some grace period, some conference proceedings are published the next year
            num_results=1,
            pg=pg,
        )
        results.extend(best_paper_results)

    # sort by num citations
    sorted_results_tmp = sorted(results, key=lambda k: k["num_citations"], reverse=True)

    # get more details
    sorted_results = []
    new_entry_paper_titles = []
    for s in sorted_results_tmp:
        # avoid duplicates
        if s["bib"]["title"] not in new_entry_paper_titles and (
            "eprint_url" in s or "pub_url" in s
        ):
            new_entry_paper_titles.append(s["bib"]["title"])

            if use_full_author_list:
                # filling is required to get all authors
                new_s = scholarly.fill(s)
                sorted_results.append(new_s)
            else:
                sorted_results.append(s)

            if len(sorted_results) >= num_output_top_results:
                break

    new_entry = OrderedDict()
    new_entry["venue"] = venue
    new_entry["year"] = year
    new_entry["last_updated"] = today_str
    new_entry["source"] = "https://scholar.google.com{0}".format(search_query_url)
    new_entry["mostcited"] = []
    for s in sorted_results:
        print("Rank in search results:", results.index(s))
        # scholarly.pprint(s)
        paper = OrderedDict()
        paper["citations"] = s["num_citations"]
        paper["title"] = s["bib"]["title"]
        paper["author"] = ", ".join(format_author_list(s["bib"]["author"]))
        for link in ["eprint_url", "pub_url"]:
            if link in s:
                paper["link"] = s[link]
                break

        new_entry["mostcited"].append(paper)

    # replace or append new entry
    if existing_entry:
        # find index
        existing_index = [
            index
            for index, item in enumerate(data_mostcited)
            if item["venue"] == venue and item["year"] == year
        ]
        data_mostcited[existing_index[0]] = new_entry
    else:
        data_mostcited.append(new_entry)


# write to yaml file
with open("mostcited.yml", "w") as outfile:
    for line in ordered_dump(
        data_mostcited,
        Dumper=yaml.SafeDumper,
        default_flow_style=False,
        explicit_start=True,
        allow_unicode=True,
    ).splitlines():
        outfile.write(line.replace("- venue:", "\n- venue:"))
        outfile.write("\n")

# {'author_id': ['0oIAvO8AAAAJ', '', 'zGOh8jYAAAAJ', '6gd_QS0AAAAJ'],
# 'bib': {'abstract': "Bridging thereality gap'that separates simulated "
#                     'robotics from experiments on hardware could accelerate '
#                     'robotic research through improved data availability. '
#                     'This paper explores domain randomization, a simple '
#                     'technique for training models on simulated images that',
#         'author': ['J Tobin', 'R Fong', 'A Ray', 'J Schneider'],
#         'pub_year': '2017',
#         'title': 'Domain randomization for transferring deep neural networks '
#                  'from simulation to the real world',
#         'venue': '… and Systems (IROS)'},
# 'citedby_url': '/scholar?cites=15526924004125954281&as_sdt=5,33&sciodt=1,33&hl=en',
# 'eprint_url': 'https://arxiv.org/pdf/1703.06907',
# 'filled': False,
# 'gsrank': 5,
# 'num_citations': 964,
# 'pub_url': 'https://ieeexplore.ieee.org/abstract/document/8202133/',
# 'source': 'PUBLICATION_SEARCH_SNIPPET',
