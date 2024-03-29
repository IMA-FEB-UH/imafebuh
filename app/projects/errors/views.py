from flask import Blueprint, render_template

errorsBlueprint = Blueprint("errors", __name__, template_folder="templates")


@errorsBlueprint.app_errorhandler(401)
def error_401(error):
    return render_template("401.html")


@errorsBlueprint.app_errorhandler(403)
def error_403(error):
    return render_template("403.html")


@errorsBlueprint.app_errorhandler(404)
def error_404(error):
    return render_template("404.html")


@errorsBlueprint.app_errorhandler(500)
def error_500(error):
    return render_template("500.html")
