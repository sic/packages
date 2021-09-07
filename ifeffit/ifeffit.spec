Name:           ifeffit
Version:        1.2.13
Release:        2%{?dist}
Summary:        IFEFFIT is an interactive program for XAFS analysis

License:        BSD and GPLv2
URL:            https://cars9.uchicago.edu/ifeffit/
Source0:        https://github.com/newville/ifeffit/archive/refs/tags/1.2.13.tar.gz

# Fix the locations to add the standard library path
Patch0:         iconf_pgplot_fix_pgdirs.patch

BuildRequires:  gcc-gfortran
BuildRequires:  readline-devel
BuildRequires:  make

Requires:       readline

%description
IFEFFIT is an interactive program for XAFS analysis. It combines the high-quality analysis algorithms
of AUTOBK and FEFFIT with graphical display of XAFS data and general data manipulation. IFEFFIT comes
as a command-line program, but the underlying functionality is available as a programming library.
The IFEFFIT library can be used from C, Fortran, Tcl, Perl, and Python. This allows a variety of user
interfaces (both graphical and non-graphical) to be written around IFEFFIT. Currently, three graphical
user interfaces: G.I.FEFFIT, ATHENA/ARTEMIS, and SIXPACK are built on the underlying IFEFFIT library.
IFEFFIT and all three GUIs are under active development, but are fairly well tested and ready for use.

%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING
%doc README
%doc %{_datadir}/ifeffit/README

%{_bindir}/autobk
%{_bindir}/diffkk
%{_bindir}/feff6
%{_bindir}/feffit
%{_bindir}/ifeffit
%{_libdir}/libifeffit.a
%{_libdir}/libnopgplot.a
%{_libdir}/libxafs.a
%{_includedir}/ifeffit.h
%{_datadir}/ifeffit/libifeffit.so
%{_datadir}/ifeffit/cldata/*.dat
%{_datadir}/ifeffit/config/*
%{_datadir}/ifeffit/fefftab/*.dat
%{_datadir}/ifeffit/startup.iff

%changelog
* Tue Sep 07 2021 Stuart Campbell <scampbell@bnl.gov> - 1.2.13-2
- Fixed rpmlint errors

* Sat Apr 10 2021 Stuart Campbell <scampbell@bnl.gov> - 1.2.13-1
- Initial package
