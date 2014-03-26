d3b
===

D&amp;D 3.5 Database Query Tool


\\\\\\\\\\DEPENDENCIES\\\\\\\\\\\

REQUIRES PYTHON 2.7

---Python Module Dependencies---

numpy

pandas

lxml

Beautiful Soup 4

numexpr

cython


---Just to be safe, get these---

GDAL

matplotlib

pyparsing

python-dateutil

pytz

scipy

six

pytables

---Recommended modules for development---

ipython --(replace python shell)

pip --(install modules from command line)

setuptools --(alternative to pip)



\\\\\\\\\\RUNNING THE SCRIPT\\\\\\\\\\\

first, download the data files from the following URL:

https://spideroak.com/browse/share/body-mode/d3b_dev

password is the name of our team in d&d (one word, lowercase)

unzip dnd

place dnd.sqlite and any csv files in the working directory (github\d3b\)

open shell of choice (I use powershell)

cd repository (github\d3b)

type 'ipython' (after installing ipython)

open master_prototype.py in text editor

select all, copy

in shell type %paste

after running the script you can call the functions (get_spell, get_characlass, etc.) on different id numbers to retrieve summary pages

ultimately, the idea is to call these functions by clicking on buttons corresponding to each spell, class, etc.

right now, I'm working on a way to display sorted tables for browsing