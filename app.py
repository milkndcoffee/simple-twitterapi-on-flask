'''
  Requires a created twitter_keys.py file in the root for necessary imported variables like keys.

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
      return redirect('user/'+search_user)
    except:
      return 'There was an issue with requesting the data'

  else:
    return render_template('index.html', user='')
    
@app.route('/user/<user>', methods=['POST', 'GET'])
def view_user(user):
  if request.method == 'POST':
    search_user = request.form['user']
    try:
      print('search: ', search_user)
      return redirect(search_user)
    except:
      return 'There was an issue with requesting the data'
  
  try:
    return render_template('index.html', user=api.GetUser(screen_name=user))
  except:
    return 'There was an error getting data. The user might be private, banned, or may not exist.'

@app.route('/home')
def home():
  return redirect('/')

@app.route('/user/<user>/json')
def view_json(user):
  try:
    user_json = api.GetUser(screen_name=user, return_json=True)
    return user_json
  except Exception as e:
    error_msg = 'Error requesting json data: %r' % str(e)
    return error_msg, 400
    
  

if __name__ == "__main__":
  app.run(debug=True)
