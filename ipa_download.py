import os, re, sys
import requests
from bs4 import BeautifulSoup

def fetch_infos(level, time):

    parent = 'https://www.jitec.ipa.go.jp/1_04hanni_sukiru'

    url = 'https://www.jitec.ipa.go.jp/1_04hanni_sukiru/_index_mondai.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    page_urls = []
    pattern = '(mondai_kaitou.+\.html)'
    a_tags = soup.find_all('a')
    for tag in a_tags:
        url = tag.get('href')
        if re.search(pattern, url): 
            page_title = re.search(pattern, url).group(0)
            url = parent + '/' + page_title
            if not url in page_urls:
                page_urls.append(url)

    file_infos = []
    pattern = f'(mondai_kaitou.+)/(.+{level}_{time}_qs\.pdf)'
    for url in page_urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        a_tags = soup.find_all('a')
        for tag in a_tags:
            url = tag.get('href')
            if url and re.search(pattern, url):
                extract = re.search(pattern, url).groups()
                dir_name = extract[0]
                file_name = extract[1]
                url = parent + '/' + dir_name + '/' + file_name
                file_infos.append((url, file_name))

    return file_infos

def save(url, file_name):

    r = requests.get(url)
    with open(file_name, "wb") as file:
        file.write(r.content)

def main(level, time):

    """
    Arguments:
        level: level of the test; "fe", "ap", "nw", ...
        time: "am" or "pm"

    Use:
        $ python3 ipa_download.py fe am
        Downloads a.m. problems of level fe.
    """

    file_infos = fetch_infos(level, time)
    ##### Change this part so that it will be the path of the directory you'd like to save the files to download. #####
    dir_name = "path/to/the/directory/you/like" + f"/ipa/{level}_{time}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    for url, file_name in file_infos:
        file_name = f"{dir_name}/{file_name}"
        try:
            if os.path.exists(file_name):
                print(f"skipped: {file_name}")
            else:
                save(url, file_name)
                print(f"done: {file_name}")
        except Exception as e:
            print(e)

if __name__ == '__main__':

    if not len(sys.argv) == 3:
        print("2 arguments (level, time) are required.")
    else:
        _, level, time = sys.argv
        main(level, time)
