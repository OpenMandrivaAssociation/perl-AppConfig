%define upstream_name    AppConfig
%define	upstream_version 1.71

Summary:	Perl5 modules for reading configuration
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/AppConfig
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/AppConfig-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	perl-File-HomeDir

%description
AppConfig has a powerful but easy to use module for parsing configuration
files. It also has a simple and efficient module for parsing command line
arguments.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/AppConfig
%{perl_vendorlib}/AppConfig.pm
%{_mandir}/man3/*

