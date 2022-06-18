import re
import os
import requests
from bs4 import BeautifulSoup

def make_dir(dir_name):

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
            
def make_soup(url, payload=None):

    if payload:
        r = requests.get(url, params=payload)
    else:
        r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    return soup

def extract_page_urls(soup, page_url_pattern):

    page_info_list = []
    a_tags = soup.find_all("a")
    for tag in a_tags:
        page_url = tag.get("href")
        if not page_url:
            continue
        if not re.search(page_url_pattern, page_url):
            continue
        page_info_list.append(page_url)
    return page_info_list

def select_pages(page_info_list):

    new_page_info_list = []
    print("=====Select pages. Use comma(,) as a separator.=====")
    for i, (_, page_title) in enumerate(page_info_list):
        print(i, page_title)
    print("====================================================")
    selection = input(">>")
    try:
        selection_list = selection.split(",")
        for i in selection_list:
            new_page_info_list.append(page_info_list[int(i)])
        return new_page_info_list
    except:
        return None
        
def extract_file_urls(soup, file_url_pattern, set_file_name):

    file_info_list = []
    a_tags = soup.find_all("a")
    for tag in a_tags:
        file_url = tag.get("href")
        if not file_url:
            continue
        if not re.search(file_url_pattern, file_url):
            continue
        file_name = set_file_name(file_url)
        file_info_list.append((file_url, file_name))
    return file_info_list

def fetch_file(file_url, file_name):

    if os.path.exists(file_name):
        print(f"skipped:{file_name}")
    else:
        try:
            r = requests.get(file_url)
            with open(file_name, "wb") as f:
                f.write(r.content)
            print(f"done   :{file_name}")
        except Exception as e:
            print(f"failed :{file_name}")
            print(e)
