Summary:	C I/O libraries for files in the nifti-1 data format
Summary(pl.UTF-8):	Biblioteki C wejścia/wyjścia dla plików danych w formacie nifti-1
Name:		nifticlib
Version:	2.0.0
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://downloads.sourceforge.net/niftilib/%{name}-%{version}.tar.gz
# Source0-md5:	425a711f8f92fb1e1f088cbc55bea53a
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
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
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
%attr(755,root,root) %{_bindir}/nifti1_test
%attr(755,root,root) %{_libdir}/libnifticdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnifticdf.so.2
%attr(755,root,root) %{_libdir}/libniftiio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libniftiio.so.2
%attr(755,root,root) %{_libdir}/libznz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libznz.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnifticdf.so
%attr(755,root,root) %{_libdir}/libniftiio.so
%attr(755,root,root) %{_libdir}/libznz.so
%{_includedir}/nifti
