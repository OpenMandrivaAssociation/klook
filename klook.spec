Summary:	Klook is a quick preview feature
Name:		klook
Version:	0.1
Release:	77
License:	GPLv3
Group:		Graphical desktop/KDE
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	qt4-devel	>= 4.7.0
BuildRequires:	kdelibs4-devel	>= 4.6.5

%description
Klook is a quick preview feature based on Qt and Qt Quick, allows users to look
at the contents of a file in the Dolphin

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build
%find_lang KLook

%files -f KLook.lang
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}
