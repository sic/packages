%global __provides_exclude_from	%{_datadir}/doc/.*
%global __requires_exclude_from	%{_datadir}/doc/.*
%define _exclude_files_from_autoprov    %{python2_sitearch}/.*\\.so\\|%{python3_sitearch}/.*\\.so
%global basepy3dir              %(echo ../`basename %{py3dir}`)
%global with_html               0
%global run_tests               0

# the default backend; one of GTK GTKAgg GTKCairo GTK3Agg GTK3Cairo
# CocoaAgg MacOSX Qt4Agg Qt5Agg TkAgg WX WXAgg Agg Cairo GDK PS PDF SVG
%global backend                 TkAgg

%if "%{backend}" == "TkAgg"
%global backend_subpackage tk
%else
%  if "%{backend}" == "Qt4Agg"
%global backend_subpackage qt4
%  else
%    if "%{backend}" == "Qt5Agg"
%global backend_subpackage qt5
%    endif
%  endif
%endif

%global with_bundled_fonts      1

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Name:           python-matplotlib
Version:        1.5.1
Release:        1
Summary:        Python 2D plotting library
Group:          Development/Python
# qt4_editor backend is MIT
License:        Python and MIT
URL:            http://matplotlib.org
#Modified Sources to remove the bundled libraries
Source0:        matplotlib-%{version}-without-extern.tar.xz
Source1:        setup.cfg

#Patch0:         %{name}-noagg.patch
Patch2:         20_matplotlibrc_path_search_fix.patch
Patch5:         70_bts720549_try_StayPuft_for_xkcd.patch

BuildRequires:  freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  qhull-devel
BuildRequires:  pythonegg(2)(six)
BuildRequires:  pythonegg(2)(numpy)
BuildRequires:  python-numpy-devel
BuildRequires:  pythonegg(2)(pyparsing)
BuildRequires:  pythonegg(2)(cxx)
BuildRequires:  pythonegg(2)(python-dateutil)
BuildRequires:  pythonegg(2)(setuptools)
BuildRequires:  pythonegg(2)(pillow)
%if %{with_html}
BuildRequires:  ipython2
BuildRequires:  pythonegg(2)(sphinx)
BuildRequires:  pythonegg(2)(numpydoc)
BuildRequires:  pythonegg(2)(scikit-image)
BuildRequires:  pythonegg(2)(cycler)
%endif
%if %{run_tests}
BuildRequires:  pythonegg(2)(nose)
BuildRequires:  pythonegg(3)(nose)
%endif
BuildRequires:  python2-devel
BuildRequires:  pythonegg(2)(pytz)
BuildRequires:  x11-server-xvfb
BuildRequires:  zlib-devel

Provides:       bundled(agg) = 2.4
Provides:       bundled(ttconv)

Requires:       fonts-ttf-dejavu
Requires:       pythonegg(2)(six)
Requires:       pythonegg(2)(numpy)
Requires:       pythonegg(2)(pyparsing)
Requires:       pythonegg(2)(cycler)
Requires:       pythonegg(2)(python-dateutil)
Requires:       pythonegg(2)(pytz)
Requires:       pythonegg(2)(pillow)
Requires:       font(stixmath)
Requires:       %{name}-data = %{version}-%{release}


%description
Matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell, web application servers, and
six graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible.
You can generate plots, histograms, power spectra, bar charts,
errorcharts, scatterplots, etc, with just a few lines of code.


%package -n python-matplotlib-qt4
%{?python_provide:%python_provide python-matplotlib-qt4}
Summary:        Qt4 backend for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
Requires:       python-matplotlib-qt5
BuildRequires:  python-qt4-devel
Requires:       python-qt4

%description -n python-matplotlib-qt4
%{summary}


%package -n python-matplotlib-qt5
%{?python_provide:%python_provide python-matplotlib-qt5}
Summary:        Qt5 backend for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
BuildRequires:  python-qt5
Requires:       python-qt5

