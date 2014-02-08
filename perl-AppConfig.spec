%define upstream_name    AppConfig
%define	upstream_version 1.66

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Perl5 modules for reading configuration
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/AppConfig/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-File-HomeDir
BuildArch:		noarch

%description
AppConfig has a powerful but easy to use module for parsing configuration
files. It also has a simple and efficient module for parsing command line
arguments.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/AppConfig
%{perl_vendorlib}/AppConfig.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.660.0-4mdv2012.0
+ Revision: 765051
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.660.0-3
+ Revision: 763475
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.660.0-2
+ Revision: 667025
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.660.0-1mdv2010.1
+ Revision: 402977
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.66-3mdv2009.0
+ Revision: 223498
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.66-2mdv2008.1
+ Revision: 180365
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 1.66-1mdv2008.0
+ Revision: 49307
- New version

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.65-1mdv2008.0
+ Revision: 46310
- update to new version 1.65

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.64-1mdv2008.0
+ Revision: 19184
-New version


* Fri Dec 22 2006 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2006-12-22 22:55:14 (101843)
- add BuildRequires: perl-File-HomeDir

* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org>
+ 2006-12-19 12:38:41 (99352)
Import perl-AppConfig

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.63-1mdv2007.0
- new version
- spe cleanup

* Sat Apr 01 2006 Buchan Milne <bgmilne@mandriva.org> 1.56-2mdk
- Rebuild
- use mkrel

* Wed May 05 2004 Michael Scherer <misc@mandrake.org> 1.56-1mdk
- remove unused Tag
- 1.56
- rpmbuildupdate aware

