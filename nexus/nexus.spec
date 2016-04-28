Name:           nexus
Version:        4.4.1
Release:        2%{?dist}
Summary:        NeXus scientific data file format

License:        LGPL
URL:            http://www.nexusformat.org/
Source0:        https://github.com/nexusformat/code/archive/code-issue_414.zip
# Actually install libraries for NXtranslate program
Patch0:         nexus-nxtranslate-binary.patch
Patch1:         nexus-nxtranslate-edf.patch
Patch2:         nexus-nxtranslate-frm2.patch
Patch3:         nexus-nxtranslate-loopy.patch
Patch4:         nexus-nxtranslate-snshisto.patch
Patch5:         nexus-nxtranslate-spec.patch
Patch6:         nexus-nxtranslate-text.patch


BuildRequires:  cmake
BuildRequires:  hdf5-devel
BuildRequires:  hdf-devel
BuildRequires:  mxml-devel
BuildRequires:  gcc-gfortran
BuildRequires:  python-docutils


Requires:       libgfortran
Requires:       hdf5
Requires:       hdf
Requires:       mxml


%description
NeXus is a common data format for neutron, x-ray, and muon science. It is
being developed as an international standard by scientists and programmers
representing major scientific facilities in Europe, Asia, Australia, and
North America in order to facilitate greater cooperation in the analysis and
visualization of neutron, x-ray, and muon data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Requires:       hdf5-devel
Requires:       hdf-devel
Requires:       mxml-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        Applications for reading and writing NeXus files.
Requires:       %{name} = %{version}-%{release}
Requires:       libxml2
Requires:       readline
BuildRequires:  libxml2-devel
BuildRequires:  readline-devel


%description    tools
%{summary}.



%prep
#%setup -q -n code-%{version}
%setup -q -n code-issue_414
%patch0 -p1 -b .NXtranslate-binary
%patch1 -p1 -b .NXtranslate-edf
%patch2 -p1 -b .NXtranslate-frm2
%patch3 -p1 -b .NXtranslate-loopy
%patch4 -p1 -b .NXtranslate-snshisto
%patch5 -p1 -b .NXtranslate-spec
%patch6 -p1 -b .NXtranslate-text


%build
%cmake \
       -DENABLE_HDF5=1 \
       -DENABLE_HDF4=1 \
       -DENABLE_MXML=1 \
       -DENABLE_CXX=1 \
       -DENABLE_FORTRAN77=1 \
       -DENABLE_FORTRAN90=1 \
       -DENABLE_JAVA=0 \
       -DENABLE_APPS=1
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc %{_datadir}/doc/NeXus/README.doc
%{_libdir}/libNeXus*
%{_libdir}/nexus/

%files devel
%{_includedir}/nexus/
%{_libdir}/pkgconfig/

%files tools
%{_bindir}/nxbrowse
%{_bindir}/nxconvert
%{_bindir}/nxdir
%{_bindir}/nxdump
%{_bindir}/nxingest
%{_bindir}/nxsummary
%{_bindir}/nxtranslate
%{_bindir}/nxtraverse
%{_libdir}/libBinaryRetriever.so
%{_libdir}/libEdf.so
%{_libdir}/libFRM2.so
%{_libdir}/libLoopy.so
%{_libdir}/libSNShistogram.so
%{_libdir}/libSpec.so
%{_libdir}/libTextCollist.so
%{_libdir}/libTextPlain.so
%{_libdir}/libTextXML.so
%doc %{_datadir}/doc/NeXus/programs/
%{_mandir}/man1/

%changelog
* Thu Apr 28 2016 Stuart Campbell <sic@fedoraproject.org> - 4.4.1-2
- Updated to ship all the tools libraries.

* Mon Dec 21 2015 Stuart Campbell <sic@fedoraproject.org> - 4.4.1-1
- Updated to nexus 4.4.1

* Mon Nov 30 2015 Stuart Campbell <sic@fedoraproject.org> - 4.4.0-1
- Initial package for fedora
