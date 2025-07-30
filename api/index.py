from flask import Flask
from flask_cors import CORS
from fake_useragent import UserAgent
from flask import request

ua = UserAgent()


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'https://github.com/canonheart/fake_useragent_api'


@app.route('/user-agent')
def user_agent():
    browser = request.args.get('browser')
    browsers = request.args.getlist('browsers')
    os = request.args.get('os')
    platforms = request.args.get('platforms')
    min_version = request.args.get('min_version', type=float)

    if browser:
        try:
            supported_browsers = ['chrome', 'firefox', 'safari', 'opera', 'edge', 'google', 'ff']
            if browser.lower() in supported_browsers:
                if browser.lower() == 'ff':
                    return getattr(ua, 'ff')
                else:
                    return getattr(ua, browser.lower())
            else:
                supported_browsers = ['chrome', 'firefox', 'safari', 'opera', 'edge', 'google', 'ff']
                return f"Unsupported browser. Supported browsers: {', '.join(supported_browsers)}", 400
        except AttributeError:
            return f"Cannot get user-agent from browser '{browser}'.", 400

    kwargs = {}
    if browsers:
        kwargs['browsers'] = browsers
    if os:
        kwargs['os'] = os
    if platforms:
        kwargs['platforms'] = platforms
    if min_version:
        kwargs['min_version'] = min_version

    if kwargs:
        custom_ua = UserAgent(**kwargs)
        return custom_ua.random
    
    return ua.random

if __name__ == '__main__':
    app.run(debug=True)