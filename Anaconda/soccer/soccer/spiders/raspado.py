{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tensorflow: 2.0.0\n",
      "keras: 2.3.1\n"
     ]
    }
   ],
   "source": [
    "# tensorflow\n",
    "import tensorflow\n",
    "print('tensorflow: %s' %tensorflow.__version__)\n",
    "# keras\n",
    "import keras\n",
    "print('keras: %s' %keras.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>OrderDate</th>\n",
       "      <th>Region</th>\n",
       "      <th>Rep</th>\n",
       "      <th>Item</th>\n",
       "      <th>Units</th>\n",
       "      <th>Unit Cost</th>\n",
       "      <th>Total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-01-06</td>\n",
       "      <td>East</td>\n",
       "      <td>Jones</td>\n",
       "      <td>Pencil</td>\n",
       "      <td>95</td>\n",
       "      <td>1.99</td>\n",
       "      <td>189.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-01-23</td>\n",
       "      <td>Central</td>\n",
       "      <td>Kivell</td>\n",
       "      <td>Binder</td>\n",
       "      <td>50</td>\n",
       "      <td>19.99</td>\n",
       "      <td>999.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-02-09</td>\n",
       "      <td>Central</td>\n",
       "      <td>Jardine</td>\n",
       "      <td>Pencil</td>\n",
       "      <td>36</td>\n",
       "      <td>4.99</td>\n",
       "      <td>179.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-02-26</td>\n",
       "      <td>Central</td>\n",
       "      <td>Gill</td>\n",
       "      <td>Pen</td>\n",
       "      <td>27</td>\n",
       "      <td>19.99</td>\n",
       "      <td>539.73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-03-15</td>\n",
       "      <td>West</td>\n",
       "      <td>Sorvino</td>\n",
       "      <td>Pencil</td>\n",
       "      <td>56</td>\n",
       "      <td>2.99</td>\n",
       "      <td>167.44</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   OrderDate   Region      Rep    Item  Units  Unit Cost   Total\n",
       "0 2018-01-06     East    Jones  Pencil     95       1.99  189.05\n",
       "1 2018-01-23  Central   Kivell  Binder     50      19.99  999.50\n",
       "2 2018-02-09  Central  Jardine  Pencil     36       4.99  179.64\n",
       "3 2018-02-26  Central     Gill     Pen     27      19.99  539.73\n",
       "4 2018-03-15     West  Sorvino  Pencil     56       2.99  167.44"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import io\n",
    "import requests\n",
    "import pandas as pd\n",
    "from zipfile import ZipFile\n",
    "r = requests.get('http://www.contextures.com/SampleData.zip')\n",
    "ZipFile(io.BytesIO(r.content)).extractall()\n",
    "df = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders')\n",
    "#pandas.DataFrsam.to_html\n",
    "#pd.read_htm,l(html_string)[0]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import lxml.html as lh\n",
    "import pandas as pd\n",
    "url='http://pokemondb.net/pokedex/all'\n",
    "\n",
    "page = requests.get(url)\n",
    "doc = lh.fromstring(page.content)\n",
    "tr_elements = doc.xpath('//tr')\n",
    "[len(T) for T in tr_elements[:12]]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1:\"#\"\n",
      "2:\"Name\"\n",
      "3:\"Type\"\n",
      "4:\"Total\"\n",
      "5:\"HP\"\n",
      "6:\"Attack\"\n",
      "7:\"Defense\"\n",
      "8:\"Sp. Atk\"\n",
      "9:\"Sp. Def\"\n",
      "10:\"Speed\"\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>#</th>\n",
       "      <th>Name</th>\n",
       "      <th>Type</th>\n",
       "      <th>Total</th>\n",
       "      <th>HP</th>\n",
       "      <th>Attack</th>\n",
       "      <th>Defense</th>\n",
       "      <th>Sp. Atk</th>\n",
       "      <th>Sp. Def</th>\n",
       "      <th>Speed</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [#, Name, Type, Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed]\n",
       "Index: []"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tr_elements = doc.xpath('//tr')\n",
    "col=[]\n",
    "i=0\n",
    "for t in tr_elements[0]:\n",
    "    i+=1\n",
    "    name=t.text_content()\n",
    "    print ('%d:\"%s\"'%(i,name))\n",
    "    col.append((name,[]))\n",
    "\n",
    "[len(C) for (title,C) in col]\n",
    "Dict={title:column for (title,column) in col}\n",
    "df=pd.DataFrame(Dict)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
