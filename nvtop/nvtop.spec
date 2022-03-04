# Undefine CMake in-source builds in order to be consistent with f33+
%undefine __cmake_in_source_build

%global _hardened_build 1
%global __cmake cmake3

Name:           nvtop
Version:        1.2.2
Release:        1%{?dist}
Summary:        NVIDIA GPUs htop like monitoring tool 

License:        GPLv3
URL:            https://github.com/Syllo/nvtop
Source0:        https://github.com/Syllo/nvtop/archive/refs/tags/%{version}.tar.gz


BuildRequires:  cmake
BuildRequires:  ncurses-devel


%description
Nvtop stands for NVidia TOP, a (h)top like task monitor for NVIDIA GPUs. It can handle 
multiple GPUs and print information about them in a htop familiar way.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
  
%files
%license LICENSE

%{_bindir}/nvtop
%{_mandir}/man1/nvtop.1.gz

%changelog
* Thu Mar 03 2022 Stuart Campbell <scampbell@bnl.gov> 1.2.2-1
- Initial version of package