%description -n python-matplotlib-qt5
%{summary}


%package -n python-matplotlib-gtk
%{?python_provide:%python_provide python-matplotlib-gtk}
Summary:        GTK backend for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
BuildRequires:  gtk2-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  pycairo-devel
Requires:       pycairo
Requires:       pygtk2.0

%description -n python-matplotlib-gtk
%{summary}


%package -n python-matplotlib-wx
%{?python_provide:%python_provide python-matplotlib-wx}
Summary:        wxPython backend for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
BuildRequires:  libwxPythonGTK-devel
Requires:       wxPython

%description -n python-matplotlib-wx
%{summary}


%package -n python-matplotlib-gtk3
%{?python_provide:%python_provide python-matplotlib-gtk3}
Summary:        GTK3 backend for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
# This should be converted to typelib(Gtk) when supported
BuildRequires:  gtk+3.0
Requires:       gtk+3.0%{?_isa}

%description -n python-matplotlib-gtk3
%{summary}


%package -n python-matplotlib-tk
%{?python_provide:%python_provide python-matplotlib-tk}
Summary:        Tk backend for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
BuildRequires:  tcl-devel
BuildRequires:  tkinter
BuildRequires:  tk-devel
Requires:       tkinter

%description -n python-matplotlib-tk
%{summary}


%package -n python-matplotlib-doc
%{?python_provide:%python_provide python-matplotlib-doc}
Summary:        Documentation files for python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib%{?_isa} = %{version}-%{release}
%if %{with_html}
BuildRequires:  ipython3
BuildRequires:  python-sphinx
BuildRequires:  latex
BuildRequires:  graphviz
%endif

%description -n python-matplotlib-doc
%{summary}


%package -n python-matplotlib-data
%{?python_provide:%python_provide python-matplotlib-data}
Summary:        Data used by python-matplotlib
Group:          Development/Python
%if %{with_bundled_fonts}
Requires:       python-matplotlib-data-fonts = %{version}-%{release}
%endif
BuildArch:      noarch

%description -n python-matplotlib-data
%{summary}


%if %{with_bundled_fonts}
%package -n python-matplotlib-data-fonts
%{?python_provide:%python_provide python-matplotlib-data-fonts}
Summary:        Fonts used by python-matplotlib
Group:          Development/Python
Requires:       python-matplotlib-data = %{version}-%{release}
BuildArch:      noarch

%description -n python-matplotlib-data-fonts
%{summary}
%endif


%package -n     python3-matplotlib
%{?python_provide:%python_provide python3-matplotlib}
Summary:        Python 2D plotting library
Group:          Development/Python
BuildRequires:  pythonegg(3)(pycairo) 
BuildRequires:  pythonegg(3)(python-dateutil)
BuildRequires:  python3-devel
BuildRequires:  pythonegg(3)(setuptools)
BuildRequires:  pythonegg(3)(pygobject)
BuildRequires:  pythonegg(3)(numpy)
BuildRequires:  python3-numpy-devel
BuildRequires:  pythonegg(3)(cxx)
BuildRequires:  pythonegg(3)(pyparsing)
BuildRequires:  pythonegg(3)(pytz)
BuildRequires:  pythonegg(3)(six)
BuildRequires:  pythonegg(3)(cycler)
BuildRequires:  pythonegg(3)(pillow)
Requires:       pythonegg(3)(six)
Requires:       pythonegg(3)(numpy)
Requires:       pythonegg(3)(pycairo) 
Requires:       pythonegg(3)(pyparsing)
Requires:       pythonegg(3)(cycler)
Requires:       pythonegg(3)(python-dateutil)
Requires:       pythonegg(3)(pytz)
Requires:       pythonegg(3)(pillow)
Requires:       fonts-ttf-dejavu
Requires:       font(stixmath)
Requires:       %{name}-data = %{version}-%{release}

