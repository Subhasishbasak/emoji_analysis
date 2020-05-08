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
- To collaborate in this project, here is a small guide : [grab a copy](https://drive.google.com/open?id=1VOubfPMqUFKH_UBQ2B32qbAKZNG24XPi)


## Directory layout

- code     : `.py` files and `.ipynb` notebooks
- lib      : pre-constructed dictionary
- resource : data, other resources

## The workflow :

TODO : this is dirty, make it organized

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
- [Click to view data source](https://emojipedia.org/whatsapp/2.19.352/)
	
## Sentiment Classification :
- [Click to attempt the Questionnaire](https://forms.gle/5N5LrRacngL49M5B6)

## References:
- Sentiment of Emojis, [click here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144296)

## contact:
- [Contact me](https://subhasishbasak.github.io/)

