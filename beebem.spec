%define	name	beebem
%define	version	0.0.13
%define release	3
%define	summary Beebem BBC Micro Emulator

Name:		%{name}
Summary:	%{summary}
Version:	%{version}
Release:	%{release}
Source0:	http://beebem-unix.bbcmicro.com/download/%{name}-%{version}.tar.gz
Source10:       beebem-big.png
Source11:       beebem-mini.png
Source12:       beebem.png
Patch0:		beebem-0.0.13_64bit.patch
Patch1:		beebem-0.0.13-keys.patch
Patch2: 	beebem-0.0.13_menu_crash.patch
Patch3:         beebem-0.0.13_gcc4.3.patch
Patch4:		beebem-0.0.13_gtk_chooser.patch
URL:		http://beebem-unix.bbcmicro.com/index.html
License:	Other
Group:		Emulators
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig(gtk+-2.0)
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
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
autoreconf -fiv
%configure
%make

%install
rm -rf %{buildroot}

%makeinstall

# Mandriva menu entry

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%clean
rm -rf %{buildroot}

%files
%_bindir/beebem
%dir %{_datadir}/beebem
%{_datadir}/beebem/*
%{_datadir}/applications/mandriva-%{name}.desktop
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