Requires: python3-matplotlib-%{?backend_subpackage}%{!?backend_subpackage:tk}%{?_isa} = %{version}-%{release}


%description -n python3-matplotlib
Matplotlib is a python 2D plotting library which produces publication
quality figures in a variety of hardcopy formats and interactive
environments across platforms. matplotlib can be used in python
scripts, the python and ipython shell, web application servers, and
six graphical user interface toolkits.

Matplotlib tries to make easy things easy and hard things possible.
You can generate plots, histograms, power spectra, bar charts,
errorcharts, scatterplots, etc, with just a few lines of code.


%package -n     python3-matplotlib-qt4
%{?python_provide:%python_provide python3-matplotlib-qt4}
Summary:        Qt4 backend for python3-matplotlib
Group:          Development/Python
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
Requires:       python3-matplotlib-qt5
BuildRequires:  python3-qt4-devel
Requires:       python3-qt4

%description -n python3-matplotlib-qt4
%{summary}


%package -n     python3-matplotlib-qt5
%{?python_provide:%python_provide python3-matplotlib-qt5}
Summary:        Qt5 backend for python3-matplotlib
Group:          Development/Python
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
BuildRequires:  python3-qt5
Requires:       python3-qt5

%description -n python3-matplotlib-qt5
%{summary}


# gtk2 never worked in Python 3 afaict, so no need for -gtk subpackage
%package -n     python3-matplotlib-gtk3
%{?python_provide:%python_provide python3-matplotlib-gtk3}
Summary:        GTK3 backend for python3-matplotlib
Group:          Development/Python
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
# This should be converted to typelib(Gtk) when supported
BuildRequires:  gtk+3.0
BuildRequires:  python3-gobject3
Requires:       gtk+3.0%{?_isa}
Requires:       python3-gobject3%{?_isa}

%description -n python3-matplotlib-gtk3
%{summary}


%package -n     python3-matplotlib-tk
%{?python_provide:%python_provide python3-matplotlib-tk}
Summary:        Tk backend for python3-matplotlib
Group:          Development/Python
Requires:       python3-matplotlib%{?_isa} = %{version}-%{release}
BuildRequires:  python3-tkinter
Requires:       python3-tkinter

%description -n python3-matplotlib-tk
%{summary}


%prep
%setup -q -n matplotlib-%{version}

# Copy setup.cfg to the builddir
sed 's/\(backend = \).*/\1%{backend}/' >setup.cfg <%{SOURCE1}

# Keep this until next version, and increment if changing from
# USE_FONTCONFIG to False or True so that cache is regenerated
# if updated from a version enabling fontconfig to one not
# enabling it, or vice versa
if [ %{version} = 1.4.3 ]; then
    sed -i 's/\(__version__ = 101\)/\1.1/' lib/matplotlib/font_manager.py
fi

%if !%{with_bundled_fonts}
# Use fontconfig by default
sed -i 's/\(USE_FONTCONFIG = \)False/\1True/' lib/matplotlib/font_manager.py
%endif

%patch2 -p1
%patch5 -p1

