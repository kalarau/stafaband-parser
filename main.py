# -*- coding: utf-8 -*-
from scrape import httprequest, parse, constant

"""
stafaband identifikasi lagu pakai hash,
contoh: ada url begini, didapat dari [songlist_url]
>>> http://www.stafaband.co/mp3/download/koil.html#Koil_-_Kenyataan_Dalam_Dunia_Fantasi-ExZemir-rizal-p--koil-kenyataan-dalam-dunia

nah hashnya adalah:
>>> #Koil_-_Kenyataan_Dalam_Dunia_Fantasi-ExZemir-rizal-p--koil-kenyataan-dalam-dunia

hash itu nanti ditukar dengan download url, baru deh lagunya bisa di download.

"""

if __name__ == '__main__':

    newsingle_url = 'http://www.stafaband.co/download_single_FEBRUARI_2016.htm'
    songlist_url = "http://www.stafaband.co/mp3/download/koil.html"

    #: buat iterasi url di list lagu single bulan ini
    # data = httprequest.get(first)
    # links = parse.parse_newsingle(data)
    # print links
    #
    # print "*" * 100

    #: ambil list hash dari songlist_url
    data = httprequest.get(songlist_url)
    hashes = parse.parse_songlist_extracthash(data)
    print hashes

    print "*" * 100

    #: untuk setiap hash, tukar hash dengan download link
    for h in hashes:
        print "Exchange hash with download link..."
        result = httprequest.exchange_hash(h)

        #: disini dapet link download
        url = parse.parse_extractmp3link(result)

        #: download deh lagunya
        take = httprequest.takedown(url)
        print "downloaded with filename: %s" % (take,)

    #: buat debugging
    # try:
    #     for x in links:
    #         print "->>", "{}".format(x)
    #
    # except Exception as e:
    #     print "found Exception: ", e.message
