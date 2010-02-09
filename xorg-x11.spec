%define libxorg %mklibname xorg-x11

Name: xorg-x11
Version: 7.5
Release: %mkrel 4
Summary: X11 metapackage
Group: Development/X11
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

Requires: x11-data-bitmaps
Requires: x11-server-xorg
Requires: x11-apps
Requires: x11-tools
Requires: x11-docs
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-liberation
Requires: x11-font-type1
Requires: x11-font-misc 
Requires: libx11
Requires: x11-data-cursor-themes

Obsoletes: X11R6-contrib

%description
X11 metapackage

%files
%defattr(-,root,root)

#------------------------------------------------------------------------------
%package -n %{libxorg}
Summary: X11 libraries
Group: Development/X11
License: MIT

Requires: libapplewm
Requires: libdmx
Requires: libdrm
Requires: libfontenc
Requires: libfs
Requires: libice
Requires: liblbxutil
Requires: liboldx
Requires: libsm
Requires: libwindowswm
Requires: libx11
Requires: libxau
Requires: libxaw7
Requires: libxcomposite
Requires: libxcursor
Requires: libxdamage
Requires: libxdmcp
Requires: libxevie
Requires: libxext
Requires: libxfixes
Requires: libxfontcache
Requires: libxfont
Requires: libxft
Requires: libxi
Requires: libxinerama
Requires: libxkbfile
Requires: libxkbui
Requires: libxmu
Requires: libxpm
Requires: libxrandr
Requires: libxrender
Requires: libxres
Requires: libxscrnsaver
Requires: libxt
Requires: libxtrap
Requires: libxtst
Requires: libxv
Requires: libxvmc
Requires: libxxf86dga
Requires: libxxf86misc
Requires: libxxf86vm

%description -n %{libxorg}
X11 libraries

%files -n %{libxorg}
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package -n %{libxorg}-devel
Summary: Development tools and files for X11
Group: Development/X11
Provides: XFree86-devel = %{version}
Provides: X11-devel = %{version}

Requires: libapplewm-devel
Requires: libdmx-devel
Requires: libdrm-devel
Requires: libfontenc-devel
Requires: libfs-devel
Requires: libice-devel
Requires: liblbxutil-devel
Requires: libmesagl-devel
Requires: libmesaglu-devel
Requires: libmesaglut-devel
Requires: libmesaglw-devel
Requires: liboldx-devel
Requires: libsm-devel
Requires: libwindowswm-devel
Requires: libx11-devel
Requires: libxau-devel
Requires: libxaw-devel
Requires: libxcomposite-devel
Requires: libxcursor-devel
Requires: libxdamage-devel
Requires: libxdmcp-devel
Requires: libxevie-devel
Requires: libxext-devel
Requires: libxfixes-devel
Requires: libxfontcache-devel
Requires: libxfont-devel
Requires: libxft-devel
Requires: libxi-devel
Requires: libxinerama-devel
Requires: libxkbfile-devel
Requires: libxkbui-devel
Requires: libxmu-devel
Requires: libxpm-devel
Requires: libxrandr-devel
Requires: libxrender-devel
Requires: libxres-devel
Requires: libxscrnsaver-devel
Requires: libxt-devel
Requires: libxtrap-devel
Requires: libxtst-devel
Requires: libxv-devel
Requires: libxvmc-devel
Requires: libxxf86dga-devel
Requires: libxxf86misc-devel
Requires: libxxf86vm-devel
Requires: x11-proto-devel
Requires: x11-server-devel
Requires: x11-xtrans-devel

%description -n %{libxorg}-devel
Development tools and files for X11

%files -n %{libxorg}-devel
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package -n %{libxorg}-static-devel
Summary: Development tools and files for X11
Group: Development/X11
Provides: XFree86-static-devel = %{version}
Provides: X11-static-devel = %{version}

Requires: libapplewm-static-devel
Requires: libdmx-static-devel
Requires: libdrm-static-devel
Requires: libfontenc-static-devel
Requires: libfs-static-devel
Requires: libice-static-devel
Requires: liblbxutil-static-devel
Requires: liboldx-static-devel
Requires: libsm-static-devel
Requires: libwindowswm-static-devel
Requires: libx11-static-devel
Requires: libxau-static-devel
Requires: libxaw-static-devel
Requires: libxcomposite-static-devel
Requires: libxcursor-static-devel
Requires: libxdamage-static-devel
Requires: libxdmcp-static-devel
Requires: libxevie-static-devel
Requires: libxext-static-devel
Requires: libxfixes-static-devel
Requires: libxfontcache-static-devel
Requires: libxfont-static-devel
Requires: libxft-static-devel
Requires: libxi-static-devel
Requires: libxinerama-static-devel
Requires: libxkbfile-static-devel
Requires: libxkbui-static-devel
Requires: libxmu-static-devel
Requires: libxpm-static-devel
Requires: libxrandr-static-devel
Requires: libxrender-static-devel
Requires: libxres-static-devel
Requires: libxscrnsaver-static-devel
Requires: libxt-static-devel
Requires: libxtrap-static-devel
Requires: libxtst-static-devel
Requires: libxv-static-devel
Requires: libxvmc-static-devel
Requires: libxxf86dga-static-devel
Requires: libxxf86misc-static-devel
Requires: libxxf86vm-static-devel

%description -n %{libxorg}-static-devel
Development tools and files for X11

%files -n %{libxorg}-static-devel
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package 75dpi-fonts
Summary: A set of 75 dpi resolution fonts for the X Window System
Group: System/Fonts/X11 bitmap
Obsoletes: XFree86-75dpi-fonts
Provides: XFree86-75dpi-fonts = %{version}-%{release}
Provides: X11-75dpi-fonts

Requires: x11-font-adobe-75dpi
Requires: x11-font-alias
Requires: x11-font-bh-75dpi
Requires: x11-font-bh-lucidatypewriter-75dpi
Requires: x11-font-bitstream-75dpi

%description 75dpi-fonts
X11-75dpi-fonts contains the 75 dpi fonts used
on most X Window Systems. If you're going to use the
X Window System, you should install this package, unless
you have a monitor which can support 100 dpi resolution.
In that case, you may prefer the 100dpi fonts available in
the X11-100dpi-fonts package.

%files 75dpi-fonts
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package 100dpi-fonts
Summary: X Window System 100dpi fonts
Group: System/Fonts/X11 bitmap
Obsoletes: XFree86-ISO8859-2-100dpi-fonts, XFree86-ISO8859-9-100dpi-fonts
Provides: XFree86-ISO8859-2-100dpi-fonts, XFree86-ISO8859-9-100dpi-fonts
Obsoletes: XFree86-100dpi-fonts
Provides: XFree86-100dpi-fonts = %{version}-%{release}
Provides: X11-100dpi-fonts

Requires: x11-font-adobe-100dpi
Requires: x11-font-alias
Requires: x11-font-bh-100dpi
Requires: x11-font-bh-lucidatypewriter-100dpi
Requires: x11-font-bitstream-100dpi

%description 100dpi-fonts
If you're going to use the X Window System and you have a
high resolution monitor capable of 100 dpi, you should install
X11-100dpi-fonts. This package contains a set of
100 dpi fonts used on most Linux systems.

%files 100dpi-fonts
%defattr(-,root,root)

#------------------------------------------------------------------------------
