from bs4 import BeautifulSoup
import requests
import json

base_url = "https://twitter.com/"

class TwitterScraper:

    @classmethod
    def scrape(cls, url):
        result = requests.get(url)
        return BeautifulSoup(result.text, "html.parser")

class TwitterAccount:

    def __init__(self, handle):
        self.handle = handle
        self._src_acc_code = self.pull_account()
        self.tweets = self._pull_all_tweets()
        self.pinned_tweet = self.get_tweet(0)

        self.followers = []
        self.following = []

    def get_url(self):
        return base_url + self.handle + '/'

    def pull_account(self):
        return TwitterScraper.scrape(self.get_url())

    def _pull_all_tweets(self):
        tweets = self._src_acc_code.find_all('p', class_='tweet-text')
        dates = self._src_acc_code.find_all('span', class_='_timestamp')
        return [TwitterTweet(tweet.text, date.text) for tweet, date in zip(tweets,dates)]

    def _pull_all_followers(self):
        print(self.get_url()+"followers")
        soup = TwitterScraper.scrape("https://twitter.com/lnitiator/followers")
        print(soup)

        follower_handles = soup.find_all('span', class_="ProfileCard-screennameLink")
        return [follower_handle.text for follower_handle in follower_handles]

    def get_all_tweets(self):
        return [tweet.get_pretty_tweet() for tweet in self.tweets]

    def get_all_following_handles(self):
        return [following.get_handle() for following in self.following]

    def get_follower(self, index):
        return self.followers[index]

    def get_tweet(self, index):
        return self.tweets[index]

    def get_handle(self):
        return self.handle

    def follow(self, handle):
        self.following.append(handle)

    def get_following(self):
        return self.following.count()

    def get_followers(self):
        return self.followers.count()

    def get_all_follower_handle(self):
        return [ follower.get_handle() for follower in self.followers ]

class TwitterTweet:

    def __init__(self, tweet, date):
        self.tweet = tweet
        self.date = date

    def update(self, tweet, date):
        self.tweet = tweet
        self.date = date

    def get_tweet(self):
        return {
            "tweet": self.tweet,
            "date": self.date
        }

    def get_pretty_tweet(self):
        print(json.dumps(self.get_tweet(), sort_keys=True,
                  indent=4, separators=(',', ': ')))


class TwitterFollower(TwitterAccount):

    def __init__(self, handle):
        super(TwitterFollower, self).__init__(handle)




class TwitterFollowing(TwitterAccount):

    def __init__(self, handle):
        super(TwitterFollowing, self).__init__(handle)