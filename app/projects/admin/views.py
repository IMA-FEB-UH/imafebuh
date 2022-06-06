from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    session,
    abort,
)
from app.services.firebase import DB
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

adminBlueprint = Blueprint("admin", __name__, template_folder="templates")


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return f(*args, **kwargs)
        else:
            flash("Maaf anda belum login", "warning")
            return redirect(url_for("admin.login"))

    return wrapper


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" in session:
            if session["user"]["level_akses"] == "Super User":
                return f(*args, **kwargs)
            else:
                # flash('Maaf anda bukan admin', 'danger')
                abort(403)
        else:
            flash("Anda belum login", "warning")
            return redirect(url_for("admin.login"))

    return wrapper


def kekasi_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" in session:
            if session["user"]["departemen"] == "Kekasi":
                return f(*args, **kwargs)
            else:
                # flash('Maaf anda bukan admin', 'danger')
                abort(403)
        else:
            flash("Anda belum login", "warning")
            return redirect(url_for("admin.login"))

    return wrapper


@adminBlueprint.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "departemen": request.form["departemen"],
            "nim": request.form["nim"],
            "password": request.form["password"],
            "level_akses": "Basic",
            "otorisasi": "0",
        }
        users = DB.collection("users").where("email", "==", data["email"]).stream()
        user = {}
        for us in users:
            user = us.to_dict()
        if user:
            flash("Email sudah terdaftar !!", "danger")
            return redirect(url_for("admin.register"))

        users = DB.collection("users").where("nim", "==", data["nim"]).stream()
        user = {}
        for us in users:
            user = us.to_dict()
        if user:
            flash("NIM sudah terdaftar !!", "danger")
            return redirect(url_for("admin.register"))

        if data["password"] != request.form["confirm_password"]:
            flash("Password tidak sama", "danger")
            return redirect(url_for("admin.register"))

        data["password"] = generate_password_hash(request.form["password"], "sha256")
        DB.collection("users").document().set(data)
        flash(
            "Selamat..!! Akun sudah diregistrasi hubungi departemen Kekasi untuk otorisasi",
            "success",
        )
        return redirect(url_for("admin.login"))

    return render_template("register.html")


@adminBlueprint.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == "POST":
        data = {"nim": request.form["nim"], "password": request.form["password"]}

        users = DB.collection("users").where("nim", "==", data["nim"]).stream()
        user = {}
        for us in users:
            user = us.to_dict()
        if user and check_password_hash(user["password"], data["password"]):
            # login_user(user)
            session["user"] = user
            session["userId"] = us.id
            # flash('Anda berhasil login', 'success')
            return redirect(url_for("dashboard.dashboard"))
        else:
            flash("Maaf, NIM atau password salah..!!", "danger")

    return render_template("login.html")


@adminBlueprint.route("/logout")
@login_required
def logout():
    session.clear()
    return render_template("login.html")
