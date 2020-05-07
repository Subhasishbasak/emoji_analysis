## emoji_analysis

**Topic** : sentiment analysis using WhatsApp emojis.

**Platform** : Python

## To run:
- Clone the reposiory and *cd* into `code`

Syntax:
```
python3 get_score.py 'screenshot_name'
```

Example:
```
python3 get_score.py 'subhasish_2'
```
## To collaborate
- If you are interested and you are most to collaborate in this project. Here is a basic small guide : https://drive.google.com/open?id=1VOubfPMqUFKH_UBQ2B32qbAKZNG24XPi


## Directory layout

TODO: explain here how things are organized in this repo

## The workflow can be divided into the following branches:
- Data collection & pre-processing
	- Collection of whatsapp recent used emojis (observed samples) : user screenshots
	- Collection of labelled whatsapp emojis : emoji_name & unicode representation
	- Collection of sentiment labelled emojis : see reference
- Image Processing (template matching)
	- implement template matching using CV2
	- obtain emojis for a perticular user 
- Sentiment analysis(easy)
	- compute consolidated sentiment score
- Sentiment analysis(advanced)
	- classify different sentiment classes
	- propose a bijective mapping of sentiment score* and sentiment class

## Data source :
- https://emojipedia.org/whatsapp/2.19.352/
	
## Sentiment Classification :
- https://forms.gle/5N5LrRacngL49M5B6

## References:
- Sentiment of Emojis, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144296

