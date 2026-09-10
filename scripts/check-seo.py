"""Check built page metadata, structured data, share images, and sitemap coverage."""
import json
import struct
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / '_site'
ORIGIN = 'https://zain-hoda.com'


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.meta, self.canonicals, self.schemas = {}, [], []
        self.title, self.h1s, self.capture = '', 0, None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            key = attrs.get('property', attrs.get('name'))
            if key:
                assert key not in self.meta, f'Duplicate metadata: {key}'
                self.meta[key] = attrs.get('content', '')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs['href'])
        if tag == 'h1':
            self.h1s += 1
        if tag == 'title':
            self.capture = 'title'
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.capture = 'schema'
            self.schemas.append('')

    def handle_data(self, data):
        if self.capture == 'title':
            self.title += data
        if self.capture == 'schema':
            self.schemas[-1] += data

    def handle_endtag(self, tag):
        if tag in ('title', 'script'):
            self.capture = None


def jpeg_dimensions(path):
    data = path.read_bytes()
    assert data[:2] == b'\xff\xd8', f'Not a JPEG: {path}'
    offset = 2
    while offset < len(data):
        assert data[offset] == 0xFF
        marker = data[offset + 1]
        offset += 2
        length = int.from_bytes(data[offset:offset + 2], 'big')
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack('>HH', data[offset + 3:offset + 7])
            return width, height
        offset += length
    raise AssertionError(f'JPEG dimensions not found: {path}')


sitemap = ET.parse(ROOT / 'sitemap.xml')
urls = [node.text for node in sitemap.findall('.//{*}loc')]
assert len(urls) == len(set(urls))
titles, descriptions = set(), set()
for url in urls:
    assert url.startswith(ORIGIN + '/')
    relative = urlsplit(url).path.lstrip('/')
    path = ROOT / (relative + 'index.html' if url.endswith('/') else relative)
    page = Page(path.read_text())
    assert page.canonicals == [url], path
    assert page.h1s == 1, f'Expected one H1: {path}'
    assert page.title and page.title not in titles, path
    titles.add(page.title)
    description = page.meta['description']
    assert 60 <= len(description) <= 170, (path, len(description))
    assert description not in descriptions, path
    descriptions.add(description)
    assert 'noindex' not in page.meta['robots']
    assert page.meta['og:title'] == page.meta['twitter:title'] == page.title
    assert page.meta['og:description'] == page.meta['twitter:description'] == description
    assert page.meta['og:url'] == url
    assert page.meta['twitter:card'] == 'summary_large_image'
    image = page.meta['og:image']
    assert image == page.meta['twitter:image'] == page.meta['og:image:secure_url']
    assert image.startswith(ORIGIN + '/')
    image_path = ROOT / urlsplit(image).path.lstrip('/')
    assert jpeg_dimensions(image_path) == (1200, 630)
    assert image_path.stat().st_size < 500_000
    assert page.meta['og:image:alt'] == page.meta['twitter:image:alt']
    assert page.meta['og:image:alt']
    assert page.meta['og:image:width'] == '1200'
    assert page.meta['og:image:height'] == '630'
    assert len(page.schemas) == 1
    graph = json.loads(page.schemas[0])['@graph']
    assert graph[0]['@type'] == 'Person'
    assert graph[1]['@type'] == 'WebSite'
    assert graph[2]['url'] == url
    if page.meta['og:type'] == 'article':
        assert graph[2]['@type'] == 'BlogPosting'
        assert graph[2]['headline'] and graph[2]['datePublished']
        assert graph[2]['author']['@id'] == ORIGIN + '/#person'

not_found = Page((ROOT / '404.html').read_text())
assert 'noindex' in not_found.meta['robots']
assert ORIGIN + '/404.html' not in urls
assert 'Sitemap: ' + ORIGIN + '/sitemap.xml' in (ROOT / 'robots.txt').read_text()
print(f'Passed: {len(urls)} indexable pages, unique metadata, JSON-LD, 1200×630 images, sitemap, and 404 indexing rules.')
