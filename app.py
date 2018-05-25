__author__ = "Rajat Kulshreshtha"
"""
Provides a Web Interface for Simulation Tracker.
"""
from flask import Flask, render_template
from SQLdatabase import displaydata
import webbrowser
import subprocess

app = Flask(__name__, template_folder="C:\\Users\\RAJAT KULSHRESHTHA\\template")

@app.route("/")
def main():
    displaydat = displaydata(server='localhost',user='root', password='', db='reports')
    display, tables = displaydat.select()
    return render_template('template.html', display=display, tables = tables)
    

if __name__=="__main__":
    url = "http://localhost:5000"
    webbrowser.Chrome('chrome')
    webbrowser.open_new_tab(url)
    app.run()