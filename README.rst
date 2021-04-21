terminal title change
=====================

End user Installation via Homebrew
----------------------------------

``brew install termtitle``

If it is not accessable, try 

``brew install https://raw.githubusercontent.com/grimmer0125/homebrew-core/termtitle/Formula/termtitle.rb``

End user Installation via pip
-----------------------------

.. image:: https://img.shields.io/pypi/dw/termtitle.svg

Thare are several ways to install, and it depends on your Python environment and preference.

1. default system python + install globally (accessable for each user)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``sudo pip install termtitle``

2. default system python + install in current user folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pin install --user termtitle``.

But you need to add Python bin directories to PATH,

- test it first, ``python2.7 -m site &> /dev/null && PATH="$PATH:`python2.7 -m site --user-base`/bin"`` (ref: https://stackoverflow.com/a/48380776/7354486)
- ``termtitle random_title``
- if you see your titles change, then you can permanently change your PATH, ``echo 'export PATH="$PATH:`python2.7 -m site --user-base`/bin"' >>~/.bash_profile``

3. Python3+pip3 (which might be from "brew install python3")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip3 install termtitle``.

4. non system Python of pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip install termtitle``.

Usage
---------------------

If you are using zsh and this package does not take effect, you might need to set `DISABLE_AUTO_TITLE="true"` in `~/.zshrc` and restart shell to try again.


- ``termtitle demo_project_root``
- ``termtitle 這是秘密的鋼彈計劃``
- ``termtitle サイボーグ009のメンバー``
- ``termtitle ""`` # reset the title to empty


Dev
---------------------

local test:

- Install: `python setup.py install`
- Uninstall: `pip uninstall termtitle`

publish:

1. change ``version="x.y.z`` in ``setup.py``
2. ``python setup.py check --restructuredtext -s`` do some check before publishing
3. ``python setup.py sdist``
4. Use twine to publish: ``twine upload dist/*``
