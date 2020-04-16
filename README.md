# NMT(Neural Machine Translation)

The dataset we use is the IIT Bombay corpus. (http://www.cfilt.iitb.ac.in/iitb_parallel/)
We download the full dataset and unzip it in a folder. We then take both the pruned corpus files (pruned_train.en, pruned_train.hi) and run convert.py to convert them into a single text file with bothe English and Hindi sentences seperated by a tab on the same line.

We then run the codes in the following order:
	1. pre_process_1.py
	2. split_text.py
	3. model.py
	4. test_results.py
	
The above four were run on my system with very small datasets. 'MyCodeNMT.ipynb' was run on Google colab with a larger dataset. 