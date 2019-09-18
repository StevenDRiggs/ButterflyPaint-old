from sys import argv

debug = False


if len(argv) > 1:
    if 'debug' in argv:
        debug = True


if __name__ == '__main__':
    from bpaint import app, db
    from flask import current_app, g
    print('app:', app, '\ndb:', db)
    with app.app_context():
        print('current_app:', current_app, 'g:', g)
    app.run(debug=debug)
