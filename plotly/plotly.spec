%global srcname plotly
%global summary Python plotting library for collaborative, interactive, publication-quality graphs.

%define version 1.10.0
%define unmangled_version 1.10.0
%define release 1

Summary: %{summary}
Name: python-%{srcname}
Version: %{version}
Release: %{release}%{?dist}
Source0: %{srcname}-%{unmangled_version}.tar.gz
#Source0: https://pypi.python.org/packages/2a/7f/74aff937097c6fa9938a5d3a3f0f98a387055a60457507be9d60b1c4dc85/plotly-1.10.0.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris P <chris@plot.ly>
Url: https://plot.ly/python/

BuildRequires: python2-devel
BuildRequires: python3-devel


%description
Source rpm for plotly python package to build both python2 and python3 libraries.

License: MIT

.. _Plotly: https://plot.ly
.. _Quickstart: https://plot.ly/python
.. _GitHub repo: https://github.com/plotly/python-api
.. _Plotly and mpld3: https://plot.ly/python/matplotlib-to-plotly-tutorial/
.. _Plotly and Python: https://plot.ly/python/overview/
.. _set of notebooks: https://plot.ly/python/user-guide/
.. _plotly profile: https://plot.ly/~mpld3/
.. _@plotlygraphs: https://twitter.com/plotlygraphs
.. _feedback@plot.ly: feedback@plot.ly


%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires: python-setuptools
Requires:      python
%if 0%{?rhel}
Requires: python-matplotlib
%else
Requires: python2-matplotlib
%endif
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
=======
plotly:
=======
--------------------------
It's all about the graphs.
--------------------------

The Nutshell
~~~~~~~~~~~~

Use this package to make collaborative, interactive,
publication-quality graphs from Python.

Here's how you import::

    import plotly.plotly as py              # for sending things to plotly
    import plotly.tools as tls              # for mpl, config, etc.
    from plotly.graph_objs import *         # __all__ is safely defined

Here's how you sign in::

    py.sign_in('PythonAPI', 'ubpiol2cve')   # get your own at https://plot.ly/

Here's how you plot data or a figure::

    py.plot(data_or_figure_here)

Here's what you get:

* an account on plotly
* a unique url for your data/figures
* an interactive web-application to edit your figure or make new figures
* a platform on which to share your data/figures with the world

You can also convert supported matplotlib figures::

    py.plot_mpl(mplfig)

Stop fighting with your figures; start designing them. Check out our
Quickstart_ to get going.


About
~~~~~

Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.

Install via pip
~~~~~~~~~~~~~~~

Assuming you have already installed pip, you can simply enter the following
in a terminal program::

    $ pip install plotly

Contributing!
~~~~~~~~~~~~~

If you want to contribute to making Plotly's Python API experience better,
head to our `GitHub repo`_. Instructions for installing from here,
updating the included submodules, and contributing are detailed there!

Plotly, matplotlib, and mpld3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The matplotlylib sub-package allows you to convert matplotlib figures to
plotly figures, with a one-liner::

    py.plot_mpl(fig)

Checkout the `Plotly and mpld3`_ IPython notebook for more infomataion.

Introduction to working with out API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checkout the `Plotly and Python`_ IPython notebook to get a more in depth
exposition of our Python API.

Plotly's *guide book*
~~~~~~~~~~~~~~~~~~~~~

Still here? Don't worry, we've got more documentation for you. Checkout a
*highly* complete `set of notebooks`_ for walk-throughs on all the features
we offer!

Details
~~~~~~~

The plotly package depends on requests, which will be installed by pip for you.

To use the matplotlylib subpackage, you'll also need to have matplotlib 1.3.1
properly installed on your machine.

The matpotlylib package is based on the mplexporter framework for crawling
and exporting matplotlib images.

Created by: Plotly_, `@plotlygraphs`_, `feedback@plot.ly`_

License: MIT

