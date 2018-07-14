from flask import abort
from flask_login import current_user
from functools import wraps
from flask_middle_app.models import User

def role_required(role):
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrargs):
            #未登录用户或者角色不满足引发404
            #为什么不是403？因为不希望把路由暴露给不具有权限的用户
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args, **kwrargs)
        return wrapper
    return decorator

staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)
