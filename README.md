# Bitly url shorterer

This project uses the Bitly API, which allows you to create shorten links. When the user input a link, a shortened link is displayed. But if the user specified a short link, it shows statistics of clicks on it.
The result of code completion is presented below.
![Image alt](https://github.com/Fiskless/Bitly/blob/master/Bitly_example.png)

### How to install

First of all, you should create account on bitly.com. Then you need to get access token. For this purpose, log in your account, then select profile settings > Generic access Token. Enter your password and token will be generated automatically. You will get a token string similar to 99c09e20aa122225122fc1977542fecf77771da7.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
