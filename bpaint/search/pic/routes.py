# import cv2

# import numpy as np

# import os

# from collections import Counter

# from flask import Blueprint # , flash, redirect, render_template, url_for

# from PIL import Image, ImageFile

# from skimage.color import rgb2lab, deltaE_cie76 as dE76

# from sklearn.cluster import KMeans

# from typing import List, Tuple

# from werkzeug.utils import secure_filename

# from bpaint.config import DEFAULT_PIC_SEARCH_NUM_COLORS, DEFAULT_PIC_SEARCH_THRESHOLD
# from bpaint.search.pic.forms import PicSearchForm

bp = Blueprint('pic_search', __name__, static_folder='static', template_folder='templates', url_prefix='/search/pic')


# def get_image(image_path: str) -> np.ndarray:
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     return image

# def get_color(image: np.ndarray, num_colors: int = DEFAULT_PIC_SEARCH_NUM_COLORS, heuristic: bool = True) -> List[np.ndarray]:
#     modified_image = cv2.resize(image, (200, 200), interpolation=cv2.INTER_AREA)
#     modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

#     clf = KMeans(n_clusters=num_colors)
#     labels = clf.fit_predict(modified_image)

#     counts = Counter(labels)
#     counts = dict(sorted(counts.items()))

#     center_colors = clf.cluster_centers_
#     ordered_colors = [center_colors[i] for i in counts.keys()]
#     rgb_colors = [ordered_colors[i] for i in counts.keys()]

#     if heuristic:
#         return tuple(np.int_(np.mean(np.array(rgb_colors), axis=0)))

#     else:
#         return tuple(np.int_(rgb_colors[0]))

# def match_image_by_color(image: np.ndarray, rgb: Tuple[int, int, int], threshold: int = DEFAULT_PIC_SEARCH_THRESHOLD, num_colors: int = DEFAULT_PIC_SEARCH_NUM_COLORS, heuristic: bool = True) -> bool:
#     image_color = get_color(image, num_colors=num_colors, heuristic=heuristic)
#     select_image = False

#     diff = dE76(image_color, rgb)
#     if diff <= threshold:
#         select_image = True

#     return select_image


# @bp.route('/', methods=['GET'])
# def pic_search():
#     form = PicSearchForm()
#     return render_template('pic/index.html', form=form)

# @bp.route('/results', methods=['POST'])
# def pic_search_results():
#     form = PicSearchForm()
#     if form.validate_on_submit():
#         from bpaint import app, db, load_db, uploads
#         from bpaint.models import Color

#         formdata = form.data
#         threshold = formdata.get('threshold', DEFAULT_PIC_SEARCH_THRESHOLD)
#         heuristic = formdata.get('heuristic', False)
#         num_colors = DEFAULT_PIC_SEARCH_NUM_COLORS * 2 if formdata.get('extra_heuristic') else DEFAULT_PIC_SEARCH_NUM_COLORS

#         IMAGE_DIRECTORY = os.path.join(app.config['UPLOAD_FOLDER'], 'temp')
#         if not os.path.exists(IMAGE_DIRECTORY):
#             os.mkdir(IMAGE_DIRECTORY)

#         records = load_db()
#         image_names = os.listdir(IMAGE_DIRECTORY)

#         colors = {
#             record.name: \
#                 (
#                     record.swatch,
#                     get_color(
#                         get_image(
#                             os.path.join(
#                                 app.config['UPLOAD_FOLDER'],
#                                 record.swatch.rsplit('/', 1)[1]
#                             )
#                         ),
#                         num_colors=num_colors,
#                         heuristic=heuristic
#                     )
#                 ) \
#             for record in records
#         }
        
#         results = []

#         image_to_match = formdata['image_to_search']
#         image_to_match.filename = secure_filename(image_to_match.filename)
#         image_path = os.path.join(IMAGE_DIRECTORY, image_to_match.filename)
#         with open(image_path, 'w'):
#             image_to_match.save(image_path)
#         ImageFile.LOAD_TRUNCATED_IMAGE = True
#         with Image.open(image_path) as image:
#             image = image.resize((200, 200))
#             image.save(image_path)

#         for color_name, color_data in colors.items():
#             if match_image_by_color(get_image(image_path), color_data[1], threshold=threshold, num_colors=num_colors):
#                 results.append(color_data[0])

#         os.remove(image_path)
#         os.rmdir(IMAGE_DIRECTORY)

#         if results:
#             return render_template('pic/results.html', results=results)
#         else:
#             flash('No results found.')
#             return redirect(url_for('.pic_search'))

#     else:  # not validate_on_submit()
#         flash(str(form.errors))
#         return redirect(url_for('.pic_search'))
