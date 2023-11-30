%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6FrameworkIntegraion
%define devname %mklibname KF6FrameworkIntegraion -d
#define git 20231103

Name: kf6-frameworkintegration
Version: 5.246.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/frameworkintegration/-/archive/master/frameworkintegration-master.tar.bz2#/frameworkintegration-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{version}/frameworkintegration-%{version}.tar.xz
%endif
Summary: Framework providing components to allow applications to integrate with a KDE Workspace
URL: https://invent.kde.org/frameworks/frameworkintegration
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Notifications)
BuildRequires: pkgconfig(packagekitqt6)
BuildRequires: cmake(AppStreamQt) >= 1.0.0
Requires: %{libname} = %{EVRD}

%description
Framework providing components to allow applications to integrate with a KDE Workspace

%package -n %{libname}
Summary: Framework providing components to allow applications to integrate with a KDE Workspace
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Framework providing components to allow applications to integrate with a KDE Workspace

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Framework providing components to allow applications to integrate with a KDE Workspace

%prep
%autosetup -p1 -n frameworkintegration-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/knotifications6/plasma_workspace.notifyrc
%{_libdir}/libexec/kf6/kpackagehandlers/appstreamhandler

%files -n %{devname}
%{_includedir}/KF6/FrameworkIntegration
%{_includedir}/KF6/KStyle
%{_libdir}/cmake/KF6FrameworkIntegration

%files -n %{libname}
%{_libdir}/libKF6Style.so*
%{_libdir}/libexec/kf6/kpackagehandlers/knshandler
%{_qtdir}/plugins/kf6/FrameworkIntegrationPlugin.so
