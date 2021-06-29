# Google Scholar Rest API

__This is still in development process 😄__
It may not work properly.

## Deployment
Visit [tiangolo/uwsgi-nginx-flask](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) for more information.

## Routes
### Index : `/`
Example response:
```
{
  "status": "ok",
  "timestamp": "2012-12-12T12:12:12.120000"
}
```
### Search Author by name : `/author/name/<name>` 
### Search Author by name : `/author/id/<scholar_id>` 
Example response:
```
{
  "container_type": "Author",
  "filled": [
    "coauthors",
    "counts",
    "basics",
    "indices",
    "publications"
  ],
  "scholar_id": "ID ID ID",
  "source": null,
  "name": "君の名は。",
  "url_picture": "https://cat.com/cat.jpg",
  "affiliation": "My Home",
  "interests": [
    "Cats"
  ],
  "email_domain": "@ktnis.me",
  "citedby": 5,
  "coauthors": [
    coauthors...
  ],
  "cites_per_year": {
    "2142": 5,
  },
  "citedby5y": 100,
  "hindex": 5,
  "hindex5y": 5,
  "i10index": 5,
  "i10index5y": 5,
  "publications": [
    {
      publications...
    },
  ]
}
```
### Search Publication by name : `/pubs/<name>`
```
{
  "container_type": "Publication",
  "source": null,
  "bib": {
    "title": "turtle turtle turtle turtle turtle turtle turtle",
    "author": [
      "君の名は。",
    ],
    "pub_year": "2042",
    "venue": "The lazy fox…",
    "abstract": "lorem50<tab>"
  },
  "filled": false,
  "gsrank": 1,
  "pub_url": "<url>",
  "author_id": [
    "ID ID ID"
  ],
  "num_citations": 5000000,
  "url_scholarbib": "<url>",
  "url_add_sclib": "<url>",
  "citedby_url": "<url>",
  "url_related_articles": "<url>",
  "eprint_url": "<url>"
}
```

## Contributions
You can open PR if you want :)

## References
- [Scholary](https://scholarly.readthedocs.io/)
- [tiangolo/uwsgi-nginx-flask](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)
