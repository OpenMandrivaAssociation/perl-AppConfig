%define upstream_name    AppConfig

Summary:	Perl5 modules for reading configuration
Name:		perl-%{upstream_name}
Version:	1.71
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/AppConfig
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/AppConfig-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl-File-HomeDir

%description
AppConfig has a powerful but easy to use module for parsing configuration
files. It also has a simple and efficient module for parsing command line
arguments.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/AppConfig
%{perl_vendorlib}/AppConfig.pm
%{_mandir}/man3/*
