
ARCHIVE_DIR=FragScape
ARCHIVE_NAME=FragScape.zip
TO_COPY_DIRS=algs help i18n icons sample_data steps
MC_LIB_DIR=qgis_lib_mc

.PHONY: archive

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
