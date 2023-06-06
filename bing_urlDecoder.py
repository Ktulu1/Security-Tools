import urllib.parse
import base64

#search_result = "https%3A%2F%2Fwww.bing.com%2Fck%2Fa%3F!%26%26p%3D962b413ab5cdc4a0JmltdHM9MTY4NjAwOTYwMCZpZ3VpZD0xZWI0ODRlYS04YjRlLTZlOGQtMjRiNi05N2MyOGE4NTZmZDUmaW5zaWQ9NTE2MQ%26ptn%3D3%26hsh%3D3%26fclid%3D1eb484ea-8b4e-6e8d-24b6-97c28a856fd5%26u%3Da1aHR0cHM6Ly93d3cuZWNvZ2VzdGlvbmFyLmNvbS5hci8%23bHVraWV3c2tpQHRyYW5zZ2xvYmFsY28uY29t"

search_result = input("Enter Bing Search Result:")

decoded_search_result = urllib.parse.unquote(search_result)

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