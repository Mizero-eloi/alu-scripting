#!/usr/bin/python3
"""Print titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print each hot post title on its own line, or None if subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(
        url,
        headers=headers,
        params={'limit': 10},
        allow_redirects=False,
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        children = response.json().get('data', {}).get('children', [])
    except (ValueError, TypeError):
        print(None)
        return

    for post in children[:10]:
        title = post.get('data', {}).get('title')
        if title is not None:
            print(title)
