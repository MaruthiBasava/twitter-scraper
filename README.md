# Twitter Scraper
Makes scraping tweets easy with one line of code and returns it in json; Emulates twitter without twitter api.

# Requirements
* MUST HAVE PYTHON 2.7 INSTALLED

# Libraries 
```bash
pip install beautifulsoup4
pip install requests
pip install json
```

# Example

```python
mar = TwitterAccount('lnitiator') # twitter handle as parameter
mar.get_all_tweets() # returns all present tweets in json
```
