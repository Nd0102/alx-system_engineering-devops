#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
            "limit": 10
    }
                                            
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 404:
            print("None")
            return

        results = response.json().get("data", {}).get("children", [])

        if not results:
            print("None")
            return

        for post in results:
            print(post.get("data", {}).get("title"))
    except requests.RequestException as e:
        print("None")
