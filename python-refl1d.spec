%global srcname refl1d
%global summary 1-D reflectometry fitting
%global descr Refl1D is a program for analyzing 1D reflectometry measurements made with X-ray and neutron beamlines. The 1-D models give the depth profile for material scattering density composed of a mixture of flat and continuously varying freeform layers. With polarized neutron measurements, scientists can study the sub-surface structure of magnetic samples. The architecture supports the addition of specialized layer types such as models for the density distribution of polymer brushes, and volume space modeling for proteins in bio-membranes. We provide a number of these models as well as supporting user defined layer types for both structural and magnetic scattering densities.
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 0.8.11
Release: %{release}%{?dist}
Source0: https://github.com/reflectometry/refl1d/archive/v%{version}.tar.gz
License: Public Domain
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
Requires: python%{python3_pkgversion}-bumps >= 0.7.16
Requires: python%{python3_pkgversion}-matplotlib
Requires: python%{python3_pkgversion}-numpy
Requires: python%{python3_pkgversion}-periodictable
Requires: python%{python3_pkgversion}-scipy

BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python%{python3_pkgversion}-bumps >= 0.7.16
BuildRequires: python%{python3_pkgversion}-matplotlib
BuildRequires: python%{python3_pkgversion}-nose
BuildRequires: python%{python3_pkgversion}-numpy
BuildRequires: python%{python3_pkgversion}-periodictable
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
#{python3_sitelib}/*  nothing in sitelib
%{python3_sitearch}/*
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}_cli.py
%{_bindir}/%{srcname}_gui
%{_bindir}/%{srcname}_gui.py
