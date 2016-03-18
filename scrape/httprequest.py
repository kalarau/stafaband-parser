# -*- coding: utf-8 -*-
import requests
import urlparse
import constant



def get(url, payload=()):
    r = requests.get(url, params=payload)
    return r.content


def exchange_hash(fuckinghash):
    baseurl = "http://www.stafaband.co/get"
    call = requests.post(
        baseurl,
        data={
            'hash': fuckinghash
        }
    )

    return call.content

def _get_filename(urlsegment):
    qs = urlparse.urlparse(urlsegment)
    qs = urlparse.parse_qs(qs.query)
    realurl = qs['direct'][0].decode('base64')
    qs = urlparse.urlparse(realurl)
    qs = urlparse.parse_qs(qs.query)
    m = qs['url'][0]
    realname = "-".join(m.split("/")[-2:])
    return realname + ".mp3"


def takedown(urlsegment):
    if isinstance(urlsegment, list):
        urlsegment = urlsegment[-1]

    fullurl = "{}{}".format(
        constant.baseurl,
        urlsegment
    )

    local_filename = _get_filename(urlsegment)
    print local_filename
    print "Downloading at: %s" % (fullurl,)
    r = requests.get(fullurl, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    #             #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename
