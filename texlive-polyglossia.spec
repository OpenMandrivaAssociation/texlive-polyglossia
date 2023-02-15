Name:		texlive-polyglossia
Version:	65792
Release:	1
Summary:	Modern multilingual typesetting with XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polyglossia
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polyglossia.source.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/polyglossia
%{_texmfdistdir}/tex/latex/polyglossia
%doc %{_texmfdistdir}/doc/latex/polyglossia
#- source
%doc %{_texmfdistdir}/source/latex/polyglossia

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
