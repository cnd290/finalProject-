from flask import Blueprint, render_template, session, redirect, url_for
from flask_cors import cross_origin
from Project.Resource import RestfulAPIResource

Hash = RestfulAPIResource.Hash
ManagerLessonDetail = Blueprint('ManagerLessonDetail', __name__)


@ManagerLessonDetail.route(r'/GET/ManagerLessonDetail')
@cross_origin()
def manager_lesson_detail_page():
    if session.get('Login') == 'Login' and session.get('Access') == Hash.hash_sha512('Super'):
        return render_template('/Manager/ManagerLessonDetail.html')
    else:
        return redirect(url_for('Login.login_page'))
