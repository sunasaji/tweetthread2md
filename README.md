# Introduction
This python script can convert tweet thread into markdown format.

# Getting Started
1. Get access to the Twitter API. Edit config.py to set consumer_key, consumer_secret, access_token_key, access_token_secret.
2. Prepare Python 3.x and install requests_oauthlib and tzlocal libraries.  
If you are using Ubuntu or Debian, execute ```sudo apt install python3-requests-oauthlib python3-tzlocal```
3. Pass the LAST tweet URL in your thread to this script.  
```./tweetthread2md.py THE_LAST_TWEET_URL_OF_A_THREAD```
4. Markdown formatted tweets will be displayed.

# Output example
```
1st tweet in the thread

[2019/10/27 12:30](https://twitter.com/sunasaji/status/xxxxxxxxxxxxxxxxxxx)

2nd tweet in the thread<br>
<http://example.com>
![image](https://pbs.twimg.com/media/xxxxxxxxxxxxxxx.png)

[2019/10/27 12:31](https://twitter.com/sunasaji/status/xxxxxxxxxxxxxxxxxxx)

```

# License

These codes are licensed under CC0.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

