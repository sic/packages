%global srcname plotly
%global summary Python plotting library for collaborative, interactive, publication-quality graphs.
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: 4.5.4
Release: %{release}%{?dist}
Source0: https://files.pythonhosted.org/packages/67/b1/35bbbfe4c80e4b4f439fe498a42d728e651373bdb6f5a955d75ef358122f/plotly-4.5.4.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris P <chris@plot.ly>
Url: https://plot.ly/python/

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-ipython
BuildRequires: python%{python3_pkgversion}-pytest
BuildRequires: python%{python3_pkgversion}-chart-studio

%description
Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.

This source rpm will generate both python2 and python3 libraries.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:      python3
Requires: python%{python3_pkgversion}-matplotlib
Requires: python%{python3_pkgversion}-pandas
Requires: python%{python3_pkgversion}-chart-studio
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.

%prep
%setup -n %{srcname}-%{version} -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test
# ipywidgets is missing
# skimage is missing

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%{python3_sitelib}/%{srcname}/*
%{python3_sitelib}/%{srcname}-%{version}-py3*.egg-info/*
%{python3_sitelib}/_plotly_future_/*
%{python3_sitelib}/_plotly_utils/*
%{python3_sitelib}/plotlywidget/*
/usr/share/jupyter/nbextensions/plotlywidget/*
/usr/etc/jupyter/nbconfig/notebook.d/plotlywidget.json
