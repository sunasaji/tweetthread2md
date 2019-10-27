#!/usr/bin/env python

#   This software has been dedicated to the public domain under the CC0
#   public domain dedication.
#
#   To the extent possible under law, the person who associated CC0 with
#   this script has waived all copyright and related or neighboring rights.
#
#   You should have received a copy of the CC0 legalcode along with this
#   work in doc/cc0.txt.  If not, see
#      <http://creativecommons.org/publicdomain/zero/1.0/>.

import json, config
from requests_oauthlib import OAuth1Session
from tzlocal import get_localzone
from sys import argv
from re import search
from datetime import datetime

localzone = get_localzone()

api = OAuth1Session(
    config.consumer_key,
    config.consumer_secret,
    config.access_token_key,
    config.access_token_secret
)

endpoint_url = 'https://api.twitter.com/1.1/statuses/show.json'

params = {
    'include_entities' : True,
    'tweet_mode' : 'extended',
    'trim_user' : True
}

def get_tweet_recursively(username, tweet_id):
    r = api.get(endpoint_url + '?id=' + tweet_id, params=params)
    tweet = r.json()
    result = ''

    if tweet['in_reply_to_status_id_str']:
        result += get_tweet_recursively(
            tweet['in_reply_to_screen_name'],
            tweet['in_reply_to_status_id_str'])

    tweet_text = tweet['full_text']

    if 'urls' in tweet['entities'].keys():
        for url in tweet['entities']['urls']:
            tweet_text = tweet_text.replace(
                url['url'], "<%s>" % url['expanded_url'])

    if 'extended_entities' in tweet:
        if 'media' in tweet['extended_entities'].keys():
            for media in tweet['extended_entities']['media']:
                tweet_text = tweet_text.replace(
                    media['url'], "![image](%s)" % media['media_url_https'])

    tweet_lines = tweet_text.splitlines()
    tweet_text = "<br>\n".join(tweet_lines)

    created_at = datetime.strptime(
        tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
    created_at_local = created_at.astimezone(localzone).strftime(
        '%Y/%m/%d %H:%M')
    tweet_url = 'https://twitter.com/' + username + '/status/' + tweet['id_str']

    result += tweet_text + '\n\n[' + created_at_local + '](' + tweet_url + ')\n\n'
    return result

    #print(json.dumps(tweet, indent=4, ensure_ascii=False))

def main():

    usage = 'Usage: %s URL_OF_THE_LAST_TWEET_IN_A_THREAD' % argv[0]

    if len(argv) != 2:
        return usage

    tweet_url = argv[1]
    match = search('https://twitter.com/(.+)/status/([0-9]+)', tweet_url)
    if match != None:
        return get_tweet_recursively(match.group(1), match.group(2))
    else:
        return usage

if __name__ == '__main__':
    result = main()
    print(result)
