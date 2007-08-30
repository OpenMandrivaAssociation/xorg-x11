%define libxorg %mklibname xorg-x11

Name: xorg-x11
Version: 7.2.0
Release: %mkrel 2
Summary: X11 metapackage
Group: Development/X11
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

Requires: x11-data-xkbdata
Requires: x11-data-bitmaps
Requires: x11-server-xorg
Requires: x11-apps
Requires: x11-tools
Requires: x11-docs
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-liberation
Requires: x11-font-bh-ttf
Requires: x11-font-type1
Requires: x11-font-misc 
Requires: libx11
Requires: x11-data-cursor-themes
Requires: xkbcomp

%description
X11 metapackage

%install 
mkdir -p %{buildroot}%{_libdir}/X11

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
Requires: libxaw8
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
Requires: x11-font-adobe-utopia-75dpi
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
Requires: x11-font-adobe-utopia-100dpi
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

%package cyrillic-fonts
Summary: Cyrillic fonts - only needed on the server side
Group: System/Fonts/X11 bitmap
Obsoletes: XFree86-cyrillic-fonts
Provides: XFree86-cyrillic-fonts = %{version}-%{release}
Provides: X11-cyrillic-fonts

Requires: x11-font-alias
Requires: x11-font-cronyx-cyrillic
Requires: x11-font-misc-cyrillic
Requires: x11-font-screen-cyrillic
Requires: x11-font-winitzki-cyrillic

%description cyrillic-fonts
The Cyrillic fonts included with XFree86 3.3.2 and higher. Those who
use a language requiring the Cyrillic character set should install
this package.

%files cyrillic-fonts
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package doc
Summary: Documentation on various X11 programming interfaces
Group: System/X11
Obsoletes: XFree86-doc
Provides: XFree86-doc = %{version}-%{release}
Provides: X11-doc
Requires: x11-docs

%description doc
X11-doc provides a great deal of extensive PostScript documentation
on the various X APIs, libraries, and other interfaces.  If you need
low level X documentation, you will find it here.  Topics include the
X protocol, the ICCCM window manager standard, ICE session management,
the font server API, etc.

%files doc 
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package server
Summary: The X server and associated modules
Group: System/X11
Requires: %{name} = %{version}
Obsoletes: xserver-wrapper
Obsoletes: XFree86-server
Provides: XFree86-server  = %{version}-%{release}
Provides: X11-server
Conflicts: nvidia <= 7676-2mdk
Requires: x11-server-xorg
Requires: x11-driver-video
Requires: x11-driver-input

%description server
X11-xorg-server is the new generation of X server from X.Org.

%files server 
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package -n X11R6-contrib
Summary:        A collection of user-contributed X Window System programs
Group:          System/X11
Requires:       %{name} = %{version}
Requires: ico
Requires: listres
Requires: viewres
Requires: xbiff
Requires: xcalc
Requires: xditview
Requires: xedit
Requires: xev
Requires: xeyes
Requires: xfontsel
Requires: xgc
Requires: xload
Requires: xman
Requires: xmessage

%description -n X11R6-contrib
If you want to use the X Window System, you should install X11R6-contrib. This
package holds many useful programs from the X Window System, version 11,
release 6 contrib tape. The programs, contributed by various users, include
listres, xbiff, xedit, xeyes, xcalc, xload and xman, among others.

%files -n X11R6-contrib
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package Xvfb
Summary: A virtual framebuffer X Windows System server for X11
Group: System/X11
Requires: %{name} = %{version}
Obsoletes: XFree86-Xvfb
Provides: XFree86-Xvfb = %{version}-%{release}
Provides: X11-Xvfb
Requires: x11-server-xvfb

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Windows System server
that is capable of running on machines with no display hardware and no
physical input devices.  Xvfb emulates a dumb framebuffer using virtual
memory.  Xvfb doesn't open any devices, but behaves otherwise as an X
display.  Xvfb is normally used for testing servers.  Using Xvfb, the mfb
or cfb code for any depth can be exercised without using real hardware
that supports the desired depths.  Xvfb has also been used to test X
clients against unusual depths and screen configurations, to do batch
processing with Xvfb as a background rendering engine, to do load testing,
to help with porting an X server to a new platform, and to provide an
unobtrusive way of running applications which really don't need an X
server but insist on having one.

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%files Xvfb 
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package xauth
Summary: Authentication information tool for X
Group: System/X11
Requires: xauth 


%description xauth
The xauth program is used to edit and display the authorization information
used in connecting to the X server.

%files xauth 
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package Xnest
Summary: A nested X11 server
Group: System/X11
Requires: %{name} = %{version}
Obsoletes: XFree86-Xnest
Provides: XFree86-Xnest = %{version}-%{release}
Provides: X11-Xnest
Requires: x11-server-xnest

%description Xnest
Xnest is an X Window System server which runs in an X window.
Xnest is a 'nested' window server, actually a client of the
real X server, which manages windows and graphics requests
for Xnest, while Xnest manages the windows and graphics
requests for its own clients.

You will need to install Xnest if you require an X server which
will run as a client of your real X server (perhaps for
testing purposes).

%files Xnest 
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package Xdmx
Summary: Distributed Multi-head X server
Group: System/X11
Requires: %{name} = %{version}
Provides: XFree86-Xdmx = %{version}-%{release}
Provides: X11-Xdmx
Requires: x11-server-xdmx

%description Xdmx
Xdmx is a proxy X server that uses one or more other X servers
as its display devices. It provides multi-head X functionality
for displays that might be located on different machines.
 Xdmx functions as a front-end X server that acts as a proxy
to a set of back-end X servers. All of the visible rendering is
passed to the back-end X servers. Clients connect to the Xdmx
front-end, and everything appears as it would in a regular
multi-head configuration. If Xinerama is enabled (e.g.,
with +xinerama on the command line), the clients see a single large screen.

Xdmx communicates to the back-end X servers using the standard X11 protocol,
and standard and/or commonly available X server extensions.

%files Xdmx 
%defattr(-,root,root)

#------------------------------------------------------------------------------

%package xfs
Group: System/Servers
Summary: Font server for X11
Requires: initscripts >= 5.27-28mdk
Requires: xfs
Obsoletes: XFree86-xfs
Provides: XFree86-xfs = %{version}-%{release}

%description xfs
This is a font server for X11.  You can serve fonts to other X servers
remotely with this package, and the remote system will be able to use all
fonts installed on the font server, even if they are not installed on the
remote computer.

%files xfs
%defattr(-,root,root)

#------------------------------------------------------------------------------

