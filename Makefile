main:
	pdflatex main
	make clean

fake_reading:
	make fake_data
	python3 scripts/lib/data_reader.py

fake_data:
	python3 scripts/lib/data_generator.py

spec:
	markdown-pdf spec.md

bib:
	bibtex main

cycle:
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

clean:
	rm -f *.aux *.lof *.log *.lot *.synctex.gz *.toc *.out

diff.tex:
	@echo "This command assumes you have checked out the previous version"
	@echo "of the thesis you sent to your advisor/reviewer in prev.tex"
	@echo "(Use git to obtain the previous version ofc.)"
	@echo "The latexdiff tools is fragile, so you may have errors compiling"
	@echo "the diff.pdf afterwards unless you go in and edit it yourself."
	latexdiff prev.tex main.tex > diff.tex

diff: diff.tex
	pdflatex diff.tex

