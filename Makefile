
ARCHIVE_DIR=FragScape
ARCHIVE_NAME=FragScape.zip
TO_COPY_DIRS=algs help i18n icons sample_data steps
MC_LIB_DIR=qgis_lib_mc

COMPILED_RESOURCE_FILES = resources.py

RESOURCE_SRC=$(shell grep '^ *<file' resources.qrc | sed 's@</file>@@g;s/.*>//g' | tr '\n' ' ')

.PHONY: archive

default: compile

compile: $(COMPILED_RESOURCE_FILES)

%.py : %.qrc $(RESOURCES_SRC)
	pyrcc5 -o $*.py  $<

archive:
	echo "Building delivery archive $(ARCHIVE_DIR)"
	rm -rf $(ARCHIVE_DIR)
	rm -f $(ARCHIVE_NAME)
	mkdir $(ARCHIVE_DIR)
	for d in $(TO_COPY_DIRS); do \
		cp -r $$d $(ARCHIVE_DIR) ; \
	done
	rm -rf $(ARCHIVE_DIR)/sample_data/EPCI_Clermontais_2012/CBC/outputs
	rm -rf $(ARCHIVE_DIR)/sample_data/EPCI_Clermontais_2012/CBC/tmp
	rm -rf $(ARCHIVE_DIR)/sample_data/EPCI_Clermontais_2012/CUT/outputs
	rm -rf $(ARCHIVE_DIR)/sample_data/EPCI_Clermontais_2012/CUT/tmp
	mkdir $(ARCHIVE_DIR)/docs
	cp docs/FragScape_UserGuide_en.pdf $(ARCHIVE_DIR)/docs
	cp -r $(MC_LIB_DIR) $(ARCHIVE_DIR)
	cp *.py $(ARCHIVE_DIR)
	cp *.ui $(ARCHIVE_DIR)
	cp *.md $(ARCHIVE_DIR)
	cp LICENSE $(ARCHIVE_DIR)
	cp metadata.txt $(ARCHIVE_DIR)
	cp resources.qrc $(ARCHIVE_DIR)
	zip -r $(ARCHIVE_NAME) $(ARCHIVE_DIR)

ui:
	pyuic5 -o FragScape_dialog_base.py FragScape_dialog_base.ui
	pyuic5 -o FragScapeAbout_dialog_base.py FragScapeAbout_dialog_base.ui
