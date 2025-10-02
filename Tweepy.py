import tweepy

# Replace these with your actual API keys/secrets
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

def get_trending_topics(woeid=1, exclude_hashtags=False):
    """
    Fetch trending topics for a given location.
    woeid = “Where On Earth ID” (1 = worldwide)
    If exclude_hashtags = True, filters out hashtag trends.
    """
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Use get_place_trends (Tweepy) to fetch trends for the location
    trends = api.get_place_trends(id=woeid, exclude="hashtags" if exclude_hashtags else None)
    # trends is a list; the first item contains “trends” key
    if not trends:
        return []
    trend_list = trends[0].get("trends", [])
    # Return list of trend names and maybe volume
    return [(t["name"], t.get("tweet_volume")) for t in trend_list]

if __name__ == "__main__":
    # WOEID 1 is for "Worldwide"
    trending = get_trending_topics(woeid=1)
    print("Trending Topics (Worldwide):")
    for name, volume in trending[:10]:
        print(f"{name} — volume: {volume}")
