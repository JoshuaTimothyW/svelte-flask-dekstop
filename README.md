# svelte-flask-dekstop

svelte + flaskwebgui + py2exe = hybrid dekstop app

## Run the following for development:

- `python server.py` to start the Flask server.
- `cd client; npm install; npm run auto` to automatically build and reload the Svelte frontend when it's changed.

## Build dekstop app
Generate portable dekstop app in dist folder
`python setup.py py2exe`