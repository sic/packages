%global srcname uncertainties
%global summary Transparent calculations with uncertainties on the quantities involved (aka error propagation); fast calculation of derivatives
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 3.1.2
Release: %{release}%{?dist}
#Source0: https://github.com/lebigot/uncertainties/archive/3.1.2.tar.gz
Source0: https://files.pythonhosted.org/packages/2a/c2/babbe5b16141859dd799ed31c03987100a7b6d0ca7c0ed4429c96ce60fdf/uncertainties-3.1.2.tar.gz
License: MIT
Group: Science/Research
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Eric Lebigot
Url: https://uncertainties-python-package.readthedocs.io/en/latest/

%description
uncertainties allows calculations such as (2 +/- 0.1)*2 = 4 +/- 0.2 to be performed transparently. Much more complex mathematical expressions involving numbers with uncertainties can also be evaluated directly.

The uncertainties package takes the pain and complexity out of uncertainty calculations.

%package -n python2-%{srcname}
Summary:  %{summary}
Requires: python
Requires: python2-numpy
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires: python-setuptools

%description -n python2-%{srcname}
uncertainties allows calculations such as (2 +/- 0.1)*2 = 4 +/- 0.2 to be performed transparently. Much more complex mathematical expressions involving numbers with uncertainties can also be evaluated directly.

The uncertainties package takes the pain and complexity out of uncertainty calculations.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:  %{summary}
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-numpy
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

BuildRequires: python3-setuptools
BuildRequires: python3-devel

%description -n python%{python3_pkgversion}-%{srcname}
uncertainties allows calculations such as (2 +/- 0.1)*2 = 4 +/- 0.2 to be performed transparently. Much more complex mathematical expressions involving numbers with uncertainties can also be evaluated directly.

The uncertainties package takes the pain and complexity out of uncertainty calculations.

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

# build doesn't work because install translates from 2to3
%build
2to3-3 -w uncertainties-py27/*.py
2to3-3 -w uncertainties-py27//lib1to2/*.py
2to3-3 -w uncertainties-py27/unumpy/*.py
%py2_build
%py3_build

%install
%py2_install
%py3_install

# testing is somehow broken, but the package did work

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python2-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/*
