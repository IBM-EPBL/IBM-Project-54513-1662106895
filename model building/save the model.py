{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": []
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
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7Hk8lZ4aV1S9",
        "outputId": "a3d74893-a4ab-4274-c82d-7586cb2b8f09"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting findspark\n",
            "  Downloading findspark-2.0.1-py2.py3-none-any.whl (4.4 kB)\n",
            "Installing collected packages: findspark\n",
            "Successfully installed findspark-2.0.1\n"
          ]
        }
      ],
      "source": [
        "pip install findspark"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pyspark"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qC3B9aQ1WPuG",
        "outputId": "38dfbf43-b1e0-4623-8a85-3ec4d1b644a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pyspark\n",
            "  Downloading pyspark-3.3.1.tar.gz (281.4 MB)\n",
            "\u001b[K     |████████████████████████████████| 281.4 MB 43 kB/s \n",
            "\u001b[?25hCollecting py4j==0.10.9.5\n",
            "  Downloading py4j-0.10.9.5-py2.py3-none-any.whl (199 kB)\n",
            "\u001b[K     |████████████████████████████████| 199 kB 44.7 MB/s \n",
            "\u001b[?25hBuilding wheels for collected packages: pyspark\n",
            "  Building wheel for pyspark (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pyspark: filename=pyspark-3.3.1-py2.py3-none-any.whl size=281845514 sha256=79060493224d8fc16f5e1a17b94edd258d52d4cf17f3c89c0df8535805d1d74f\n",
            "  Stored in directory: /root/.cache/pip/wheels/42/59/f5/79a5bf931714dcd201b26025347785f087370a10a3329a899c\n",
            "Successfully built pyspark\n",
            "Installing collected packages: py4j, pyspark\n",
            "Successfully installed py4j-0.10.9.5 pyspark-3.3.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install geopandas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Eh2jIzywWhgr",
        "outputId": "f9373078-2077-4899-acdb-9ba2afb2a350"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting geopandas\n",
            "  Downloading geopandas-0.10.2-py2.py3-none-any.whl (1.0 MB)\n",
            "\u001b[K     |████████████████████████████████| 1.0 MB 8.1 MB/s \n",
            "\u001b[?25hCollecting fiona>=1.8\n",
            "  Downloading Fiona-1.8.22-cp37-cp37m-manylinux2014_x86_64.whl (16.7 MB)\n",
            "\u001b[K     |████████████████████████████████| 16.7 MB 40.9 MB/s \n",
            "\u001b[?25hCollecting pyproj>=2.2.0\n",
            "  Downloading pyproj-3.2.1-cp37-cp37m-manylinux2010_x86_64.whl (6.3 MB)\n",
            "\u001b[K     |████████████████████████████████| 6.3 MB 39.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: shapely>=1.6 in /usr/local/lib/python3.7/dist-packages (from geopandas) (1.8.5.post1)\n",
            "Requirement already satisfied: pandas>=0.25.0 in /usr/local/lib/python3.7/dist-packages (from geopandas) (1.3.5)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (57.4.0)\n",
            "Collecting munch\n",
            "  Downloading munch-2.5.0-py2.py3-none-any.whl (10 kB)\n",
            "Collecting click-plugins>=1.0\n",
            "  Downloading click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)\n",
            "Collecting cligj>=0.5\n",
            "  Downloading cligj-0.7.2-py3-none-any.whl (7.1 kB)\n",
            "Requirement already satisfied: six>=1.7 in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (1.15.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (2022.9.24)\n",
            "Requirement already satisfied: click>=4.0 in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (7.1.2)\n",
            "Requirement already satisfied: attrs>=17 in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (22.1.0)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.25.0->geopandas) (2022.6)\n",
            "Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.25.0->geopandas) (1.21.6)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.25.0->geopandas) (2.8.2)\n",
            "Installing collected packages: munch, cligj, click-plugins, pyproj, fiona, geopandas\n",
            "Successfully installed click-plugins-1.1.1 cligj-0.7.2 fiona-1.8.22 geopandas-0.10.2 munch-2.5.0 pyproj-3.2.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "%matplotlib inline\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import geopandas as gpd\n",
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n",
        "\n",
        "from pylab import *\n",
        "from pyspark.sql.functions import udf, concat, col, lit\n",
        "from pyspark import SparkConf, SparkContext\n",
        "from pyspark.sql import SparkSession, SQLContext\n",
        "\n",
        "from pyspark.sql.types import *\n",
        "import pyspark.sql.functions as F\n",
        "sc = SparkContext.getOrCreate(SparkConf().setMaster(\"local[*]\"))\n",
        "from pyspark.sql import SparkSession\n",
        "spark = SparkSession \\\n",
        "    .builder \\\n",
        "    .getOrCreate()\n",
        "sqlContext = SQLContext(sc)"
      ],
      "metadata": {
        "id": "mXVz_NQOWq0-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "yHLGf57vWy82",
        "outputId": "47fd4a84-2404-4a89-f100-140882fde033"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-445b2d79-4d9a-495d-a4ff-38089a229f08\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-445b2d79-4d9a-495d-a4ff-38089a229f08\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving water_data.csv to water_data.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df = pd.read_csv('water_data.csv', encoding=\"cp1252\")"
      ],
      "metadata": {
        "id": "NaRRYC6mXFCh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = spark.read.format(\"csv\").option(\"header\", \"true\").load('water_data.csv')"
      ],
      "metadata": {
        "id": "31JEyqbVqhRP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.show(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UGgdE1iAq8ke",
        "outputId": "16f3a4a4-8a5c-4eb2-cef1-f9a6495d339e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+------------+--------------------+-----------+----+---+---+------------+---+-------------------+--------------+--------------+\n",
            "|STATION CODE|           LOCATIONS|      STATE|TEMP| DO| pH|CONDUCTIVITY|BOD|NITRATE_N_NITRITE_N|FECAL_COLIFORM|TOTAL_COLIFORM|\n",
            "+------------+--------------------+-----------+----+---+---+------------+---+-------------------+--------------+--------------+\n",
            "|        1312|GODAVARI AT JAYAK...|MAHARASHTRA|29.2|6.4|8.1|         735|3.4|                  2|             3|            73|\n",
            "|        2177|GODAVARI RIVER NE...|MAHARASHTRA|24.5|  6|  8|         270|3.1|                  2|            72|           182|\n",
            "|        2182|GODAVARI RIVER AT...|MAHARASHTRA|25.8|5.5|7.8|         355|4.2|                  9|            59|           133|\n",
            "|        2179|GODAVARI RIVER AT...|MAHARASHTRA|24.8|5.5|7.8|         371|5.6|               3.55|            90|           283|\n",
            "|        2183|GODAVARI RIVER AT...|MAHARASHTRA|25.7|5.7|7.9|         294|3.2|               2.69|            45|           132|\n",
            "+------------+--------------------+-----------+----+---+---+------------+---+-------------------+--------------+--------------+\n",
            "only showing top 5 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.dtypes"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gE6JIUSCrA5Q",
        "outputId": "0ac40455-ae32-424c-d600-a0a54e89db7d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('STATION CODE', 'string'),\n",
              " ('LOCATIONS', 'string'),\n",
              " ('STATE', 'string'),\n",
              " ('TEMP', 'string'),\n",
              " ('DO', 'string'),\n",
              " ('pH', 'string'),\n",
              " ('CONDUCTIVITY', 'string'),\n",
              " ('BOD', 'string'),\n",
              " ('NITRATE_N_NITRITE_N', 'string'),\n",
              " ('FECAL_COLIFORM', 'string'),\n",
              " ('TOTAL_COLIFORM', 'string')]"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.sql.types import FloatType"
      ],
      "metadata": {
        "id": "u5VZkGFCrGW6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = df.withColumn(\"TEMP\",df[\"TEMP\"].cast(FloatType()))\n",
        "df = df.withColumn(\"pH\",df[\"pH\"].cast(FloatType()))\n",
        "df = df.withColumn(\"DO\",df[\"DO\"].cast(FloatType()))\n",
        "df = df.withColumn(\"CONDUCTIVITY\",df[\"CONDUCTIVITY\"].cast(FloatType()))\n",
        "df = df.withColumn(\"BOD\",df[\"BOD\"].cast(FloatType()))\n",
        "df = df.withColumn(\"NITRATE_N_NITRITE_N\",df[\"NITRATE_N_NITRITE_N\"].cast(FloatType()))\n",
        "df = df.withColumn(\"FECAL_COLIFORM\",df[\"FECAL_COLIFORM\"].cast(FloatType()))\n",
        "df.dtypes"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d0PFtCLPrMW_",
        "outputId": "e8c6957f-a9b0-4936-b210-6fbbbee2aee4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('STATION CODE', 'string'),\n",
              " ('LOCATIONS', 'string'),\n",
              " ('STATE', 'string'),\n",
              " ('TEMP', 'float'),\n",
              " ('DO', 'float'),\n",
              " ('pH', 'float'),\n",
              " ('CONDUCTIVITY', 'float'),\n",
              " ('BOD', 'float'),\n",
              " ('NITRATE_N_NITRITE_N', 'float'),\n",
              " ('FECAL_COLIFORM', 'float'),\n",
              " ('TOTAL_COLIFORM', 'string')]"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=df.drop('TOTAL_COLIFORM')"
      ],
      "metadata": {
        "id": "rHSMYyr4sM-C"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.createOrReplaceTempView(\"df_sql\")"
      ],
      "metadata": {
        "id": "l-VuEkEZsa1N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_clean = spark.sql('''Select * from df_sql where TEMP is not null and DO is not null \n",
        "                        and pH is not null and BOD is not null and CONDUCTIVITY is not null\n",
        "                        and NITRATE_N_NITRITE_N is not null and FECAL_COLIFORM is not null''')"
      ],
      "metadata": {
        "id": "rlaAHdufsdbW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_clean.createOrReplaceTempView(\"df_sql\")"
      ],
      "metadata": {
        "id": "1Q8g_xA_sin1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "do = spark.sql(\"Select DO from df_sql\")\n",
        "do = do.rdd.map(lambda row : row.DO).collect()\n",
        "ph = spark.sql(\"Select pH from df_sql\")\n",
        "ph = ph.rdd.map(lambda row : row.pH).collect()\n",
        "bod = spark.sql(\"Select BOD from df_sql\")\n",
        "bod = bod.rdd.map(lambda row : row.BOD).collect()\n",
        "nn = spark.sql(\"Select NITRATE_N_NITRITE_N from df_sql\")\n",
        "nn = nn.rdd.map(lambda row : row.NITRATE_N_NITRITE_N).collect()"
      ],
      "metadata": {
        "id": "ER2diR0LsqmK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fig,ax = plt.subplots(num=None,figsize=(14,6), dpi=80, facecolor='w', edgecolor='k')\n",
        "size=len(do)\n",
        "ax.plot(range(0,size), do, color='blue', animated=True, linewidth=1, label='Dissolved Oxygen')\n",
        "ax.plot(range(0,size), ph, color='red', animated=True, linewidth=1, label='pH')\n",
        "fig,ax2 = plt.subplots(num=None,figsize=(14,6), dpi=80, facecolor='w', edgecolor='k')\n",
        "ax2.plot(range(0,size), bod, color='orange', animated=True, linewidth=1, label='BOD')\n",
        "ax2.plot(range(0,size), nn, color='green', animated=True, linewidth=1, label='NN')\n",
        "legend=ax.legend()\n",
        "legend=ax2.legend()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 809
        },
        "id": "SC4zacZpst2b",
        "outputId": "69005891-35ab-456f-9e63-71c75e1018e7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1120x480 with 1 Axes>"
            ],
            "image/png": "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4NKlSwgNDQUA1K1bFz169MCyZcswf/58TJkypdBjUIJsJRtpjfp2b29vGAyGQv9Ge3BOIhEReaSJE4FvvnH1URARaU+nk0yfVl+OlJquXbsW8+fPx8SJE/P9LDY2Fg0bNsQzzzyDSZMmITo6GgaDASdPnkSHDh3wyiuvYMCAAdi1axeaNm2KnJwc/PHHHwBk/t6FCxdMC+SoPfLII9i9ezc+/vhjDB06FD4+PqbbFyxYYJormJWVhX379gEAevXqhUWLFsFoNOLGjRv46aefrP49gYGBeOmllzB27FhcvnwZAHDlyhWMHTsWEyZMQIUKFQAAo0aNwpAhQ7B8+XI89dRTuHLliukxXnrpJUyePBnJycno1asXAKBp06bIysrC1q1bAQBbt241ldIGBgaiZ8+e+OSTT0yPkZCQgPj4eHvfBocxk0hERB7p1i35IiKikjF48GAEBAQgLS0NzZs3x/r1663O75s7dy7++usv+Pn5wdvbG59//jmys7MxcuRIXL16FT4+PqhRowYWLVoEPz8/rF69GuPHj8fEiRMREBCAlStXIjAw0BSsKfz9/TFo0CDMmzcPR48eNd0+ZMgQXLlyxVTSaTAYMHLkSLRt2xZvv/02Ro8ejWbNmqFGjRro3r07MjIyrP59H3/8MaZNm4auXbvC29sbOTk5GDVqlKmsde7cubh69SrefvtteHl5Ydy4cXj66afx66+/QqfTITw8HJUrV8bYsWNN2UJ/f38sXboUzz//PHJyctC+fXs0bdrUtLXHkiVLMGHCBLRs2RI6nQ4VKlRAZGRknlJbLeiMLtrYIygoqESiYCIiKpv69wfatwcmT3b1kRAROU92djaOHz+O0NBQeHt7u/pwqAjOnz+PDh064Pjx46ioquFNSUkxfb979248/PDDOHnyJMqXL1/s5yzofCkoHrOr3HT8+PEIDg6GTqfD/v37TbdnZGTghRdeQEhICMLCwjB06NBi/AlERETOk5MDqNYmICIicpl33nkHnTt3xieffJInQASAVatWoXXr1mjVqhXGjh2LxYsXOyVALA67yk0HDBiA1157zbTykOKNN96ATqfD8ePHodPpcOHCBU0OkoiIqKiysyVQJCIicrUpU6bYXKxm+PDhGD58eMkeUCHsChJ79OiR77a0tDR88803iI+PN9XU1q5d27lHR0RE5KDsbGYSiYiI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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1120x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA4kAAAGMCAYAAAB3fOfPAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAMTQAADE0B0s6tTgAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeZQc9X3v/U/1MjOSRrtAEh6EkLWAjY2QLZvgOHiPr6+PsS8h5BDASiBA7iHOE/lJ4HmI7+F5QjC+j6Mkts8N2MHK9dGNAzFebrzia7NesC2x2LFsQAK0IQmhkWZfuruqnj9+Xd3VPd093VW9Vc37dY7OjGZ6ekrqme761Pf7+/4s13VdAQAAAAAgKdHpAwAAAAAAdA9CIgAAAACggJAIAAAAACggJAIAAAAACgiJAAAAAIACQiIAAAAAoICQCAAAAAAoSHXqG/f29uqMM87o1LcHAAAAgDnrtdde0/T0dMXPdSwknnHGGTpy5Einvj0AAAAAzFkDAwNVP0e7KQAAAACggJAIAAAAACjoWLspAAAAALSL4zhyXbfTh9E2lmUpkQhWEyQkAgAAAIgtx3F08OBBTU1NdfpQ2q6vr0/nnHNOw2GRkAgAAAAgtk6cOKFEIqENGzbIsqxOH07buK6rV155RSdOnNCqVasa+lpCIgAAAIBYcl1XQ0NDWrt2rVKpuRd9Vq5cqQMHDmjlypUNBWQG1wAAAACIJdd15bqu0ul0pw+lI9LpdOH/oBGERAAAAACxNJcG1dRCSAQAAACALrV27Vpt2rRJmzdv1vnnn6+rrrpK4+PjkqRvf/vb2rp1qzZt2qR169bppptu0sjISOFr3/Wud+ncc8/V5s2btX79er3//e/Xd77znaYfIyERAAAAANrovvvu07PPPqu9e/dqeHhY//RP/6Tvf//7uvHGG/XFL35Rzz//vF544QWl02l9+MMfLqkE/u3f/q2effZZ7d+/X7fddpuuu+46ff3rX2/q8RESAQAAAKADMpmMJiYmtHTpUt1xxx267bbbdNFFF0mSUqmU/uZv/kYvvfSSHnrooYpf/653vUu33367Pv3pTzf1uAiJAAAAAOYG15WyI637U+favyuvvFKbN2/WqlWrlEgk9Lu/+7t6+umn9Ru/8Rslt+vp6dFb3vIWPfXUU1Xv6+1vf7v27t0b6r+l3NybAwsAAABgbsqNSv+6uHX3f8WwlF40683uu+8+bd68WblcTjfeeKNuueWWwN+yFcN5CIkAEIZjS5OvSAvWdPpIAADAbFILTZBr5f03cvNUSpdffrn+/M//XFu2bNGTTz5ZaDeVTDvqU089pU984hNV72P37t264IILAh9yxeNq6r0BwFzz2mPSU38qfejnnT4SAAAwG8uqq9LXTj/+8Y+1adMmXX/99br++ut1ySWXFKqMn/zkJ7V27Vq95z3vqfi1jz32mG6//XZ94QtfaOoxERIBIAx7WrKnOn0UAAAgQq688krNmzdPuVxO55xzju6++26dffbZ+od/+Addd911GhsbUzab1fve9z595zvfkWVZha/9sz/7M91+++0aHx/XOeecoy996Uv68Ic/3NTjIyQCQCiO5DqdPggAABARBw4cqPq5yy67TJdddlnVzz/88MPNP6AKmG4KAGG4riRCIgAAiA9CIgCEQiURAADECyERAMJwXUIiAACIFUIiAIRCuykAAIgXQiIAhOHSbgoAAOKFkAgAodBuCgAA4oWQCABhuI5oNwUAAHFCSASAUKgkAgCA+q1du1bnnXeecrlc4WNvfetb9fDDD+v222+XZVl67LHHCp/7whe+oG3btrX1GAmJABAKIREAADRmenpa9957b8XPrV27Vrfcckubj6hUqqPfHQCijsE1AABEhuu6Gs2Mtuz+F/YslGVZs97u9ttv12233aZrrrlG8+fPL/ncRz7yET3xxBP6xje+oY997GOtOtSaCIkAEIbLFhgAAETFaGZUi+9a3LL7H751WIt6F816uwsvvFDvfve79bd/+7e67bbbSj5nWZbuuusu3XzzzfrIRz7SqkOtiZAIAKHQbgoAQFQs7Fmo4VuHW3r/9fqrv/orve1tb9NNN90043Pvfe97dfbZZ+vLX/5yMw+vboREAAiDdlMAACLDsqy6Kn3tsHbtWl111VW64447Kn7+rrvu0mWXXaY/+ZM/afORERIBICTaTQEAQDB/+Zd/qfPPP1/pdHrG57Zs2aLf/M3f1D/8wz/o0ksvbetxMd0UAMKgkggAAAJasWKFPvGJT+jYsWMVP//Xf/3XeuWVV9p8VFQSASAk1iQCAID6HThwoOTvn/rUp/SpT31KkvSud72r5HPr1q1TJpNp05EVUUkEgFBoNwUAAPFCSASAMGg3BQAAMVNXSBwcHNTmzZsLfzZu3KhUKqVTp07pxIkT+uAHP6gNGzboggsu0KOPPtrqYwaALuLm37idPQwAAIAmqWtN4vLly/Xss88W/v7Zz35WjzzyiJYtW6Y//MM/1MUXX6zvf//72r17tz72sY/p5ZdfrjihBwBixwuHriNZyc4eCwAAKGFZliTJnaMXc71/t/f/UK9Ag2vuvfdeffrTn5Yk3X///dq/f78kaevWrTrrrLP0yCOP6H3ve1+QuwaAiHF8bwmJAAB0k0QioXQ6rcHBQS1fvrzhsBRlrutqcHBQ6XRaiURjqwwbDolPPPGETp8+rQ9/+MMaHBxUNpvVqlWrCp9fu3atDh061OjdAkA0+SuJAACg66xZs0aHDh3SqVOnOn0obZdOp7VmzZqGv67hkHjvvffq2muvVSrV2Jfu2LFDO3bsKPx9bGys0W8NAF0oHw4JiQAAdKWenh6tX79ejuPMqbZTy7IariB6Gkp6Y2Njuv/++7V7925JZq1iKpXS8ePHC9XEAwcOVEyr27dv1/bt2wt/HxgYCHTAANBVCi82hEQAALpZ0MA0FzX0P3Xffffpwgsv1HnnnVf42BVXXKG7775bkrR792698soruvTSS5t7lADQtWg3BQAA8dJQJfHee+/VH/3RH5V87DOf+YyuueYabdiwQT09Pdq1axeTTQHMHS7tpgAAIF4aColPPPHEjI+tXLlSDz74YNMOCACihXZTAAAQLzTmAkAYTDcFAAAxQ0gEgFBoNwUAAPFCSASAMKgkAgCAmCEkAkAoTtlbAACAaCMkAkAYVBIBAEDMEBIBIBRCIgAAiBdCIgCE4dJuCgAA4oWQCAChUEkEAADxQkgEgDBctsAAAADxQkgEgFCoJAIAgHghJAJAGIXppnZnjwMAAKBJCIkAEAqDawAAQLwQEgEgDPZJBAAAMUNIBIBQCIkAACBeCIkAEAb7JAIAgJghJAJAKFQSAQBAvBASASAM9kkEAAAxQ0gEgFCoJAIAgHghJAJAKPmQyJpEAAAQE4REAAiDdlMAABAzhEQACIV2UwAAEC+ERAAIw6XdFAAAxAshEQDCoN0UAADEDCERAEKh3RQAAMQLIREAwiiEQ0IiAACIB0IiAIRCJREAAMQLIREAQiEkAgCAeCEkAkAYDK4BAAAxQ0gEgFDYAgMAAMQLIREAwqCSCAAAYoaQCAChsCYRAADECyERAMJwaTcFAADxQkgEgFBoNwUAAPFCSASAMFzaTQEAQLzUHRKnp6d18803a8OGDXrTm96kq6++WpK0b98+XXLJJdq4caO2bt2qvXv3tuxgAaD7EBIBAEC8pOq94a233irLsvTCCy/IsiwdP35cknTjjTfqhhtu0LZt2/S1r31N27Zt0+7du1t2wADQVQrhkJAIAADioa6QOD4+rnvvvVdHjhyRZVmSpFWrVunEiRPas2ePHnzwQUnS5Zdfrptvvln79+/X+vXrW3fUANA1qCQCAIB4qavd9MUXX9SyZct055136q1vfave+c536kc/+pEOHz6s1atXK5UyWdOyLK1Zs0aHDh1q6UEDQNdgn0QAABAzdYXEXC6ngwcP6g1veIP27Nmjz33uc7ryyiuVy+Xq/kY7duzQwMBA4c/Y2FjggwaA7sEWGAAAIF7qColr1qxRIpHQ7//+70uSLrroIp177rk6ePCgjh07VgiLruvq0KFDWrNmzYz72L59u44cOVL409/f38R/BgB0CNNNAQBAzNQVElesWKH3vve9+sEPfiBJevnll/Xyyy/rHe94h7Zs2aJdu3ZJkh544AENDAywHhHAHEK7KQAAiJe6p5vefffduu6663TLLbcokUjonnvu0ete9zrdc8892rZtm+68804tWrRIO3fubOXxAkB3cWk3BQAA8VJ3SFy3bp0eeuihGR/ftGmTnnzyyaYeFABEB+2mAAAgXupqNwUAVMF0UwAAEDOERAAIhUoiAACIF0IiAIRRCIeERAAAEA+ERAAIhUoiAACIF0IiAIRCSAQAAPFCSASAMGg3BQAAMUNIBIAwXCqJAAAgXgiJABAKIREAAMQLIREAwqDdFAAAxAwhEQBCoZIIAADihZAIAGF44ZCQCAAAYoKQCAChUEkEAADxQkgEgFBcyUqKNYkAACAuCIkAEIbrSFaKSiIAAIgNQiIAhJKvJBISAQBATBASASAM16HdFAAAxAohEQBCcaUE7aYAACA+CIkAEIZLuykAAIgXQiIAhOIQEgEAQKwQEgEgDNc1001ZkwgAAGKCkAgAodBuCgAA4oWQCABhuA6DawAAQKwQEgEgFJctMAAAQKwQEgEgDJfBNQAAIF4IiQAQSn5wDSERAADEBCERAMJwXbMmkXZTAAAQE4REAAjFoZIIAABihZAIAGG4bIEBAADihZAIAKEQEgEAQLwQEgEgDG+fRNYkAgCAmCAkAkAoVBIBAEC8EBIBIAz2SQQAADFDSASAUPL7JNJuCgAAYoKQCACh0G4KAADihZAIAGF4g2sIiQAAICbqDolr167Vpk2btHnzZm3evFn33XefJGnfvn265JJLtHHjRm3dulV79+5t2cECQNcp7JNod/pIAAAAmiLVyI3vu+8+bd68ueRjN954o2644QZt27ZNX/va17Rt2zbt3r27qQcJAN3LC4mZTh8IAABAU4RqNz1x4oT27Nmjq6++WpJ0+eWX6/Dhw9q/f39TDg4Aup7rMLgGAADESkMh8dprr9Wb3vQmXXfddXrttdd0+PBhrV69WqmUKUhalqU1a9bo0KFDLTlYAOg+DK4BAADxUndIfPTRR/WLX/xCTz/9tFasWKGPf/zjDX2jHTt2aGBgoPBnbGys4YMFgK7DPokAACBmLNd13Ua/6NixY9q4caNefPFFrV+/XqdOnVIqlZLrulq9erUef/xxrV+/vuZ9DAwM6MiRI4EPHAC6wjfXSKs/II0flN7zw04fDQAAQF1q5bG6Konj4+MaGhoq/P2rX/2qLrroIp155pnasmWLdu3aJUl64IEHNDAwMGtABID4oN0UAADES13TTV999VVdfvnlsm1brutq3bp1+spXviJJuueee7Rt2zbdeeedWrRokXbu3NnSAwaAruINriEkAgCAmKgrJK5bt07PPPNMxc9t2rRJTz75ZFMPCgCiI19JZLopAACIiVBbYADAnMfgGgAAEDOERAAIxZUStJsCAID4ICQCQBgug2sAAEC8EBIBIJT84BrWJAIAgJggJAJAGFQSAQBAzBASASAUQiIAAIgXQiIAhOE6ZnAN7aYAACAmCIkAEAqVRAAAEC+ERAAIg30SAQBAzBASASAUl+mmAAAgVgiJABAG000BAEDMEBIBIJT84BpCIgAAiAlCIgCEQSURAADEDCERAELJh8SQaxId15FD0AQAAF2AkAgAYbiOGVwTMuB96sef0l2P39WkgwIAAAgu1ekDAIBoa0676anJU8rYmSYdEwAAQHBUEgEgDK+SSLspAACICUIiAITiSonwlUTbtWW7dpOOCQAAIDhCIgAE5brmbRPaTakkAgCAbkFIBIDAvJBIuykAAIgPQiIABNXESqLt2rId2k0BAEDnERIB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H/zgB7VhwwZdcMEFevTRR1t6wADQPZymVBKL000jtAVGlCuJbtY8XlEMuf41ibUG15RPN82OSOnFUmqBuaAxW8upa7dnei2VRCBe6qkkZk5L9kR7jwsNq7uSeMMNN+j555/Xz3/+c1122WW6/vrrJUm33nqrLr74Yu3bt087d+7UVVddpWyWRaoA5gDXN7gmxBYYjusoYSWUtCzZUaimeCExEeHBNYl0NIel2NMzw6FdNrjGW5Pobzf19i6zLKlnqTQ9y4TTdrWbFiqJTDcFYsGtY01ibqz04ha6Ul0hsa+vTx/60Idk5a+YX3zxxTpw4IAk6f7779dNN90kSdq6davOOussPfLII605WgDoKmWDa8JMN01QSWwbN2tCfdQriV67qeM72fLWJJa3m+bye5dJUu+yOiuJaZmf8RYq/CxRSQRiwfZXEqtc/MmOEhIjINCaxL//+7/XZZddpsHBQWWzWa1atarwubVr1+rQoUNNO0AA6FpN2ifRdiLWbupEPCT618FF7fj9axKrVRIL7abjxTWFXiVRktJL6wiJvn0SXbe5/4aS7+NrN41aVRfATOWVxEoXf7KjpQO30JUanm565513av/+/frRj36kycnJur9ux44d2rFjR+HvY2NjNW4NAFFQtk9imHbTREJJK4qDayJwvOWcbLHdNGrVKyczc6pppS0w0gsluaaymM5XFVP5SmLPUikzW7tpfgsM8xcVLoY0m+sP7BF7LADMVM+axNxoNF875piGKomf/exn9fWvf13f+973NH/+fC1fvlypVErHjx8v3ObAgQNas2bNjK/dvn27jhw5UvjT398f/ugBoJOatE+iI6dQSbSdCFQS/SExitUf/958UTt+u0Il0Ws3dd3S6aZScV2iv5I4W7up60pyiyd6rTyZc6gkArHiZIsXmKq9LmZHSzsg0JXqDok7duzQV7/6Vf3whz/UkiVLCh+/4oordPfdd0uSdu/erVdeeUWXXnpp848UALqOb59EK23CR4DWPMd1lLSS+XbTCFxdjU0lMeJrEu0p82/wTracrHk8vH0SE73FdYm50WJI7Jml3dRrUfVaxlr5GBcCe/A1vQC6iJORkvnnjmoXf3KjpWup0ZXqajc9cuSIPvnJT2rdunV697vfLUnq7e3VT3/6U33mM5/RNddcow0bNqinp0e7du1SOp2e5R4BIAZc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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "con = spark.sql(\"Select CONDUCTIVITY from df_sql\")\n",
        "con = con.rdd.map(lambda row : row.CONDUCTIVITY).collect()\n",
        "fec = spark.sql(\"Select FECAL_COLIFORM from df_sql\")\n",
        "fec = fec.rdd.map(lambda row : row.FECAL_COLIFORM).collect()"
      ],
      "metadata": {
        "id": "varQbj4gs0JE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fig,ax = plt.subplots(num=None,figsize=(14,6), dpi=80, facecolor='w', edgecolor='k')\n",
        "ax.plot(range(0,size), con, color='blue', animated=True, linewidth=1)\n",
        "fig,ax2 = plt.subplots(num=None,figsize=(14,6), dpi=80, facecolor='w', edgecolor='k')\n",
        "ax2.plot(range(0,size), fec, color='red', animated=True, linewidth=1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 826
        },
        "id": "6LCUouUWs6aq",
        "outputId": "9e48a7ca-f3f9-4bea-f7c1-4372b4f2b996"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7fe79c570910>]"
            ]
          },
          "metadata": {},
          "execution_count": 32
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1120x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1120x480 with 1 Axes>"
            ],
            "image/png": "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TtSUKVP01FNPdesyoKQwTykAAAA8kHOldOHChdqwYYNeffVVzZ07V5/73Ofalt18881as2aN1qxZoy9/+ctt919//fWaOXOmNm3apOrqal166aVqbm7utmVASWGeUgAAAHggp1Dat29fXXDBBYrFYpKkmTNnqra2tsPnrVixQldddZUkacaMGTrhhBP05JNPdtsyoKQwTykAAAA80Kk+pbfeeqvmzp3b9vP111+vqVOn6pJLLtGbb74pSdq1a5eam5s1atSotseNGzdOdXV13bIs1dKlS1VZWdl2a2xs7MymAuGVGkZTfwYAAAAiIO9QesMNN6impkY/+MEPJEn/8R//ob/85S9au3atzjrrLF100UUFX8nOWLx4serr69tuAwYMKPYqAYXFQEcAAADwQF6h9KabbtK9996rhx56SP3795ckjRkzRpIUi8V09dVX680339SuXbs0dOhQVVRUaNu2bW3Pr62tVVVVVbcsA0pO6kBHNN8FAABABOUcSpcuXaq7775bjz76qIYMGSJJamlp0fbt29ses3LlSo0cOVJDhw6VJM2fP1+33367JGn16tXasmWLZs+e3W3LgJLCQEcAAADwQEUuD6qvr9d1112n8ePHa86cOZKkPn366H/+53904YUX6siRIyorK9OwYcP0+9//vu15N954oy6//HJNnDhRvXv31rJly9SrV69uWwaUlNTmu0wJAwAAgAiKOVcaZ7CVlZWqr68v9moAhXPrrdK110qf+pS0fLnUr590+LC0dq00dWqx1w4AAABoky2PdWr0XQAhQJ9SAAAAeIBQCkQVo+8CAADAA4RSIKoyzVNKpRQAAAARQigFoiq5UupcIoxSKQUAAECEEEqBqEruU5pcHaVSCgAAgAghlAJRFY9LsZhVRoOqqUSlFAAAAJFCKAWiKh6X+vSxr0EQraigUgoAAIBIIZQCURWPS716WSBNDqVUSgEAABAhhFIgqlpapN6921dKy8uplAIAACBSCKVAVMXjiVAa9CmlUgoAAICIIZQCURWE0tTmu1RKAQAAECGEUiCqkiul9CkFAABARBFKgahKN9BReTmhFAAAAJFCKAWiKnmgo+Q+pTTfBQAAQIQQSoGoSjdPaVA5BQAAACKCUApEVabmu1RKAQAAECGEUiCq0k0JQ59SAAAARAyhFIiqlharlAbNd8vKpFiMSikA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AAAAAIqG5rsAAAAAgKIhlAIAAAAAioZQWmSbNm3SrFmzNGnSJM2YMUPr1q0r9ioB7VxzzTUaN26cYrGY1qxZ03Z/tn2X/RphcvjwYV188cWaNGmSTj31VJ1zzjmqqamRJO3YsUPnn3++Jk6cqClTpuipp55qe162ZUBPOvfcc3XKKado2rRpOuuss/TKK69I4jiM6KmurlYsFtP9998viWMwkjgU1Zw5c1x1dbVzzrl77rnHnX766cVdISDFk08+6TZv3uzGjh3rXnnllbb7s+277NcIk6amJvfAAw+41tZW55xzt912m5s9e7Zzzrm///u/d9/61recc8698MIL7sQTT3RHjx7tcBnQk/bs2dP2/b333utOOeUU5xzHYUTLW2+95T74wQ+6mTNnuvvuu885xzEYCYTSItq+fbsbOHCga25uds4519ra6kaOHOk2bdpU5DUDjpUcSrPtu+zXCLvVq1e7sWPHOuecO+6441xDQ0PbshkzZrhHH320w2VAsVRXV7tTTz2V4zAiJR6Pu4985CPuxRdfdLNnz24LpRyDEagodqW2lG3evFmjR49WRYW9DLFYTFVVVaqrq9OECROKvHZAZtn23cGDB7NfI9RuvfVWzZ07V7t27VJzc7NGjRrVtmzcuHGqq6vLugwohiuuuEJPPPGEJOnBBx/kOIxIWbp0qc4880yddtppbfdxDEYyQikAoGTccMMNqqmp0eOPP66mpqZirw6Qs7vuukuS9Otf/1pLlizRd7/73SKvEZCb1157TStXrqRPKLJioKMiGjNmjBoaGtTS0iJJcs6prq5OVVVVRV4zILts+y77NcLqpptu0r333quHHnpI/fv319ChQ1VRUaFt27a1Paa2tlZVVVVZlwHFdOWVV+qJJ55QZWUlx2FEwtNPP63a2lpNnDhR48aN03PPPaeFCxdqxYoVHIPRhlBaRCNGjND06dO1bNkySdLKlStVWVlJ0xqEXrZ9l/0aYbR06VLdfffdevTRRzVkyJC2++fPn6/bb79dkrR69Wpt2bJFs2fP7nAZ0FP27t2rrVu3tv18//33a+jQoRyHERlf+MIX1NDQoNraWtXW1mrmzJn6+c9/ri984Qscg9Em5pxzxV6JUrZhwwYtWLBAu3bt0qBBg1RdXa2pU6cWe7WANosWLdIDDzygbdu2aejQoRo4cKBqamqy7rvs1wiT+vp6jRkzRuPHj9fAgQMlSX369NHzzz+v7du36/LLL9dbb72l3r1769/+7d80Z84cScq6DOgpb7/9tubPn6+mpiaVlZVp+PDhuummmzRt2jSOw4iks88+W9dee60uvvhijsFoQygFAAAAABQNzXcBAAAAAEVDKAUAAAAAFA2hFAAAAABQNIRSAAAAAEDREEoBAAAAAEVDKAUAAAAAFA2hFAAAAABQNIRSAAAAAEDREEoBAAAAAEXz/wFIZByetPYLaQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=df_clean.toPandas()\n",
        "df.dtypes"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FFp8x8JPs9ft",
        "outputId": "b7052da5-9e1e-42b6-bd64-75033c77a903"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "STATION CODE            object\n",
              "LOCATIONS               object\n",
              "STATE                   object\n",
              "TEMP                   float32\n",
              "DO                     float32\n",
              "pH                     float32\n",
              "CONDUCTIVITY           float32\n",
              "BOD                    float32\n",
              "NITRATE_N_NITRITE_N    float32\n",
              "FECAL_COLIFORM         float32\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "start=0\n",
        "end=448\n",
        "station=df.iloc [start:end ,0]\n",
        "location=df.iloc [start:end ,1]\n",
        "state=df.iloc [start:end ,2]\n",
        "do= df.iloc [start:end ,4].astype(np.float64)\n",
        "value=0\n",
        "ph = df.iloc[ start:end,5]  \n",
        "co = df.iloc [start:end ,6].astype(np.float64)\n",
        "bod = df.iloc [start:end ,7].astype(np.float64)\n",
        "na= df.iloc [start:end ,8].astype(np.float64)\n",
        "fc=df.iloc [2:end ,9].astype(np.float64)"
      ],
      "metadata": {
        "id": "zrV_BBEqtCYt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.concat([station,location,state,do,ph,co,bod,na,fc],axis=1)\n",
        "df. columns = ['station','location','state','do','ph','co','bod','na','fc']"
      ],
      "metadata": {
        "id": "lLrBVdn_tJYp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['npH']=df.ph.apply(lambda x: (100 if (8.5>=x>=7)  \n",
        "                                 else(80 if  (8.6>=x>=8.5) or (6.9>=x>=6.8) \n",
        "                                      else(60 if (8.8>=x>=8.6) or (6.8>=x>=6.7) \n",
        "                                          else(40 if (9>=x>=8.8) or (6.7>=x>=6.5)\n",
        "                                              else 0)))))"
      ],
      "metadata": {
        "id": "Re8rGrMrtOUA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['ndo']=df.do.apply(lambda x:(100 if (x>=6)  \n",
        "                                 else(80 if  (6>=x>=5.1) \n",
        "                                      else(60 if (5>=x>=4.1)\n",
        "                                          else(40 if (4>=x>=3) \n",
        "                                              else 0)))))"
      ],
      "metadata": {
        "id": "bClQ_ZlIth9q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['nco']=df.fc.apply(lambda x:(100 if (5>=x>=0)  \n",
        "                                 else(80 if  (50>=x>=5) \n",
        "                                      else(60 if (500>=x>=50)\n",
        "                                          else(40 if (10000>=x>=500) \n",
        "                                              else 0)))))"
      ],
      "metadata": {
        "id": "-7fRbPdMtlgb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['nbdo']=df.bod.apply(lambda x:(100 if (3>=x>=0)  \n",
        "                                 else(80 if  (6>=x>=3) \n",
        "                                      else(60 if (80>=x>=6)\n",
        "                                          else(40 if (125>=x>=80) \n",
        "                                              else 0)))))"
      ],
      "metadata": {
        "id": "EsbSZdWJtq23"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['nec']=df.co.apply(lambda x:(100 if (75>=x>=0)  \n",
        "                                 else(80 if  (150>=x>=75) \n",
        "                                      else(60 if (225>=x>=150)\n",
        "                                          else(40 if (300>=x>=225) \n",
        "                                              else 0)))))"
      ],
      "metadata": {
        "id": "i5bLlZFpttOp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['nna']=df.na.apply(lambda x:(100 if (20>=x>=0)  \n",
        "                                 else(80 if  (50>=x>=20) \n",
        "                                      else(60 if (100>=x>=50)\n",
        "                                          else(40 if (200>=x>=100) \n",
        "                                              else 0)))))\n",
        "\n",
        "df.head()\n",
        "df.dtypes"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lA6AMzeWtw8b",
        "outputId": "c5ff9e65-4d1e-4d52-eb0e-6eb00e79c144"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "station      object\n",
              "location     object\n",
              "state        object\n",
              "do          float64\n",
              "ph          float32\n",
              "co          float64\n",
              "bod         float64\n",
              "na          float64\n",
              "fc          float64\n",
              "npH           int64\n",
              "ndo           int64\n",
              "nco           int64\n",
              "nbdo          int64\n",
              "nec           int64\n",
              "nna           int64\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['wph']=df.npH * 0.165\n",
        "df['wdo']=df.ndo * 0.281\n",
        "df['wbdo']=df.nbdo * 0.234\n",
        "df['wec']=df.nec* 0.009\n",
        "df['wna']=df.nna * 0.028\n",
        "df['wco']=df.nco * 0.281\n",
        "df['wqi']=df.wph+df.wdo+df.wbdo+df.wec+df.wna+df.wco \n",
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 607
        },
        "id": "XVTmGSl5t2wR",
        "outputId": "3604504d-b10d-43fa-b02b-66a99c85afb9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    station                                           location        state  \\\n",
              "0      1312  GODAVARI AT JAYAKWADI DAM, AURNAGABAD,MAHARASHTRA  MAHARASHTRA   \n",
              "1      2177              GODAVARI RIVER NEAR SOMESHWAR TEMPLE.  MAHARASHTRA   \n",
              "2      2182                        GODAVARI RIVER AT SAIKHEDA.  MAHARASHTRA   \n",
              "3      2179       GODAVARI RIVER AT HANUMAN GHAT, NASHIK CITY.  MAHARASHTRA   \n",
              "4      2183          GODAVARI RIVER AT NANDUR- MADMESHWAR DAM.  MAHARASHTRA   \n",
              "..      ...                                                ...          ...   \n",
              "442    2940             GAPE- SAGAR LAKE, DUNGARPUR, RAJASTHAN    RAJASTHAN   \n",
              "443    2941  LAKE JAISAMAND, SALUMBER, UDAIPUR, POINT NO. 1...    RAJASTHAN   \n",
              "444    2942  LAKE JAISAMAND, SALUMBER, UDAIPUR, POINT NO. 2...    RAJASTHAN   \n",
              "445    2943  LODHA TALAB, BANSWARA- DUNGARPUR ROAD, BANSWAR...    RAJASTHAN   \n",
              "446    2944                        JALMAHAL, JAIPUR, RAJASTHAN    RAJASTHAN   \n",
              "\n",
              "      do   ph      co  bod    na    fc  npH  ...  nbdo  nec  nna   wph    wdo  \\\n",
              "0    6.4  8.1   735.0  3.4  2.00   NaN  100  ...    80    0  100  16.5  28.10   \n",
              "1    6.0  8.0   270.0  3.1  2.00   NaN  100  ...    80   40  100  16.5  28.10   \n",
              "2    5.5  7.8   355.0  4.2  9.00  59.0  100  ...    80    0  100  16.5  22.48   \n",
              "3    5.5  7.8   371.0  5.6  3.55  90.0  100  ...    80    0  100  16.5  22.48   \n",
              "4    5.7  7.9   294.0  3.2  2.69  45.0  100  ...    80   40  100  16.5  22.48   \n",
              "..   ...  ...     ...  ...   ...   ...  ...  ...   ...  ...  ...   ...    ...   \n",
              "442  4.4  8.1   538.0  1.2  1.00   5.0  100  ...   100    0  100  16.5  16.86   \n",
              "443  5.6  8.4   591.0  1.1  3.00   4.0  100  ...   100    0  100  16.5  22.48   \n",
              "444  5.8  8.5   588.0  1.2  3.00   4.0  100  ...   100    0  100  16.5  22.48   \n",
              "445  4.1  7.9  1133.0  2.3  2.00   7.0  100  ...   100    0  100  16.5   0.00   \n",
              "446  3.5  8.9  2004.0  6.5  1.00  13.0   40  ...    60    0  100   6.6  11.24   \n",
              "\n",
              "      wbdo   wec  wna    wco    wqi  \n",
              "0    18.72  0.00  2.8   0.00  66.12  \n",
              "1    18.72  0.36  2.8   0.00  66.48  \n",
              "2    18.72  0.00  2.8  16.86  77.36  \n",
              "3    18.72  0.00  2.8  16.86  77.36  \n",
              "4    18.72  0.36  2.8  22.48  83.34  \n",
              "..     ...   ...  ...    ...    ...  \n",
              "442  23.40  0.00  2.8  28.10  87.66  \n",
              "443  23.40  0.00  2.8  28.10  93.28  \n",
              "444  23.40  0.00  2.8  28.10  93.28  \n",
              "445  23.40  0.00  2.8  22.48  65.18  \n",
              "446  14.04  0.00  2.8  22.48  57.16  \n",
              "\n",
              "[447 rows x 22 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a0fc82ec-3fcc-4a11-a98d-deba0eadd305\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>station</th>\n",
              "      <th>location</th>\n",
              "      <th>state</th>\n",
              "      <th>do</th>\n",
              "      <th>ph</th>\n",
              "      <th>co</th>\n",
              "      <th>bod</th>\n",
              "      <th>na</th>\n",
              "      <th>fc</th>\n",
              "      <th>npH</th>\n",
              "      <th>...</th>\n",
              "      <th>nbdo</th>\n",
              "      <th>nec</th>\n",
              "      <th>nna</th>\n",
              "      <th>wph</th>\n",
              "      <th>wdo</th>\n",
              "      <th>wbdo</th>\n",
              "      <th>wec</th>\n",
              "      <th>wna</th>\n",
              "      <th>wco</th>\n",
              "      <th>wqi</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1312</td>\n",
              "      <td>GODAVARI AT JAYAKWADI DAM, AURNAGABAD,MAHARASHTRA</td>\n",
              "      <td>MAHARASHTRA</td>\n",
              "      <td>6.4</td>\n",
              "      <td>8.1</td>\n",
              "      <td>735.0</td>\n",
              "      <td>3.4</td>\n",
              "      <td>2.00</td>\n",
              "      <td>NaN</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>80</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>28.10</td>\n",
              "      <td>18.72</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>0.00</td>\n",
              "      <td>66.12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2177</td>\n",
              "      <td>GODAVARI RIVER NEAR SOMESHWAR TEMPLE.</td>\n",
              "      <td>MAHARASHTRA</td>\n",
              "      <td>6.0</td>\n",
              "      <td>8.0</td>\n",
              "      <td>270.0</td>\n",
              "      <td>3.1</td>\n",
              "      <td>2.00</td>\n",
              "      <td>NaN</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>80</td>\n",
              "      <td>40</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>28.10</td>\n",
              "      <td>18.72</td>\n",
              "      <td>0.36</td>\n",
              "      <td>2.8</td>\n",
              "      <td>0.00</td>\n",
              "      <td>66.48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2182</td>\n",
              "      <td>GODAVARI RIVER AT SAIKHEDA.</td>\n",
              "      <td>MAHARASHTRA</td>\n",
              "      <td>5.5</td>\n",
              "      <td>7.8</td>\n",
              "      <td>355.0</td>\n",
              "      <td>4.2</td>\n",
              "      <td>9.00</td>\n",
              "      <td>59.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>80</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>22.48</td>\n",
              "      <td>18.72</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>16.86</td>\n",
              "      <td>77.36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2179</td>\n",
              "      <td>GODAVARI RIVER AT HANUMAN GHAT, NASHIK CITY.</td>\n",
              "      <td>MAHARASHTRA</td>\n",
              "      <td>5.5</td>\n",
              "      <td>7.8</td>\n",
              "      <td>371.0</td>\n",
              "      <td>5.6</td>\n",
              "      <td>3.55</td>\n",
              "      <td>90.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>80</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>22.48</td>\n",
              "      <td>18.72</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>16.86</td>\n",
              "      <td>77.36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2183</td>\n",
              "      <td>GODAVARI RIVER AT NANDUR- MADMESHWAR DAM.</td>\n",
              "      <td>MAHARASHTRA</td>\n",
              "      <td>5.7</td>\n",
              "      <td>7.9</td>\n",
              "      <td>294.0</td>\n",
              "      <td>3.2</td>\n",
              "      <td>2.69</td>\n",
              "      <td>45.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>80</td>\n",
              "      <td>40</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>22.48</td>\n",
              "      <td>18.72</td>\n",
              "      <td>0.36</td>\n",
              "      <td>2.8</td>\n",
              "      <td>22.48</td>\n",
              "      <td>83.34</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>442</th>\n",
              "      <td>2940</td>\n",
              "      <td>GAPE- SAGAR LAKE, DUNGARPUR, RAJASTHAN</td>\n",
              "      <td>RAJASTHAN</td>\n",
              "      <td>4.4</td>\n",
              "      <td>8.1</td>\n",
              "      <td>538.0</td>\n",
              "      <td>1.2</td>\n",
              "      <td>1.00</td>\n",
              "      <td>5.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>100</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>16.86</td>\n",
              "      <td>23.40</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>28.10</td>\n",
              "      <td>87.66</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>443</th>\n",
              "      <td>2941</td>\n",
              "      <td>LAKE JAISAMAND, SALUMBER, UDAIPUR, POINT NO. 1...</td>\n",
              "      <td>RAJASTHAN</td>\n",
              "      <td>5.6</td>\n",
              "      <td>8.4</td>\n",
              "      <td>591.0</td>\n",
              "      <td>1.1</td>\n",
              "      <td>3.00</td>\n",
              "      <td>4.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>100</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>22.48</td>\n",
              "      <td>23.40</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>28.10</td>\n",
              "      <td>93.28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>444</th>\n",
              "      <td>2942</td>\n",
              "      <td>LAKE JAISAMAND, SALUMBER, UDAIPUR, POINT NO. 2...</td>\n",
              "      <td>RAJASTHAN</td>\n",
              "      <td>5.8</td>\n",
              "      <td>8.5</td>\n",
              "      <td>588.0</td>\n",
              "      <td>1.2</td>\n",
              "      <td>3.00</td>\n",
              "      <td>4.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>100</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>22.48</td>\n",
              "      <td>23.40</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>28.10</td>\n",
              "      <td>93.28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>445</th>\n",
              "      <td>2943</td>\n",
              "      <td>LODHA TALAB, BANSWARA- DUNGARPUR ROAD, BANSWAR...</td>\n",
              "      <td>RAJASTHAN</td>\n",
              "      <td>4.1</td>\n",
              "      <td>7.9</td>\n",
              "      <td>1133.0</td>\n",
              "      <td>2.3</td>\n",
              "      <td>2.00</td>\n",
              "      <td>7.0</td>\n",
              "      <td>100</td>\n",
              "      <td>...</td>\n",
              "      <td>100</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>16.5</td>\n",
              "      <td>0.00</td>\n",
              "      <td>23.40</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>22.48</td>\n",
              "      <td>65.18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>446</th>\n",
              "      <td>2944</td>\n",
              "      <td>JALMAHAL, JAIPUR, RAJASTHAN</td>\n",
              "      <td>RAJASTHAN</td>\n",
              "      <td>3.5</td>\n",
              "      <td>8.9</td>\n",
              "      <td>2004.0</td>\n",
              "      <td>6.5</td>\n",
              "      <td>1.00</td>\n",
              "      <td>13.0</td>\n",
              "      <td>40</td>\n",
              "      <td>...</td>\n",
              "      <td>60</td>\n",
              "      <td>0</td>\n",
              "      <td>100</td>\n",
              "      <td>6.6</td>\n",
              "      <td>11.24</td>\n",
              "      <td>14.04</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2.8</td>\n",
              "      <td>22.48</td>\n",
              "      <td>57.16</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>447 rows × 22 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a0fc82ec-3fcc-4a11-a98d-deba0eadd305')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a0fc82ec-3fcc-4a11-a98d-deba0eadd305 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a0fc82ec-3fcc-4a11-a98d-deba0eadd305');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['quality']=df.wqi.apply(lambda x:('Excellent' if (25>=x>=0)  \n",
        "                                 else('Good' if  (50>=x>=26) \n",
        "                                      else('Poor' if (75>=x>=51)\n",
        "                                          else('Very Poor' if (100>=x>=76) \n",
        "                                              else 'Unsuitable')))))"
      ],
      "metadata": {
        "id": "ZvU4IZSXt-wI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.lineplot(df[\"state\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 296
        },
        "id": "ma74LesExTdt",
        "outputId": "5d61e059-a9cc-4524-ecb6-1083727ef3fb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fe79beacc90>"
            ]
          },
          "metadata": {},
          "execution_count": 48
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "spark_df = sqlContext.createDataFrame(df)"
      ],
      "metadata": {
        "id": "GIyBiPl1zOln"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "spark_df.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "edWSMaRlzRus",
        "outputId": "f7d572c3-d057-4c92-d7c4-ccebfbb80903"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+-------+--------------------+--------------+-----------------+-----------------+-----+------------------+------------------+-----+---+---+---+----+---+---+------------------+------------------+------------------+------------------+------------------+------------------+-----------------+---------+\n",
            "|station|            location|         state|               do|               ph|   co|               bod|                na|   fc|npH|ndo|nco|nbdo|nec|nna|               wph|               wdo|              wbdo|               wec|               wna|               wco|              wqi|  quality|\n",
            "+-------+--------------------+--------------+-----------------+-----------------+-----+------------------+------------------+-----+---+---+---+----+---+---+------------------+------------------+------------------+------------------+------------------+------------------+-----------------+---------+\n",
            "|   1312|GODAVARI AT JAYAK...|   MAHARASHTRA|6.400000095367432|8.100000381469727|735.0|3.4000000953674316|               2.0|  NaN|100|100|  0|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|               0.0|            66.12|     Poor|\n",
            "|   2177|GODAVARI RIVER NE...|   MAHARASHTRA|              6.0|              8.0|270.0|3.0999999046325684|               2.0|  NaN|100|100|  0|  80| 40|100|              16.5|              28.1|18.720000000000002|              0.36|2.8000000000000003|               0.0|            66.48|     Poor|\n",
            "|   2182|GODAVARI RIVER AT...|   MAHARASHTRA|              5.5|7.800000190734863|355.0| 4.199999809265137|               9.0| 59.0|100| 80| 60|  80|  0|100|              16.5|22.480000000000004|18.720000000000002|               0.0|2.8000000000000003|16.860000000000003|            77.36|Very Poor|\n",
            "|   2179|GODAVARI RIVER AT...|   MAHARASHTRA|              5.5|7.800000190734863|371.0| 5.599999904632568| 3.549999952316284| 90.0|100| 80| 60|  80|  0|100|              16.5|22.480000000000004|18.720000000000002|               0.0|2.8000000000000003|16.860000000000003|            77.36|Very Poor|\n",
            "|   2183|GODAVARI RIVER AT...|   MAHARASHTRA|5.699999809265137|7.900000095367432|294.0| 3.200000047683716| 2.690000057220459| 45.0|100| 80| 80|  80| 40|100|              16.5|22.480000000000004|18.720000000000002|              0.36|2.8000000000000003|22.480000000000004|            83.34|Very Poor|\n",
            "|   2181|GODAVARI RIVER AT...|   MAHARASHTRA|              4.5|              7.5|513.0|12.600000381469727| 2.299999952316284|131.0|100| 60| 60|  60|  0|100|              16.5|16.860000000000003|14.040000000000001|               0.0|2.8000000000000003|16.860000000000003|            67.06|     Poor|\n",
            "|   2180|GODAVARI RIVER NE...|   MAHARASHTRA|5.199999809265137|7.699999809265137|475.0|10.300000190734863| 1.899999976158142|122.0|100| 80| 60|  60|  0|100|              16.5|22.480000000000004|14.040000000000001|               0.0|2.8000000000000003|16.860000000000003|            72.68|     Poor|\n",
            "|   1096|GODAVARI AT PANCH...|   MAHARASHTRA|5.599999904632568|7.699999809265137|385.0| 3.799999952316284|               1.0|110.0|100| 80| 60|  80|  0|100|              16.5|22.480000000000004|18.720000000000002|               0.0|2.8000000000000003|16.860000000000003|            77.36|Very Poor|\n",
            "|   1211|GODAVARI AT NASIK...|   MAHARASHTRA|5.199999809265137|7.800000190734863|410.0| 5.199999809265137|               1.5| 77.0|100| 80| 60|  80|  0|100|              16.5|22.480000000000004|18.720000000000002|               0.0|2.8000000000000003|16.860000000000003|            77.36|Very Poor|\n",
            "|   1095|GODAVARI AT U/S O...|   MAHARASHTRA|              6.5|7.800000190734863|178.0|               2.5|1.9900000095367432| 22.0|100|100| 80| 100| 60|100|              16.5|              28.1|23.400000000000002|0.5399999999999999|2.8000000000000003|22.480000000000004|93.82000000000001|Very Poor|\n",
            "|   2160|GODAVARI RIVER AT...|   MAHARASHTRA|6.199999809265137|7.900000095367432|749.0|               3.5|              1.75|  2.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|   2158|GODAVARI RIVER AT...|   MAHARASHTRA|6.400000095367432|              8.0|834.0| 4.699999809265137|1.7999999523162842|  2.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|   2159|GODAVARI RIVER AT...|   MAHARASHTRA|6.199999809265137|              8.0|925.0| 4.199999809265137| 6.900000095367432|  2.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|   2161|GODAVARI RIVER AT...|   MAHARASHTRA|              6.5|              8.0|730.0|               4.0|2.9000000953674316|  2.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|     12|GODAVARI AT DHALE...|   MAHARASHTRA|              7.0|7.900000095367432|637.0| 4.699999809265137|               6.5|  2.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|   1209|GODAVARI AT RAHER...|   MAHARASHTRA|6.400000095367432|              8.0|656.0|3.5999999046325684|1.7999999523162842|  3.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|   2157|GODAVARI RIVER AT...|   MAHARASHTRA|6.599999904632568|8.100000381469727|601.0| 3.200000047683716|              6.75|  2.0|100|100|100|  80|  0|100|              16.5|              28.1|18.720000000000002|               0.0|2.8000000000000003|              28.1|            94.22|Very Poor|\n",
            "|   2360|GODAVARI AT BASAR...|ANDHRA PRADESH|              5.5|8.100000381469727|826.0|1.7000000476837158|               1.0| 27.0|100| 80| 80| 100|  0|100|              16.5|22.480000000000004|23.400000000000002|               0.0|2.8000000000000003|22.480000000000004|87.66000000000001|Very Poor|\n",
            "|   2361|GODAVARI  AT MANC...|ANDHRA PRADESH|6.900000095367432|              9.0|526.0|              12.0|               0.0|130.0| 40|100| 60|  60|  0|100|6.6000000000000005|              28.1|14.040000000000001|               0.0|2.8000000000000003|16.860000000000003|             68.4|     Poor|\n",
            "|   2362|GODAVARI AT RAMAG...|ANDHRA PRADESH|5.699999809265137|              8.5|575.0|              13.0|               0.0|240.0|100| 80| 60|  60|  0|100|              16.5|22.480000000000004|14.040000000000001|               0.0|2.8000000000000003|16.860000000000003|            72.68|     Poor|\n",
            "+-------+--------------------+--------------+-----------------+-----------------+-----+------------------+------------------+-----+---+---+---+----+---+---+------------------+------------------+------------------+------------------+------------------+------------------+-----------------+---------+\n",
            "only showing top 20 rows\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "spark_df.createOrReplaceTempView(\"df_sql\")"
      ],
      "metadata": {
        "id": "kNI2_qiPzYkB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "State = spark.sql(\"Select state from df_sql\")\n",
        "State = State.rdd.map(lambda row : row.state).collect()"
      ],
      "metadata": {
        "id": "ynf2e9cszmdZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Wqi = spark.sql(\"Select wqi from df_sql\")\n",
        "Wqi = Wqi.rdd.map(lambda row : row.wqi).collect()"
      ],
      "metadata": {
        "id": "WpJleMvRzp_i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.barh(State,Wqi)\n",
        "\n",
        "plt.xlabel(\"WQI\")\n",
        "plt.ylabel(\"STATES\")\n",
        "\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 279
        },
        "id": "aiCP6CHRzwds",
        "outputId": "3f808525-ae88-456e-a0b6-01ab6fc6478d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "spark_df = sqlContext.createDataFrame(df)"
      ],
      "metadata": {
        "id": "SnYgI6N0zztg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.ml.feature import StringIndexer"
      ],
      "metadata": {
        "id": "4ckNPJ7s0L4N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.ml.feature import VectorAssembler\n",
        "from pyspark.ml.feature import Normalizer\n",
        "\n",
        "vectorAssembler = VectorAssembler(inputCols=[\"npH\",\"ndo\",\"nbdo\",\"nec\",\"nna\",\"nco\"], outputCol=\"features\")\n",
        "normalizer = Normalizer(inputCol=\"features\",outputCol=\"features_norm\")"
      ],
      "metadata": {
        "id": "wEZiNzVa0p2n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "indexer = StringIndexer(inputCol=\"quality\",outputCol=\"label\")\n",
        "vectorAssembler2 = VectorAssembler(inputCols=[\"npH\",\"ndo\",\"nbdo\",\"nec\",\"nna\",\"nco\",\"wqi\"], outputCol=\"features2\")\n",
        "normalizer2 = Normalizer(inputCol=\"features2\",outputCol=\"features_norm2\")"
      ],
      "metadata": {
        "id": "M8mCxPa100mT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.ml.classification import LogisticRegression"
      ],
      "metadata": {
        "id": "f_Ou9kCl03Bw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lor = LogisticRegression(featuresCol=\"features_norm2\",labelCol=\"label\",maxIter=10)"
      ],
      "metadata": {
        "id": "278swfvl07ZG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.ml import Pipeline"
      ],
      "metadata": {
        "id": "AJlHHMsK1SMC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pipeline2 = Pipeline(stages=[indexer,vectorAssembler2,normalizer2,lor])"
      ],
      "metadata": {
        "id": "yLm9goYC1YVd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_data,test_data=spark_df.randomSplit([0.8,0.2])"
      ],
      "metadata": {
        "id": "zVWLOg_S1cBY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model3 = pipeline2.fit(train_data)"
      ],
      "metadata": {
        "id": "talTKT_f1gFk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "predictions2 = model3.transform(train_data)"
      ],
      "metadata": {
        "id": "J4lY3Q6f1kVp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "predictions2 = model3.transform(train_data)"
      ],
      "metadata": {
        "id": "bJIUk9Zx1n6Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyspark.ml.evaluation import MulticlassClassificationEvaluator\n",
        "eval = MulticlassClassificationEvaluator().setMetricName('accuracy').setLabelCol('label').setPredictionCol('prediction')\n",
        "eval.evaluate(predictions2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KPX-oAOz1sZZ",
        "outputId": "17e04639-60c2-4105-e4e5-b5b23738518e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9970760233918129"
            ]
          },
          "metadata": {},
          "execution_count": 69
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "names = [\"Very Poor\",\"Poor\",\"Good\",\"Unsuitable\",\"Excellent\"]"
      ],
      "metadata": {
        "id": "BE7LMNEo12-y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "predictions2.createOrReplaceTempView(\"predictions2_sql\")"
      ],
      "metadata": {
        "id": "-G4VP6S414tC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pred = spark.sql(\"Select prediction from predictions2_sql\")\n",
        "pred = pred.rdd.map(lambda row : int(row.prediction)).collect()\n",
        "qua = spark.sql(\"Select quality from predictions2_sql\")\n",
        "qua = qua.rdd.map(lambda row : row.quality).collect()"
      ],
      "metadata": {
        "id": "6iDBL9q51_pI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for x in range(100):\n",
        "    print(\"Predicted:\", names[pred[x]], \"Actual:\", qua[x])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kosuuIU02C_4",
        "outputId": "d84fb2fb-9d25-4e3e-997e-686c8dbee28d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Good Actual: Good\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Good Actual: Good\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Good Actual: Good\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Very Poor Actual: Very Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n",
            "Predicted: Poor Actual: Poor\n"
          ]
        }
      ]
    }
  ]
}