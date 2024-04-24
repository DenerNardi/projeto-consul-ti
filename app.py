from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def home():
    connection = sql.connect("empresas_db.db")
    connection.row_factory=sql.Row
    cursor = connection.cursor()
    command = f'SELECT * FROM empresas'
    cursor.execute(command)
    result = cursor.fetchall()

    return render_template("home.html", datas=result)
   

@app.route("/cadastrar-empresa")
def cadastrar_empresa():
    return render_template("add_company.html")

@app.route("/cadastrar-empresa", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        razao_social = request.form["razao_social"]
        nfant = request.form["nome_fantasia"]
        cnpj = request.form["cnpj"]
        connection = sql.connect("empresas_db.db")
        cursor = connection.cursor()

        if razao_social and nfant and cnpj:
            command = f'INSERT INTO empresas (razao_social, nome_fantasia, cnpj) VALUES ("{razao_social}", "{nfant}", "{cnpj}")'
            cursor.execute(command)
            connection.commit()
            return redirect(url_for("home"))
    return  render_template("add_company.html")


@app.route("/editar-empresa/<string:id>", methods=["GET", "POST"])
def editar(id):
    if request.method =="POST":
        razao_social = request.form["razao_social"]
        nfant = request.form["nome_fantasia"]
        cnpj = request.form["cnpj"]
        connection = sql.connect("empresas_db.db")
        cursor = connection.cursor()      
        command = f'UPDATE empresas SET razao_social= "{razao_social}",nome_fantasia = "{nfant}", cnpj="{cnpj}" WHERE idempresas={id}'
        cursor.execute(command)
        connection.commit()
        return redirect(url_for("home"))
    connection=sql.connect("empresas_db.db")
    connection.row_factory=sql.Row
    cursor = connection.cursor()
    command = f'SELECT * FROM empresas WHERE idempresas={id}'
    cursor.execute(command)
    empresas=cursor.fetchone()
    return render_template("edit_company.html", datas=empresas) 


@app.route("/deletar/<string:id>", methods=["GET"])
def deletar(id):
    connection = sql.connect("empresas_db.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM empresas where idempresas={id}")
    connection.commit()
    return redirect(url_for("home"))

if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)
