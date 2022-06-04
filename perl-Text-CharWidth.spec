#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-CharWidth
Version  : 0.04
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/K/KU/KUBOTA/Text-CharWidth-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KU/KUBOTA/Text-CharWidth-0.04.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0
Requires: perl-Text-CharWidth-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Text::CharWidth version 0.04
============================
This is a module to provide equivalent feature as wcwidth(3) and
wcswidth(3).  This also provides mblen(3) equivalent subroutine.

%package dev
Summary: dev components for the perl-Text-CharWidth package.
Group: Development
Provides: perl-Text-CharWidth-devel = %{version}-%{release}
Requires: perl-Text-CharWidth = %{version}-%{release}

%description dev
dev components for the perl-Text-CharWidth package.


%package perl
Summary: perl components for the perl-Text-CharWidth package.
Group: Default
Requires: perl-Text-CharWidth = %{version}-%{release}

%description perl
perl components for the perl-Text-CharWidth package.


%prep
%setup -q -n Text-CharWidth-0.04
cd %{_builddir}/Text-CharWidth-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::CharWidth.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
