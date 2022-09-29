from flask import Blueprint, redirect, render_template, request, flash, url_for
from app.services.firebase import DB
from ..admin.views import admin_required, login_required

databaseKema = Blueprint("database", __name__, template_folder="templates")


@databaseKema.route("/form", methods=["GET", "POST"])
@admin_required
@login_required
def form():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "angkatan": request.form["angkatan"],
            "status_kuliah": request.form["status_kuliah"],
        }
        DB.collection("KEMA").document().set(data)
        flash("Terima kasih, data anda berhasil diinput", "success")
        return redirect(url_for("database.form"))
    return render_template("form.html")
