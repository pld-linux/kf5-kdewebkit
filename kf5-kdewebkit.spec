#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.111
%define		qtver		5.15.2
%define		kfname		kdewebkit
Summary:	Integration of the HTML rendering engine WebKit
Name:		kf5-%{kfname}
Version:	5.111.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	8aa419d8b5df83d14cf286e05f2d04ce
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5OpenGL-devel >= 5.3.1
BuildRequires:	Qt5Positioning-devel >= 5.3.1
BuildRequires:	Qt5PrintSupport-devel >= 5.3.1
BuildRequires:	Qt5Qml-devel >= 5.3.1
BuildRequires:	Qt5Quick-devel >= 5.3.1
BuildRequires:	Qt5Sensors-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebKit-devel >= 5.3.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel >= 5.2.0
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kparts-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwallet-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This library provides KDE integration of the QtWebKit library. If you
are using QtWebKit in your KDE application, you are encouraged to use
this layer instead of using the QtWebKit classes directly.

In particular, you should use KWebView in place of QWebView,
KGraphicsWebView in place of QGraphicsWebView and KWebPage in place of
QWebPage. See the documentation for those classes for more
information.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%{?with_tests:%ninja_build -C build test}


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5WebKit.so.5
%attr(755,root,root) %{_libdir}/libKF5WebKit.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kdewebkit5widgets.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDEWebKit
%{_libdir}/cmake/KF5WebKit
%{_libdir}/libKF5WebKit.so
%{qt5dir}/mkspecs/modules/qt_KDEWebKit.pri
