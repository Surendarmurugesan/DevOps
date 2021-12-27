### This is used for start our wesite (or) start our web-server.
from website import create_app

app = create_app()

## IF only we run this file, not we import this file
if __name__ == '__main__':
    app.run(debug=True)  ## start our website, It helps, every time we make some changes in python code it can automatically rerun the website.