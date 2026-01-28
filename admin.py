from flask import Blueprint, render_template, redirect, flash, request
from flask_jwt_extended import jwt_required, get_jwt
from database import get_db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

def admin_only():
    claims = get_jwt()
    return claims.get("role") == "admin"

@admin_bp.route("/dashboard")
@jwt_required()
def dashboard():
    if not admin_only():
        return render_template("403.html"), 403
    return render_template("admin/dashboard.html")

@admin_bp.route("/books", methods=["GET", "POST"])
@jwt_required()
def books():
    if not admin_only():
        return render_template("403.html"), 403

    db = get_db()

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]

        db.execute(
            "INSERT INTO books (title, author, available) VALUES (?, ?, 1)",
            (title, author)
        )
        db.commit()
        flash("Book added successfully")

        return redirect("/admin/books")

    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("admin/books.html", books=books)

@admin_bp.route("/books/add", methods=["GET", "POST"])
@jwt_required()
def add_book():
    if not admin_only():
        return render_template("403.html"), 403

    if request.method == "POST":
        db = get_db()
        db.execute(
            "INSERT INTO books (title, author, available) VALUES (?, ?, 1)",
            (request.form["title"], request.form["author"])
        )
        db.commit()
        flash("Book added successfully")
        return redirect("/admin/books")

    return render_template("admin/add_book.html")
