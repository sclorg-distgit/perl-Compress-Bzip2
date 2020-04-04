%{?scl:%scl_package perl-Compress-Bzip2}

# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_Compress_Bzip2_enables_optional_test
%else
%bcond_with perl_Compress_Bzip2_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Compress-Bzip2
Version:        2.26
Release:        14%{?dist}
Summary:        Interface to Bzip2 compression library
# bzlib-src/win-tst-dlltest.c (unbundled):  Public Domain
# bzlib-src/LICENSE (unbundled):            BSD
# bzlib-src/manual.ps (unbundled):          GPL+ with exception
# other files:                              GPL+ or Artistic
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Compress-Bzip2
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Compress-Bzip2-%{version}.tar.gz
BuildRequires:  bzip2-devel >= 1.0.5
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
# VMS::Filespec not needed
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(AutoLoader)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant) >= 1.04
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
BuildRequires:  %{?scl_prefix}perl(Getopt::Std)
BuildRequires:  %{?scl_prefix}perl(warnings)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Cwd)
# Memory::Usage not used
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Test::Kwalitee not used
# Optional tests:
%if !%{defined perl_bootstrap} && %{with perl_Compress_Bzip2_enables_optional_test}
BuildRequires:  %{?scl_prefix}perl(Test::LeakTrace)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(constant) >= 1.04

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(constant\\)$

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2 compression
library. A relevant subset of the functionality provided by Bzip2 is available
in Compress::Bzip2. Compress::Bzip2 is not well integrated into PerlIO, use
the preferred IO::Compress::Bzip2 instead.

%prep
%setup -q -n Compress-Bzip2-%{version}
# Remove bundled bzip2 library
find bzlib-src -mindepth 1 -type f \! -name 'sample*' -delete
sed -i -e '/^bzlib-src\//d' MANIFEST
find bzlib-src -type f >>MANIFEST

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc COPYING
%doc ANNOUNCE Changes NEWS README.md
%{perl_vendorarch}/Compress/
%{perl_vendorarch}/auto/Compress/
%{_mandir}/man3/*.3pm*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-14
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-12
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-8
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-2
- Perl 5.26 rebuild

* Tue Apr 11 2017 Petr Pisar <ppisar@redhat.com> - 2.26-1
- 2.26 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Petr Pisar <ppisar@redhat.com> - 2.25-1
- 2.25 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-4
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Petr Pisar <ppisar@redhat.com> - 2.24-1
- 2.24 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.22-2
- Perl 5.22 rebuild

* Thu Feb 19 2015 Petr Pisar <ppisar@redhat.com> - 2.22-1
- 2.22 bump

* Fri Jan 30 2015 Petr Pisar <ppisar@redhat.com> - 2.20-1
- 2.20 bump

* Wed Oct 29 2014 Petr Pisar <ppisar@redhat.com> - 2.19-2
- Do not build-require version module

* Mon Oct 27 2014 Petr Pisar <ppisar@redhat.com> - 2.19-1
- 2.19 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Petr Pisar <ppisar@redhat.com> - 2.18-1
- 2.18 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Petr Pisar <ppisar@redhat.com> - 2.17-1
- 2.17 bump
- License changed to (GPL+ or Artistic)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.16-2
- Perl 5.18 rebuild

* Thu Jun 20 2013 Petr Pisar <ppisar@redhat.com> - 2.16-1
- 2.16 bump

* Mon Apr 08 2013 Petr Pisar <ppisar@redhat.com> - 2.15-1
- 2.15 bump

* Thu Apr 04 2013 Petr Pisar <ppisar@redhat.com> - 2.13-1
- 2.13 bump

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 2.10-1
- 2.10 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.09-15
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.09-13
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.09-11
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.09-10
- Mass rebuild with perl-5.12.0

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 2.09-9
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-6.2
Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.09-5.2
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-4.2
- add BR: perl(Test::More)

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-4
- Rebuild for FC6.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-3
- Rebuild for FC5 (perl 5.8.8).

* Mon Jan  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-2
- Applied two of the Ville's suggestions (#177166): trimmed down
  the description to the first paragraph and added the file ANNOUNCE
  as documentation.

* Thu Aug 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.09-1
- Update to 2.09.

* Mon May 02 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.07-1
- Update to 2.07.

* Mon Apr 25 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.04-1
- Update to 2.04.

* Sun Apr 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.03-1
- Update to 2.03.

* Sun Apr 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.00-1
- Update to 2.00.

* Thu Apr 21 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- First build.
