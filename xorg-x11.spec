%define libxorg %mklibname xorg-x11

Name:		xorg-x11
Version:	7.7
Release:	4
Summary:	X11 metapackage
Group:		Development/X11
License:	MIT

Requires:	x11-data-bitmaps
Requires:	x11-server-xorg
Requires:	x11-apps
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
Requires:	libxinerama
Requires:	libxkbfile
Requires:	libxkbui
Requires:	libxmu
Requires:	libxpm
Requires:	libxrandr
Requires:	libxrender
Requires:	libxres
Requires:	libxscrnsaver
Requires:	libxt
Requires:	libxtrap
Requires:	libxtst
Requires:	libxv
Requires:	libxvmc
Requires:	libxxf86dga
Requires:	libxxf86misc
Requires:	libxxf86vm

%description -n %{libxorg}
X11 libraries

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
Requires:	libmesaglu-devel
Requires:	pkgconfig(glut)
#Requires:	pkgconfig(glw)
Requires:	liboldx-devel
Requires:	pkgconfig(sm)
Requires:	libwindowswm-devel
Requires:	libx11-devel
Requires:	libxau-devel
Requires:	libxaw-devel
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
Requires:	libxpm-devel
Requires:	libxrandr-devel
Requires:	libxrender-devel
Requires:	libxres-devel
Requires:	libxscrnsaver-devel
Requires:	libxt-devel
Requires:	libxtrap-devel
Requires:	libxtst-devel
Requires:	libxv-devel
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



%changelog
* Wed Jun 13 2012 Matthew Dawkins <mattydaw@mandriva.org> 7.7-2
+ Revision: 805449
- rebuild removed requires for obsolete libapplewm

* Tue Jun 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 7.7-1
+ Revision: 805279
- new xorg version 7.7
- cleaned up spec
- obsoleted static pkg

* Wed May 25 2011 Funda Wang <fwang@mandriva.org> 7.6-1
+ Revision: 678960
- should be 7.6 for xserver 1.9 and libx11 1.4

* Thu Apr 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 7.5-7
+ Revision: 660099
- Do not requires applewm*devel for now, it need to be fixed first

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 7.5-6
+ Revision: 647358
- rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 7.5-5mdv2011.0
+ Revision: 608226
- rebuild

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - x11-data-xkbdata and xkbcomp are already indirectly required by x11-server-xorg

* Fri Feb 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 7.5-4mdv2010.1
+ Revision: 501232
- xorg-x11-cyrillic-fonts obsoleted by x11-font-cyrillic

* Thu Jan 21 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 7.5-3mdv2010.1
+ Revision: 494629
- Don't require non-free fonts

* Thu Jan 14 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 7.5-2mdv2010.1
+ Revision: 491475
- Obsolete X11R6-contrib

* Fri Nov 13 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 7.5-1mdv2010.1
+ Revision: 465890
- Remove obsolete packages:
  xorg-x11-server
  X11R6-contrib
- Remove obsolete packages:
  xorg-x11-xfs
  xorg-x11-Xvfb
  xorg-x11-Xnest
  xorg-x11-xauth
  xorg-x11-doc

* Fri Oct 16 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 7.3-6mdv2010.0
+ Revision: 457926
- Remove Xdmx package since it doesn't exist in current cooker (2010.0)

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 7.3-5mdv2009.1
+ Revision: 350874
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 7.3-4mdv2009.0
+ Revision: 266144
- rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Oden Eriksson <oeriksson@mandriva.com> 7.3-3mdv2009.0
+ Revision: 213505
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 7.3-1mdv2008.1
+ Revision: 97197
- new version: 7.3 (to reflect the x.org global release)

* Thu Aug 30 2007 Frederic Crozat <fcrozat@mandriva.com> 7.2.0-2mdv2008.0
+ Revision: 75573
- Remove old Prereq, not needed in this package
- Add dependency on liberation font

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 7.2.0-1mdv2008.0
+ Revision: 49154
- Major update to sync this meta-package with the current xorg packages:
 - increase version to 7.2.0 (to match the current xorg upstream release)
 - fix license (s/GPL/MIT/)
 - remove requirement for xfs from the xserver (xfs was deprecated in
   favor of the new fontpath.d schema)
 - remove requirements for xprint libraries (xprint support is
   disabled on xserver)
 - remove Xprt package (xprint is not being generated by the
   xserver package anymore)
 - remove xfs trigger that removed the X11R6 path from the
   config file (there's a compatibility symlink already)


* Mon Sep 18 2006 Pixel <pixel@mandriva.com>
+ 2006-09-18 18:52:34 (62003)
- use a versioned provides XFree86-xfs as used to be (other conflicts with initscripts)

* Mon Sep 18 2006 Pixel <pixel@mandriva.com>
+ 2006-09-18 18:50:57 (62002)
- use a versioned provides XFree86-xfs as used to be (other conflicts with initscripts)

* Mon Sep 18 2006 Pixel <pixel@mandriva.com>
+ 2006-09-18 16:16:45 (61940)
- restore obsolete/provide from xorg-x11-xfs on XFree86-xfs

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:21:00 (59426)
- requires fonts-ttf-dejavu instead of fonts-ttf-bitstream-vera (#13493)

* Mon Aug 21 2006 Pixel <pixel@mandriva.com>
+ 2006-08-21 13:41:03 (56961)
- handle xfs config file migration to /usr/share/fonts (was done in package xfs)

* Mon Aug 14 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-14 14:03:41 (55963)
- Remove old legacy xaw libs as explicit requires. Current one in libxaw8

* Mon Jun 12 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-12 21:03:43 (37126)
- Fixed buildroot of package

* Mon Jun 12 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-12 20:34:22 (37124)
- provides should use the version of the metapackage

* Thu Jun 08 2006 Anssi Hannula <anssi@mandriva.org>
+ 2006-06-08 22:40:55 (36846)
- fix Release, we are not yet in 6mdv
- arch the package to fix libxorg-x11 upgrading issue on x86_64

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Fri May 19 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-19 22:55:03 (27804)
- 5mdk

* Fri May 19 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-19 22:52:33 (27803)
- do not own /usr/lib/X11 directory

* Thu May 18 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-18 15:14:37 (27616)
- increase the release

* Thu May 18 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-18 15:13:50 (27615)
- Requires for the metapackage x11-tools

* Thu May 11 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-11 17:05:35 (27119)
- incrementing release

* Thu May 11 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-11 16:40:06 (27110)
- created metapackages mapping the old xorg package layout.
  By doing this urpmi can handle the upgrade much better.

* Fri May 05 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-05 21:32:13 (26967)
- adding missing spec file

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

