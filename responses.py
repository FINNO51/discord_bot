import snscrape.modules.twitter as sntwitter
import re


def handle_response(message) -> str:
    p_message = message
    if 'vm.tiktok' in p_message:
        tiktok_id = re.findall('.*//vm.tiktok.com/([a-zA-Z0-9]*).*', p_message)
        return "https://vm.vxtiktok.com/" + tiktok_id[0] + "/"

    if 'www.tiktok' in p_message and '/video/' in p_message:
        tiktok_id__ = re.findall('.*//www.tiktok.com/@([^\s]*)\s*', p_message)
        return "https://www.vxtiktok.com/@" + tiktok_id__[0] + "/"

    if '/twitter.com' in p_message and '/status/' in p_message:
        tweet_id = re.findall('.*//.*/.*/.*/([0-9]*).*', p_message)
        tweets = sntwitter.TwitterTweetScraper(tweet_id[0])
        for tweet in tweets.get_items():
            if 'Video' in str(tweet.media[0]):
                return "https://vxtwitter.com/i/status/" + tweet_id[0] + "/"
        
        

    #  return 'Yeah, I don\'t know. Try typing "!help".'