chmod -x lib/matplotlib/mpl-data/images/*.svg


%build
MPLCONFIGDIR=$PWD \
MATPLOTLIBDATA=$PWD/lib/matplotlib/mpl-data \
  %py2_build

%if %{with_html}
# Need to make built matplotlib libs available for the sphinx extensions:
pushd doc
    MPLCONFIGDIR=$PWD/.. \
    MATPLOTLIBDATA=$PWD/../lib/matplotlib/mpl-data \
    PYTHONPATH=`realpath ../build/lib.linux*` \
        %{__python2} make.py html
popd
%endif
# Ensure all example files are non-executable so that the -doc
# package doesn't drag in dependencies
find examples -name '*.py' -exec chmod a-x '{}' \;

MPLCONFIGDIR=$PWD \
MATPLOTLIBDATA=$PWD/lib/matplotlib/mpl-data \
  %py3_build
# documentation cannot be built with python3 due to syntax errors
# and building with python 2 exits with cryptic error messages


%install
MPLCONFIGDIR=$PWD \
MATPLOTLIBDATA=$PWD/lib/matplotlib/mpl-data/ \
  %py2_install

chmod +x %{buildroot}%{python2_sitearch}/matplotlib/dates.py
mkdir -p %{buildroot}%{_sysconfdir} %{buildroot}%{_datadir}/matplotlib
mv %{buildroot}%{python2_sitearch}/matplotlib/mpl-data/matplotlibrc \
   %{buildroot}%{_sysconfdir}
mv %{buildroot}%{python2_sitearch}/matplotlib/mpl-data \
   %{buildroot}%{_datadir}/matplotlib
%if !%{with_bundled_fonts}
rm -rf %{buildroot}%{_datadir}/matplotlib/mpl-data/fonts
%endif

MPLCONFIGDIR=$PWD/.. \
MATPLOTLIBDATA=$PWD/../lib/matplotlib/mpl-data/ \
    %py3_install

chmod +x %{buildroot}%{python3_sitearch}/matplotlib/dates.py
rm -fr %{buildroot}%{python3_sitearch}/matplotlib/mpl-data
rm -f %{buildroot}%{python3_sitearch}/six.py


%if %{run_tests}
%check
# This should match the default backend
echo "backend      : %{backend}" > matplotlibrc
MPLCONFIGDIR=$PWD \
MATPLOTLIBDATA=%{buildroot}%{_datadir}/matplotlib/mpl-data \
PYTHONPATH=%{buildroot}%{python2_sitearch} \
     xvfb-run %{__python2} -c "import matplotlib; matplotlib.test()"

MPLCONFIGDIR=$PWD \
MATPLOTLIBDATA=%{buildroot}%{_datadir}/matplotlib/mpl-data \
PYTHONPATH=%{buildroot}%{python3_sitearch} \
     xvfb-run %{__python3} -c "import matplotlib; matplotlib.test()"
%endif # run_tests


%files -n python-matplotlib
%license LICENSE/
%doc CONTRIBUTING.md
%doc CHANGELOG
%doc README.rst
%{python2_sitearch}/*egg-info
%{python2_sitearch}/matplotlib-*-nspkg.pth
%{python2_sitearch}/matplotlib/
%{python2_sitearch}/mpl_toolkits/
%{python2_sitearch}/pylab.py*
%exclude %{python2_sitearch}/matplotlib/backends/backend_qt4*
%exclude %{python2_sitearch}/matplotlib/backends/backend_qt5*
%exclude %{python2_sitearch}/matplotlib/backends/backend_gtk*
%exclude %{python2_sitearch}/matplotlib/backends/_gtkagg.*
%exclude %{python2_sitearch}/matplotlib/backends/backend_tkagg.*
%exclude %{python2_sitearch}/matplotlib/backends/tkagg.*
%exclude %{python2_sitearch}/matplotlib/backends/_tkagg.so
%exclude %{python2_sitearch}/matplotlib/backends/backend_wx.*
%exclude %{python2_sitearch}/matplotlib/backends/backend_wxagg.*
%exclude /%{_pkgdocdir}/*/*


%files -n python-matplotlib-qt4
%{python2_sitearch}/matplotlib/backends/backend_qt4.*
%{python2_sitearch}/matplotlib/backends/backend_qt4agg.*


%files -n python-matplotlib-qt5
%{python2_sitearch}/matplotlib/backends/backend_qt5.*
%{python2_sitearch}/matplotlib/backends/backend_qt5agg.*


%files -n python-matplotlib-gtk
%{python2_sitearch}/matplotlib/backends/backend_gtk.py*
%{python2_sitearch}/matplotlib/backends/backend_gtkagg.py*
%{python2_sitearch}/matplotlib/backends/backend_gtkcairo.py*
%{python2_sitearch}/matplotlib/backends/_gtkagg.so


