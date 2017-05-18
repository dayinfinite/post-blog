# -*- coding:utf-8 -*-
# __author__ = 'dayinfinte'

import requests
import click
import markdown
from datetime import datetime
import codecs

def m2h(file):
    input_file = codecs.open(file, mode='r', encoding='utf-8')
    content = input_file.read()
    html = markdown.markdown(content)
    return html

@click.command()
@click.option('--title', '-t', help='This is article title')
@click.option('--file', '-f', help='This is article content, and it is markdown file')
@click.option('--tags', multiple=True, help='This is article tags')
@click.option('--url', '-r', help="This is url")
def post_blog(title, file, tags, url):
    html = m2h(file)
    payload = {
        'title': title,
        'content': html,
        'tags': ' '.join(tags)
    }
    r = requests.post(url=url, json=payload)
    print {'status_code': r.status_code, 'msg': 'suc'}

if __name__ == '__main__':
    post_blog()