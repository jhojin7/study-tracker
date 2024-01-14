from db import DB
import time
import requests
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup

from config import Config

# import selenium.webdriver.chrome.webdriver as webdriver
# driver = webdriver.WebDriver()
# driver.get()


class StatusCrawler:
    # Config.RESULT
    # print(*result_types.items(), sep='\n')

    def __init__(self, uid):
        self.uid = uid
        self.init_url = f"https://www.acmicpc.net/status?user_id={self.uid}"

    def get_soup_http(self, url):
        # return BeautifulSoup(open("status.html", 'r'), "lxml")
        resp = requests.get(url, headers=Config.headers,)
        html = resp.text
        if resp.status_code != 200:
            print(resp.url)
            print(html)
            raise FileNotFoundError(f"Response for {self.url} was NOT 200.")
        return BeautifulSoup(html, "lxml")

    def get_current_page(self, soup):
        trs = soup.find("tbody").find_all("tr")
        result = []
        for tr in trs:
            result.append({
                "sid": int(tr.select_one("td:first-child").text),
                "uid": (tr.select_one("td:nth-child(2)").text),
                "pid": int(tr.select_one("td>a.problem_title").text),
                "result": tr.select_one("td.result>span").get("data-color"),
                "timestamp": int(tr.select_one("td:last-child>a").get("data-timestamp")),
                # "bytes": int(tr.select_one("td:has(span.b-text)").text),
                # "memory": tr.select_one(".memory"),
            })
        self.result = result
        return result

    def get_next_url(self, soup):
        next_urls = []
        for a in soup.select("div.col-md-12")[-1].select("a"):
            url = a.get("href")
            if "top" not in url:
                continue
            next_urls.append(url)
        print(sorted(next_urls))
        url = "https://www.acmicpc.net"
        return url+sorted(next_urls)[0]


db = DB(config=Config.db_local)
for uid in Config.uids:
    c = StatusCrawler(uid)
    result = []
    url = c.init_url
    for _ in range(1):
        soup = c.get_soup_http(url)
        result.extend(c.get_current_page(soup))
        print(url, len(result))
        url = c.get_next_url(soup)
        time.sleep(3)
    print(f"insert to table for uid={uid}")
    print(result[-1])
    db.cursor.executemany(
        """insert ignore into submission (sid, uid, pid, result, timestamp)
        values (%(sid)s, %(uid)s, %(pid)s, %(result)s, %(timestamp)s)""",result
    )
