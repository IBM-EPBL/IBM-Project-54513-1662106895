{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from flask import Flask.render_template.request\n",
        "import pickle\n",
        "app = Flask(_name_)\n",
        "model = pickle.load(open('wqi.pkl','rb'))\n",
        "@app.route('/')\n",
        "def home() :\n",
        "  return render_template(\"web.html\")\n",
        "@app.route('/login'.methods=['Post'])\n",
        "def login() :\n",
        "  year = request.form[\"year\"]\n",
        "  do = request.form[\"do\"]\n",
        "  ph = request.form[\"ph\"] \n",
        "  co = request.form[\"co\"]\n",
        "  bod = request.form[\"bod\"] \n",
        "  na = request.form[\"na\"] \n",
        "  tc = request.form[\"tc\"]\n",
        "  total = [[int(year),float(do),float(ph),float(co),float(bod),float(na),float(tc)]]\n",
        "  y_pred = model.predict(total)\n",
        "  y_pred = y_pred[[0]]\n",
        "  if(y_pred >= 95 and y_pred <= 100):\n",
        "    return render_template(\"web.html\",showcase = 'Excellent,The predicted value is '+ str(y_pred))\n",
        "  elif(y_pred >= 89 and y_pred <= 94):\n",
        "    return render_template(\"web.html\",showcase = 'Very good,The predicted value is '+ str(y_pred))\n",
        "  elif(y_pred >= 88 and y_pred <= 88):\n",
        "    return render_template(\"web.html\",showcase = 'Good,The predicted value is '+ str(y_pred))\n",
        "  elif(y_pred >= 65 and y_pred <= 79):\n",
        "    return render_template(\"web.html\",showcase = 'Fair,The predicted value is '+ str(y_pred))\n",
        "  elif(y_pred >= 45 and y_pred <= 64):\n",
        "    return render_template(\"web.html\",showcase = 'Marginal,The predicted value is '+ str(y_pred))\n",
        "  else :\n",
        "    return render_template(\"web.html\",showcase = 'Poor,The predicted value is '+ str(y_pred))\n",
        "if__name__##'__main__' :\n",
        "  app.run(debug = True,port = 5000)"
      ],
      "metadata": {
        "id": "d-F-P1TxzMfz"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}