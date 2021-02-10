# facebook_bot
A bot to automate facebook login and other stuff using selenium.

### Prerequisites
First make sure python is installed in your OS.
As well as Chrome as this script is written for chrome browser.

Install the folowing libraries

pip install selenium
pip install webdriver-manager

If instruction is needed these are the following links:
Selenium - https://pypi.org/project/selenium/
Webdriver-Manager - https://pypi.org/project/webdriver-manager/

### Set the initial Values
open the python file with editor
If your ID is - qwerty
Pass is - qwerty
The content to post is - Hello World!
and Comment is  - Comment Made
This should be the entries
```
###################################################################################################################
#############################  Only these are the values to be added  #############################################

facebook_id = "qwerty"   # facebook id 
facebook_pass = "qwerty" # facebook pass
Post_content = "Hello World!"  # content of the facebook post to be made
Comment = "Comment Made"  # Comment on the random friend timeline's first post

###################################################################################################################


```


### What it do

First Login with the credentials
Then get yor location from profile and search it and add a friend near you.(If location is not specified a random friends of friends is added
Then it make a text post with the content you provided in the beginning.
And then comment on a random friend's Timeline's first Post with the comment content you provided.
Then run the script

# Done :wink:
