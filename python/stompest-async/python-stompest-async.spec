%global summary Stompest is a full-featured STOMP 1.0, 1.1, and 1.2 implementation for Python
%global srcname stompest-async

Name:           python-stompest-async
Version:        2.1.6
Release:        1%{?dist}
Summary:        %{summary}

License:        Apache
URL:            https://github.com/nikipore/stompest
Source0:        https://pypi.python.org/packages/source/s/stompest.async/stompest.async-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel

%description
This package provides the asynchronous STOMP client based upon the stompest library. It leverages 
the power of Twisted, a very mature and powerful asynchronous programming framework. The client 
supports destination specific message and error handlers (with default “poison pill” error handling), 
concurrent message processing, graceful shutdown, and connect, receipt, and disconnect timeouts.


%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python-sphinx
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This package provides the asynchronous STOMP client based upon the stompest library. It leverages 
the power of Twisted, a very mature and powerful asynchronous programming framework. The client 
supports destination specific message and error handlers (with default “poison pill” error handling), 
concurrent message processing, graceful shutdown, and connect, receipt, and disconnect timeouts.


%prep
%autosetup -n stompest.async-%{version}

%build
python setup.py build


%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files -n python2-%{srcname}
%{python_sitelib}/stompest/
%{python_sitelib}/stompest.async*


%changelog
* Tue Jun 28 2016 Stuart Campbell <sic@fedoraproject.org> - 2.1.6-1
- Initial package 
