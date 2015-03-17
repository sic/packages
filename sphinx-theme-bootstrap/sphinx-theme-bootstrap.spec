Name:           python-sphinx-theme-bootstrap
Version:        0.4.5
Release:        1%{?dist}
Summary:        A sphinx theme integrates the Bootstrap framework

License:        MIT
URL:            http://ryan-roemer.github.com/sphinx-bootstrap-theme/
Source0:        https://pypi.python.org/packages/source/s/sphinx-bootstrap-theme/sphinx-bootstrap-theme-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-sphinx

%description
This sphinx theme integrates the Booststrap CSS / Javascript framework with various layout options, 
hierarchical menu navigation, and mobile-friendly responsive design.  It is configurable, extensible
and can use any number of difference Bootswatch CSS themes.

%prep
%setup -q -n sphinx-bootstrap-theme-%{version}


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE.txt README.txt README.rst
%{python2_sitelib}/*

%changelog
* Tue Jan 13 2015 Stuart Campbell <sic@fedoraproject.org> - 0.4.5-1
- Initial package
