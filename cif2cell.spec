%global summary A tool to generate the geometrical setup for various electronic structure codes from a CIF
%global srcname cif2cell

Name:           %{srcname}
Version:        1.2.7
Release:        1%{?dist}
Summary:        %{summary}

License:        GPLv3
URL:            http://sourceforge.net/projects/cif2cell/
Source0:        http://sourceforge.net/projects/%{srcname}/files/%{srcname}-%{version}.tar.gz/download

BuildArch:      noarch
BuildRequires:  python2-devel

%description
CIF2Cell is a tool to generate the geometrical setup for various electronic structure codes from a CIF (Crystallographic Information Framework) file. The program currently supports output for a number of popular electronic structure programs, including ABINIT, ASE, CASTEP, CP2K, CPMD, CRYSTAL09, Elk, EMTO, Exciting, Fleur, FHI-aims, Hutsepot, MOPAC, Quantum Espresso, RSPt, Siesta, SPR-KKR, VASP. Also exports some related formats like .coo, .cfg and .xyz-files. The program has been published in Computer Physics Communications 182 (2011) 1183–1186.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install
mkdir -p  %{buildroot}/%{_defaultdocdir}
mkdir -p  %{buildroot}/%{_datadir}/%{name}
mv %{buildroot}/usr/lib/%{name}/sample_cifs %{buildroot}/%{_datadir}/%{name}/
rm -fr %{buildroot}/usr/lib/%{name}

%files 
%{_bindir}/cif2cell
%{python2_sitelib}/*
%{_datadir}/cif2cell/sample_cifs/*
%license LICENSE
%doc README HOWTOCITE docs/cif2cell.pdf

%changelog
* Thu Nov 12 2015 Stuart Campbell <sic@fedoraproject.org> - 1.2.7-1
- Initial package for fedora only
