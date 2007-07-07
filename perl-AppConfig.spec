%define module AppConfig
%define name	perl-%{module}
%define	version	1.66
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:  	Perl5 modules for reading configuration
License:	GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/AppConfig/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:	perl-File-HomeDir
buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
AppConfig has a powerful but easy to use module for parsing configuration
files. It also has a simple and efficient module for parsing command line
arguments.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -fr %{buildroot}

%files
%defattr(-,root,root) 
%doc README
%{perl_vendorlib}/AppConfig
%{perl_vendorlib}/AppConfig.pm
%{_mandir}/*/*
