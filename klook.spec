#This is a spec file for Klook

Summary:	Quick file preview
Name:		klook
Version:	2.0
Release:	6
License:	GPLv3
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel	>= 4.7.0
BuildRequires:	kdelibs4-devel	>= 4.6.5
Requires:	okular
Requires:	okular-ooo
Requires:	okular-chm
Requires:	okular-pdf
Requires:	okular-fb
Requires:	gstreamer0.10-decoders
Requires:	gstreamer0.10-vp8

%description
Klook is a quick preview feature based on Qt and Qt Quick

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

%files
%{_kde_appsdir}/klook/*
%{_kde_iconsdir}/hicolor/*
%{_kde_bindir}/klook
%{_kde_datadir}/locale

