# revision 34205
# category Package
# catalog-ctan /macros/latex/contrib/polyglossia
# catalog-date 2014-05-22 01:04:51 +0200
# catalog-license lppl1.3
# catalog-version v1.33.5
Name:		texlive-polyglossia
Version:	v1.33.5
Release:	3
Summary:	Modern multilingual typesetting with XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polyglossia
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-etoolbox
Requires:	texlive-fontspec
Requires:	texlive-ifluatex
Requires:	texlive-makecmds
Requires:	texlive-xkeyval

%description
This package provides a complete Babel replacement for users of
LuaLaTeX and XeLaTeX; it relies on the fontspec package,
version 2.0 at least. This is the first release that supports
use with LuaLaTeX; it should be considered "transitional" in
that role.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%{_texmfdistdir}/tex/latex/polyglossia/arabicnumbers.sty
%{_texmfdistdir}/tex/latex/polyglossia/babel-hebrewalph.def
%{_texmfdistdir}/tex/latex/polyglossia/babelsh.def
%{_texmfdistdir}/tex/latex/polyglossia/cal-util.def
%{_texmfdistdir}/tex/latex/polyglossia/devanagaridigits.sty
%{_texmfdistdir}/tex/latex/polyglossia/farsical.sty
%{_texmfdistdir}/tex/latex/polyglossia/gloss-albanian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-amharic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-arabic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-armenian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-asturian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bahasai.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bahasam.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-basque.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bengali.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-brazil.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-breton.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-bulgarian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-catalan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-coptic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-croatian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-czech.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-danish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-divehi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-dutch.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-english.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-esperanto.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-estonian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-farsi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-finnish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-french.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-friulan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-galician.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-german.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-greek.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hebrew.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-hindi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-icelandic.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-interlingua.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-irish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-italian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-kannada.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lao.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latin.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-latvian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lithuanian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-lsorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-magyar.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-malayalam.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-marathi.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-nko.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-norsk.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-nynorsk.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-occitan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-piedmontese.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-polish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-portuges.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-romanian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-romansh.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-russian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-samin.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-sanskrit.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-scottish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-serbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-slovak.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-slovenian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-spanish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-swedish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-syriac.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-tamil.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-telugu.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-thai.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-tibetan.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-turkish.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-turkmen.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-ukrainian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-urdu.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-usorbian.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-vietnamese.ldf
%{_texmfdistdir}/tex/latex/polyglossia/gloss-welsh.ldf
%{_texmfdistdir}/tex/latex/polyglossia/hebrewcal.sty
%{_texmfdistdir}/tex/latex/polyglossia/hijrical.sty
%{_texmfdistdir}/tex/latex/polyglossia/nkonumbers.sty
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-frpt.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia-tibt.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia.lua
%{_texmfdistdir}/tex/latex/polyglossia/polyglossia.sty
%{_texmfdistdir}/tex/latex/polyglossia/xgreek-fixes.def
%doc %{_texmfdistdir}/doc/latex/polyglossia/README
%doc %{_texmfdistdir}/doc/latex/polyglossia/example-arabic.pdf
%doc %{_texmfdistdir}/doc/latex/polyglossia/example-arabic.tex
%doc %{_texmfdistdir}/doc/latex/polyglossia/example-thai.pdf
%doc %{_texmfdistdir}/doc/latex/polyglossia/example-thai.tex
%doc %{_texmfdistdir}/doc/latex/polyglossia/examples.pdf
%doc %{_texmfdistdir}/doc/latex/polyglossia/examples.tex
%doc %{_texmfdistdir}/doc/latex/polyglossia/polyglossia.pdf
%doc %{_texmfdistdir}/doc/latex/polyglossia/polyglossia.tex
#- source
%doc %{_texmfdistdir}/source/latex/polyglossia/polyglossia.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
