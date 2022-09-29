from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from urllib.parse import unquote
from app.services.firebase import Storage, DB, firestore

homeBlueprint = Blueprint(
    "home", __name__, static_folder="staticHome", template_folder="templates"
)


@homeBlueprint.route("/")
@homeBlueprint.route("/home")
def index():
    return render_template("index.html")


@homeBlueprint.route("/tentang_ima")
def about():
    return render_template("about.html")


@homeBlueprint.route("/review_buku")
def review_buku():
    data = (
        DB.collection("Review")
        .order_by("date_posted", direction=firestore.Query.DESCENDING)
        .stream()
    )
    datas = []
    for dt in data:
        d = dt.to_dict()
        d["id"] = dt.id
        datas.append(d)
    return render_template("review_buku.html", data=datas)


@homeBlueprint.route("/review_buku", methods=["GET", "POST"])
def buat_review():
    if request.method == "POST":
        image = request.files["foto"]
        blob = Storage.blob(image.filename)
        blob.upload_from_file(image, content_type=image.headers._list[1][1])
        blob.make_public()
        data = {
            "foto_buku": blob.public_url,
            "judul": request.form["judul"],
            "penulis": request.form["penulis"],
            "isi": request.form["ckeditor"],
            "tanggal": datetime.utcnow().strftime("%d %B, %Y"),
            "date_posted": datetime.utcnow().strftime("%Y/%m/%d"),
        }
        DB.collection("Review").document().set(data)
        return redirect(url_for("home.review_buku"))
    return render_template("review_buku.html")


@homeBlueprint.route("/review_buku/<uid>", methods=["GET", "POST"])
def konten_review(uid):
    data = DB.collection("Review").document(uid).get().to_dict()
    if request.method == "POST":
        datas = {
            "judul": request.form["judul"],
            "penulis": request.form["penulis"],
            "isi": request.form["ckeditor"],
        }
        if "foto" in request.files and request.files["foto"]:
            image = request.files["foto"]

            old_image = data["foto_buku"].split("/")[-1]
            old_blob = Storage.blob(unquote(old_image))
            if old_blob.exists():
                old_blob.delete()

            blob = Storage.blob(image.filename)
            blob.upload_from_file(image, content_type=image.headers._list[1][1])
            blob.make_public()
            datas["foto_buku"] = blob.public_url
        DB.collection("Review").document(uid).set(datas, merge=True)
        return redirect(url_for("home.review_buku"))
    user = DB.collection("Review").document(uid).get().to_dict()
    user["id"] = uid
    return render_template("konten_review.html", data=data, user=user)


@homeBlueprint.route("/review_buku/hapus/<uid>")
def hapus_review(uid):
    data = DB.collection("Review").document(uid).get().to_dict()

    old_image = data["foto_buku"].split("/")[-1]
    old_blob = Storage.blob(unquote(old_image))
    if old_blob.exists():
        old_blob.delete()

    DB.collection("Review").document(uid).delete()
    return redirect(url_for("home.review_buku"))


@homeBlueprint.route("/tulisan_kkn")
def tulisan_kkn():
    data = (
        DB.collection("Tulisan_KKN")
        .order_by("date_posted", direction=firestore.Query.DESCENDING)
        .stream()
    )
    datas = []
    for dt in data:
        d = dt.to_dict()
        d["id"] = dt.id
        datas.append(d)
    return render_template("tulisan_kkn.html", data=datas)


@homeBlueprint.route("/tulisan_kkn", methods=["GET", "POST"])
def buat_tulisan():
    if request.method == "POST":
        image = request.files["foto"]
        blob = Storage.blob(image.filename)
        blob.upload_from_file(image, content_type=image.headers._list[1][1])
        blob.make_public()
        data = {
            "foto_buku": blob.public_url,
            "judul": request.form["judul"],
            "penulis": request.form["penulis"],
            "isi": request.form["ckeditor"],
            "tanggal": datetime.utcnow().strftime("%d %B, %Y"),
            "date_posted": datetime.utcnow().strftime("%Y/%m/%d"),
        }
        DB.collection("Tulisan_KKN").document().set(data)
        return redirect(url_for("home.tulisan_kkn"))
    return render_template("tulisan_kkn.html")


@homeBlueprint.route("/tulisan_kkn/<uid>", methods=["GET", "POST"])
def konten_tulisan(uid):
    data = DB.collection("Tulisan_KKN").document(uid).get().to_dict()
    if request.method == "POST":
        datas = {
            "judul": request.form["judul"],
            "penulis": request.form["penulis"],
            "isi": request.form["ckeditor"],
        }
        if "foto" in request.files and request.files["foto"]:
            image = request.files["foto"]

            old_image = data["foto_buku"].split("/")[-1]
            old_blob = Storage.blob(unquote(old_image))
            if old_blob.exists():
                old_blob.delete()

            blob = Storage.blob(image.filename)
            blob.upload_from_file(image, content_type=image.headers._list[1][1])
            blob.make_public()
            datas["foto_buku"] = blob.public_url
        DB.collection("Tulisan_KKN").document(uid).set(datas, merge=True)
        return redirect(url_for("home.tulisan_kkn"))
    user = DB.collection("Tulisan_KKN").document(uid).get().to_dict()
    user["id"] = uid
    return render_template("konten_tulisan.html", data=data, user=user)


@homeBlueprint.route("/tulisan_kkn/hapus/<uid>")
def hapus_tulisan(uid):
    data = DB.collection("Tulisan_KKN").document(uid).get().to_dict()

    old_image = data["foto_buku"].split("/")[-1]
    old_blob = Storage.blob(unquote(old_image))
    if old_blob.exists():
        old_blob.delete()

    DB.collection("Tulisan_KKN").document(uid).delete()
    return redirect(url_for("home.tulisan_kkn"))
