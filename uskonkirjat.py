###
# Copyright (c) 2014, Heikki Hokkanen
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from bs4 import BeautifulSoup
import urllib2
from contextlib import closing

baseurl = 'http://raamattu.uskonkirjat.net/servlet/biblesite.Bible'

def get_verse(verse):
    full_url = baseurl + '?ref=' + urllib2.quote(verse)
    return parse_results(full_url)

def search(text):
    full_url = baseurl + '?search=' + urllib2.quote(text)
    return parse_results(full_url)

def parse_results(full_url):
    with closing(urllib2.urlopen(full_url)) as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc)

        result = []
        for i in soup.find_all('div', 'text'):
            tr = i.parent.parent
            result.append(tr.text.encode('utf-8'))
        return result

if __name__ == '__main__':
    import sys
    verse = ' '.join(sys.argv[1:])
    print 'Getting verse:', verse
    print get_verse(verse)

    print 'Search test'
    print search('luulottele')

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
