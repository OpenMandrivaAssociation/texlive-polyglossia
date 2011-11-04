# revision 24291
# category Package
# catalog-ctan /macros/xetex/latex/polyglossia
# catalog-date 2011-10-14 01:12:48 +0200
# catalog-license lppl1.3
# catalog-version v1.2.0cc
Name:		texlive-polyglossia
Version:	v1.2.0cc
Release:	1
Summary:	Modern multilingual typesetting with XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/polyglossia
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides a complete Babel replacement for users of
XeLaTeX; it relies on the fontspec package, version 2.0 at
least. The current release offers support of 68 languages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/arabicdigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/arabicdigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/bengalidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/bengalidigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/devanagaridigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/devanagaridigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/farsidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/farsidigits.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/thaidigits.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia/thaidigits.tec
%{_texmfdistdir}/tex/xelatex/polyglossia/arabicnumbers.sty
%{_texmfdistdir}/tex/xelatex/polyglossia/babel-hebrewalph.def
%{_texmfdistdir}/tex/xelatex/polyglossia/babelsh.def
%{_texmfdistdir}/tex/xelatex/polyglossia/cal-util.def
%{_texmfdistdir}/tex/xelatex/polyglossia/devanagaridigits.sty
%{_texmfdistdir}/tex/xelatex/polyglossia/farsical.sty
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-albanian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-amharic.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-arabic.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-armenian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-asturian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-bahasai.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-bahasam.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-basque.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-bengali.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-brazil.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-breton.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-bulgarian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-catalan.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-coptic.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-croatian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-czech.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-danish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-divehi.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-dutch.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-english.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-esperanto.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-estonian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-farsi.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-finnish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-french.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-galician.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-german.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-greek.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-hebrew.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-hindi.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-icelandic.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-interlingua.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-irish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-italian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-kannada.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-lao.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-latin.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-latvian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-lithuanian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-lsorbian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-magyar.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-malayalam.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-marathi.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-norsk.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-nynorsk.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-occitan.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-polish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-portuges.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-romanian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-russian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-samin.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-sanskrit.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-scottish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-serbian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-slovak.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-slovenian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-spanish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-swedish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-syriac.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-tamil.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-telugu.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-thai.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-turkish.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-turkmen.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-ukrainian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-urdu.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-usorbian.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-vietnamese.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/gloss-welsh.ldf
%{_texmfdistdir}/tex/xelatex/polyglossia/hebrewcal.sty
%{_texmfdistdir}/tex/xelatex/polyglossia/hijrical.sty
%{_texmfdistdir}/tex/xelatex/polyglossia/polyglossia.sty
%{_texmfdistdir}/tex/xelatex/polyglossia/xgreek-fixes.def
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/README
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/example-arabic.pdf
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/example-arabic.tex
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/example-thai.pdf
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/example-thai.tex
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/examples.pdf
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/examples.tex
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/polyglossia.pdf
%doc %{_texmfdistdir}/doc/xelatex/polyglossia/polyglossia.tex
#- source
%doc %{_texmfdistdir}/source/xelatex/polyglossia/polyglossia.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
