# Proj has proved not beeing compatible all the time, bug #839651
%{bcond_without perl_PDL_enables_proj}

# Slatec does not work on PPC64 since 2.4.something
# could be a big endian related issue
%ifarch ppc64 s390 s390x
%{bcond_with perl_PDL_enables_slatec}
%else
%{bcond_without perl_PDL_enables_slatec}
%endif

# Run optional test
%{bcond_without perl_PDL_enables_optional_test}

Name:           perl-PDL
%global cpan_version 2.034
Version:        2.34.0
Release:        1%{?dist}
Summary:        The Perl Data Language
License:        GPL+ or Artistic
Url:            http://pdl.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/PDL-%{cpan_version}.tar.gz
# Uncomment to enable PDL::IO::Browser
# Patch0:         perl-PDL-2.4.10-settings.patch
# Disable Proj support when it's not compatible, bug #839651
Patch2:         PDL-2.4.10-Disable-PDL-GIS-Proj.patch
# Compile Slatec as PIC, needed for ARM
Patch3:         PDL-2.6.0.90-Compile-Slatec-code-as-PIC.patch
# Disable Slatec code crashing on PPC64, bug #1041304
Patch4:         PDL-2.14.0-Disable-PDL-Slatec.patch
Patch5:         PDL-2.17.0-Update-additional-deps-for-Basic-Core.patch
# Fix numbering of line in test when shebang is added
Patch6:         PDL-2.28.0-Fix-numbering-of-line-in-test.patch
BuildRequires:  coreutils
BuildRequires:  fftw2-devel
BuildRequires:  findutils
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gd-devel
BuildRequires:  gsl-devel >= 1.0
BuildRequires:  hdf-static hdf-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# perl(Astro::FITS::Header) not packaged yet
BuildRequires:  perl(blib)
# Modified perl(Carp) bundled
# Modified perl(Carp::Heavy) bundled
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper) >= 2.121
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Devel::REPL)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::F77)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
# OpenGL >= 0.6702 is required but newer OpenGL-0.70 shortened the version
BuildRequires:  perl(OpenGL) >= 0.67.02
# OpenGL::Config is private OpenGL hash
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::REPL::Plugin)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Map) >= 0.57
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Simple) >= 0.88
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Inline) >= 0.43
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Compile) >= 0.23
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SelfLoader)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Text::Balanced) >= 1.89
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
%if %{with perl_PDL_enables_optional_test}
# Optional tests:
# netpbm-progs for jpegtopnm
BuildRequires:  netpbm-progs
BuildRequires:  perl(Convert::UU)
BuildRequires:  perl(Storable) >= 1.03
%endif

%if %{with perl_PDL_enables_proj}
# Needed by PDL::GIS::Proj
BuildRequires:  proj-devel
%endif
# Need by PDL::IO::Browser, currently disabled
# BuildRequires:  ncurses-devel
BuildRequires:  sharutils
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(ExtUtils::Liblist)
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(ExtUtils::MM)
Requires:       perl(File::Map) >= 0.57
Requires:       perl(File::Spec) >= 0.6
Requires:       perl(Filter::Simple) >= 0.88
Requires:       perl(Inline) >= 0.43
Requires:       perl(Module::Compile) >= 0.23
# OpenGL >= 0.6702 is required but newer OpenGL-0.70 shortened the version
Requires:       perl(OpenGL) >= 0.67.02
Requires:       perl(Prima::Application)
Requires:       perl(Prima::Buttons)
Requires:       perl(Prima::Edit)
Requires:       perl(Prima::Label)
Requires:       perl(Prima::PodView)
Requires:       perl(Prima::Utils)
Requires:       perl(Text::Balanced) >= 1.89
Provides:       perl(PDL::Config) = %{version}
Provides:       perl(PDL::DiskCache) = %{version}
Provides:       perl(PDL::PP::CType) = %{version}
Provides:       perl(PDL::PP::Dims) = %{version}
Provides:       perl(PDL::PP::PDLCode) = %{version}
Provides:       perl(PDL::PP::SymTab) = %{version}
Provides:       perl(PDL::PP::XS) = %{version}
Provides:       perl(PDL::Graphics::TriD::Objects) = %{version}

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((OpenGL::Config|PDL::Demos::Screen|PDL::Graphics::PGPLOT|PDL::Graphics::PGPLOT::Window|Tk|Win32::DDE::Client)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Inline\\)$
%global __provides_exclude %__provides_exclude|^perl\\(Win32.*\\)$
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Data::Dumper|File::Spec|Filter::Simple|Inline|Module::Compile|OpenGL|Text::Balanced)\\)$
# Remove modules not compiled
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((PDL::GIS::Proj|PDL::IO::HDF.*)\\)$

