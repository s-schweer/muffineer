# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = ../.venv/bin/sphinx-build
SPHINXPROJ    = Muffineer
SOURCEDIR     = source
BUILDDIR      = ../docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
apidoc:
	rm -rf ../docs/conf.py
	../.venv/bin/sphinx-apidoc -f -A "Stefan Schweer" -H "Muffineer" -F -d 4 -e -P -o "$(BUILDDIR)" "../muffineer"
	cp -f source/conf.py ../docs/
	cp -f source/index.rst ../docs/
	cp -rf source/_templates/* ../docs/_templates/
	cp -rf source/documentation ../docs/

gh-pages: apidoc html

.PHONY: help apidoc gh-pages Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "../docs" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


