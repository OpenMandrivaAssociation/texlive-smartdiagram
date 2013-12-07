# revision 30046
# category Package
# catalog-ctan /graphics/pgf/contrib/smartdiagram
# catalog-date 2013-04-02 02:01:45 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-smartdiagram
Version:	0.3
Release:	2
Summary:	Generate diagrams from lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/smartdiagram
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartdiagram.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartdiagram.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smartdiagram.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will create 'smart' diagrams from lists of items,
for simple documents and for presentations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/smartdiagram/smartdiagram.sty
%{_texmfdistdir}/tex/latex/smartdiagram/smartdiagramlibraryadditions.code.tex
%{_texmfdistdir}/tex/latex/smartdiagram/smartdiagramlibrarycore.commands.code.tex
%{_texmfdistdir}/tex/latex/smartdiagram/smartdiagramlibrarycore.definitions.code.tex
%{_texmfdistdir}/tex/latex/smartdiagram/smartdiagramlibrarycore.styles.code.tex
%doc %{_texmfdistdir}/doc/latex/smartdiagram/README
%doc %{_texmfdistdir}/doc/latex/smartdiagram/smartdiagram.pdf
#- source
%doc %{_texmfdistdir}/source/latex/smartdiagram/smartdiagram.dtx
%doc %{_texmfdistdir}/source/latex/smartdiagram/smartdiagram.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
