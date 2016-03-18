# -*- coding: utf-8 -*-
from lxml import etree
from lxml import html
import constant

def _parser(htmltext, rule):
    parser = etree.HTMLParser()

    tree = html.fromstring(htmltext, parser=parser)

    # data = tree.xpath("//div[@id='result']/div[@class='tdc']")
    data = tree.xpath(rule)
    return data


def parse_newsingle(htmltext):
    rule = constant.newsingle_selector
    return _parser(htmltext, rule)


def parse_songlist_extracthash(htmltext):
    print "extracting hash..."
    rule = constant.hash_selector
    return _parser(htmltext, rule)


def parse_extractmp3link(htmltext):
    rule = constant.mp3_link
    return _parser(htmltext, rule)
