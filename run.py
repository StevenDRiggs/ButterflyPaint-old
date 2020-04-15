from sys import argv

from bpaint import app


if __name__ == '__main__':
    debug = 'debug' in argv
    app.config['SQLALCHEMY_ECHO'] = 'sql' in argv
    app.run(debug=debug)
