# Stock News Alert
Gets daily prices for a stock (Alpha Vantage), compares the last two closing prices, gets related news (NewsAPI) and prepares an SMS with Twilio.
Needs your own API keys and a Twilio account; keys and phone numbers in the file are placeholders.
Known limit: the alert threshold is set to any change (`> 0`), meant to be raised.
