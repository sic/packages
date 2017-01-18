%global srcname sphinx-bootstrap-theme

%global common_sum A sphinx theme that integrates the Bootstrap framework
%global common_desc \
This sphinx theme integrates the Booststrap CSS / Javascript framework \
with various layout options, hierarchical menu navigation, and mobile-friendly \
responsive design.  It is configurable, extensible and can use any number \
of different Bootswatch CSS themes.

# RHEL doesn't have python 3 and does not know about __python2
%{?!__python2:%global __python2 %{__python}}
%{?!python2_sitelib:%global python2_sitelib %{python_sitelib}}
%{?!python2_version:%global python2_version %{python_version}}

%if 0%{?fedora} >= 13 || 0%{?rhel} >= 8
%global with_py3 1
%endif # 0#{?fedora} >= 13 || 0#{?rhel} >= 8

%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%global with_web 1
%endif # 0#{?fedora} >= 21 || 0#{?rhel} >= 7


Name:           python-%{srcname}
Version:        0.4.13
Release:        2%{?dist}
Summary:        %{common_sum}

License:        MIT and ASL 2.0
URL:            http://ryan-roemer.github.com/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?with_web}
BuildRequires:  web-assets-devel
%else
BuildRequires:  epel-rpm-macros
%endif

%description
%{common_desc}


%package -n python2-%{srcname}
Summary:        %{common_sum}

BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%if 0%{?with_web}
Requires:       glyphicons-halflings-fonts
Requires:       js-jquery1
%endif
Requires:       python-sphinx

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_desc}


%if 0%{?with_py3}
%package -n python3-%{srcname}
Summary:        %{common_sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?with_web}
Requires:       glyphicons-halflings-fonts
Requires:       js-jquery1
%endif
Requires:       python3-sphinx

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

# Remove the bundled JQuery and fonts and link against webasset.
%if 0%{?with_web}
for d in %{python2_sitelib} %{?with_py3:%{python3_sitelib}}; do
  %{__rm} -f %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/js/jquery-1.11.0.min.js
  %{__ln_s} -f %{_webassetdir}/jquery/1/jquery.min.js \
    %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/js/jquery-1.11.0.min.js
  %{__rm} -f %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-3.3.6/fonts/glyphicons-halflings-regular.ttf
  %{__ln_s} -f %{_datadir}/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf \
    %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-3.3.6/fonts/glyphicons-halflings-regular.ttf
done
%endif


%files -n python2-%{srcname}
%license LICENSE.txt
%doc PKG-INFO *.rst
%{python2_sitelib}/sphinx_bootstrap_theme
%{python2_sitelib}/sphinx_bootstrap_theme-%{version}-py%{python2_version}.egg-info


%if 0%{?with_py3}
%files -n python3-%{srcname}
%license LICENSE.txt
%doc PKG-INFO *.rst
%{python3_sitelib}/sphinx_bootstrap_theme
%{python3_sitelib}/sphinx_bootstrap_theme-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Mon Jan 16 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.13-1
- Update to latest upstream-release

* Mon Jan 16 2017 Björn Esser <besser82@fedoraproject.org> - 0.4.5-4
- Spec-file optmization

* Thu Nov 17 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-3
- Added check and disable python 3 for el.

* Sat Jun 18 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-2
- Removed bundled JQuery and added links to central version

* Thu Nov 05 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-1
- Initial package for fedora only
