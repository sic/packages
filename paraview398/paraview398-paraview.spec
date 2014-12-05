%{?scl:%scl_package paraview}
%{!?scl:%global pkg_name %{name}}

%ifarch s390 s390x
%global build_openmpi 0
%endif
%{!?build_openmpi:%global build_openmpi 0}
%{!?build_mpich2:%global build_mpich2 0}
%global pv_maj 3
%global pv_min 98
%global pv_patch 1
%global pv_majmin %{pv_maj}.%{pv_min}
%global rcver %{nil}

# %{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           %{?scl_prefix}paraview
Version:        %{pv_majmin}.%{pv_patch}
Release:        4%{?dist}
Summary:        Parallel visualization application

Group:          Applications/Engineering
License:        BSD
URL:            http://www.paraview.org/
Source0:        http://www.paraview.org/files/v%{pv_majmin}/ParaView-%{version}%{?rcver}-source.tar.gz
Source1:        paraview_22x22.png
Source2:        paraview.xml
# Patch to fix install locations
# http://paraview.org/Bug/view.php?id=13704
Patch0:         paraview-install.patch
#Patch to vtk (from vtk package) to use system libraries
Patch1:         vtk-6.0.0-system.patch
# Capitalize Protobuf so it finds FindProtobuf.cmake
Patch2:         paraview-Protobuf.patch
#Patch to vtk to use system netcdf library
Patch3:         vtk-6.0.0-netcdf.patch
# Upstream patch for jpeg_mem_src support
Patch4:         vtk-jpeg.patch
# Patch for glxext.h 
# https://bugzilla.redhat.com/show_bug.cgi?id=1138466
Patch5: vtk-glxext.patch

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: scl-utils-build
#Requires: %scl_require mantidlibs
 
BuildRequires:  cmake
%if %{build_openmpi}
BuildRequires:  openmpi-devel
BuildRequires:  netcdf-devel
#BuildRequires:  netcdf-openmpi-devel
%endif
%if %{build_mpich2}
BuildRequires:  mpich2-devel
BuildRequires:  netcdf-devel
#BuildRequires:  netcdf-mpich2-devel
%endif
BuildRequires:  qt-devel
#BuildRequires:  qt-assistant-adp-devel
BuildRequires:  qt-assistant
BuildRequires:  qt-webkit-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  python-devel, tk-devel, hdf5-devel
BuildRequires:  freetype-devel, libtiff-devel, zlib-devel
BuildRequires:  expat-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen, graphviz
BuildRequires:  readline-devel
BuildRequires:  openssl-devel
BuildRequires:  gnuplot
BuildRequires:  wget
BuildRequires:  boost-devel
BuildRequires:  gl2ps-devel >= 1.3.8
BuildRequires:  hwloc-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libxml2-devel
BuildRequires:  netcdf-devel
#BuildRequires:  netcdf-cxx-devel
BuildRequires:  protobuf-devel
Requires:       hdf5 = %{_hdf5_version}
Requires:       %{?scl_prefix}%{pkg_name}-data = %{version}-%{release}
Requires:       %{?scl_prefix}%{pkg_name}-doc = %{version}-%{release}
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes:      %{?scl_prefix}paraview-demos < %{version}-%{release}
Provides:       %{?scl_prefix}paraview-demos = %{version}-%{release}
Obsoletes:      %{?scl_prefix}paraview-doc < %{version}-%{release}
Provides:       %{?scl_prefix}paraview-doc = %{version}-%{release}

%{?scl:Requires: %scl_runtime}

