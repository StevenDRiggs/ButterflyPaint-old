from sys import argv

debug = False
verbose = False


if len(argv) > 1:
    if 'debug' in argv:
        debug = True
    if 'verbose' in argv:
        verbose = True


if __name__ == '__main__':
    from bpaint import app, db
    print('app:', app, '\ndb:', db)
    if verbose:
        app.config['SQLALCHEMY_ECHO'] = True
    app.run(debug=debug)
