Name:           perl-File-CountLines
Version:        0.0.3
Release:        3%{?dist}
Summary:        Efficiently count the number of line breaks in a file
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-CountLines/
Source0:        http://www.cpan.org/authors/id/M/MO/MORITZ/File-CountLines-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(charnames) >= 1.01
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More::UTF8)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(warnings)
Requires:       perl(Carp)
Requires:       perl(charnames) >= 1.01
Requires:       perl(Exporter) >= 5.57
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(File::CountLines)

%description
perlfaq5 answers the question on how to count the number of lines in a
file. This module is a convenient wrapper around that method, with
additional options.

%prep
%setup -q -n File-CountLines-v%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 16 2022 Stuart Campbell (scampbell@bnl.gov) 0.0.3-3
- Added perl-interpreter and perl-generators to build dependencies

* Mon May  3 2021 Stuart Campbell (scampbell@bnl.gov) 0.0.3-2
- Add Provides info

* Sat Apr 10 2021 Stuart Campbell (scampbell@bnl.gov) 0.0.3-1
- Specfile autogenerated by cpanspec 1.78.
