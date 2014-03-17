%define oname loki
%define major %{version}
%define libname %mklibname %{oname} %{major}
%define devname %mklibname %{oname} -d

Summary:	Loki C++ Library of design patterns and idioms
Name:		%{oname}-lib
Version:	0.1.7
Release:	2
# License text not included
# https://sourceforge.net/tracker/?func=detail&aid=3027570&group_id=29557&atid=396647
License:	MIT
Group:		System/Libraries
Url:		http://sourceforge.net/projects/loki-lib
Source0:	http://prdownloads.sourceforge.net/loki-lib/%{oname}-%{version}.tar.gz

%description
A C++ library of designs, containing flexible implementations of common design
patterns and idioms.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Loki C++ Library of design patterns and idioms
Group:		System/Libraries
Obsoletes:	%{_lib}loki0 < 0.1.7-2
Conflicts:	%{_lib}loki0 < 0.1.7-2

%description -n %{libname}
A C++ library of designs, containing flexible implementations of common design
patterns and idioms.

%files -n %{libname}
%{_libdir}/lib%{oname}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	The Loki C++ headers and development libraries
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	%{oname}-devel = %{EVRD}

%description -n  %{devname}
Headers and shared object symlinks for the Loki C++ Library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib%{oname}.so
%{_libdir}/lib%{oname}.a

#----------------------------------------------------------------------------

%package doc
Summary:	The Loki C++ html docs
Group:		Development/C++
BuildArch:	noarch

%description doc
HTML documentation files for the Loki C++ Library.

%files doc
%doc README CHANGES doc/html doc/flex doc/yasli

#----------------------------------------------------------------------------

%prep
%setup -n %{oname}-%{version} -q
chmod -x doc/html/*
rm doc/html/installdox
iconv -f ISO88591 -t utf8 CHANGES -o CHANGES

%build
%ifarch x86_64
sed -i s,"/lib","/lib64",g src/Makefile
sed -i s,"/lib/","/lib64/",g test/Makefile.common
mkdir lib64
%endif

make CXXFLAGS="%{optflags}"

%install
%makeinstall

