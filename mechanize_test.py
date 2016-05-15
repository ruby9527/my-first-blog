import mechanicalsoup
import urllib

browser = mechanicalsoup.Browser()
#These are the parameters you've got from checking with the aforementioned tools
parameters = {'parameter1' : 'your content',
              'parameter2' : 'a constant value',
              'parameter3' : 'unique characters you might need to extract from the page'
             }
#Encode the parameters
data = urllib.urlencode(parameters)
#Submit the form (POST request). You get the post_url and the request type(POST/GET) the same way with the parameters.
browser.open(post_url,data)
#Submit the form (GET request)
browser.open(post_url + '%s' % data)
