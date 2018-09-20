terminal title change
=====================

^^^^^^^^^^^^^^^^^^^^^
End user Installation
^^^^^^^^^^^^^^^^^^^^^

1.
install globally: ``sudo pip install termtitle``

2.
install in user folder: ``pin install --user termtitle``
But you need to modify your path, e.g.
``python2.7 -m site &> /dev/null && PATH="$PATH:`python2.7 -m site --user-base`/bin"``

^^^^^^^^^^^^^^^^^^^
Usage
^^^^^^^^^^^^^^^^^^^

- ``termtitle demo_project_root``

^^^^^^^^^^^^^^^^^^^
Dev
^^^^^^^^^^^^^^^^^^^

publish:
1. ``python setup.py check --restructuredtext -s`` do some check before publishing
2. ``python setup.py sdist``
3. Use twine to publish: ``twine upload dist/*``
