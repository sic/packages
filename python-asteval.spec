%global srcname asteval
%global summary minimalistic evaluator of python expression using ast module
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 0.9.17
Release: %{release}%{?dist}
Source0: https://github.com/newville/asteval/archive/0.9.17.tar.gz
License: MIT
Group: Science/Research
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matt Newville
Url: https://github.com/newville/asteval/

%description
ASTEVAL provides a numpy-aware, safe(ish) ‘eval’ function

Emphasis is on mathematical expressions, and so numpy ufuncs are used if available. Symbols are held in the Interpreter symbol table ‘symtable’: a simple dictionary supporting a simple, flat namespace.

Expressions can be compiled into ast node for later evaluation, using the values in the symbol table current at evaluation time.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:  %{summary}
Requires: python%{python3_pkgversion}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

BuildRequires: python3-setuptools

%description -n python%{python3_pkgversion}-%{srcname}
ASTEVAL provides a numpy-aware, safe(ish) ‘eval’ function

Emphasis is on mathematical expressions, and so numpy ufuncs are used if available. Symbols are held in the Interpreter symbol table ‘symtable’: a simple dictionary supporting a simple, flat namespace.

Expressions can be compiled into ast node for later evaluation, using the values in the symbol table current at evaluation time.

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# testing isn't registered correctly with setup.py
#check
#{__python3} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
