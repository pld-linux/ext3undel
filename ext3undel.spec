Summary:	A collection of scripts to help you recover files from ext2/ext3
Summary(pl.UTF-8):	Zestaw skryptów do odzyskiwania plików z ext2/ext3
Name:		ext3undel
Version:	0.1.6
Release:	1
License:	GPL v2
Group:		Applications
# Source0Download: http://projects.izzysoft.de/trac/ext3undel/wiki/Download
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	996107eead228ed476e89e8b9b82242f
Patch0:		%{name}-bashizm.patch
URL:		http://projects.izzysoft.de/trac/ext3undel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ext3undel is a collection of scripts to help you recover deleted files
from ext2/ext3 file systems. ext3undel tries to automate most of the
difficult manual work of recovery so that it may be possible to
recover a single specified file or all data on a given disk.

%description -l pl.UTF-8
ext3undel to zestaw skryptów wspomagających odzyskiwanie usuniętych
plików z systemów plików ext2/ext3. ext3undel stara się zautomatyzować
większość trudnych czynność, tak aby możliwe było odzyskanie
pojedynczego pliku lub całości danych na dysku.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{history,install.txt,ralf.txt,readme.txt}
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%{_mandir}/man5/ext3undel.conf.5*
%{_mandir}/man8/*.8*