#-- Plugin: VRPlugin - Virtual Reality Devices and Interactor styles : Disabled - Requires VRPN
#-- Plugin: MantaView - Manta Ray-Cast View : Disabled - Requires Manta
#-- Plugin: ForceTime - Override time requests : Disabled - Build is failing
#-- Plugin: VaporPlugin - Plugin to read NCAR VDR files : Disabled - Requires vapor
%define paraview_cmake_options \\\
        -DCMAKE_INSTALL_PREFIX=%{_scl_root}/usr \\\
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
        -DCMAKE_CXX_COMPILER:FILEPATH=$CXX \\\
        -DCMAKE_C_COMPILER:FILEPATH=$CC \\\
        -DTCL_LIBRARY:PATH=tcl \\\
        -DTK_LIBRARY:PATH=tk \\\
        -DPARAVIEW_INSTALL_DEVELOPMENT:BOOL=ON \\\
        -DVTK_CUSTOM_LIBRARY_SUFFIX="" \\\
        -DVTK_INSTALL_PACKAGE_DIR=share/cmake/paraview \\\
        -DVTK_USE_BOOST:BOOL=ON \\\
        -DVTK_USE_INFOVIS:BOOL=OFF \\\
        -DVTK_USE_N_WAY_ARRAYS:BOOL=ON \\\
        -DVTK_USE_OGGTHEORA_ENCODER:BOOL=ON \\\
        -DVTK_USE_SYSTEM_ICET=OFF \\\
        -DVTK_USE_SYSTEM_LIBRARIES=ON \\\
        -DVTK_USE_SYSTEM_HDF5=ON \\\
        -DHDF5_HL_LIBRARY:FILEPATH=%{_libdir}/libhdf5_hl.so \\\
        -DVTK_USE_SYSTEM_LIBPROJ4=OFF \\\
        -DVTK_USE_SYSTEM_NETCDF=ON \\\
        -DVTK_USE_SYSTEM_QTTESTING=OFF \\\
        -DVTK_USE_SYSTEM_XDMF2=OFF \\\
        -DXDMF_WRAP_PYTHON:BOOL=ON \\\
        -DBUILD_DOCUMENTATION:BOOL=ON \\\
        -DBUILD_EXAMPLES:BOOL=ON 


%description
ParaView is an application designed with the need to visualize large data
sets in mind. The goals of the ParaView project include the following:

    * Develop an open-source, multi-platform visualization application.
    * Support distributed computation models to process large data sets.
    * Create an open, flexible, and intuitive user interface.
    * Develop an extensible architecture based on open standards.

ParaView runs on distributed and shared memory parallel as well as single
processor systems and has been successfully tested on Windows, Linux and
various Unix workstations and clusters. Under the hood, ParaView uses the
Visualization Toolkit as the data processing and rendering engine and has a
user interface written using a unique blend of Tcl/Tk and C++.

NOTE: The version in this package has NOT been compiled with MPI support.
%if %{build_openmpi}
Install the paraview-openmpi package to get a version compiled with openmpi.
%endif
%if %{build_mpich2}
Install the paraview-mpich2 package to get a version compiled with mpich2.
%endif

%package        data
Summary:        Data files for ParaView
Group:          Applications/Engineering
Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch:      noarch

%description    data
%{summary}.

%package        devel
Summary:        Development files for %{pkg_name}
Group:          Development/Libraries
Requires:       %{?scl_prefix}%{pkg_name}%{?_isa} = %{version}-%{release}

%description    devel
The %{pkg_name}-devel package contains libraries and header files for
developing applications that use %{pkg_name}.

%package        doc
Summary:        Documentation files for ParaView
Group:          Applications/Engineering
Requires:       %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
%{summary}.


%if %{build_openmpi}

%package        openmpi
Summary:        Parallel visualization application
Group:          Applications/Engineering
Requires:       %{?scl_prefix}%{pkg_name}-data = %{version}-%{release}
Requires:       openmpi
Obsoletes:      %{?scl_prefix}%{pkg_name}-mpi < %{version}-%{release}
Provides:       %{?scl_prefix}%{pkg_name}-mpi = %{version}-%{release}

%description    openmpi
This package contains copies of the ParaView server binaries compiled with
OpenMPI.  These are named pvserver_openmpi, pvbatch_openmpi, etc.

You will need to load the openmpi-%{_arch} module to setup your path properly.

%package        openmpi-devel
Summary:        Development files for %{pkg_name}-openmpi
Group:          Development/Libraries
Requires:       %{?scl_prefix}%{pkg_name}-openmpi%{?_isa} = %{version}-%{release}

%description    openmpi-devel
The %{pkg_name}-openmpi-devel package contains libraries and header files for
developing applications that use %{pkg_name}-openmpi.
%endif

%if %{build_mpich2}

%package        mpich2
Summary:        Parallel visualization application
Group:          Applications/Engineering
Requires:       %{?scl_prefix}%{pkg_name}-data = %{version}-%{release}
Requires:       mpich2

