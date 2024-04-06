Name:		beebem
Summary:	Beebem BBC Micro Emulator
Version:	0.0.14
Release:	2
Source0:	https://github.com/beebem-unix/beebem/archive/refs/tags/v%{version}.tar.gz
Source10:       beebem-big.png
Source11:       beebem-mini.png
Source12:       beebem.png
Patch1:		beebem-0.0.14_gtk3.patch
URL:		http://beebem-unix.bbcmicro.com/index.html
License:	Other
Group:		Emulators
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:  autoconf

%description
BeebEm is a popular Acorn BBC Micro and Master 128 emulator. 

Development of BeebEm started in 1994 by David Gilbert on UNIX, 
and has since been ported to many other platforms, most 
notably Microsoft Windows and Apple OS X.

There are many versions of BeebEm floating around the Net, 
and each version has a different set of features. This 
version of BeebEm for UNIX is an SDL port of the Windows 
version of BeebEm.

%prep
%autosetup -p1

%build
export CXXFLAGS="-Wno-unused-result"
autoreconf -fiv
%configure
%make_build

%install
%old_makeinstall

# Mandriva menu entry

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Beebem
Comment=BBC Micro/Master Emulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Emulator;System;
EOF

install -D %SOURCE10 $RPM_BUILD_ROOT%_liconsdir/%name.png
install -D %SOURCE11 $RPM_BUILD_ROOT%_miconsdir/%name.png
install -D %SOURCE12 $RPM_BUILD_ROOT%_iconsdir/%name.png

%files
%_bindir/beebem
%dir %{_datadir}/beebem
%{_datadir}/beebem/*
%{_datadir}/applications/%{name}.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

