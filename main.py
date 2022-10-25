import requests

proxies = { 
  'http': '188.165.201.211',

'https': '188.165.201.211:1080'

}
r = requests.get('http://example.org', proxies=proxies)
