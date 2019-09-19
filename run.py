from sys import argv

debug = False


if len(argv) > 1:
    if 'debug' in argv:
        debug = True


if __name__ == '__main__':
    from bpaint import app, db
    print('app:', app, '\ndb:', db)
    app.run(debug=debug)
