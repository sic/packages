Name:           efl
Version:        1.12.2
Release:        1%{?dist}
Summary:        Foundation libraries for Enlightenment Window Manager

License:        MIT
URL:            http://web.enlightenment.org/p.php?p=about/efl&l=en
Source0:        http://download.enlightenment.org/rel/libs/efl/efl-1.12.2.tar.gz

BuildRequires:  bullet-devel
BuildRequires:  giflib-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel

BuildRequires:  libmount-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXcomposite-devel
BuildRequires:	libXp-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  luajit-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  SDL-devel tslib-devel


Requires:       gstreamer1

%description
The Enlightenment Foundation Libraries (EFL) are a collection of libraries that make up the foundation of the Enlightenment window manager.

%prep
%setup -q -n %{name}-%{version}


%build
%configure			   \
	   --prefix=%{buildroot}   \
           --enable-systemd        \
           --disable-rpath         \
	   --enable-ecore-sdl      \
           --enable-tslib          

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc



%changelog
* Sat Jan 17 2015 Stuart Campbell <stuart@sicampbell.com>
- 
