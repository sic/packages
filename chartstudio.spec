%global srcname chart-studio
%global summary Utilities for interfacing with plotlys Chart Studio
%define release 1

Summary: ${summary}
Name: python-%{srcname}
Version: 1.0.0
Release: %{release}%{?dist}
Source0: https://files.pythonhosted.org/packages/ab/ca/9ba86244828a8d8eff279ef49914faaea96ce86b9285eb907ec1123331f5/chart-studio-1.0.0.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris P <chris@plot.ly>
Url: https://plot.ly/python/

BuildRequires: python%{python3_pkgversion}-devel

%description
This package contains utilities for interfacing with Plotlys Chart Studio service (both Chart Studio cloud and Chart Studio On-Prem). Prior to plotly.py version 4, This functionality was included in the plotly package under the plotly.plotly module. As part of plotly.py version 4, the Chart Studio functionality was removed from the plotly package and released in this chart-studio package.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:      python3
#Requires: python%{python3_pkgversion}-matplotlib
#Requires: python%{python3_pkgversion}-pandas
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains utilities for interfacing with Plotlys Chart Studio service (both Chart Studio cloud and Chart Studio On-Prem). Prior to plotly.py version 4, This functionality was included in the plotly package under the plotly.plotly module. As part of plotly.py version 4, the Chart Studio functionality was removed from the plotly package and released in this chart-studio package.

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test
# chart-studio was split off into a separate package
# ipywidgets is missing
# skimage

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%{python3_sitelib}/chart_studio/*
%{python3_sitelib}/chart_studio-%{version}-py3*.egg-info/*
