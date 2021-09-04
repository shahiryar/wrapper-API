# wrapper-API

The repo is self-contained scholarly API. In current it exposes a handler function from `main.py`
Handler function takes in an `event` object.
event object looks like this:
`{"operation": "search_pubs_for", "payload": "Steven A. Cholewiak", "fill": "False"}`
available operations are
- search_pubs_for
- search_author
the payload for both of these functions is a string of Author's name.
Moreover, this function uses proxy to make requests to bypass the scraping threshold for each request.
