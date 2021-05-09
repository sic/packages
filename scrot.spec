Name:           scrot
Version:        0.10.0
Release:        1%{?dist}
Summary:        Screen-shot capture using Imlib 2

License:        MIT
URL:            https://github.com/dreamer/scrot
Source0:        https://github.com/dreamer/scrot/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  imlib2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel

%description
A nice and straightforward screen capture utility implementing the dynamic
loaders of imlib2.


%prep
%autosetup

%build
meson setup build --prefix=%{buildroot}/%{_prefix}
ninja -C build


%install
ninja -C build install 


%files
%doc README.md AUTHORS ChangeLog
%license COPYING
%{_bindir}/scrot
%{_mandir}/man1/scrot.1.gz

%changelog
* Sat May 08 2021 Stuart Campbell <scampbell@bnl.gov> - 0.10.0-1
- Initial Package
