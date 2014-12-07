%define libxorg %mklibname xorg-x11

Name:		xorg-x11
Version:	7.7
Release:	14
Summary:	X11 metapackage
Group:		Development/X11
License:	MIT

Requires:	x11-data-bitmaps
Requires:	x11-server-xorg
#Requires:	x11-apps
Requires:	x11-tools
Requires:	x11-docs
Requires:	fonts-ttf-dejavu
Requires:	fonts-ttf-liberation
Requires:	x11-font-type1
Requires:	x11-font-misc 
Requires:	libx11
Requires:	x11-data-cursor-themes

Obsoletes:	X11R6-contrib

%description
X11 metapackage.

%files

#------------------------------------------------------------------------------
%package -n %{libxorg}
Summary:	X11 libraries
Group:		Development/X11

Requires:	libdmx
Requires:	libdrm
Requires:	libfontenc
Requires:	libfs
Requires:	libice
Requires:	liblbxutil
Requires:	liboldx
Requires:	libsm
Requires:	libwindowswm
Requires:	libx11
Requires:	libxau
Requires:	libxaw7
Requires:	libxcomposite
Requires:	libxcursor
Requires:	libxdamage
Requires:	libxdmcp
Requires:	libxevie
Requires:	libxext
Requires:	libxfixes
Requires:	libxfontcache
Requires:	libxfont
Requires:	libxft
Requires:	libxi
Requires:	%{_lib}xinerama1
Requires:	libxkbfile
Requires:	libxkbui
Requires:	libxmu
Requires:	libxpm
Requires:	libxrandr
Requires:	libxrender
Requires:	libxres
Requires:	libxscrnsaver
Requires:	%{_lib}xt6
Requires:	libxtrap
Requires:	%{_lib}xtst6
Requires:	%{_lib}xv1
Requires:	libxvmc
Requires:	%{_lib}xxf86dga1
Requires:	libxxf86misc
Requires:	%{_lib}xxf86vm1

%description -n %{libxorg}
X11 libraries.

%files -n %{libxorg}

#------------------------------------------------------------------------------

%package -n %{libxorg}-devel
Summary:	Development tools and files for X11
Group:		Development/X11
Provides:	XFree86-devel = %{version}
Provides:	X11-devel = %{version}

Requires:	libdmx-devel
Requires:	libdrm-devel
Requires:	libfontenc-devel
Requires:	libfs-devel
Requires:	libice-devel
Requires:	liblbxutil-devel
Requires:	pkgconfig(gl)
Requires:	glu-devel
Requires:	pkgconfig(glut)
#Requires:	pkgconfig(glw)
Requires:	liboldx-devel
Requires:	pkgconfig(sm)
Requires:	libwindowswm-devel
Requires:	pkgconfig(x11)
Requires:	libxau-devel
Requires:	xaw-devel
Requires:	libxcomposite-devel
Requires:	libxcursor-devel
Requires:	libxdamage-devel
Requires:	libxdmcp-devel
Requires:	libxevie-devel
Requires:	libxext-devel
Requires:	libxfixes-devel
Requires:	libxfontcache-devel
Requires:	libxfont-devel
Requires:	libxft-devel
Requires:	libxi-devel
Requires:	libxinerama-devel
Requires:	libxkbfile-devel
Requires:	libxkbui-devel
Requires:	libxmu-devel
Requires:	xpm-devel
Requires:	libxrandr-devel
Requires:	libxrender-devel
Requires:	libxres-devel
Requires:	libxscrnsaver-devel
Requires:	libxt-devel
Requires:	libxtrap-devel
Requires:	libxtst-devel
Requires:	pkgconfig(xv)
Requires:	libxvmc-devel
Requires:	libxxf86dga-devel
Requires:	libxxf86misc-devel
Requires:	libxxf86vm-devel
Requires:	x11-proto-devel
Requires:	x11-server-devel
Requires:	x11-xtrans-devel

Obsoletes:	 %{libxorg}-static-devel

%description -n %{libxorg}-devel
Development tools and files for X11.

%files -n %{libxorg}-devel

#------------------------------------------------------------------------------

%package 75dpi-fonts
Summary:	A set of 75 dpi resolution fonts for the X Window System
Group:		System/Fonts/X11 bitmap
Obsoletes:	XFree86-75dpi-fonts
Provides:	XFree86-75dpi-fonts = %{version}-%{release}
Provides:	X11-75dpi-fonts
Requires:	x11-font-adobe-75dpi
Requires:	x11-font-alias
Requires:	x11-font-bh-75dpi
Requires:	x11-font-bh-lucidatypewriter-75dpi
Requires:	x11-font-bitstream-75dpi

%description 75dpi-fonts
X11-75dpi-fonts contains the 75 dpi fonts used
on most X Window Systems. If you're going to use the
X Window System, you should install this package, unless
you have a monitor which can support 100 dpi resolution.
In that case, you may prefer the 100dpi fonts available in
the X11-100dpi-fonts package.

%files 75dpi-fonts

#------------------------------------------------------------------------------

%package 100dpi-fonts
Summary:	X Window System 100dpi fonts
Group:		System/Fonts/X11 bitmap
Obsoletes:	XFree86-ISO8859-2-100dpi-fonts, XFree86-ISO8859-9-100dpi-fonts
Provides:	XFree86-ISO8859-2-100dpi-fonts, XFree86-ISO8859-9-100dpi-fonts
Obsoletes:	XFree86-100dpi-fonts
Provides:	XFree86-100dpi-fonts = %{version}-%{release}
Provides:	X11-100dpi-fonts

Requires:	x11-font-adobe-100dpi
Requires:	x11-font-alias
Requires:	x11-font-bh-100dpi
Requires:	x11-font-bh-lucidatypewriter-100dpi
Requires:	x11-font-bitstream-100dpi

%description 100dpi-fonts
If you're going to use the X Window System and you have a
high resolution monitor capable of 100 dpi, you should install
X11-100dpi-fonts. This package contains a set of
100 dpi fonts used on most Linux systems.

%files 100dpi-fonts


