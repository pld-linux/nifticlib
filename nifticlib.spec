Summary:	C I/O libraries for files in the nifti-1 data format
Summary(pl.UTF-8):	Biblioteki C wejścia/wyjścia dla plików danych w formacie nifti-1
Name:		nifticlib
Version:	3.0.0
Release:	1
License:	Public Domain
Group:		Libraries
#Source0Download: https://github.com/NIFTI-Imaging/nifti_clib/releases
Source0:	https://github.com/NIFTI-Imaging/nifti_clib/archive/v%{version}/nifti_clib-%{version}.tar.gz
# Source0-md5:	ee40068103775a181522166e435ee82d
Patch1:		%{name}-cmake.patch
URL:		https://github.com/NIFTI-Imaging/nifti_clib
BuildRequires:	cmake >= 3.10.2
BuildRequires:	expat-devel
BuildRequires:	help2man
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
niftilib is a set of I/O library for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing
medical image data, e.g. magnetic resonance image (MRI) and
functional MRI (fMRI) brain images.

This package contains C libraries.

%description -l pl.UTF-8
niftilib to biblioteki wejścia/wyjścia do odczytu i zapisu plików
danych w formacie nifti-1. Jest to binarny format plików do
przechowywania danych obrazów medycznych, np. obrazów rezonansu
magnetycznego (MRI) czy funkcjonalnych obrazów rezonansu
magnetycznego (fMRI) mózgu.

Ten pakiet zawiera biblioteki C.

%package devel
Summary:	Header files for niftilib C libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek C niftilib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

%description devel
Header files for niftilib C libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek C niftilib.

%prep
%setup -q -n nifti_clib-%{version}
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DDOWNLOAD_TEST_DATA=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

for f in nifti1_tool nifti_stats nifti_tool ; do
	%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/${f}_manpage.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/${f}.1.gz
done

install -d $RPM_BUILD_ROOT%{_examplesdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/NIFTI/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/NIFTI/README.md

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md Updates.txt
%attr(755,root,root) %{_bindir}/nifti1_tool
%attr(755,root,root) %{_bindir}/nifti_stats
%attr(755,root,root) %{_bindir}/nifti_tool
%attr(755,root,root) %{_libdir}/libnifti2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnifti2.so.2
%attr(755,root,root) %{_libdir}/libnifticdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnifticdf.so.2
%attr(755,root,root) %{_libdir}/libniftiio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libniftiio.so.2
%attr(755,root,root) %{_libdir}/libznz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libznz.so.3
%{_mandir}/man1/nifti1_tool.1*
%{_mandir}/man1/nifti_stats.1*
%{_mandir}/man1/nifti_tool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnifti2.so
%attr(755,root,root) %{_libdir}/libnifticdf.so
%attr(755,root,root) %{_libdir}/libniftiio.so
%attr(755,root,root) %{_libdir}/libznz.so
%{_includedir}/nifti
%{_datadir}/cmake/NIFTI
%{_examplesdir}/%{name}-%{version}
