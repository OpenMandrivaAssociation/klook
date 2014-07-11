Summary:	Quick file preview
Name:		klook
Version:	2.0
Release:	18
License:	GPLv3
Group:		Graphical desktop/KDE
Url:		https://abf.rosalinux.ru/uxteam/KLook
Source0:	%{name}-%{version}.tar.gz
Patch0:		klook-2.0-codec.patch
BuildRequires:	qt4-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(exiv2)
Requires: 	okular
Requires: 	okular-ooo
Requires: 	okular-chm
Requires: 	okular-pdf
Requires:	okular-fb
Requires:	gstreamer0.10-decoders
Requires:	gstreamer0.10-vp8

%description
Klook is a quick preview feature based on Qt and Qt Quick.

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%{_kde_bindir}/klook
%{_kde_appsdir}/klook
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
