### emoji_analysis

Topic : sentiment analysis using WhatsApp emojis.

Platform : Python

The workflow can be divided into the following branches:
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

Data source :
- https://emojipedia.org/whatsapp/2.19.352/
	
Sentiment Classification :
- <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSd699SP2OPLb_Z9xY6L8O901ihM6VY1ooKU2fbfYBS_yrWV0A/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>

References:
- Sentiment of Emojis, PLoS ONE 10(12): e0144296, doi:10.1371/journal.pone.0144296, 2015. 

