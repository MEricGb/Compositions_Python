from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root7@127.0.0.1:3306/moroiu_eric'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Compozitii(db.Model):
    __tablename__ = 'compozitii'
    id_compozitie = db.Column(db.Integer, primary_key=True)
    titlu = db.Column(db.String(100), nullable=False)
    gen_muzical = db.Column(db.String(100), nullable=False)
    an_compunere = db.Column(db.Integer, nullable=False)


class Compozitori(db.Model):
    __tablename__ = 'compozitori'
    id_compozitor = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    prenume = db.Column(db.String(100), nullable=False)
    tara_origine = db.Column(db.String(105), nullable=False)
    an_nastere = db.Column(db.Integer, nullable=False)


class CompozitoriCompozitii(db.Model):
    __tablename__ = 'compozitori_compozitii'
    id_compozitor = db.Column(db.Integer, db.ForeignKey('compozitori.id_compozitor'), primary_key=True)
    id_compozitie = db.Column(db.Integer, db.ForeignKey('compozitii.id_compozitie'), primary_key=True)
    detalii = db.Column(db.String(100), nullable=True)

    compozitor = db.relationship('Compozitori', backref=db.backref('compozitor_compozitii', cascade='all, delete-orphan'))
    compozitie = db.relationship('Compozitii', backref=db.backref('compozitori_compozitii', cascade='all, delete-orphan'))



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compozitori_page')
def compozitori_page():
    compozitori = Compozitori.query.all()
    return render_template('compozitori_page.html', compozitori=compozitori)


@app.route('/compozitii_page')
def compozitii_page():
    compozitii = Compozitii.query.all()
    return render_template('compozitii_page.html', compozitii=compozitii)


@app.route('/compozitori_compozitii_page')
def compozitori_compozitii_page():
    compozitori_compozitii = CompozitoriCompozitii.query.all()
    return render_template('compozitori_compozitii_page.html', compozitori_compozitii=compozitori_compozitii)



@app.route('/add_compozitor', methods=['GET', 'POST'])
def add_compozitor():
    if request.method == 'POST':
        nume = request.form['nume']
        prenume = request.form['prenume']
        tara_origine = request.form['tara_origine']
        an_nastere = request.form['an_nastere']
        new_compozitor = Compozitori(nume=nume, prenume=prenume, tara_origine=tara_origine, an_nastere=an_nastere)
        db.session.add(new_compozitor)
        db.session.commit()
        return redirect(url_for('compozitori_page'))
    return render_template('add_compozitor.html')


@app.route('/add_compozitie', methods=['GET', 'POST'])
def add_compozitie():
    if request.method == 'POST':
        titlu = request.form['titlu']
        gen_muzical = request.form['gen_muzical']
        an_compunere = request.form['an_compunere']
        new_compozitie = Compozitii(titlu=titlu, gen_muzical=gen_muzical, an_compunere=an_compunere)
        db.session.add(new_compozitie)
        db.session.commit()
        return redirect(url_for('compozitii_page'))
    return render_template('add_compozitie.html')


@app.route('/add_compozitor_compozitie', methods=['GET', 'POST'])
def add_compozitor_compozitie():
    compozitori = Compozitori.query.all() 
    compozitii = Compozitii.query.all()  
    
    if request.method == 'POST':
        id_compozitor = request.form['id_compozitor']
        id_compozitie = request.form['id_compozitie']
        detalii = request.form['detalii']
    
        existing_association = CompozitoriCompozitii.query.filter_by(
            id_compozitor=id_compozitor,
            id_compozitie=id_compozitie
        ).first()

        try:
            if existing_association:
                existing_association.detalii = detalii
                db.session.commit()
            else:
                new_association = CompozitoriCompozitii(
                    id_compozitor=id_compozitor,
                    id_compozitie=id_compozitie,
                    detalii=detalii
                )
                db.session.add(new_association)
                db.session.commit()

            return redirect(url_for('compozitori_compozitii_page'))

        except Exception as e:
            db.session.rollback()
            return redirect(url_for('compozitori_compozitii_page'))
        
    return render_template('add_compozitor_compozitie.html', compozitori=compozitori, compozitii=compozitii)



@app.route('/edit_compozitor/<int:id>', methods=['GET', 'POST'])
def edit_compozitor(id):
    compozitor = Compozitori.query.get_or_404(id)
    if request.method == 'POST':
        compozitor.nume = request.form['nume']
        compozitor.prenume = request.form['prenume']
        compozitor.tara_origine= request.form['tara_origine']
        compozitor.an_nastere = request.form['an_nastere']

        db.session.commit()
        return redirect(url_for('compozitori_page'))
    
    return render_template('edit_compozitor.html', compozitor=compozitor)

@app.route('/edit_compozitie/<int:id>', methods=['GET', 'POST'])
def edit_compozitie(id):
    compozitie = Compozitii.query.get_or_404(id)
    if request.method == 'POST':
        compozitie.titlu = request.form['titlu']
        compozitie.gen_muzical = request.form['gen_muzical']
        compozitie.an_compunere = request.form['an_compunere']
        
        db.session.commit()
        return redirect(url_for('compozitii_page'))
    
    return render_template('edit_compozitie.html', compozitie=compozitie)



@app.route('/edit_compozitor_compozitie/<int:id_compozitor>/<int:id_compozitie>', methods=['GET', 'POST'])
def edit_compozitor_compozitie(id_compozitor, id_compozitie):
    combine = CompozitoriCompozitii.query.filter_by(id_compozitor=id_compozitor, id_compozitie=id_compozitie).first_or_404()
    
    if not combine:
        return redirect(url_for('compozitori_compozitii_page')) 
    
    if request.method == 'POST':
        combine.detalii = request.form['detalii']
        db.session.commit()
        return redirect(url_for('compozitori_compozitii_page'))

    return render_template('edit_compozitor_compozitie.html', combine=combine)




@app.route('/delete_compozitor/<int:id>')
def delete_compozitor(id):
    compozitor = Compozitori.query.get_or_404(id)
    db.session.delete(compozitor)
    db.session.commit()
    return redirect(url_for('compozitori_page'))

@app.route('/delete_compozitie/<int:id>')
def delete_compozitie(id):
    compozitie = Compozitii.query.get_or_404(id)
    db.session.delete(compozitie)
    db.session.commit()
    return redirect(url_for('compozitii_page'))

@app.route('/delete_compozitor_compozitie/<int:id_compozitor>/<int:id_compozitie>')
def delete_compozitor_compozitie(id_compozitor, id_compozitie):
    entry = CompozitoriCompozitii.query.filter_by(id_compozitor=id_compozitor, id_compozitie=id_compozitie).first_or_404()
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('compozitori_compozitii_page'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Database tables created successfully!")
    app.run(debug=True)