%description
PDL ("Perl Data Language") gives standard Perl the ability to
compactly store and speedily manipulate the large N-dimensional data
arrays which are the bread and butter of scientific computing.  PDL
turns perl into a free, array-oriented, numerical language similar to
such commercial packages as IDL and MatLab.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Devel::CheckLib)

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n PDL-%{cpan_version}
# Uncomment to enable PDL::IO::Browser
# %%patch0 -p1 -b .settings
%if %{without perl_PDL_enables_proj}
%patch2 -p1 -b .proj
%endif
%patch3 -p1 -b .slatecpic
%if %{without perl_PDL_enables_slatec}
%patch4 -p1 -b .slatec
%endif
%patch5 -p1
%patch6 -p1
# Fix shellbang
perl -MConfig -pi -e 's|^#!/usr/bin/env perl|$Config{startperl}|' Perldl2/pdl2

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
# Suppress numerous warnings about unused variables
CFLAGS="%{optflags} -Wno-unused"
# Fused multiply-add instructions cause segfaults on 64-bit PowerPC if GSL
# support is enabled (the same option is in gsl.spec), bug #1410162
%ifarch ppc64 ppc64le s390 s390x
CFLAGS="$CFLAGS -ffp-contract=off"
%endif
# Uncomment to enable PDL::IO::Browser
# CFLAGS="$CFLAGS -DNCURSES"
CFLAGS="$CFLAGS" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$CFLAGS"
make OPTIMIZE="$CFLAGS" %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
perl -Mblib Doc/scantree.pl %{buildroot}%{perl_vendorarch}
perl -pi -e "s|%{buildroot}/|/|g" %{buildroot}%{perl_vendorarch}/PDL/pdldoc.db
find %{buildroot}%{perl_vendorarch} -type f -name "*.pm" | xargs chmod -x
find %{buildroot} -type f -name '*.bs' -empty -delete

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t m51.fits %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
unset DISPLAY
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%{_fixperms} %{buildroot}/*

%check
unset DISPLAY
export PERL5LIB=`pwd`/blib/lib
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license COPYING
%doc Changes INTERNATIONALIZATION README TODO
%{_bindir}/*
%{perl_vendorarch}/Inline/*
%{perl_vendorarch}/PDL*
%{perl_vendorarch}/auto/PDL/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Apr 06 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.34.0-1
- 2.034 bump

* Wed Mar 31 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.33.0-1
- 2.033 bump

* Wed Mar 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.32.0-1
- 2.032 bump

* Tue Mar 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.31.0-1
- 2.031 bump

* Mon Mar 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.30.0-1
- 2.030 bump

* Mon Mar 15 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.29.0-1
- 2.029 bump

* Mon Mar 08 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.28.0-1
- 2.028 bump
- Package tests

* Mon Feb 15 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.26.0-1
- 2.026 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.25.0-1
- 2.25.0 bump

* Thu Sep 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.24.0-1
- 2.24.0 bump

* Mon Sep 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.23.0-1
- 2.23.0 bump

* Mon Sep 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.22.0-1
- 2.22.0 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.21.0-5
- Perl 5.32 rebuild

* Thu Apr  2 2020 Robin Lee <cheeselee@fedoraproject.org> - 2.21.0-4
- Fix broken deps since 2.20. PDL::Graphics::PGPLOT is no longer provided but
  PDL::Demos::PGPLOT_demo still requires it

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.21.0-3
- Specify all dependencies

* Mon Mar 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.21.0-1
- 2.21.0 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.20.0-1
- 2.20.0 bump

* Thu Sep 05 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.19.0-9
- Rename BR proj-nad to proj-datumgrid

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.19.0-8
- Rebuilt for GSL 2.6.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.19.0-6
- Perl 5.30 rebuild

* Thu Feb 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.19.0-5
- rebuilt (proj)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.19.0-2
- Perl 5.28 rebuild

* Mon May 07 2018 Petr Pisar <ppisar@redhat.com> - 2.19.0-1
- 2.019 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Petr Pisar <ppisar@redhat.com> - 2.18.0-5
- Modernize spec file

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18.0-2
- Perl 5.26 rebuild

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.18.0-1
- 2.018 bump

* Thu Apr 27 2017 Petr Pisar <ppisar@redhat.com> - 2.17.0-8
- Adapt to changes in List-MoreUtils-0.418 (bug #1446104)

* Fri Feb 17 2017 Petr Pisar <ppisar@redhat.com> - 2.17.0-7
- Adapt OpenGL dependency to OpenGL-0.70

* Wed Feb 15 2017 Dan Horák <dan[at]danny.cz> - 2.17.0-6
- Fix build on s390(x)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Petr Pisar <ppisar@redhat.com> - 2.17.0-4
- Rebuild against libgfortran-7.0.1

* Wed Jan 25 2017 Petr Pisar <ppisar@redhat.com> - 2.17.0-3
- Rebuild against proj-4.9.3

* Thu Jan 05 2017 Petr Pisar <ppisar@redhat.com> - 2.17.0-2
- Disable fused multiply-add instructions on 64-bit PowerPC because of GSL
  (bug #1410162)

* Mon Oct 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.17.0-1
- 2.017 bump

* Mon Jun 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.16.0-1
- 2.016 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.15.0-5
- Perl 5.24 rebuild

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.15.0-4
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.15.0-2
- Add patch for gsl 2 support

* Mon Nov 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.15.0-1
- 2.015 bump

* Tue Oct 27 2015 Petr Pisar <ppisar@redhat.com> - 2.14.0-2
- Rebase Disable-PDL-Slatec patch
- Improve shellbang fix

* Tue Oct 13 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.14.0-1
- 2.014 bump

* Mon Aug 17 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.13.0-1
- 2.013 bump

* Thu Jun 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.0-1
- 2.012 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.11.0-1
- 2.011 bump

* Mon May 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.8.0-1
- 2.008 bump

* Fri Apr 03 2015 Petr Pisar <ppisar@redhat.com> - 2.7.0-9
- Rebuild against proj-4.9

* Tue Feb 10 2015 Petr Pisar <ppisar@redhat.com> - 2.7.0-8
- Fix parallel build in Basic/Core directory

* Tue Feb 10 2015 Petr Pisar <ppisar@redhat.com> - 2.7.0-7
- Run-require ExtUtils::MakeMaker for script generated by pptemplate tool

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.0-6
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Petr Pisar <ppisar@redhat.com> - 2.7.0-3
- Skip PDL::Slatec reverse dependencies if Slatec is disabled (bug #1041304)

* Mon Dec 16 2013 Petr Pisar <ppisar@redhat.com> - 2.7.0-2
- Disable Slatec on PPC64 (bug #1041304)

* Mon Dec 16 2013 Petr Pisar <ppisar@redhat.com> - 2.7.0-1
- 2.007 bump

* Mon Oct 14 2013 Petr Pisar <ppisar@redhat.com> - 2.6.0.90-1
- 2.006_90 bump
- Enable Proj support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 2.4.10-9
- Perl 5.18 rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 2.4.10-8
- rebuild for new GD 2.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 2.4.10-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.4.10-5
- rebuild against new libjpeg

* Tue Sep 04 2012 Petr Pisar <ppisar@redhat.com> - 2.4.10-4
- Disable Proj support (bug #839651)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 2.4.10-2
- Perl 5.16 rebuild

* Mon Feb 06 2012 Petr Šabata <contyk@redhat.com> - 2.4.10-1
- 2.4.10 bump
- Remove (hopefully) useless macros and rpm4.8 filters
- Drop PDL::IO::Browser support for now
- Some cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 2.4.9-4
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.4.9-3
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.4.9-2
- Perl mass rebuild

* Mon Apr 11 2011 Petr Sabata <psabata@redhat.com> - 2.4.9-1
- 2.4.9 bump

* Thu Mar 31 2011 Petr Sabata <psabata@redhat.com> - 2.4.8-1
- 2.4.8 bump
- Removing Buildroot tag and clean section
- Filtering Win32 from provides
- Removing `-lext' filtering patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Marcela Mašláňová <mmaslano@redhat.com> 2.4.7-1
- update to 2.4.7
- add new provides PDL::Graphics::TriD*
- add BR perl(version)
- remove patches included in new version

* Sat Jun 05 2010 Iain Arnell <iarnell@gmail.com> 2.4.6-4
- restore the manual provides

* Fri Jun  4 2010 Petr Pisar <ppisar@redhat.com> - 2.4.6-3
- Move PERL_DL_NONLAZY=0 setting from OpenGL to POGL

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4.6-2
- Mass rebuild with perl-5.12.0

* Wed Jan  6 2010 Stepan Kasal <skasal@redhat.com> - 2.4.6-1
- new upstream version
- add BuildRequires: perl(OpenGL) freeglut-devel libXmu-devel libXi-devel
- use better BuildRoot
- use filtering macros
- update patches settings and x86_64
- move the charset conversion before the build

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.4.4_05-7
- Explicitly BR hdf-static in accordance with the Packaging
  Guidelines (hdf-devel is still static-only).

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.4.4_05-6
- rebuild against perl 5.10.1

* Thu Sep 10 2009 Orion Poplawski <orion@cora.nwra.com> - 2.4.4_05-5
- Remove PDL::Graphics::PLplot to make way for separate package

* Wed Sep 9 2009 Orion Poplawski <orion@cora.nwra.com> - 2.4.4_05-4
- No, we really need to strip out the PLplot version so it can load

* Wed Sep 9 2009 Orion Poplawski <orion@cora.nwra.com> - 2.4.4_05-3
- Don't strip out PLplot version so that plplot can detect it

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4_05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Orion Poplawski <orion@cora.nwra.com> - 2.4.4_05-1
- Update to 2.4.4_05 and PDL-Graphics-PLplot-0.50
- Drop test patch, no longer needed

* Tue Feb 24 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.4-3
- rebuild

* Thu Jan 1 2009 Orion Poplawski <orion@cora.nwra.com> - 2.4.4-2
- Use PDL-Graphics-PLplot-0.47 to support latest plplot

* Sat Nov 29 2008 Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
- Update to 2.4.4
- New source URL
- Update cleanup, test, x86_64, and Xext patches for 2.4.4
- Drop gsl, perl510, noDISPLAY and missingfnc patches fixed upstream
- Add BR proj-nad needed for tests
- Add patch to fix plplot test with latest plplot

* Wed Oct  1 2008 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.3-15
- rebuilt for F-10

* Thu Sep 18 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.4.3-14
- 461803 Missing Functions from PDL::Graphics::PLplot

* Thu Sep 04 2008 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-13
- Add patch to add plparseopts function
- Update URL

* Mon Mar 10 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.4.3-12
- PERL_DL_NONLAZY=0 was uncommented in check part of spec.

* Sat Mar 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.3-11
- PERL_DL_NONLAZY=0 for all the GL tests
- don't run GL tests if DISPLAY is unset

* Sat Mar 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.3-9
- patch to fix build against perl 5.10, get useful random numbers

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.3-8
- Rebuild for new perl

* Tue Mar 04 2008 Orion Poplawski <orion@cora.nwra.com> - 2.4.3-7
- Add patch to build GSL support with GSL 1.10
- unset DISPLAY in %%check for mock builds

* Tue Feb 26 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.4.3-6
- remove two of hdf test for some time, because can't be build

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4.3-5
- Autorebuild for GCC 4.3

* Wed Aug 15 2007 Robin Norwood <rnorwood@redhat.com> - 2.4-3-4
- Updated perl-PDL-2.4.3-test.patch from Orion to fix ppc and ppc64
- Fixed license string
- Fixed old changelog version number

* Fri Aug 10 2007 Robin Norwood <rnorwood@redhat.com> - 2.4.3-3
- More changes from Orion Poplawski
- BuildRequires and patch for fortran/f77 support
- Added Provides: perl(PDL::Graphics::TriD::Object
- Filter perl(Win32::DDE::Client) from Requires

* Mon Aug 06 2007 Robin Norwood <rnorwood@redhat.com> - 2.4.3-2
- Apply changes from package review
- untabify spec file
- Add various files to %%doc
- turn on 3D/GL
- turn on IO Browser
- add a bunch of BRs to enable more modules
- remove unneeded Provides
- perl-PDL-2.4.3-hdf.patch to look for hdf devel files in the right place
- perl-PDL-2.4.3-test.patch to fix some tests
- perl-PDL-2.4.3-x86_64.patch to find 64bit libraries for some modules
- perl-PDL-2.4.3-Xext.patch to remove -lXext from GL linking options

* Sat Dec 02 2006 Robin Norwood <rnorwood@redhat.com> - 2.4.3-1
- Latest version from CPAN: 2.4.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-4.fc5.1
- rebuild

* Fri Mar 10 2006 Jason Vas Dias <jvdias@redhat.com> - 2.4.2-4
- Further code cleanup & CFLAGS settings required to enable tests
  to succeed on all platforms

* Thu Mar 09 2006 Jason Vas Dias <jvdias@redhat.com> - 2.4.2-4
- Enable tests to succeed on ia64 (remove casts from int to * !)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-2.fc5.1.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-2.fc5.1.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 2.4.2-2.fc5.1.2
- rebuild for new perl-5.8.8
- enable build to succeed without perl-PDL being installed :-)

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sun Sep 25 2005 Warren Togami <wtogami@redhat.com> - 2.4.2-2
- Ship pdldoc.db, tune build dependencies and file permissions (#163219 scop)

* Fri May 27 2005 Warren Togami <wtogami@redhat.com> - 2.4.2-1
- 2.4.2
- filter perl(Inline) from provides (#158733)

* Wed May 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.4.1-11
- Add missing perl(PDL::Graphics::TriD*) provides. (#156482)
- Explicitly filter perl(Tk). (#156482)

* Sat Apr 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.4.1-10
- Bring up to date with current Fedora.Extras perl spec template. (#156482)
- disable SMP flags so it actually builds

* Sat Dec 18 2004 Miloslav Trmac <mitr@redhat.com> - 2.4.1-9
- Rebuild with fixed gsl-devel (#142695)

* Sun Dec 12 2004 Miloslav Trmac <mitr@redhat.com> - 2.4.1-8
- Fix more bugs on 64-bit platforms
- BuildRequires: gsl-devel

* Sun Dec 12 2004 Miloslav Trmac <mitr@redhat.com> - 2.4.1-7
- Fix rangeb on 64-bit platforms (I hope) (#141413)

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 2.4.1-6
- Convert man page to UTF-8

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 2.4.1-1
- update to 2.4.1

* Mon Jun 16 2003 Chip Turner <cturner@redhat.com> 2.4.0-2
- move to 2.4.0, integrate dependency fixes from other tree

* Wed Jan 29 2003 Chip Turner <cturner@redhat.com>
- bump

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Wed Nov 20 2002 Chip Turner <cturner@redhat.com>
- move to 2.3.4

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Tue Jul 16 2002 Chip Turner <cturner@redhat.com>
- updated %%description

* Thu Jun 27 2002 Chip Turner <cturner@redhat.com>
- description update

* Fri Jun 07 2002 cturner@redhat.com
- Specfile autogenerated

