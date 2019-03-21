
.PHONY: pdf

pdf-en:
	xelatex -shell-escape FragScape_UserGuide_en.tex
	bibtex FragScape_UserGuide_en
	xelatex -shell-escape FragScape_UserGuide_en.tex
	cp FragScape_UserGuide_en.pdf ..

pdf-fr:
	xelatex -shell-escape FragScape_UserGuide_fr.tex
	bibtex FragScape_UserGuide_fr
	xelatex -shell-escape FragScape_UserGuide_fr.tex
	cp FragScape_UserGuide_fr.pdf ..

clean:
	rm -f *.pdf *.xml *.toc *.log *.blg *.bbl *.aux *-blx.bib *.out
