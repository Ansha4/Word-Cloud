#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# <br><br>
# Now you will need to upload your input file here so that your script will be able to process it.  To do the upload, you will need an uploader widget.  Run the following cell to perform all the installs and imports for your word cloud script and uploader widget.  It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.
# <br><br>
# **Enabling notebook extension fileupload/extension...**
# <br>
# **- Validating: <font color =green>OK</font>**

# In[13]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys



def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()





file_contents = """I was sitting in my easy-chair, idly turning the pages of a
#paperbacked book someone had left on the bus, when I came across the
#reference that first put me on the trail. For a moment I didn't
#respond. It took some time for the full import to sink in. After I'd
#comprehended, it seemed odd I hadn't noticed it right away.

#The reference was clearly to a nonhuman species of incredible
#properties, not indigenous to Earth. A species, I hasten to point out,
#customarily masquerading as ordinary human beings. Their disguise,
#however, became transparent in the face of the following observations
#by the author. It was at once obvious the author knew everything. Knew
#everything--and was taking it in his stride. The line (and I tremble
#remembering it even now) read:

   # _... his eyes slowly roved about the room._

#Vague chills assailed me. I tried to picture the eyes. Did they roll
#like dimes? The passage indicated not; they seemed to move through the
#air, not over the surface. Rather rapidly, apparently. No one in the
#story was surprised. That's what tipped me off. No sign of amazement
#at such an outrageous thing. Later the matter was amplified.
"""


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    

    word_count = {}
    final_text = []
    
    for word in file_contents.split():
        text = ""
        for letter in word.lower():
            if letter not in punctuations and letter.isalpha():
                text += letter
            
        if word not in uninteresting_words:
            final_text.append(text)
            
    for word in final_text:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
                      
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    return cloud.to_array()



myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

