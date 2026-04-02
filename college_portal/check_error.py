import urllib.request, urllib.error, re
try:
    urllib.request.urlopen('http://127.0.0.1:8000/portalnotes')
except urllib.error.HTTPError as e:
    html = e.read().decode('utf-8')
    match = re.search(r'Exception Value:</th>.*?(?:<pre>|<td>)(.*?)(?:</pre>|</td>)', html, re.IGNORECASE | re.DOTALL)
    if match:
        print('ERROR_MSG:', match.group(1).strip())
    else:
        # Fallback dump
        print('Fallback dump:', re.search(r'Exception Value:(.{0,100})', re.sub(r'<[^>]+>', '', html), re.IGNORECASE).group(1))
