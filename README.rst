terminal title change
=====================

End user Installation
---------------------

1. default system python + install globally
^^^^^^^^^^^^^^^^^^^^^

``sudo pip install termtitle``

2. default system python + install in user folder
^^^^^^^^^^^^^^^^^^^^^

``pin install --user termtitle``.
But you need to modify your path, e.g.
``python2.7 -m site &> /dev/null && PATH="$PATH:`python2.7 -m site --user-base`/bin"``
(ref: https://stackoverflow.com/a/48380776/7354486)

[Not tested] cases of Python 3 from homebrew should be the same as 1. & 2. except pip3 instead.

3. pyenv non system Python
^^^^^^^^^^^^^^^^^^^^^

``pip install termtitle``.

Usage
---------------------

- ``termtitle demo_project_root``
- ``termtitle 這是秘密的鋼彈計劃``
- ``termtitle サイボーグ009のメンバー``
- ``termtitle`` # reset the title to empty


Dev
---------------------

publish:

1. ``python setup.py check --restructuredtext -s`` do some check before publishing
2. ``python setup.py sdist``
3. Use twine to publish: ``twine upload dist/*``