.. _Plotly: https://plot.ly
.. _Quickstart: https://plot.ly/python
.. _GitHub repo: https://github.com/plotly/python-api
.. _Plotly and mpld3: https://plot.ly/python/matplotlib-to-plotly-tutorial/
.. _Plotly and Python: https://plot.ly/python/overview/
.. _set of notebooks: https://plot.ly/python/user-guide/
.. _plotly profile: https://plot.ly/~mpld3/
.. _@plotlygraphs: https://twitter.com/plotlygraphs
.. _feedback@plot.ly: feedback@plot.ly


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires: python3-setuptools
Requires:      python3
Requires: python3-matplotlib
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
=======
plotly:
=======
--------------------------
It's all about the graphs.
--------------------------

The Nutshell
~~~~~~~~~~~~

Use this package to make collaborative, interactive,
publication-quality graphs from Python.

Here's how you import::

    import plotly.plotly as py              # for sending things to plotly
    import plotly.tools as tls              # for mpl, config, etc.
    from plotly.graph_objs import *         # __all__ is safely defined

Here's how you sign in::

    py.sign_in('PythonAPI', 'ubpiol2cve')   # get your own at https://plot.ly/

Here's how you plot data or a figure::

    py.plot(data_or_figure_here)

Here's what you get:

* an account on plotly
* a unique url for your data/figures
* an interactive web-application to edit your figure or make new figures
* a platform on which to share your data/figures with the world

You can also convert supported matplotlib figures::

    py.plot_mpl(mplfig)

Stop fighting with your figures; start designing them. Check out our
Quickstart_ to get going.


About
~~~~~

Plotly_ is an online collaborative data analysis and graphing tool. The
Python API allows you to access all of Plotly's functionality from Python.
Plotly figures are shared, tracked, and edited all online and the data is
always accessible from the graph.

That's it. Find out more, sign up, and start sharing by visiting us at
https://plot.ly.

Install via pip
~~~~~~~~~~~~~~~

Assuming you have already installed pip, you can simply enter the following
in a terminal program::

    $ pip install plotly

Contributing!
~~~~~~~~~~~~~

If you want to contribute to making Plotly's Python API experience better,
head to our `GitHub repo`_. Instructions for installing from here,
updating the included submodules, and contributing are detailed there!

Plotly, matplotlib, and mpld3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The matplotlylib sub-package allows you to convert matplotlib figures to
plotly figures, with a one-liner::

    py.plot_mpl(fig)

Checkout the `Plotly and mpld3`_ IPython notebook for more infomataion.

Introduction to working with out API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checkout the `Plotly and Python`_ IPython notebook to get a more in depth
exposition of our Python API.

Plotly's *guide book*
~~~~~~~~~~~~~~~~~~~~~

Still here? Don't worry, we've got more documentation for you. Checkout a
*highly* complete `set of notebooks`_ for walk-throughs on all the features
we offer!

Details
~~~~~~~

The plotly package depends on requests, which will be installed by pip for you.

To use the matplotlylib subpackage, you'll also need to have matplotlib 1.3.1
properly installed on your machine.

The matpotlylib package is based on the mplexporter framework for crawling
and exporting matplotlib images.

Created by: Plotly_, `@plotlygraphs`_, `feedback@plot.ly`_

License: MIT

.. _Plotly: https://plot.ly
.. _Quickstart: https://plot.ly/python
.. _GitHub repo: https://github.com/plotly/python-api
.. _Plotly and mpld3: https://plot.ly/python/matplotlib-to-plotly-tutorial/
.. _Plotly and Python: https://plot.ly/python/overview/
.. _set of notebooks: https://plot.ly/python/user-guide/
.. _plotly profile: https://plot.ly/~mpld3/
.. _@plotlygraphs: https://twitter.com/plotlygraphs
.. _feedback@plot.ly: feedback@plot.ly


%prep
%setup -n %{srcname}-%{unmangled_version} -n %{srcname}-%{unmangled_version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python2-%{srcname}
%doc README.rst
%{python2_sitelib}/%{srcname}/*
%{python2_sitelib}/%{srcname}-%{version}-py2*.egg-info/*

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}/*
%{python3_sitelib}/%{srcname}-%{version}-py3*.egg-info/*
