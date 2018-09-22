terminal title change
=====================

End user Installation
---------------------

1. default system python + install globally (for each user)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``sudo pip install termtitle``

2. default system python + install in user folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pin install --user termtitle``.

But you need to add Python bin directories to PATH,

- test it first, ``python2.7 -m site &> /dev/null && PATH="$PATH:`python2.7 -m site --user-base`/bin"`` (ref: https://stackoverflow.com/a/48380776/7354486)
- ``termtitle random_title``
- if you see your titles change, then you can permanently change your PATH, ``echo 'export PATH="$PATH:`python2.7 -m site --user-base`/bin"' >>~/.bash_profile``

3. Python 3 from homebrew (via "brew install python3")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip3 install termtitle``.

4. non system Python of pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
