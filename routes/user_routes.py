from routes import app
from werkzeug.utils import secure_filename
from common import utils
from common.profile import Profile
from forms.image_upload_form import ImageUploadForm
from flask import render_template, abort, redirect, url_for, flash, send_from_directory
import os 
 
@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():
    # 先删除之前保存的图片
    cmd1 = r'rm  C:\codes\my_projects\flask_practice\image_transfer\data\images\*'
    # 使用PowerShell执行命令
    os.system(f'powershell -Command "{cmd1}"')

    form = ImageUploadForm()

    if form.validate_on_submit():
        image_file = form.image_file.data

        images_path = Profile.get_images_path()
        image_filename = secure_filename(image_file.filename)
        image_fullpath = utils.get_save_filepath(images_path, image_filename)

        image_file.save(image_fullpath)
        flash(f'图片保存为: {image_fullpath}', category='success')

    # 再将生成的图片放到C:\codes\my_projects\flask_practice\image_transfer\data\images下面为前端扫描到
    cmd2 = r'python C:\codes\my_projects\flask_practice\test\test_ossystem.py'
    os.system(cmd2)

    image_filenames = utils.ImageService().get_image_filename_list()

    return render_template('images.html', form=form, image_filenames=image_filenames)


@app.route('/image/<image_filename>')
def download_image(image_filename: str):
    image_path = Profile.get_images_path()
    image_filepath = image_path.joinpath(image_filename)
    if not image_filepath:
        return abort(404)

    return send_from_directory(directory=image_path, path=image_filename)