%files -n python-matplotlib-wx
%{python2_sitearch}/matplotlib/backends/backend_wx.*
%{python2_sitearch}/matplotlib/backends/backend_wxagg.*


%files -n python-matplotlib-gtk3
%{python2_sitearch}/matplotlib/backends/backend_gtk3*.py*


%files -n python-matplotlib-tk
%{python2_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python2_sitearch}/matplotlib/backends/tkagg.py*
%{python2_sitearch}/matplotlib/backends/_tkagg.so


%files -n python-matplotlib-doc
%doc examples
%if %{with_html}
%doc doc/build/html/*
%endif


%files -n python-matplotlib-data
%{_sysconfdir}/matplotlibrc
%{_datadir}/matplotlib/mpl-data/
%if %{with_bundled_fonts}
%exclude %{_datadir}/matplotlib/mpl-data/fonts/
%endif

%if %{with_bundled_fonts}
%files -n python-matplotlib-data-fonts
%{_datadir}/matplotlib/mpl-data/fonts/
%endif


%files -n python3-matplotlib
%license LICENSE/
%doc CONTRIBUTING.md
%doc CHANGELOG
%doc README.rst
%{python3_sitearch}/*egg-info
%{python3_sitearch}/matplotlib-*-nspkg.pth
%{python3_sitearch}/matplotlib/
%{python3_sitearch}/mpl_toolkits/
%{python3_sitearch}/pylab.py*
%{python3_sitearch}/__pycache__/*
%exclude %{python3_sitearch}/matplotlib/backends/backend_qt4*
%exclude %{python3_sitearch}/matplotlib/backends/__pycache__/backend_qt4*
%exclude %{python3_sitearch}/matplotlib/backends/backend_qt5*
%exclude %{python3_sitearch}/matplotlib/backends/__pycache__/backend_qt5*
%exclude %{python3_sitearch}/matplotlib/backends/backend_gtk*
%exclude %{python3_sitearch}/matplotlib/backends/__pycache__/backend_gtk*
%exclude %{python3_sitearch}/matplotlib/backends/backend_tkagg.*
%exclude %{python3_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*
%exclude %{python3_sitearch}/matplotlib/backends/tkagg.*
%exclude %{python3_sitearch}/matplotlib/backends/__pycache__/tkagg.*
%exclude %{python3_sitearch}/matplotlib/backends/_tkagg.*
%exclude /%{_pkgdocdir}/*/*


%files -n python3-matplotlib-qt4
%{python3_sitearch}/matplotlib/backends/backend_qt4.*
%{python3_sitearch}/matplotlib/backends/__pycache__/backend_qt4.*
%{python3_sitearch}/matplotlib/backends/backend_qt4agg.*
%{python3_sitearch}/matplotlib/backends/__pycache__/backend_qt4agg.*


%files -n python3-matplotlib-qt5
%{python3_sitearch}/matplotlib/backends/backend_qt5.*
%{python3_sitearch}/matplotlib/backends/__pycache__/backend_qt5.*
%{python3_sitearch}/matplotlib/backends/backend_qt5agg.*
%{python3_sitearch}/matplotlib/backends/__pycache__/backend_qt5agg.*


%files -n python3-matplotlib-gtk3
%{python3_sitearch}/matplotlib/backends/backend_gtk*
%{python3_sitearch}/matplotlib/backends/__pycache__/backend_gtk*


%files -n python3-matplotlib-tk
%{python3_sitearch}/matplotlib/backends/backend_tkagg.py*
%{python3_sitearch}/matplotlib/backends/__pycache__/backend_tkagg.*
%{python3_sitearch}/matplotlib/backends/tkagg.*
%{python3_sitearch}/matplotlib/backends/__pycache__/tkagg.*
%{python3_sitearch}/matplotlib/backends/_tkagg.*