%description    mpich2
This package contains copies of the ParaView server binaries compiled with
mpich2.  These are named pvserver_mpich2, pvbatch_mpich2, etc.

You will need to load the mpich2-%{_arch} module to setup your path properly.

%package        mpich2-devel
Summary:        Development files for %{pkg_name}-mpich2
Group:          Development/Libraries
Requires:       %{?scl_prefix}%{pkg_name}-mpich2%{?_isa} = %{version}-%{release}

%description    mpich2-devel
The %{pkg_name}-mpich2-devel package contains libraries and header files for
developing applications that use %{pkg_name}-mpich2.
%endif

%prep
%setup -q -n ParaView-%{version}-source
%patch0 -p1 -b .install
%patch1 -p0 -b .system
%patch2 -p1 -b .Protobuf
%patch3 -p0 -b .netcdf
%patch4 -p0 -b .jpeg
%patch5 -p0 -b .glxext
#Remove included thirdparty sources just to be sure
#for x in protobuf
#do
#  rm -r ThirdParty/${x}/vtk${x}
#done
#for x in expat freetype hdf5 jpeg libxml2 netcdf oggtheora png sqlite tiff zlib
#do
#  rm -r VTK/ThirdParty/${x}/vtk${x}
#done

%build
export CC='gcc'
export CXX='g++'
export MAKE='make'
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
mkdir fedora
pushd fedora
cmake .. \
        -DVTK_INSTALL_INCLUDE_DIR:PATH=include/paraview \
        -DVTK_INSTALL_ARCHIVE_DIR:PATH=%{_lib}/paraview \
        -DVTK_INSTALL_LIBRARY_DIR:PATH=%{_lib}/paraview \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
        %{paraview_cmake_options}
make VERBOSE=1 %{?_smp_mflags}
popd

%if %{build_openmpi}
mkdir fedora-openmpi
pushd fedora-openmpi
%{_openmpi_load}
cmake .. \
        -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/openmpi \
        -DVTK_INSTALL_INCLUDE_DIR:PATH=include/paraview \
        -DVTK_INSTALL_ARCHIVE_DIR:PATH=lib/paraview \
        -DVTK_INSTALL_LIBRARY_DIR:PATH=lib/paraview \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
        -DPARAVIEW_USE_MPI:BOOL=ON \
        -DICET_BUILD_TESTING:BOOL=ON \
        -DMPI_COMPILER:FILEPATH=%{_libdir}/openmpi/bin/mpicxx \
        %{paraview_cmake_options}
# Fixup forward paths
sed -i -e 's,../%{_lib}/openmpi,..,' `find -name \*-forward.c`
make VERBOSE=1 %{?_smp_mflags}
%{_openmpi_unload}
popd
%endif
%if %{build_mpich2}
mkdir fedora-mpich2
pushd fedora-mpich2
%{_mpich2_load}
cmake .. \
        -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/mpich2 \
        -DVTK_INSTALL_INCLUDE_DIR:PATH=include/paraview \
        -DVTK_INSTALL_ARCHIVE_DIR:PATH=lib/paraview \
        -DVTK_INSTALL_LIBRARY_DIR:PATH=lib/paraview \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
        -DPARAVIEW_USE_MPI:BOOL=ON \
        -DICET_BUILD_TESTING:BOOL=ON \
        -DMPI_COMPILER:FILEPATH=%{_libdir}/mpich2/bin/mpicxx \
        %{paraview_cmake_options}
# Fixup forward paths
sed -i -e 's,../%{_lib}/mpich2,..,' `find -name \*-forward.c`
#make VERBOSE=1 %{?_smp_mflags}
make %{?_smp_mflags}
%{_mpich2_unload}
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT

#Fix permissions
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -print0 | xargs -0 chmod -x

# Create some needed directories
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m644 %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages
install -m644 %SOURCE2 $RPM_BUILD_ROOT%{_datadir}/mime/packages

%if %{build_openmpi}
# Install openmpi version
pushd fedora-openmpi
make install DESTDIR=$RPM_BUILD_ROOT

#Remove mpi copy of doc and man pages
rm -rf $RPM_BUILD_ROOT%{_libdir}/openmpi/share/{doc,man}
popd
%endif

%if %{build_mpich2}
# Install mpich2 version
pushd fedora-mpich2
make install DESTDIR=$RPM_BUILD_ROOT

