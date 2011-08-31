%define oname		loki
%define major		0
%define libname		%mklibname %{oname} %{major}
%define develname	%mklibname -d %{oname}

%define rel		%mkrel 1
%define ver		0.1.7

Name: 			%{oname}-lib
Version: 		%{ver}
Release: 		%{rel}
Summary:		Loki C++ Library of design patterns and idioms
Group:			System/Libraries
License:		MIT
# License text not included
# https://sourceforge.net/tracker/?func=detail&aid=3027570&group_id=29557&atid=396647
URL:			http://sourceforge.net/projects/loki-lib
Source0:		http://prdownloads.sourceforge.net/loki-lib/%{oname}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/build-%{name}-%{version}

%description
A C++ library of designs, containing flexible implementations of common design
patterns and idioms.

%package -n %{libname}
Summary: Loki C++ Library of design patterns and idioms
Group: System/Libraries
Provides: %{name} = %{version}-%{release}
Provides: %{oname} = %{version}-%{release}

%description -n  %{libname}
A C++ library of designs, containing flexible implementations of common design
patterns and idioms.

%package -n %{develname}
Summary: The Loki C++ headers and development libraries
Group: Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{oname}-devel = %{version}-%{release}

%description -n  %{develname}
Headers and shared object symlinks for the Loki C++ Library

%package doc
Summary: The Loki C++ html docs
Group: Development/C++
BuildArch: noarch

%description doc
HTML documentation files for the Loki C++ Library

%prep
%setup -n %{oname}-%{version} -q
%__chmod -x doc/html/*
%__rm doc/html/installdox
iconv -f ISO88591 -t utf8 CHANGES -o CHANGES

%build
%ifarch x86_64
%__sed -i s,"/lib","/lib64",g src/Makefile
%__mkdir lib64
%endif

%make CXXFLAGS="%{optflags}" build-static build-shared

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%files doc
%defattr(-,root,root,-)
%doc README CHANGES doc/html doc/flex doc/yasli

