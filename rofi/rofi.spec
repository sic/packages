Name:           rofi
Version:        0.15.12
Release:        1%{?dist}
Summary:        A window switcher, run dialog and dmenu replacement

License:        MIT
URL:            https://davedavenport.github.io/rofi/
Source0:        https://github.com/DaveDavenport/rofi/releases/download/%{version}/rofi-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  i3
BuildRequires:  libX11-devel
BuildRequires:  libXinerama-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  startup-notification-devel

Requires:       cairo
Requires:       libX11
Requires:       pango


%description
A window switcher, run dialog and dmenu replacement

%prep
%setup -qn %{name}-%{version}

%build
./configure --prefix=/usr/
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_mandir}/man1/

%changelog
* Fri Feb  5 2016 Stuart Campbell <sic@fedoraproject.org> - 0.15.12-1
- Initial package
