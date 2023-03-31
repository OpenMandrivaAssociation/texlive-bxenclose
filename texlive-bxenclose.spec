Name:		texlive-bxenclose
Version:	40213
Release:	2
Summary:	Enclose the document body with some pieces of code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxenclose
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxenclose.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxenclose.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables authors to designate in the preamble to
make the document body enclosed with the given pieces of code.
As is known, there are already various mechanisms provided by
LaTeX kernel or packages that attach hooks at the beginning and
end of documents.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxenclose
%doc %{_texmfdistdir}/doc/latex/bxenclose

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
