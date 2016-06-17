# Websocket challange

[![Deploy](http://www.herokucdn.com/deploy/button.png)](http://chat-room-interview.herokuapp.com/)

> HTTPS does not work in this project - This [issue](https://github.com/johnidm/python-websocket-challenge/issues/4) will fix this problem

#### Known issues

> Sometimes in Heroku we are having this problem https://github.com/johnidm/python-websocket-challenge/issues/2. To solve this problem you need to refresh the client connections. Our team is trying to solve this problem :-(

#### Setup project
```
pyenv install 2.7.11
pyenv virutalenv 2.7.11 venv-2.7.11
pyenv activate venv-2.7.11
```

```
git clone git@github.com:johnidm/python-websocket-challenge.git
pip install -r requirements.txt
```

#### Run project
```
python app.py
````
or 
```
foreman start
```

Open the url [http://localhost:5000](http://localhost:5000) in many tabs and different browsers and enjoy yourself!

#### How to contribute  

[Check the issues list](https://github.com/johnidm/python-websocket-challenge/issues/)

> We love well-written code, please before commit check pep8 - https://www.python.org/dev/peps/pep-0008/

#### How project work

[Please watch this video](http://i.imgur.com/jgsaINw.gifv)

#### References

I did not do this project alone, I researched and used many things that articles:

* http://codepen.io/supah/pen/jqOBqp
* https://www.fullstackpython.com/websockets.html
* https://github.com/tornadoweb/tornado/tree/master/demos/chat
* http://code.runnable.com/UqDMKY-VwoAMABDk/simple-websockets-chat-with-tornado-for-python
* http://www.jpablo128.com/multi-room-websockets-server-with-tornado-i-basic-chat-server/
* http://www.codecheese.com/2013/11/running-tornado-web-server-on-heroku/
* https://github.com/jbalogh/tornado-websocket-client
