%global tl_name smartdiagram
%global tl_revision 42781

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3b
Release:	%{tl_revision}.1
Summary:	Generate diagrams from lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/smartdiagram
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smartdiagram.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smartdiagram.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/smartdiagram.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package will create 'smart' diagrams from lists of items, for simple
documents and for presentations.

