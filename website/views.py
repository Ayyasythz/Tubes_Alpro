import base64
from io import BytesIO
from flask import Blueprint, redirect, render_template, request, send_file, url_for
from flask_login import  login_required, current_user
from sqlalchemy import func
from . import db

from website.models import User, Wallpaper
views = Blueprint('views', __name__)

@views.route('/')
def home():
    wallpapers = Wallpaper.query.all()
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Anime')
def anime():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Anime'")
    for a in wallpapers:
        x  =a.date
        print(a.date.strftime("%b %d %Y"))
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Tech')
def tech():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Tech'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Beauty')
def beauty():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Beauty'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Design')
def design():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Design'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Illustration')
def illus():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Illustrations'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Abstract')
def abstract():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Abstract'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Fashions')
def fashions():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Fashions'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Arts')
def arts():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Arts'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/Music')
def music():
    wallpapers = db.engine.execute("SELECT * FROM wallpaper where tipeWallpaper = 'Music'")
    wallpapers = list(wallpapers)
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    return render_template("home.html", user=current_user,wallpapers = zip(wallpapers,imgWallpaper))

@views.route('/dashboard/<string:nama>')
@login_required
def dashboard(nama):
    user = User.query.filter_by(username = nama).first()
    wallpaper = Wallpaper.query.filter_by(user_id=current_user.id).count()
    if user == current_user:
        return render_template("dashboard.html", user = user, wallpaper=wallpaper)
    else:
        return redirect(url_for('views.home'))

@views.route('/dashboard/<string:nama>/profile')
@login_required
def profile(nama):
    user = User.query.filter_by(username = nama).first()
    wallpaper = Wallpaper.query.filter_by(user_id=current_user.id).count()
    jml_download = Wallpaper.query.filter_by(user_id=current_user.id).all()
    wallpapers = Wallpaper.query.all()
    imgWallpaper = []
    for i in wallpapers:
        imageData = base64.b64encode(i.dataWallpaper)
        imgWallpaper.append(imageData.decode("UTF-8"))
    sum = 0
    for x in jml_download:
        print(x.downloads)
        sum += x.downloads
    if user == current_user:
        return render_template("profile.html", user=user,wallpaper = wallpaper,jml_download=sum)
    else:
        return redirect(url_for('views.home'))
    

@views.route('/dashboard/<string:nama>/add-wallpaper', methods = ['GET','POST'])
@login_required
def add_wallaper(nama):
    user = User.query.filter_by(username = nama).first()
    if user == current_user:
        if request.method == 'GET':
            return render_template("add-wallpaper.html",user = user)
        if request.method == 'POST':
            wallpaper = Wallpaper.query.filter_by(user_id=current_user.id).count()
            wallpaperTitle = request.form.get('wallpaperTitle')
            wallpaperSubTitle = request.form.get('wallpaperSubTitle')
            tipeWallpaper = request.form.get('tipeWallpaper')
            file = request.files['wallpaperFile']
            upload_wallpaper = Wallpaper(wallpaperTitle=wallpaperTitle,wallpaperSubTitle=wallpaperSubTitle,tipeWallpaper=tipeWallpaper,fileWallpaper=file.filename,dataWallpaper=file.read(),user_id=current_user.id)
            wallpaper+=1
            db.session.add(upload_wallpaper)
            db.session.commit()
            return redirect(url_for('views.dashboard', nama=current_user.username))
    else:
        return redirect(url_for('views.home'))
    

@views.route('/dashboard/<string:nama>/wallpaper', methods= ['GET'])
@login_required
def wallpaper(nama):
    user = User.query.filter_by(username = nama).first()
    wallpapers = Wallpaper.query.all()
    if user == current_user:
        return render_template("table-wallpaper.html", wallpapers = wallpapers, user=current_user)
    else:
        return redirect(url_for('views.home'))
    
@views.route('/dashboard/<int:id>/update', methods = ['GET', 'POST'])
def update(id,nama):
    wallpaper = Wallpaper.query.filter_by(id=id).first()
    user = User.query.filter_by(username = nama).first()
    if request.method == "POST":
        if wallpaper:
            db.session.delete(wallpaper)
            db.session.commit()
            
            wallpaperTitle = request.form.get('wallpaperTitle')
            wallpaperSubTitle = request.form.get('wallpaperSubTitle')
            tipeWallpaper = request.form.get('tipeWallpaper')
            file = request.files['wallpaperFile']
            upload_wallpaper = Wallpaper(wallpaperTitle=wallpaperTitle,wallpaperSubTitle=wallpaperSubTitle,tipeWallpaper=tipeWallpaper,fileWallpaper=file.filename,dataWallpaper=file.read(),user_id=current_user.id)
            
            db.session.add(wallpaper)
            db.session.commit()
            return redirect(url_for('views.wallpaper', user = current_user))
        

@views.route('download/<wp_id>')
def download(wp_id):
    wallpaper = Wallpaper.query.filter_by(id=wp_id).first()
    wallpaper.downloads += 1
    db.session.commit()
    return send_file(BytesIO(wallpaper.dataWallpaper), attachment_filename=wallpaper.fileWallpaper, as_attachment=True)
    




    
    
    
    