#Remove mpi copy of doc and man pages
rm -rf $RPM_BUILD_ROOT%{_libdir}/mpich2/share/{doc,man}
popd
%endif

#Install the normal version
pushd fedora
make install DESTDIR=$RPM_BUILD_ROOT

#Create desktop file
cat > paraview.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=ParaView Viewer
GenericName=Data Viewer
Comment=ParaView allows viewing of large data sets
Type=Application
Terminal=false
Icon=paraview_22x22
MimeType=application/x-paraview;
Categories=Application;Graphics;
Exec=paraview
EOF

desktop-file-install --vendor=fedora \
       --add-category=X-Fedora \
       --dir %{buildroot}%{_datadir}/applications/ \
       paraview.desktop

#Cleanup only vtk conflicting binaries
rm $RPM_BUILD_ROOT%{_bindir}/vtk{EncodeString,ParseJava,Wrap{Hierarchy,Java,Python,Tcl}}*

#Remove cmake files
#rm -rf $RPM_BUILD_ROOT%{libdir}/cmake/

popd

# Strip build dir from VTKConfig.cmake (bug #917425)
find $RPM_BUILD_ROOT -name VTKConfig.cmake | xargs sed -i -e '/builddir/s/^/#/'

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
update-desktop-database &> /dev/null ||:


%postun
/sbin/ldconfig
update-desktop-database &> /dev/null ||:


#Handle changing from directory to file
%pre
if [ -d %{_libdir}/paraview/paraview ]
then
  rm -r %{_libdir}/paraview/paraview
fi


%post   data
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun data
update-mime-database %{_datadir}/mime &> /dev/null || :

%files
%doc License_v1.2.txt
%{_bindir}/paraview
#%{_bindir}/pvbatch
#%{_bindir}/pvblot
%{_bindir}/pvdataserver
#%{_bindir}/pvpython
%{_bindir}/pvrenderserver
%{_bindir}/pvserver
%{_bindir}/smTestDriver
%{_libdir}/paraview/

%files data
%{_datadir}/applications/fedora-paraview.desktop
%{_datadir}/pixmaps/paraview_22x22.png
%{_datadir}/mime/packages/paraview.xml

%files devel
%{_bindir}/vtk*
%{_includedir}/paraview/
# we will probably need this line for the -devel to work properly
#%{_scl_root}/usr/lib/cmake/
%{_datadir}/doc/paraview-%{pv_majmin}/


%if %{build_openmpi}

%files openmpi
%doc License_v1.2.txt
%{_libdir}/openmpi/bin/[ps]*
%{_libdir}/openmpi/lib/paraview/

%files openmpi-devel
%{_libdir}/openmpi/bin/vtk*
%{_libdir}/openmpi/include/paraview/
%{_libdir}/openmpi/share/cmake/
%endif


%if %{build_mpich2}

%files mpich2
%doc License_v1.2.txt
%{_libdir}/mpich2/bin/[ps]*
%{_libdir}/mpich2/lib/paraview/

%files mpich2-devel
%{_libdir}/mpich2/bin/vtk*
%{_libdir}/mpich2/include/paraview/
%{_libdir}/mpich2/share/cmake/
%endif

