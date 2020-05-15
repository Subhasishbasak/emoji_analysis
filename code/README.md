## description of this directroy

### The idea/approach

- Here we take *screenshots* of **recently used emoji box** of a WhatsApp user (see `resources/screenshots` for references).
- Process the screenshots to extract and identify the emojis.
- Compute a consolidated sentiment score based on the emois.


### Directory layout

- core     : `.py` files containing **main functions**
- debug    : `.py` files for easy/quick debugging 
- notebook : `.ipynb` notebooks for experiments
- utils    : `.py` files containing **utility functions**
- launcher files : Till now there are 3 launcher files
	- `get_diag.py` : produces diagostic report for a given screenshot
	- `get_graph.py`: produces graph plots of sentiment scores for (>1) screenshots
	- `get_score.py`: produces sentiment scores for screenshot(s)

