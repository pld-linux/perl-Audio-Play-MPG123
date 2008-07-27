#
# TODO: add subpackage with included version of mpg123, or add patches to
#       mpg123 package (this module works better with modified version)
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Play-MPG123
Summary:	Audio::Play::MPG123 Perl module - a frontend to mpg123
Summary(pl.UTF-8):	Moduł Perla Audio::Play::MPG123 - frontend do mpg123
Name:		perl-Audio-Play-MPG123
Version:	0.63
Release:	2
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd5134e4a7b5a537a921e464dc264e5f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
Requires:	mpg123 >= 0.59r
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a frontend to the mpg123 player. It works by starting an
external mpg123 process with the `-R' option and feeding commands to
it.

%description -l pl.UTF-8
To jest frontend do odtwarzacza mpg123. Funkcjonuje poprzez
uruchomienie zewnętrznego procesu mpg123 z opcją -R i karmienie go
poleceniami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%attr(755,root,root) %{_bindir}/mpg123sh
%dir %{perl_vendorlib}/Audio/Play
%{perl_vendorlib}/Audio/Play/MPG123.pm
%{_mandir}/man3/*
