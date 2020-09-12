'''
  Requires a twitter_keys.py file in the root for necessary imported variables like keys.

    [twitter_keys.py] should look like:
    CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxx'
    CONSUMER_KEY_SECRET = 'yyyyyyyyyyyyyyyyyyy'
    .. and so forth

'''

from flask import Flask, render_template, url_for, request, redirect
from twitter_keys import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
import twitter

app = Flask(__name__)
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_KEY_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET)


@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    search_user = request.form['user']
    try:
      print('search: ', search_user)
      return redirect(search_user)
    except:
      return 'There was an issue with requesting the data'

  else:
    print('printing in index() else:')
    screenName = 'milkndcoffee'
    #bruh = api.VerifyCredentials()
    #bruh = api.GetUser(screen_name=screenName)
 
    #print(bruh)
    message = 'searched: '
    return render_template('index.html')
    
@app.route('/<user>', methods=['POST', 'GET'])
def get(user):
  if request.method == 'POST':
    search_user = request.form['user']
    try:
      print('search: ', search_user)
      return redirect(search_user)
    except:
      return 'There was an issue with requesting the data'

  print('getting user')
  return render_template('index.html', message=str(user))



if __name__ == "__main__":
  app.run(debug=True)
