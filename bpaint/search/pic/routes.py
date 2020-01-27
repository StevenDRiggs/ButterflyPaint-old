import cv2

import numpy as np

import os

from collections import Counter

from flask import Blueprint, flash, redirect, render_template, url_for

from PIL import Image, ImageFile

from skimage.color import rgb2lab, deltaE_cie76 as dE76

from sklearn.cluster import KMeans

from werkzeug.utils import secure_filename

from bpaint.search.pic.forms import PicSearchForm

bp = Blueprint('pic_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/pic')


def rgb_to_hex(rgb):
    return f'#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}'

def get_colors(image, num_colors):
    modified_image = cv2.resize(image, (200, 200), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=num_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)
    counts = dict(sorted(counts.items()))

    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    return rgb_colors

def match_image_by_color(image, rgb, threshold=60, num_colors=1):
    image_colors = get_colors(image, num_colors)
    selected_color = rgb2lab(np.uint8(np.asarray([[rgb]])))

    select_image = False
    for i in range(num_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = dE76(selected_color, curr_color)
        if diff < threshold:
            select_image = True

    return select_image


@bp.route('/', methods=['GET'])
def pic_search():
    form = PicSearchForm()
    return render_template('pic/index.html', form=form)

@bp.route('/results', methods=['POST'])
def pic_search_results(threshold=2):
    form = PicSearchForm()
    if form.validate_on_submit():
        from bpaint import app, db, uploads
        from bpaint.models import Color
        from bpaint.admin.routes import load_db

        formdata = form.data
        if formdata['threshold'] != 2:
            threshold = formdata['threshold']

        for k, v in formdata.items():
            print(f'\n{k=}\n{v=}\n{type(v)=}\n')

        IMAGE_DIRECTORY = os.path.join(app.config['UPLOAD_FOLDER'], 'temp')

        records = load_db()
        images = os.listdir(IMAGE_DIRECTORY)
        colors = {color.name: (color.swatch, get_colors(image, threshold)) for color in records for image in [get_colors(os.path.join(IMAGE_DIRECTORY, file_), num_colors=threshold) for file_ in images if not file_.startswith('.')]}
        
        results = []

        image_to_match = formdata['image_to_search']
        image_to_match.filename = secure_filename(image_to_match.filename)
        image_path = os.path.join(IMAGE_DIRECTORY, image_to_match.filename)
        with open(image_path, 'w'):
            image_to_match.save(image_path)
        ImageFile.LOAD_TRUNCATED_IMAGE = True
        with Image.open(image_path) as image:
            image = image.resize((200, 200))
            image.save(image_path)

        for color_name, color_data in colors.items():
            if match_image_by_color(image_path, color_data[1], threshold=threshold):
                results.append(color_data[0])

        return render_template('pic/results.html', results=results)

    else:  # not validate_on_submit()
        flash(str(form.errors))
        return redirect(url_for('.pic_search'))
