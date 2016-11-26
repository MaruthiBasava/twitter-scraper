# Twitter Scraper
Makes scraping tweets easy with one line of code and returns it in json; Includes more.

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
from twitter import TwitterAccount

mar = TwitterAccount('lnitiator') # twitter handle as parameter
mar.get_all_tweets() # returns all present tweets in json
```
# Methods
```python
TwitterAccount.get_url() # return account url
TwitterAccount.get_all_tweets() # returns all present tweets in json 
TwitterAccount.get_handle() # returns twitter handle
TwitterAccount.get_all_following_handles() # returns all following twitter handles
TwitterAccount.get_follower(index) # returns follower of that index
TwitterAccount.get_tweet(index) # returns tweet of that index
TwitterAccount.follow(handle) # follows a twitter account with a handle as a parameter
TwitterAccount.get_following() # returns all following
TwitterAccount.get_followers() # return all followers
TwitterAccount.get_all_follower_handle() # returns all follower handles
```
