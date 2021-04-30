SRCS := proposal.tex midterm.tex final.tex
PDFS = ${SRCS:%.tex=%.pdf}
SECTIONS = $(wildcard sections/*/*.tex)
FIGURES = $(wildcard figures/*)
BIB = ref.bib

RM = rm -rf

all: $(PDFS)

%.pdf: %.tex $(SECTIONS) $(FIGURES) $(BIB) ACM-Reference-Format.bst acmart.cls
	pdflatex $<
	@if test -f $(@:.pdf=.aux) &&  test `grep citation $(@:.pdf=.aux) | wc -l` -ge 1; then bibtex $(@:.pdf=); fi
	pdflatex $<
	pdflatex $<

clean:
	$(RM)  *.log *.aux *.cfg *.glo *.idx *.toc *.ilg *.ind *.out *.lof \
	*.lot *.bbl *.blg *.gls *.cut *.hd *.dvi *.ps *.thm *.tgz *.zip    \
	*.rpi *.pdf auto

distclean: clean
	$(RM) *.pdf

view: $(PDFS)
	evince $(PDFS) &

.PHONY: all clean distclean view

