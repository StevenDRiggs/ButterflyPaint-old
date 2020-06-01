from sys import argv

from bpaint import app
if __name__ =='__main__':
    debug = 'debug' in argv
    app.config['SQLALCHEMY_ECHO'] = 'verbose' in argv
    app.run(debug=debug)
        
