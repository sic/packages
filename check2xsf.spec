%global summary A tool to convert output of CASTEP into various other formats. 
%global srcname check2xsf 

Name:           %{srcname}
Version:        1.0
Release:        1%{?dist}
Summary:        %{summary}

License:        GPLv2
URL:            http://www.tcm.phy.cam.ac.uk/sw/check2xsf/
Source0:        https://github.com/stuartcampbell/%{srcname}/archive/v%{version}.tar.gz

%description


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