%changelog
* Thu Mar 7 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-3
- Remove builddir path from VTKConfig.cmake (bug #917425)

* Sun Feb 24 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-2
- Remove only vtk conflicting binaries (bug #915116)
- Do not move python libraries

* Wed Feb 20 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.1-1
- Update to 3.98.1
- Drop pvblot patch
- Add upstream patch to fix jpeg_mem_src support

* Mon Jan 28 2013 Orion Poplawski <orion@cora.nwra.com> - 3.98.0-3
- Drop kwProcessXML patch, leave as vtkkwProcessXML with rpath

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.98.0-2
- rebuild due to "jpeg8-ABI" feature drop

* Mon Dec 17 2012 Orion Poplawski <orion@cora.nwra.com> - 3.98.0-1
- Update to 3.98.0
- Remove source of more bundled libraries
- Drop include, gcc47, vtkboost, and hdf5 patches
- Rebase kwprocessxml_rpath and system library patches
- Add patch to fix install locations
- Add patch to use system protobuf
- Add BR gl2ps-devel >= 1.3.8
- Disable pvblot for now
- Build with hdf5 1.8.10

* Thu Nov 1 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-5
- Rebuild for mpich2 1.5
- Add patch to compile with current boost

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-3
- Don't ship vtkWrapHierarchy, conflicts with vtk (Bug 831834)

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-2
- Rebuild with hdf5 1.8.9

* Mon Apr 9 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.1-1
- Update to 3.14.1
- Add BR hwloc-devel

* Tue Apr 3 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-4
- Add patch to buid kwProcessXML as a forwarded executable (bug #808490)

* Thu Mar 29 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-3
- Only remove vtk conflicting binaries (bug #807756)

* Wed Feb 29 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-2
- Add patch to make vtk use system libraries

* Wed Feb 29 2012 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-1
- Update to 3.14.0
- Rebase gcc47 patch
- Try to handle python install problems manually

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-8
- Rebuilt for c++ ABI breakage

* Thu Jan 26 2012 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-7
- Build with gcc 4.7
- Add patch to support gcc 4.7
- Build with new libOSMesa

* Tue Dec 27 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-6
- vtkPV*Python.so needs to go into the paraview python dir
- Drop chrpath

* Fri Dec 16 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-5
- Oops, install vtk*Python.so, not libvtk*Python.so

* Mon Dec 12 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-4
- Install more libvtk libraries by hand and manually remove rpath

* Fri Dec 9 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-3
- Add patch from Petr Machata to build with boost 1.48.0

* Thu Dec 1 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-2
- Enable PARAVIEW_INSTALL_DEVELOPMENT and re-add -devel sub-package
- Install libvtk*Python.so by hand for now

* Thu Nov 10 2011 Orion Poplawski <orion@cora.nwra.com> - 3.12.0-1
- Update to 3.12.0

* Fri Oct 28 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-6
- Fixup forward paths for mpi versions (bug #748221)

* Thu Jun 23 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-5
- Add BR qtwebkit-devel, fixes FTBS bug 716151

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-4
- Rebuild for hdf5 1.8.7

* Tue Apr 19 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-3
- No need to move python install with 3.10.1

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 3.10.1-2
- no openmpi on s390(x)

* Mon Apr 18 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.1-1
- Update to 3.10.1
- Drop build patch fixed upstream

* Mon Apr 4 2011 Orion Poplawski <orion@cora.nwra.com> - 3.10.0-1
- Update to 3.10.0
- Drop lib and py27 patches fixed upstream
- Add patch for gcc 4.6.0 support
- Update system hdf5 handling
- Cleanup unused build options
- Build more plugins

* Tue Mar 29 2011 Deji Akingunola <dakingun@gmail.com> - 3.8.1-5
- Rebuild for mpich2 soname bump

* Wed Oct 20 2010 Adam Jackson <ajax@redhat.com> 3.8.1-4
- Rebuild for new libOSMesa soname

* Thu Oct 7 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.1-3
- Remove any previous %%{_libdir}/paraview/paraview directories
  which prevent updates

* Tue Oct 5 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.1-2
- Disable install of third party libraries

* Fri Oct 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.1-1
- Update to 3.8.1
- Drop devel sub-package
- Drop installpath patch
- Drop hdf5-1.8 patch, build with hdf5 1.8 API
- Cleanup build

* Fri Jul 30 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-4
- Add patch to support python 2.7

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jun 4 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-2
- Drop doc sub-package

* Tue Jun 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-1
- Update to 3.8.0
- Update demo patch
- Update hdf5 patch
- Drop old documentation patches
- Add patch to add needed include headers
- Add patch from upstream to fix install path issue

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.6.2-4
- BR qt-assistant-adp-devel
- Don't Require qt4-assistant, should be qt-assistant-adp now, and it (or qt-x11
  4.6.x which Provides it) gets dragged in anyway by the soname dependencies

* Fri Feb 19 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-3
- More MPI packaging changes

* Tue Feb 16 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-2
- Conform to updated MPI packaging guidelines
- Build mpich2 version

* Mon Jan 4 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-1
- Update to 3.6.2

* Thu Nov 19 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-7
- New location for openmpi (fixes FTBFS bug #539179)

* Mon Aug 31 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-6
- Don't ship lproj, conflicts with vtk

* Thu Aug 27 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-5
- Specify PV_INSTALL_LIB_DIR as relative path, drop install prefix patch
- Update assitant patch to use assistant_adp, don't ship assistant-real

* Wed Aug 26 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-4
- Disable building various plugins that need OverView

* Tue Aug 25 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-3
- Disable building OverView - not ready yet

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.6.1-2
- rebuilt with new openssl

* Wed Jul 22 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-1
- Update to 3.6.1

* Thu May 7 2009 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-5
- Update doc patch to look for help file in the right place (bug #499273)

* Tue Feb 24 2009 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-4
- Rebuild with hdf5 1.8.2, gcc 4.4.0
- Update hdf5-1.8 patch to work with hdf5 1.8.2
- Add patch to allow build with Qt 4.5
- Move documentation into noarch sub-package

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 3.4.0-3
- rebuild with new openssl

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.4.0-2
- Rebuild for Python 2.6

* Fri Oct 17 2008 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-1
- Update to 3.4.0 final

* Thu Oct 2 2008 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-0.20081002.1
- Update 3.4.0 CVS snapshot
- Update gcc43 patch
- Drop qt patch, upstream now allows compiling against Qt 4.4.*

* Mon Aug 11 2008 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-0.20080811.1
- Update 3.3.1 CVS snapshot
- Update hdf5 patch to drop upstreamed changes
- Fix mpi build (bug #450598)
- Use rpath instead of ls.so conf files so mpi and non-mpi can be installed at
  the same time
- mpi package now just ships mpi versions of the server components
- Drop useless mpi-devel subpackage
- Update hdf5 patch to fix H5pubconf.h -> H5public.h usage

* Wed May 21 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.20080520.1
- Update to 3.3.0 CVS snapshot
- Update qt and gcc43 patches, drop unneeded patches
- Add openssl-devel, gnuplot, and wget BRs
- Update license text filename
- Set VTK_USE_RPATH to off, needed with development versions
- Run ctest in %%check - still need to exclude more tests

* Wed Mar 5 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-5
- Rebuild for hdf5 1.8.0 using compatability API define and new patch

* Mon Feb 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Add patch to compile with gcc 4.3

* Fri Jan 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-3
- Add patch to fix parallel make
- Obsolete demos package (bug #428528)

* Tue Dec 18 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-2
- Name ld.so.conf.d file with .conf extension
- Drop parallel make for now

* Mon Dec 03 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-1
- Update to 3.2.1
- Use macros for version numbers
- Add patches to fix documentation install location and use assistant-qt4,
  not install copies of Qt libraries, and not use rpath.
- Install ld.so.conf.d file
- Fixup desktop files

* Thu Aug 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.0.2-2
- Update license tag to BSD
- Fix make %%{_smp_mflags}
- Rebuild for ppc32

* Wed Jul 11 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.0.2-1
- Update to 3.0.2
- Turn mpi build back on
- Add devel packages
- Remove demo package no longer in upstream
- Use cmake macros

* Thu Mar 08 2007 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-6
- Don't build mpi version until upstream fixes the build system

* Fri Dec 22 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-5
- Fix .so permissions
- Patch for const issue
- Patch for new cmake
- Build with openmpi

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 2.4.4-4
- Bump and build for python 2.5

* Fri Oct  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-3
- Install needed python libraries to get around make install bug

* Wed Oct  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-2
- Re-enable OSMESA support for FC6
- Enable python wrapping

* Fri Sep 15 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
- Update to 2.4.4

* Thu Jun 29 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-8
- No OSMesa support in FC5
- Make data sub-package pull in main package (bug #193837)
- A patch from CVS to fix vtkXOpenRenderWindow.cxx
- Need lam-devel for FC6

* Fri Apr 21 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-7
- Re-enable ppc

* Mon Apr 17 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-6
- Exclude ppc due to gcc bug #189160

* Wed Apr 12 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-5
- Cleanup permissions

* Mon Apr 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-4
- Add icon and cleanup desktop file

* Mon Apr 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-3
- Add VTK_USE_MANGLE_MESA for off screen rendering
- Cleanup source permisions
- Add an initial .desktop file
- Make requirement on -data specific to version
- Don't package Ice-T man pages and cmake files

* Thu Apr  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-2
- Add mpi version

* Tue Apr  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-1
- Initial Fedora Extras version
