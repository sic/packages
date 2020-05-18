%global srcname bumps
%global summary Data fitting with uncertainty analysis
%global descr Bumps provides data fitting and Bayesian uncertainty modeling for inverse problems. It has a variety of optimization algorithms available for locating the most like value for function parameters given data, and for exploring the uncertainty around the minimum.
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 0.7.14
Release: %{release}%{?dist}
#ource0: %{pypi_source} - missing LICENSE and test files
Source0: https://github.com/bumps/bumps/archive/v%{version}.tar.gz
License: Custom
Group: Science/Engineering
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Paul Kienzle <paul.kienzle@nist.gov>
Url: https://github.com/bumps/bumps/

%description
%{descr}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:  %{summary}
Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-matplotlib
Requires: python%{python3_pkgversion}-scipy

BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python%{python3_pkgversion}-nose
BuildRequires: python%{python3_pkgversion}-matplotlib
BuildRequires: python%{python3_pkgversion}-scipy

%description -n python%{python3_pkgversion}-%{srcname}
%{descr}

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/*
%exclude %{_bindir}/bumps
