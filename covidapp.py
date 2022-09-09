import json
import requests
import os
from flask import Flask, render_template , request
#import urllib.request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def covid():
    if request.method == "POST":
        country = request.form["country"]
        print(country)
        #api="997ea79e1c9575bd4f087cf90e68205d"
        url = "https://api.covid19api.com/summary"
        print(url)

        response = requests.get(url).json()
        print(response)

        data= {}
        countrydict = response["Countries"]
        for countrydict in countrydict:
            if countrydict["Country"]==country:
                data = {"Country": countrydict["Country"],
                      "TotalConfirmed": countrydict["TotalConfirmed"],
                      "TotalDeaths": countrydict["TotalDeaths"]}
                break

        return render_template("cov.html", data=data)

    else:
        data = None
        return render_template("cov.html", data=data)


port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(port=port)

