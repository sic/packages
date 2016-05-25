%global srcname plotly
%global summary Python plotting library for collaborative, interactive, publication-quality graphs.
# RHEL doesn't know about __python2
%{!?__python2: %define __python2 %{__python}}

%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 1.10.0
Release: %{release}%{?dist}
Source0: %{srcname}-%{version}.tar.gz
#Source0: https://pypi.python.org/packages/2a/7f/74aff937097c6fa9938a5d3a3f0f98a387055a60457507be9d60b1c4dc85/plotly-1.10.0.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris P <chris@plot.ly>
Url: https://plot.ly/python/

BuildRequires: python2-devel
BuildRequires: python-ipython
BuildRequires: python3-devel
BuildRequires: python3-ipython


%description
Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.

This source rpm will generate both python2 and python3 libraries.


%package -n python2-%{srcname}
Summary:        %{summary}
Requires:      python
%if 0%{?rhel}
Requires: python-matplotlib
%else
Requires: python2-matplotlib
%endif
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:      python3
Requires: python3-matplotlib
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.


%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python2-%{srcname}
%doc README.rst
%{python2_sitelib}/%{srcname}/*
%{python2_sitelib}/%{srcname}-%{version}-py2*.egg-info/*

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}/*
%{python3_sitelib}/%{srcname}-%{version}-py3*.egg-info/*
