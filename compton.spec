Name:           compton
Version:        0.1
Release:        1%{?dist}
Summary:        Compositor for X, and a fork of xcompmgr-dana

License:        UNKNOWN
URL:            https://github.com/chjj/compton
Source0:        https://github.com/chjj/compton/archive/v0.1_beta2.tar.gz

BuildRequires:  libconfig-devel

%description
Compton was forked from Dana Jansens fork of xcompmgr and refactored.

%prep
%setup -qn %{name}-%{version}_beta2


%build
make %{?_smp_mflags}
make %{?_smp_mflags} docs

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%{_bindir}/compton
%{_bindir}/compton-trans
%{_mandir}/man1/
%{_datadir}/applications/compton.desktop

%changelog
* Fri Jan  8 2016 Stuart Campbell <sic@fedoraproject.org> - 0.1-1
- Initial package
