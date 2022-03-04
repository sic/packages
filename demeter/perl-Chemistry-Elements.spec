Name:           perl-Chemistry-Elements
Version:        1.074
Release:        2%{?dist}
Summary:        Perl extension for working with Chemical Elements
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Chemistry-Elements/
Source0:        http://www.cpan.org/authors/id/B/BD/BDFOY/Chemistry-Elements-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.010
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More) >= 1
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:	perl(Chemistry::Elements)

%description
There are two parts to the module: the object stuff and the exportable
functions for use outside of the object stuff. The exportable functions are
discussed in "Exportable functions".

%prep
%setup -q -n Chemistry-Elements-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes INSTALL.SKIP LICENSE META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon May  3 2021 Stuart Campbell (scampbell@bnl.gov) 1.074-2
- Added Provides info

* Sat Apr 10 2021 Stuart Campbell (scampbell@bnl.gov) 1.074-1
- Specfile autogenerated by cpanspec 1.78.