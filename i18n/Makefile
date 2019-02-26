
FILES=$(shell find .. -name *.py -not -path "../algs/*")

.PHONY: update release

update:
	echo "update"
	pylupdate5 $(FILES) -ts FragScape_en.ts
	pylupdate5 $(FILES) -ts FragScape_fr.ts

release:
	echo "release"
	lrelease FragScape_en.ts -qm FragScape_en.qm
	lrelease FragScape_fr.ts -qm FragScape_fr.qm
