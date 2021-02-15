import tweepy
import config
import time

auth = tweepy.OAuthHandler(config.TWITTER_API_KEY,
                           config.TWITTER_API_KEY_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN,
                      config.TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)


def dm_them(users):
    for user in users:
        api.send_direct_message(user, config.DM_TEXT)
        print(f'DM sent to : {user}')
        time.sleep(3)


def start():
    # status = api.rate_limit_status()
    # print(status['resources']['direct_messages'])
    print('Getting followers ...')
    cur = -1
    results = api.followers(config.TARGET_USERNAME, cursor=cur)
    while True:
        results = api.followers(config.TARGET_USERNAME, cursor=cur)
        cur = results[1][1]
        followers = results[0].ids()
        dm_them(followers)
        if len(followers) == 0:
            break


if __name__ == '__main__':
    start()
