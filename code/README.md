## description of this directroy

### The idea/approach

- Here we take *screenshots* (see `resources/screenshots` for references) of **recently used emoji box** of a WhatsApp user as inputs.
- Process the screenshots to extract and identify the emojis.
	- crop the screenshots to discard everything except the emoji box (used intensity differences to identify a suitable crop) and convert it into a process-able image.
	- the process-able image is then divided into suitable grids to isolate each emoji as smaller images (*70 x 70*) and contruct the `emoji_list` with them.
	- used `cv2.matchTemplate` to identify the emojis in the `emoji_list`.
- Compute a consolidated sentiment score based on the emojis.
	- see `References`

### Directory layout

- core     : `.py` files containing **main functions**
- debug    : `.py` files for easy/quick debugging 
- notebook : `.ipynb` notebooks for experiments
- utils    : `.py` files containing **utility functions**
- launcher files : Till now there are 3 launcher files
	- `get_diag.py` : produces diagostic report for a given screenshot
	- `get_graph.py`: produces graph plots of sentiment scores for (>1) screenshots
	- `get_score.py`: produces sentiment scores for screenshot(s)

