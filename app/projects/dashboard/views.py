from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for,
    session,
    abort,
    request,
)
from ..admin.views import (
    login_required,
    admin_required,
    kekasi_required,
)
from app.services.firebase import DB, firestore

# from ..admin.views import login_required

dashboardBlueprint = Blueprint("dashboard", __name__, template_folder="templates")

# CORE | DASHBOARD
@dashboardBlueprint.route("/")
@login_required
def dashboard():
    if "user" in session:
        if session["user"]["otorisasi"] != "verified":
            session.clear()
            abort(401)
    return render_template("dashboard.html")


# CORE | PENGURUS
@dashboardBlueprint.route("/pengurus")
@kekasi_required
@login_required
def pengurus():
    data = (
        DB.collection("users")
        .order_by("name", direction=firestore.Query.ASCENDING)
        .stream()
    )
    users = []
    for user in data:
        us = user.to_dict()
        us["id"] = user.id
        users.append(us)
    return render_template("pengurus.html", data=users)


@dashboardBlueprint.route("/pengurus/ubah/<uid>", methods=["GET", "POST"])
@admin_required
@login_required
def ubah_pengurus(uid):
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "departemen": request.form["departemen"],
            "nim": request.form["nim"],
            "level_akses": request.form["level_akses"],
            "otorisasi": request.form["otorisasi"],
        }
        DB.collection("users").document(uid).set(data, merge=True)
        flash("berhasil ubah data", "success")
        return redirect(url_for("dashboard.pengurus"))
    user = DB.collection("users").document(uid).get().to_dict()
    user["id"] = uid
    return render_template("ubah_pengurus.html", data=user)


@dashboardBlueprint.route("/pengurus/hapus/<uid>")
@admin_required
@login_required
def hapus_pengurus(uid):
    DB.collection("users").document(uid).delete()
    flash("Data berhasil dihapus", "success")
    return redirect(url_for("dashboard.pengurus"))


# ADMINISTRASI | MAHASISWA | KEMA
@dashboardBlueprint.route("/kema")
@admin_required
@login_required
def kema():
    data = (
        DB.collection("KEMA")
        .order_by("angkatan", direction=firestore.Query.ASCENDING)
        .stream()
    )
    kema = []
    for km in data:
        k = km.to_dict()
        k["id"] = km.id
        kema.append(k)
    return render_template("kema.html", data=kema)


@dashboardBlueprint.route("/kema/ubah/<uid>", methods=["GET", "POST"])
@admin_required
@login_required
def ubah_kema(uid):
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "angkatan": request.form["angkatan"],
            "status_kuliah": request.form["status_kuliah"],
        }
        DB.collection("KEMA").document(uid).set(data, merge=True)
        flash("berhasil ubah data", "success")
        return redirect(url_for("dashboard.kema"))
    user = DB.collection("KEMA").document(uid).get().to_dict()
    user["id"] = uid
    return render_template("ubah_kema.html", data=user)


@dashboardBlueprint.route("/kema/hapus/<uid>")
@admin_required
@login_required
def hapus_kema(uid):
    DB.collection("KEMA").document(uid).delete()
    flash("Data berhasil dihapus", "success")
    return redirect(url_for("dashboard.kema"))


# INVENTARIS | BUKU IMA
@dashboardBlueprint.route("buku")
@login_required
def buku():
    return render_template("buku.html")
