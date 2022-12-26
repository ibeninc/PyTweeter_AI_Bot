import openai, tweepy, random
# import API keys
from keys import *
# import prompts json
from promptSample import *

class AiBot():

    # Twitter Auth 
    auth = tweepy.OAuthHandler(twitter_key, twitter_secret)
    auth.set_access_token(twitter_access_token, twitter_access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

   

    def __init__(self):
        error = 1
        while(error == 1):
            tweet = self.create_tweet()
            try:
                error = 0
                self.api.update_status(tweet)
            except:
                error = 1
    
    def create_tweet(self):
        chosen_prompt = random.choice(prompts)
        text = chosen_prompt["text"]
        hashtags = chosen_prompt["hashtag"]

        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=text,
            max_tokens=64,
        )

        tweet = response.choices[0].text
        tweet = tweet + " " + hashtags
        return tweet


twitter = AiBot()
twitter.create_tweet()
