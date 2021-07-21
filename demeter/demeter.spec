Name:           demeter
Version:        0.9.26
Release:        3%{?dist}
Summary:        A comprehensive XAS data analysis system using Feff and Ifeffit or Larch

License:        Artistic  
URL:            http://bruceravel.github.io/demeter/
Source0:        https://github.com/bruceravel/demeter/archive/refs/heads/master.tar.gz

Patch0:         demeter-remove-fityk-declaration.patch

BuildArch:      x86_64
BuildRequires:  gcc-gfortran
BuildRequires:  gnuplot
BuildRequires:  ifeffit
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Chemistry::Elements)
BuildRequires:  perl(Config::INI)
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encoding::FixLatin)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::CountLines)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Touch)
BuildRequires:  perl(Graph)
BuildRequires:  perl(Heap)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Math::Combinatorics)
BuildRequires:  perl(Math::Derivative)
BuildRequires:  perl(Math::Random)
BuildRequires:  perl(Math::Round)
BuildRequires:  perl(Math::Spline)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::LaxNum)
BuildRequires:  perl(PDL)
BuildRequires:  perl(PDL::Stats)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::ProjectDocs)
BuildRequires:  perl(RPC::XML::Client)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Spreadsheet::WriteExcel)
BuildRequires:  perl(Statistics::Descriptive)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Tree::Simple)
BuildRequires:  perl(Want)
BuildRequires:  perl(XMLRPC::Lite)
BuildRequires:  perl(YAML::Tiny)
Requires:  gnuplot
Requires:  ifeffit
Requires:  perl(Capture::Tiny)
Requires:  perl(Chemistry::Elements)
Requires:  perl(Config::INI)
Requires:  perl(Const::Fast)
Requires:  perl(DateTime)
Requires:  perl(Encoding::FixLatin)
Requires:  perl(File::Copy::Recursive)
Requires:  perl(File::CountLines)
Requires:  perl(File::Monitor::Lite)
Requires:  perl(File::Touch)
Requires:  perl(Graph)
Requires:  perl(Graphics::GnuplotIF)
Requires:  perl(Heap)
Requires:  perl(JSON)
Requires:  perl(List::MoreUtils)
Requires:  perl(Math::Combinatorics)
Requires:  perl(Math::Derivative)
Requires:  perl(Math::Random)
Requires:  perl(Math::Round)
Requires:  perl(Math::Spline)
Requires:  perl(Moose)
Requires:  perl(MooseX::Aliases)
Requires:  perl(MooseX::Types)
Requires:  perl(MooseX::Types::LaxNum)
Requires:  perl(PDL)
Requires:  perl(PDL::Stats)
Requires:  perl(Pod::POM)
Requires:  perl(RPC::XML::Client)
Requires:  perl(Regexp::Assemble)
Requires:  perl(Regexp::Common)
Requires:  perl(Spreadsheet::WriteExcel)
Requires:  perl(Statistics::Descriptive)
Requires:  perl(Term::Sk)
Requires:  perl(Term::Twiddle)
Requires:  perl(Text::Unidecode)
Requires:  perl(Tree::Simple)
Requires:  perl(Want)
Requires:  perl(Wx)
Requires:  perl(XMLRPC::Lite)
Requires:  perl(YAML::Tiny)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  qt5-qtsvg

%{?perl_default_filter}

%description
Process and analyze X-ray Absorption Spectroscopy data using Feff and either Larch or Ifeffit. 

%prep
%setup -q -n %{name}-master
%patch0 -p1 -b .fityk

%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} -I. Build.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
./Build


%install
rm -rf $RPM_BUILD_ROOT
# make pure_install DESTDIR=$RPM_BUILD_ROOT
#find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
./Build --install_path bin=%{buildroot}/%{_bindir} \
        --install_path script=%{buildroot}/%{_bindir} \
        --install_path bindoc=%{buildroot}/%{_mandir} \
        --install_path libdoc=%{buildroot}/%{_mandir} \
        --install_path lib=$%{buildroot}/%{perl_vendorlib} \
        --install_path arch=%{buildroot}/%{perl_vendorarch} \
        install
#find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
#find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
#./Build test


%files
%license LICENSE
#%doc add-docs-here
%{_bindir}/dartemis
%{_bindir}/dathena
%{_bindir}/datoms
%{_bindir}/denergy
%{_bindir}/denv
%{_bindir}/dfeff
%{_bindir}/dfeffit
%{_bindir}/dhephaestus
%{_bindir}/dlsprj
%{_bindir}/intrp
%{_bindir}/prj2json
%{_bindir}/rdfit
%{_bindir}/standards
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/


%changelog
* Mon May  6 2021 Stuart Campbell <scampbell@bnl.gov>
- Added some missing dependencies

* Mon May  3 2021 Stuart Campbell <scampbell@bnl.gov>
- Apply patch to remove explicit fityk 

* Mon May  3 2021 Stuart Campbell <scampbell@bnl.gov>
- Initial Package
