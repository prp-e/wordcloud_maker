# Word Cloud Maker for Persian tweets 

There is a trend in Persian twitter about people making _Word Clouds_. I decided to experience the process myself, so I started studying different tools and methods for creating clouds. 

This is the result! I made this little computer program which lets you have your very own word cloud. 

## Example word cloud 

![Example](./wc.png)

## Requirements 

The code is written in Python version 3.8 (and not tested in older versions) so you need Python 3.8 installed. You also need a bunch of libraries which you can install from `requirements.txt` : 

```
pip install -r requirements.txt
``` 

## How to use

First, you need a font with support of Persian language (i.e. [Vazir](http://rastikerdar.github.io/Vazir-font)), then you will use a file including what you want to make a cloud of. I suggest a `txt` file. It can include your tweets, or just lorem impsum type of shit. But pay attention please, the code removes all non-Persian things from your test. 

So, considering you have your font `Vazir.ttf` and your file `tweets.txt`, you just need to run the code like this : 

```
python main.py tweets.txt Vazir.ttf
``` 

Then the file `wc.png` will be created. That file actually includes your cloud. You also can change `twitter_mask.png` to whatever you want, but you'll need to modify the code yourself. 

## FAQ 
*  __How can I extract all my tweets?__ There are two ways. First, you can request an API access from Twitter (through (this link)[https://developer.twitter.com]) or you can just use a tool like [twint](https://github.com/twintproject/twint). 
*  __Can I use it on a non-Persian text?__ Of course you can. But you need to modify the code. My suggestion is that simply read the code and re-implement it for your very own purpose. 
*  __Does it work on non-tweet phrases?__ It works on evey text, as long as they're Persian. 
*  __How can I contribute?__ Just fork this repository and do whatever you want. Pull requests are welcome. 

## TODO 
- [ ] Trying to make this work for _Ganjoor_. 
- [ ] Trying to make an API and make this usable for everyone. 
- [ ] Fixing verbal problem (in stop words) 
- [ ] Fixing _Stop words_ bug. 
- [x] Providing a proper `.gitignore` file. 
