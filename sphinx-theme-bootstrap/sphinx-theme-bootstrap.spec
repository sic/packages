%global summary A sphinx theme that integrates the Bootstrap framework
%global srcname sphinx-theme-bootstrap

Name:           python-%{srcname}
Version:        0.4.5
Release:        2%{?dist}
Summary:        %{summary}

License:        MIT
URL:            http://ryan-roemer.github.com/sphinx-bootstrap-theme/
Source0:        https://pypi.python.org/packages/source/s/sphinx-bootstrap-theme/sphinx-bootstrap-theme-%{version}.tar.gz

BuildArch:      noarch

Requires:       js-jquery1

BuildRequires:  python2-devel
BuildRequires:  python3-devel

%description
This sphinx theme integrates the Booststrap CSS / Javascript framework with various layout options,
hierarchical menu navigation, and mobile-friendly responsive design.  It is configurable, extensible
and can use any number of different Bootswatch CSS themes.


%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python-sphinx
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This sphinx theme integrates the Booststrap CSS / Javascript framework with various layout options,
hierarchical menu navigation, and mobile-friendly responsive design.  It is configurable, extensible
and can use any number of different Bootswatch CSS themes.


%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-sphinx
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This sphinx theme integrates the Booststrap CSS / Javascript framework with various layout options,
hierarchical menu navigation, and mobile-friendly responsive design.  It is configurable, extensible
and can use any number of different Bootswatch CSS themes.

%prep
%autosetup -n sphinx-bootstrap-theme-%{version}

%build
%py2_build
%py3_build


%install
%py2_install
%py3_install
# Remove the bundled JQuery
rm -rf %{buildroot}%{python2_sitelib}/sphinx_bootstrap_theme/bootstrap/static/js/jquery-1.11.0.min.js
rm -rf %{buildroot}%{python3_sitelib}/sphinx_bootstrap_theme/bootstrap/static/js/jquery-1.11.0.min.js
# Now link to the central jquery
ln -sf %{_datadir}/javascript/jquery/1.11.2/jquery.min.js \
%{buildroot}/%{python2_sitelib}/sphinx_bootstrap_theme/bootstrap/static/js/jquery-1.11.0.min.js
ln -sf %{_datadir}/javascript/jquery/1.11.2/jquery.min.js \
%{buildroot}/%{python3_sitelib}/sphinx_bootstrap_theme/bootstrap/static/js/jquery-1.11.0.min.js


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.txt README.rst
%{python2_sitelib}/sphinx_bootstrap_theme/*
%{python2_sitelib}/sphinx_bootstrap_theme-%{version}-py2*.egg-info/*

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.txt README.rst
%{python3_sitelib}/sphinx_bootstrap_theme/*
%{python3_sitelib}/sphinx_bootstrap_theme-%{version}-py3*.egg-info/*


%changelog
* Sat Jun 18 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-2
- Removed bundled JQuery and added links to central version

* Thu Nov 05 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-1
- Initial package for fedora only
