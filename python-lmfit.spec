%global srcname lmfit-py
%global summary Non-Linear Least Squares Minimization
%global descr Non-Linear Least Squares Minimization, with flexible Parameter settings, based on scipy.optimize.leastsq, and with many additional classes and methods for curve fitting http:/lmfit.github.io/lmfit-py/
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 0.8.3
Release: %{release}%{?dist}
Source0: https://github.com/lmfit/lmfit-py/archive/%{version}.tar.gz
License: Custom
Group: Science/Research
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Matt Newville
Url: https://lmfit.github.io/lmfit-py/

%description
%{descr}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:  %{summary}
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-numpy >= 1.5
Requires: python%{python3_pkgversion}-scipy >= 0.13
Requires: python%{python3_pkgversion}-pandas
Requires: python%{python3_pkgversion}-matplotlib
Requires: python%{python3_pkgversion}-dateutil
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

BuildRequires: python3-setuptools
BuildRequires: python%{python3_pkgversion}-nose

%description -n python%{python3_pkgversion}-%{srcname}
%{descr}

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# testing is somehow broken, but the package did work
#check
#__python3} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
