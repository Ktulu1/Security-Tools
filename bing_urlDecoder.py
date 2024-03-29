#decodes destination url in a bing search result
#command line argument is bing search results in quotes

import urllib.parse
import base64
from sys import argv

script, search_result = argv

try:
    decoded_search_result = urllib.parse.unquote(search_result)
except:
    decoded_search_result = search_result


def decode_destination_url(decoded_search_result):
    start_index = decoded_search_result.find("u=a1") + 4
    end_index = decoded_search_result.find("#", start_index)
    destination_url = decoded_search_result[start_index:end_index]

    return destination_url

destination_url = decode_destination_url(decoded_search_result)
print("\n", destination_url)

encoded_url = destination_url + '='

decoded_bytes = base64.b64decode(encoded_url)
decoded_string = decoded_bytes.decode('utf-8')
print("\n", decoded_string) 