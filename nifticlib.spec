Summary:	C I/O libraries for files in the nifti-1 data format
Summary(pl.UTF-8):	Biblioteki C wejścia/wyjścia dla plików danych w formacie nifti-1
Name:		nifticlib
Version:	1.0.0
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://dl.sourceforge.net/niftilib/%{name}-%{version}.tar.gz
# Source0-md5:	4d0828e5783df40fb98b8dd6edc11ebb
Patch0:		%{name}-link.patch
Patch1:		%{name}-cmake.patch
URL:		http://niftilib.sourceforge.net/
BuildRequires:	cmake
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
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake . \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}" \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_SKIP_RPATH=ON \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DNIFTI_INSTALL_LIB_DIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README Updates.txt
%attr(755,root,root) %{_bindir}/nifti_stats
%attr(755,root,root) %{_bindir}/nifti_tool
%attr(755,root,root) %{_libdir}/libnifticdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnifticdf.so.1
%attr(755,root,root) %{_libdir}/libniftiio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libniftiio.so.1
%attr(755,root,root) %{_libdir}/libznz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libznz.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnifticdf.so
%attr(755,root,root) %{_libdir}/libniftiio.so
%attr(755,root,root) %{_libdir}/libznz.so
%{_includedir}/nifti
