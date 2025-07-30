# Fake Useragent API
API wrapper for https://github.com/fake-useragent/fake-useragent

<br>

## Usage
```python
# Random
import requests

res = requests.get('https://fake-useragent-api.vercel.app/get')
print(res.text)
```
### Queris
##### browser
`"Google", "Chrome", "Firefox", "Edge", "Opera", "Safari", "Android", "Yandex Browser", "Samsung Internet", "Opera Mobile", "Mobile Safari", "Firefox Mobile", "Firefox iOS", "Chrome Mobile", "Chrome Mobile iOS", "Mobile Safari UI/WKWebView", "Edge Mobile", "DuckDuckGo Mobile", "MiuiBrowser", "Whale", "Twitter", "Facebook", "Amazon Silk"`<br><br>
If you want to set up multiple browsers together, use `browsers`<br>
ex: `https://fake-useragent-api.vercel.app/get?browsers=chrome&browsers=firefox`

#### os
`"Windows", "Linux", "Ubuntu", "Chrome OS", "Mac OS X", "Android", "iOS"`

#### platforms
`"desktop", "mobile", "tablet"`

<br>

## Get Your Own
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/import?repository-name=fake_useragent_api&s=https%3A%2F%2Fgithub.com%2Fcanonheart%2Ffake_useragent_api%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
