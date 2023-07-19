%define major 0
%define libname %mklibname cppdap
%define devname %mklibname cppdap -d

Name: cppdap
Version: 1.58.0_a
Release: 1
Source0: https://github.com/google/cppdap/archive/refs/tags/dap-%(echo %{version}|sed -e 's,_,-,g').tar.gz
Patch0: cppdap-shared-lib.patch
Summary: C++ Library for the Debug Adapter Protocol
URL: https://github.com/google/cppdap
License: Apache-2.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(nlohmann_json)

%description
cppdap is a C++11 library ("SDK") implementation of the Debug Adapter Protocol,
providing an API for implementing a DAP client or server.

cppdap provides C++ type-safe structures for the full DAP specification, and
provides a simple way to add custom protocol messages.

%package -n %{libname}
Summary: C++ Library for the Debug Adapter Protocol
Group: System/Libraries

%description -n %{libname}
cppdap is a C++11 library ("SDK") implementation of the Debug Adapter Protocol,
providing an API for implementing a DAP client or server.

cppdap provides C++ type-safe structures for the full DAP specification, and
provides a simple way to add custom protocol messages.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

cppdap is a C++11 library ("SDK") implementation of the Debug Adapter Protocol,
providing an API for implementing a DAP client or server.

cppdap provides C++ type-safe structures for the full DAP specification, and
provides a simple way to add custom protocol messages.

%prep
%autosetup -p1 -n cppdap-dap-%(echo %{version} |sed -e 's,_,-,g')
%cmake \
	-DCPPDAP_USE_EXTERNAL_NLOHMANN_JSON_PACKAGE:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
