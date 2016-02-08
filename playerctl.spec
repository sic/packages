Name:           playerctl
Version:        0.4.2
Release:        1%{?dist}
Summary:        Command-line controller and library for music players

License:        LGPL
URL:            https://github.com/acrisci/playerctl
Source0:        https://github.com/acrisci/playerctl/archive/v0.4.2.tar.gz

BuildRequires:       gtk-doc

%description
Playerctl is a command-line utility and library for controlling media players
that implement the MPRIS D-Bus Interface Specification. Playerctl makes it
easy to bind player actions, such as play and pause, to media keys.

%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr
# Do not build with the -j flag as it causes the build to fail
make


%install
%make_install
# make sure files are in the correct libdir for the arch
# by default this programs puts everything in /usr/lib
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/usr/lib/libplayerctl* %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}/usr/lib/pkgconfig/playerctl*.pc \
   %{buildroot}%{_libdir}/pkgconfig/
mkdir -p  %{buildroot}%{_libdir}/girepository-1.0
mv %{buildroot}/usr/lib/girepository-1.0/Playerctl* \
   %{buildroot}%{_libdir}/girepository-1.0/


%files
%{_bindir}/playerctl
%{_includedir}/playerctl/
%{_libdir}/libplayerctl*
%{_libdir}/girepository-1.0/Playerctl*
%{_libdir}/pkgconfig/playerctl-1.0.pc
%{_datadir}/gir-1.0/Playerctl*
%doc

%changelog
* Fri Feb  5 2016 Stuart Campbell <sic@fedoraproject.org> - 0.4.2-1
- Initial package
