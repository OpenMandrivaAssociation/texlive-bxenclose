%global tl_name bxenclose
%global tl_revision 40213

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Enclose the document body with some pieces of code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxenclose
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxenclose.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxenclose.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables authors to designate in the preamble to make the
document body enclosed with the given pieces of code. As is known, there
are already various mechanisms provided by LaTeX kernel or packages that
attach hooks at the beginning and end of documents.

