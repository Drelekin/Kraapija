import urllib.request
import re

url = 'https://www.1a.ee/c/arvutikomponendid-vorgutooted/malu-hdd-ja-ssd/operatiivmalu-ram/2v9?sort=price__asc'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode("utf-8") 
pattern = r"<a class='catalog-taxons-product__image-anchor' data-gtm-link='(?:[\s\S]+?)' href='(.+?)'>\n<img alt='(.+?)' class='catalog-taxons-product__image' decoding='async' loading='lazy' src='(.+?)'>\n<\/a>\n<div class='catalog-taxons-product__price'>\n<div class='catalog-taxons-product-price'>\n<span class='catalog-taxons-product-price__item-price'>\n<span>([\d,]+?)<\/span>"

matches = re.findall(pattern, html)
print(matches)

"""
NOTES
nimi, hind, pildi url ja toote link
"""