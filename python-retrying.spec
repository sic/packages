%global srcname retrying
%global summary Retrying
%define release 1

Summary: ${summary}
Name: python-%{srcname}
Version: 1.3.3
Release: %{release}%{?dist}
Source0: https://files.pythonhosted.org/packages/44/ef/beae4b4ef80902f22e3af073397f079c96969c69b2c7d52a57ea9ae61c9d/retrying-1.3.3.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ray Holder
Url: https://github.com/rholder/retrying

BuildRequires: python%{python3_pkgversion}-devel

%description
Retrying is an Apache 2.0 licensed general-purpose retrying library, written in Python, to simplify the task of adding retry behavior to just about anything.

The simplest use case is retrying a flaky function whenever an Exception occurs until a value is returned.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:      python3
#Requires: python%{python3_pkgversion}-matplotlib
#Requires: python%{python3_pkgversion}-pandas
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Retrying is an Apache 2.0 licensed general-purpose retrying library, written in Python, to simplify the task of adding retry behavior to just about anything.

The simplest use case is retrying a flaky function whenever an Exception occurs until a value is returned.

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# retrying does not currently have tests
#%check
#%{__python3} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.cpython-%{python3_pkgversion}*.pyc
%{python3_sitelib}/%{srcname}-%{version}-py3*.egg-info/*
