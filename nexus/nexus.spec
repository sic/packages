# Undefine CMake in-source builds in order to be consistent with f33+
%undefine __cmake_in_source_build

Name:           nexus
Version:        4.4.3
Release:        3%{?dist}
Summary:        Libraries and tools for the NeXus scientific data file format

License:        LGPLv2+
URL:            http://www.nexusformat.org/
Source0:        https://github.com/nexusformat/code/archive/v4.4.3.tar.gz
# Fix the version reported by the library
#   (see https://github.com/nexusformat/code/issues/437)
Patch0:         nexus-fix-version.patch
# Remove an additional flag that doesn't work in the EL6 version of gfortran
Patch1:         nexus-el6-fortran-flags.patch
# Back port fix from master branch
Patch2:         nexus-fix-nxtranslate-xml.patch

BuildRequires:  cmake
BuildRequires:	gcc
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  hdf-devel
BuildRequires:  make
BuildRequires:  mxml-devel
BuildRequires:  gcc-gfortran
BuildRequires:  python-docutils

Requires:       hdf5
Requires:       hdf
Requires:       mxml


%description
NeXus is a common data format for neutron, x-ray, and muon science. This
package provides tools and libraries for accessing these files.  The on disk
representation is based upon either HDF4, HDF5 or XML

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hdf5-devel
Requires:       hdf-devel

%description    devel
The %{name}-devel package contains header files for
developing applications that use %{name}


%package        tools
Summary:        Applications for reading and writing NeXus files.
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2
Requires:       readline
BuildRequires:  libxml2-devel
BuildRequires:  readline-devel


%description    tools
%{summary}.


%prep
%setup -q -n code-%{version}
%patch0 -p1 -b .fix-version

%if 0%{?el6}
# Fortran flag not supported on EL6
%patch1 -p1 -b .el6-flags
%endif

%patch2 -p1 -b .nxtranslate

%build
%cmake \
       -DENABLE_HDF5=1 \
       -DENABLE_HDF4=1 \
       -DENABLE_CXX=1 \
       -DENABLE_APPS=1 .
%cmake_build

%install
%cmake_install

%files
%doc %{_datadir}/doc/NeXus/README.doc
%{_datadir}/doc/NeXus/
%{_libdir}/libNeXus*

%files devel
%{_includedir}/nexus/
%{_libdir}/pkgconfig/

%files tools
%{_bindir}/nxbrowse
%{_bindir}/nxconvert
%{_bindir}/nxdir
%{_bindir}/nxsummary
%{_bindir}/nxtranslate
%{_bindir}/nxtraverse
%doc %{_datadir}/doc/NeXus/programs/
%{_mandir}/man1/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sat Aug 02 2020 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-3
- Removed Fortran bindings, added nxtranslate XML fix

* Thu Sep 15 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-2
- Added patch to fix version number

* Mon Sep 12 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.3-1
- Updated to NeXus 4.4.3

* Thu Apr 28 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.1-2
- Updated to ship all the tools libraries.

* Mon Dec 21 2015 Stuart Campbell <sic@fedoraproject.org> - 4.4.1-1
- Updated to nexus 4.4.1

* Mon Nov 30 2015 Stuart Campbell <sic@fedoraproject.org> - 4.4.0-1
- Initial package for fedora
