# kandyland_abuse
Kandyland NFT form abuse

## Description

This software helps you to register your wallets with twitters in Kandyland form (supports Selenium)

## Installation

It works via Selenium and https://anti-captcha.com/ extension. 

You need to refill anti-captcha account before starting the work. 


Also download chromedriver for your current Chrome version and system. You can download it here: https://chromedriver.chromium.org/downloads

Copy chromedriver to project folder.

Write in terminal:

```
pip install -r requirements.txt
```

Enter your `API_KEY`, `referral link` and `processes count` in `config file`.

Add your seeds in `seeds.txt` file

Add your twitter accounts with in `twitter.txt` like this format:
```
login:password:phone
```

All successfully registered accounts automatically save in `success.txt`

## WARNING! DO NOT ENTER MORE THAN 5 PROCESSES, OTHERWISE SELENIUM CAN START TO WORK UNCORRECTLY

## Developers

- [Flexter](https://github.com/flexter1)
- 
  [Telegram](https://t.me/flexterwork)
