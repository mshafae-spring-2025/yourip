
from flask import (
    Blueprint, flash, render_template, request
)

bp = Blueprint('show', __name__, url_prefix='/')

@bp.route('/me')
def show_me():
    ip = request.remote_addr
    return render_template('show.html', remote_ip=ip)