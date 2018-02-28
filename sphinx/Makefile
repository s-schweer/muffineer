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
	../.venv/bin/sphinx-apidoc -f -A "Stefan Schweer" -H "Muffineer" -F -d 4 -e -P -o "$(BUILDDIR)" "../muffineer"
	cp -f source/conf.py ../docs/conf.py



.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "../docs" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
