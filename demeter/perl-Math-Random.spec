Name:           perl-Math-Random
Version:        0.72
Release:        7%{?dist}
Summary:        Random Number Generators
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Random/
Source0:        http://www.cpan.org/authors/id/G/GR/GROMMEL/Math-Random-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Math::Random)

%description
Math::Random is a Perl port of the C version of randlib, which is a suite
of routines for generating random deviates. See "RANDLIB" for more
information.

%prep
%setup -q -n Math-Random-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes Index README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
* Fri Jun 17 2022 Stuart Campbell <scampbell@bnl.gov> - 0.72-7
- Remove ExtUtils::Typemap for build dependencies

* Fri Jun 17 2022 Stuart Campbell <scampbell@bnl.gov> - 0.72-6
- Added some more build dependencies and AutoLoader

* Thu Jun 16 2022 Stuart Campbell <scampbell@bnl.gov> - 0.72-5
- Add ExtUtils::Typemap to build deps

* Thu Jun 16 2022 Stuart Campbell <scampbell@bnl.gov> - 0.72-4
- Add make to build dependencies

* Thu Jun 16 2022 Stuart Campbell <scampbell@bnl.gov> - 0.72-3
- Added perl-generators to build dependencies

* Mon May  3 2021 Stuart Campbell (scampbell@bnl.gov) 0.72-2
- Added Provides info

* Sat Apr 10 2021 Stuart Campbell (scampbell@bnl.gov) 0.72-1
- Specfile autogenerated by cpanspec 1.78.
