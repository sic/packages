%define srcname PyCifRW

%define common_summary CIF/STAR file support for Python
%define common_desc PyCIFRW provides support for reading and writing CIF (Crystallographic Information Format) files using Python.

# RHEL doesn't have python 3 and does not know about __python2
%{?!__python2:%global __python2 %{__python}}
%{?!python2_sitelib:%global python2_sitelib %{python_sitelib}}
%{?!python2_version:%global python2_version %{python_version}}

%if 0%{?fedora} >= 13 || 0%{?rhel} >= 8
%global with_py3 1
%endif # 0#{?fedora} >= 13 || 0#{?rhel} >= 8

Name: 		%{srcname}
Version: 	4.4
Release:        1%{?dist}
Summary:        %{common_summary}

License: 	Python 2.0
URL:		https://bitbucket.org/jamesrhester/pycifrw/overview
Source0: 	https://pypi.python.org/packages/4c/ab/b4842d450c06104c3f037c391a1ac5165e677b1226b44bc47a0b9cbc1bd3/%{srcname}-%{version}.tar.gz

%description
%{common_desc}

%package -n python2-%{srcname}
Summary:        %{common_summary}

BuildRequires:  python-setuptools
BuildRequires:  python2-devel

Requires:	python2-numpy

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_desc}



%if 0%{?with_py3}
%package -n python3-%{srcname}
Summary:        %{common_summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-numpy

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}
%endif


%prep
%{__rm} -rf *.egg-info
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%{?with_py3:%py3_build}

%install
%py2_install
%{?with_py3:%py3_install}


%files -n python2-%{srcname}
%license LICENSE
%doc PKG-INFO *.rst
%{python2_sitearch}/CifFile
%{python2_sitearch}/PyCifRW-%{version}-py%{python2_version}.egg-info

%if 0%{?with_py3}
%files -n python3-%{srcname}
%license LICENSE
%doc PKG-INFO *.rst
%{python3_sitearch}/CifFile
%{python3_sitearch}/PyCifRW-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Wed Feb 28 2018 Martyn Gigg <martyn.gigg@stfc.ac.uk> - 4.4-1
- Update version to 4.4

* Wed Feb 01 2017 Stuart Campbell <sic@fedoraproject.org> - 4.2.1-1
- Initial package
