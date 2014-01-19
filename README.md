talismane_python
================

Simple python wrapper for Talismane (cf http://redac.univ-tlse2.fr/applications/talismane.html)


Install
-------

    $ wget https://raw.github.com/enavarro222/talismane_python/master/talismane.py

Usage
-----

Command line test:

    $ ./talismane.py -t "/PATH_TO_TALISMANE_JAR/talismane-fr-1.7.4b-allDeps.jar" 
    2014-01-13 11:27:15,314:INFO:Talismane:Started Talismane from command: 'java -Xmx1G -jar /home/navarro/install/talismane/talismane-fr-1.7.4b-allDeps.jar command=analyse'
    --1--
    ['1', 'Je', 'je', 'CLS', 'CLS', 'n=s|p=1', '2', 'suj', '_', '_']
    ['2', 'd\xc3\xa9guste', 'd\xc3\xa9guster', 'V', 'v', 'n=s|p=13|t=pst', '0', 'root', '_', '_']
    ['3', 'du', 'de', 'P+D', 'P+D', 'g=m|n=s', '2', 'de_obj', '_', '_']
    ['4', 'python', 'python', 'NC', 'nc', 'g=m|n=s', '3', 'prep', '_', '_']
    ['5', '.', '.', 'PONCT', 'PONCT', '_', '2', 'ponct', '_', '_']
    --2--
    ['1', 'Il', 'il', 'CLS', 'CLS', 'g=m|n=s|p=3', '2', 'suj', '_', '_']
    ['2', 'danse', 'danser', 'V', 'v', 'n=s|p=13|t=pst', '0', 'root', '_', '_']
    ['3', 'la', 'la', 'DET', 'DET', 'g=f|n=s', '4', 'det', '_', '_']
    ['4', 'Java', '_', 'NPP', '_', '_', '2', 'obj', '_', '_']
    ['5', ',', ',', 'PONCT', 'PONCT', '_', '2', 'ponct', '_', '_']
    ['6', 'mais', 'mais', 'CC', 'CC', '_', '2', 'coord', '_', '_']
    ['7', 'le', 'le', 'DET', 'DET', 'g=m|n=s', '8', 'det', '_', '_']
    ['8', 'python', 'python', 'NC', 'nc', 'g=m|n=s', '10', 'suj', '_', '_']
    ['9', 'ne', 'ne', 'ADV', 'ADV', '_', '10', 'mod', '_', '_']
    ['10', 'vas', 'aller', 'V', 'v', 'n=s|p=2|t=pst', '6', 'dep_coord', '_', '_']
    ['11', 'pas', 'pas', 'ADV', 'ADV', '_', '10', 'mod', '_', '_']
    ['12', 'lui', 'lui', 'CLO', 'CLO', 'n=s|p=3', '13', 'a_obj', '_', '_']
    ['13', 'offrir', 'offrir', 'VINF', 'v', '_', '10', 'obj', '_', '_']
    ['14', 'des', 'des', 'DET', 'DET', 'n=p', '15', 'det', '_', '_']
    ['15', 'perles', 'perle', 'NC', 'nc', 'g=f|n=p', '13', 'obj', '_', '_']
    ['16', 'ou', 'ou', 'CC', 'CC', '_', '15', 'coord', '_', '_']
    ['17', 'des', 'des', 'DET', 'DET', 'n=p', '18', 'det', '_', '_']
    ['18', 'rubis', 'rubis', 'NC', 'nc', 'g=m', '16', 'dep_coord', '_', '_']
    ['19', 'pour', 'pour', 'P', 'P', '_', '18', 'dep', '_', '_']
    ['20', 'noel', '_', 'NPP', '_', '_', '19', 'prep', '_', '_']
    ['21', '.', '.', 'PONCT', 'PONCT', '_', '2', 'ponct', '_', '_']
    ['1', 'En', 'en', 'CLO', 'CLO', '_', '2', 'aff', '_', '_']
    ['2', 'voila', 'voiler', 'V', 'v', 'n=s|p=3|t=past', '0', 'root', '_', '_']
    ['3', 'une', 'une', 'DET', 'DET', 'g=f|n=s', '5', 'det', '_', '_']
    ['4', 'autre', 'autre', 'ADJ', 'ADJ', 'n=s', '5', 'mod', '_', '_']
    ['5', 'phrase', 'phrase', 'NC', 'nc', 'g=f|n=s', '2', 'obj', '_', '_']
    ['6', '!', '!', 'PONCT', 'PONCT', '_', '2', 'ponct', '_', '_']


In python:
```python
In [2]: import talismane

In [2]: tlsmn = talismane.Talismane("/home/navarro/install/talismane/talismane-fr-1.7.4b-allDeps.jar")

In [3]: tlsmn.analyse("Ceci est une phrase de test")
Out[3]: 
[['1', 'Ceci', 'ceci', 'PRO', 'PRO', 'g=m|n=s', '2', 'suj', '_', '_'],
 ['2', 'est', '\xc3\xaatre', 'V', 'v', 'n=s|p=3|t=pst', '0', 'root', '_', '_'],
 ['3', 'une', 'une', 'DET', 'DET', 'g=f|n=s', '4', 'det', '_', '_'],
 ['4', 'phrase', 'phrase', 'NC', 'nc', 'g=f|n=s', '2', 'ats', '_', '_'],
 ['5', 'de', 'de', 'P', 'P', '_', '4', 'dep', '_', '_'],
 ['6', 'test', 'test', 'NC', 'nc', 'g=m|n=s', '5', 'prep', '_', '_']]

```


TODO
----

* create a "setup.py"

