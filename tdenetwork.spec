%bcond clang 1
%bcond aim 1
%bcond avahi 1
%bcond gadu 1
%bcond gamin 1
%bcond wifi 0
%bcond openslp 1
%bcond xmms 0
%bcond meanwhile 1
%bcond speex 1
%bcond consolehelper 1
%bcond xinetd 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdenetwork
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# Avoids relinking, which breaks consolehelper
%define dont_relink 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:			trinity-%{tde_pkg}
Summary:		Trinity Desktop Environment - Network Applications
Group:			Applications/Internet
Version:		%{tde_version}
Release:		%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:	kppp.pamd
Source2:	ktalk
Source3:	trinity-tdenetwork-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DWITH_JINGLE=ON -DWITH_WEBCAM=ON -DWITH_GSM=OFF
BuildOption:    -DWITH_XMMS=OFF -DWITH_ARTS=ON -DBUILD_ALL=ON
BuildOption:    -DBUILD_KOPETE_PLUGIN_ALL=ON
BuildOption:    -DBUILD_KOPETE_PROTOCOL_ALL=ON
BuildOption:    -DBUILD_KOPETE_PLUGIN_MOTIONAUTOAWAY=OFF
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_SPEEX=%{!?with_speex:OFF}%{?with_speex:ON}
BuildOption:    -DWITH_SLP=%{!?with_openslp:OFF}%{?with_openslp:ON}
BuildOption:    -DBUILD_KOPETE_PROTOCOL_GADU=%{!?with_gadu:OFF}%{?with_gadu:ON}
BuildOption:    -DBUILD_KOPETE_PROTOCOL_MEANWHILE=%{!?with_meanwhile:OFF}%{?with_meanwhile:ON}
BuildOption:    -DBUILD_WIFI=%{!?with_wifi:OFF}%{?with_wifi:ON}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	libtqca-devel >= %{tde_epoch}:1.0

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gettext
BuildRequires:	coreutils 

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	desktop-file-utils
BuildRequires:	fdupes

# AVAHI support
%{?with_avahi:BuildRequires:  pkgconfig(avahi-client)}

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# TLS support
BuildRequires:	pkgconfig(gnutls)

# SQLITE support
BuildRequires:  pkgconfig(sqlite3)

# GADU support
%{?with_gadu:BuildRequires:  pkgconfig(libgadu)}

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# XTST support
BuildRequires:  pkgconfig(xtst)

# XMU support
BuildRequires:  pkgconfig(xmu)

BuildRequires:  pkgconfig(xrender)

# OpenSLP support
%{?with_openslp:BuildRequires: openslp-devel}

%{?with_xmms:BuildRequires: xmms-devel}

# V4L support
BuildRequires:	%{_lib}v4l-devel

# XML support
BuildRequires:	pkgconfig(libxml-2.0)

# XSLT support
BuildRequires:  pkgconfig(libxslt)

#jabber
BuildRequires:	pkgconfig(libidn)
#jabber/jingle
BuildRequires:  pkgconfig(expat)

BuildRequires:	pkgconfig(glib-2.0)

# ACL support
BuildRequires:  pkgconfig(libacl)

# MEANWHILE support
%{?with_meanwhile:BuildRequires:	pkgconfig(meanwhile)}


# SPEEX support
%{?with_speex:BuildRequires:	pkgconfig(speex)}


# XINETD support
%{?with_xinetd:Requires:		xinetd}

Obsoletes:	trinity-kdenetwork < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdenetwork-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdenetwork-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdenetwork < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdenetwork = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-dcoprss = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-filesharing = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kdict = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdefile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kget = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-knewsticker = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kopete = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kopete-nowlistening = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpf = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kppp = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-krdc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-krfb = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksirc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktalkd = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with wifi}
Requires: trinity-kwifimanager = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: trinity-librss = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-lisa = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This metapackage includes a collection of network and networking related
applications provided with the official release of Trinity.

Networking applications, including:
* dcoprss: RSS utilities for Trinity
* filesharing: Network filesharing configuration module for Trinity
* kdict: Dictionary client for Trinity
* tdefile-plugins: Torrent metainfo plugin for Trinity
* kget: downloader manager
* knewsticker: RDF newsticker applet
* kopete: chat client
* kopete-nowlistening: (xmms) plugin for Kopete.
* kpf: Public fileserver for Trinity
* kppp: dialer and front end for pppd
* krdc: a client for Desktop Sharing and other VNC servers
* krfb: Desktop Sharing server, allow others to access your desktop via VNC
* ksirc: IRC client for Trinity
* ktalkd: Talk daemon for Trinity
%if %{with wifi}
* kwifimanager: Wireless lan manager for Trinity
%endif
* librss: RSS library for Trinity
* lisa: lan information server

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README


##########

%package -n trinity-dcoprss
Summary:		RSS utilities for Trinity
Group:			Applications/Internet

%description -n trinity-dcoprss
dcoprss is a RSS to DCOP bridge, allowing all
DCOP aware applications to access RSS news feeds. There is also
a few sample utilities provided.
RSS is a standard for publishing news headlines.
DCOP is the TDE interprocess communication protocol.

%files -n trinity-dcoprss
%defattr(-,root,root,-)
%{tde_prefix}/bin/feedbrowser
%{tde_prefix}/bin/rssclient
%{tde_prefix}/bin/rssservice
%{tde_prefix}/share/services/rssservice.desktop

##########

%package devel
Summary:		Development files for the Trinity network module
Group:			Development/Libraries/Other
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-kdict = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-kopete = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-ksirc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-librss = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-tdelibs-devel >= %{tde_version}

Obsoletes:	trinity-kdenetwork-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdenetwork-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdenetwork-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdenetwork-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This is the development package which contains the headers for the TDE RSS
library as well as the Kopete chat client, as well as miscellaneous
development-related files for the TDE network module.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kopete/
%{tde_prefix}/include/tde/rss/
%{tde_prefix}/%{_lib}/libkopete.la
%{tde_prefix}/%{_lib}/libkopete.so
%if %{with aim}
%{tde_prefix}/%{_lib}/libkopete_msn_shared.la
%{tde_prefix}/%{_lib}/libkopete_msn_shared.so
%endif
%{tde_prefix}/%{_lib}/libkopete_oscar.la
%{tde_prefix}/%{_lib}/libkopete_oscar.so
%{tde_prefix}/%{_lib}/libkopete_videodevice.la
%{tde_prefix}/%{_lib}/libkopete_videodevice.so
%{tde_prefix}/%{_lib}/librss.la
%{tde_prefix}/%{_lib}/librss.so

##########

%package filesharing
#Recommends:	perl-suid
Summary:		Network filesharing configuration module for Trinity
Group:   		Applications/Internet

Obsoletes:		tdenetwork-filesharing < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		tdenetwork-filesharing = %{?epoch:%{epoch}:}%{version}-%{release}

%description filesharing
This package provides a Trinity Control Center module to configure
NFS and Samba.

%files filesharing
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/fileshare_propsdlgplugin.la
%{tde_prefix}/%{_lib}/trinity/fileshare_propsdlgplugin.so
%{tde_prefix}/%{_lib}/trinity/kcm_fileshare.la
%{tde_prefix}/%{_lib}/trinity/kcm_fileshare.so
%{tde_prefix}/%{_lib}/trinity/kcm_kcmsambaconf.la
%{tde_prefix}/%{_lib}/trinity/kcm_kcmsambaconf.so
%{tde_prefix}/share/applications/tde/fileshare.desktop
%{tde_prefix}/share/applications/tde/kcmsambaconf.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kcmfileshare.png
%{tde_prefix}/share/icons/hicolor/*/apps/kcmsambaconf.png
%{tde_prefix}/share/services/fileshare_propsdlgplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/fileshare/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmsambaconf/

##########

%package -n trinity-kdict
Summary:		Dictionary client for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-kdict
KDict is an advanced TDE graphical client for the DICT Protocol, with full
Unicode support. It enables you to search through dictionary databases for a
word or phrase, then displays suitable definitions. KDict tries to ease
basic as well as advanced queries.

%files -n trinity-kdict
%defattr(-,root,root,-)
%{tde_prefix}/bin/kdict
%{tde_prefix}/%{_lib}/trinity/kdict.*
%{tde_prefix}/%{_lib}/trinity/kdict_panelapplet.*
%{tde_prefix}/%{_lib}/libtdeinit_kdict.*
%{tde_prefix}/share/applications/tde/kdict.desktop
%{tde_prefix}/share/apps/kdict
%{tde_prefix}/share/apps/kicker/applets/kdictapplet.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kdict.*
%{tde_prefix}/share/doc/tde/HTML/en/kdict
%{tde_prefix}/share/man/man1/kdict.1*

##########

%package tdefile-plugins
Summary:		Torrent metainfo plugin for Trinity
Group:			Applications/Internet

Obsoletes:		tdenetwork-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		tdenetwork-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-tdenetwork-kfile-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-tdenetwork-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdefile-plugins
This package provides a metainformation plugin for bittorrent files.
TDE uses tdefile-plugins to provide metainfo tab in the files properties
dialog in konqueror and other file-handling applications.

%files tdefile-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdefile_torrent.la
%{tde_prefix}/%{_lib}/trinity/tdefile_torrent.so
%{tde_prefix}/share/services/tdefile_torrent.desktop

##########

%package -n trinity-kget
Summary:		Download manager for Trinity
Group:			Applications/Internet
Requires:		trinity-tdebase-data >= %{tde_version}
Requires:		trinity-konqueror >= %{tde_version}

%description -n trinity-kget
KGet is a a download manager similar to GetRight or Go!zilla. It keeps
all your downloads in one dialog and you can add and remove transfers.
Transfers can be paused, resumed, queued or scheduled.
Dialogs display info about status of transfers - progress, size, speed
and remaining time. Program supports drag & drop from TDE
applications and Netscape.

%files -n trinity-kget
%defattr(-,root,root,-)
%{tde_prefix}/bin/kget
%{tde_prefix}/%{_lib}/trinity/tdehtml_kget.la
%{tde_prefix}/%{_lib}/trinity/tdehtml_kget.so
%{tde_prefix}/share/applications/tde/kget.desktop
%{tde_prefix}/share/apps/kget
%{tde_prefix}/share/apps/tdehtml/kpartplugins/kget_plug_in.desktop
%{tde_prefix}/share/apps/tdehtml/kpartplugins/kget_plug_in.rc
%{tde_prefix}/share/apps/konqueror/servicemenus/kget_download.desktop
%{tde_prefix}/share/icons/crystalsvg/*/actions/tdehtml_kget.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kget.png
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/kget_list.png
%{tde_prefix}/share/icons/hicolor/*/apps/kget.png
%{tde_prefix}/share/mimelnk/application/x-kgetlist.desktop
%{tde_prefix}/share/sounds/KGet_Added.ogg
%{tde_prefix}/share/sounds/KGet_Finished.ogg
%{tde_prefix}/share/sounds/KGet_Finished_All.ogg
%{tde_prefix}/share/sounds/KGet_Started.ogg
%{tde_prefix}/share/doc/tde/HTML/en/kget
%{tde_prefix}/share/man/man1/kget.1*

##########

%package -n trinity-knewsticker
Summary:		News ticker applet for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-knewsticker
This is a news ticker applet for the Trinity panel. It can scroll news from
your favorite news sites, such as lwn.net, /. and freshmeat.net.
To achieve this, KNewsTicker requires the news sites to provide a
RSS feed to newsitems. KNewsTicker already comes with a selection of
good news sources which provide such files.

%files -n trinity-knewsticker
%defattr(-,root,root,-)
%{tde_prefix}/bin/knewstickerstub
%{tde_prefix}/%{_lib}/trinity/knewsticker_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/knewsticker_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/libkntsrcfilepropsdlg.la
%{tde_prefix}/%{_lib}/trinity/libkntsrcfilepropsdlg.so
%{tde_prefix}/share/applications/tde/knewsticker-standalone.desktop
%{tde_prefix}/share/applnk/.hidden/knewstickerstub.desktop
%{tde_prefix}/share/apps/tdeconf_update/knewsticker.upd
%{tde_prefix}/share/apps/tdeconf_update/knt-0.1-0.2.pl
%{tde_prefix}/share/apps/kicker/applets/knewsticker.desktop
%{tde_prefix}/share/apps/knewsticker/
%{tde_prefix}/share/icons/hicolor/*/apps/knewsticker.png
%{tde_prefix}/share/services/kntsrcfilepropsdlg.desktop
%{tde_prefix}/share/doc/tde/HTML/en/knewsticker

##########

%package -n trinity-kopete
Summary:		Instant messenger for Trinity
Group:			Applications/Internet
Requires:		trinity-tdebase-bin >= %{tde_version}
Requires:		trinity-tdebase-data >= %{tde_version}
Requires:		trinity-filesystem >= %{tde_version}

%description -n trinity-kopete
Kopete is an instant messenger program which can communicate with a variety
of IM systems, such as Yahoo, ICQ, IRC and Jabber.

Support for more IM protocols can be added through a plugin system.

%files -n trinity-kopete
%defattr(-,root,root,-)
# nowlistening support
%exclude %{tde_prefix}/share/apps/kopete/*nowlisteningchatui*
%exclude %{tde_prefix}/share/apps/kopete/*nowlisteningui*
%exclude %{tde_prefix}/share/config.kcfg/nowlisteningconfig.kcfg
%exclude %{tde_prefix}/share/services/tdeconfiguredialog/*nowlistening*
%exclude %{tde_prefix}/share/services/*nowlistening*
%exclude %{tde_prefix}/%{_lib}/trinity/*nowlistening*
# Main kopete package
%{tde_prefix}/bin/kopete
%{tde_prefix}/bin/kopete_latexconvert.sh
%{tde_prefix}/%{_lib}/tdeconf_update_bin/kopete-account-tdeconf_update
%{tde_prefix}/%{_lib}/tdeconf_update_bin/kopete-nameTracking-tdeconf_update
%{tde_prefix}/%{_lib}/tdeconf_update_bin/kopete-pluginloader2-tdeconf_update
%{tde_prefix}/%{_lib}/trinity/kcm_kopete_*.so
%{tde_prefix}/%{_lib}/trinity/kcm_kopete_*.la
%{tde_prefix}/%{_lib}/trinity/tdeio_jabberdisco.la
%{tde_prefix}/%{_lib}/trinity/tdeio_jabberdisco.so
%{tde_prefix}/%{_lib}/trinity/kopete_*.la
%{tde_prefix}/%{_lib}/trinity/kopete_*.so
%{tde_prefix}/%{_lib}/trinity/libkrichtexteditpart.la
%{tde_prefix}/%{_lib}/trinity/libkrichtexteditpart.so
%{tde_prefix}/%{_lib}/libkopete_oscar.so.*
%{tde_prefix}/%{_lib}/libkopete.so.*
%{tde_prefix}/%{_lib}/libkopete_videodevice.so.*
%{tde_prefix}/share/applications/tde/kopete.desktop
%{tde_prefix}/share/apps/tdeconf_update/kopete-*
%{tde_prefix}/share/apps/kopete/
%{tde_prefix}/share/apps/kopete_*/
%{tde_prefix}/share/apps/kopeterichtexteditpart/
%{tde_prefix}/share/config.kcfg/historyconfig.kcfg
%{tde_prefix}/share/config.kcfg/kopeteidentityconfigpreferences.kcfg
%{tde_prefix}/share/config.kcfg/kopete.kcfg
%{tde_prefix}/share/config.kcfg/latexconfig.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/actions/voicecall.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/webcamreceive.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/webcamsend.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/account_offline_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/add_user.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/contact_away_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/contact_busy_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/contact_food_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/contact_invisible_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/contact_phone_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/contact_xa_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/delete_user.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/edit_user.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/emoticon.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_away.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_chatty.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_connecting.mng
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_group.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_invisible.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_na.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_offline.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_online.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_raw.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_serv_off.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_serv_on.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/jabber_xa.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/kopeteavailable.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/kopeteaway.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/kopeteeditstatusmessage.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/kopetestatusmessage.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/metacontact_away.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/metacontact_offline.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/metacontact_online.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/metacontact_unknown.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/newmsg.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/search_user.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/show_offliners.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/status_unknown_overlay.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/status_unknown.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_aim.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_gadu.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_http-ws.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_icq.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_irc.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_msn.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_qq.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_smtp.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_tlen.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_gateway_yahoo.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/jabber_protocol.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kopete_all_away.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kopete_offline.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kopete_some_away.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/kopete_some_online.png
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/kopete_emoticons.png
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/account_offline_overlay.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/kopete.png
%{tde_prefix}/share/icons/hicolor/*/actions/emoticon.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_away.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_chatty.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_connecting.mng
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_group.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_invisible.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_na.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_offline.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_online.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_raw.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_serv_off.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_serv_on.png
%{tde_prefix}/share/icons/hicolor/*/actions/jabber_xa.png
%{tde_prefix}/share/icons/hicolor/*/actions/kopeteavailable.png
%{tde_prefix}/share/icons/hicolor/*/actions/kopeteaway.png
%{tde_prefix}/share/icons/hicolor/*/actions/newmsg.png
%{tde_prefix}/share/icons/hicolor/*/actions/status_unknown_overlay.png
%{tde_prefix}/share/icons/hicolor/*/actions/status_unknown.png
%{tde_prefix}/share/icons/hicolor/*/apps/jabber_protocol.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kopete2.svgz
%{tde_prefix}/share/icons/crystalsvg/*/actions/newmessage.mng
%{tde_prefix}/share/icons/hicolor/*/actions/newmessage.mng
%{tde_prefix}/share/icons/crystalsvg/*/apps/icq_protocol.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/irc_protocol.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_away.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_connecting.mng
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_dnd.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_ffc.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_invisible.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_na.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_occupied.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_offline.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/icq_online.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_away.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_channel.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_connecting.mng
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_normal.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_online.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_op.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_server.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/irc_voice.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_away.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_connecting.mng
%{tde_prefix}/share/icons/hicolor/*/actions/icq_dnd.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_ffc.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_invisible.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_na.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_occupied.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_offline.png
%{tde_prefix}/share/icons/hicolor/*/actions/icq_online.png
%{tde_prefix}/share/icons/hicolor/*/apps/icq_protocol.png
%{tde_prefix}/share/mimelnk/application/x-icq.desktop
%{tde_prefix}/share/mimelnk/application/x-kopete-emoticons.desktop
%{tde_prefix}/share/services/chatwindow.desktop
%{tde_prefix}/share/services/emailwindow.desktop
%{tde_prefix}/share/services/jabberdisco.protocol
%{tde_prefix}/share/services/tdeconfiguredialog/kopete_*.desktop
%{tde_prefix}/share/services/kopete_*.desktop
%{tde_prefix}/share/icons/crystalsvg/16x16/apps/jabber_gateway_sms.png
%{tde_prefix}/share/servicetypes/kopete*.desktop
%{tde_prefix}/share/sounds/Kopete_*.ogg
%{tde_prefix}/share/doc/tde/HTML/en/kopete
# jingle support for kopete
%{tde_prefix}/bin/relayserver
%{tde_prefix}/bin/stunserver
# winpopup support for kopete
%{tde_prefix}/bin/winpopup-install.sh
%{tde_prefix}/bin/winpopup-send.sh
# smpp plugin for kopete
%{tde_prefix}/share/config.kcfg/smpppdcs.kcfg
# aim support is deprecated in TDE 14.1.x
%if %{with aim}
%{tde_prefix}/share/icons/crystalsvg/*/apps/aim_protocol.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/aim_away.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/aim_connecting.mng
%{tde_prefix}/share/icons/crystalsvg/*/actions/aim_offline.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/aim_online.png
%{tde_prefix}/share/icons/hicolor/*/actions/aim_away.png
%{tde_prefix}/share/icons/hicolor/*/actions/aim_connecting.mng
%{tde_prefix}/share/icons/hicolor/*/actions/aim_offline.png
%{tde_prefix}/share/icons/hicolor/*/actions/aim_online.png
%{tde_prefix}/share/icons/hicolor/*/apps/aim_protocol.png
%{tde_prefix}/share/services/aim.protocol
%{tde_prefix}/%{_lib}/libkopete_msn_shared.so.0
%{tde_prefix}/%{_lib}/libkopete_msn_shared.so.0.0.0
%endif
%{tde_prefix}/share/man/man1/kopete.1*

##########

%package -n trinity-kopete-nowlistening
Summary:		Nowlistening (xmms) plugin for Kopete
Group:			Applications/Internet
Requires:		trinity-kopete = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		trinity-filesystem >= %{tde_version}

%description -n trinity-kopete-nowlistening
Kopete includes the "Now Listening" plug-in that can report what music you
are currently listening to, in a number of different players, including
noatun, kscd, juk, kaffeine and amarok.

%files -n trinity-kopete-nowlistening
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kopete/*nowlisteningchatui*
%{tde_prefix}/share/apps/kopete/*nowlisteningui*
%{tde_prefix}/share/config.kcfg/nowlisteningconfig.kcfg
%{tde_prefix}/share/services/tdeconfiguredialog/*nowlistening*
%{tde_prefix}/share/services/*nowlistening*
%{tde_prefix}/%{_lib}/trinity/*nowlistening*

##########

%package -n trinity-kpf
Summary:		Public fileserver for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-kpf
kpf provides simple file sharing using HTTP. kpf is strictly a public
fileserver, which means that there are no access restrictions to shared
files. Whatever you select for sharing is available to anyone. kpf is
designed to be used for sharing files with friends.

%files -n trinity-kpf
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kpf*
%{tde_prefix}/share/apps/kicker/applets/kpfapplet.desktop
%{tde_prefix}/share/icons/crystalsvg/*/apps/kpf.*
%{tde_prefix}/share/services/kpfpropertiesdialogplugin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kpf

##########

%package -n trinity-kppp
Summary:		Modem dialer and ppp frontend for Trinity
Group:			Applications/Internet
BuildRequires:	ppp
Requires:		ppp

%if %{with consolehelper}
# package 'usermode' provides '/usr/bin/consolehelper-gtk'
Requires:	usermode
%endif

%description -n trinity-kppp
KPPP is a dialer and front end for pppd. It allows for interactive
script generation and network setup. It will automate the dialing in
process to your ISP while letting you conveniently monitor the entire
process.

Once connected KPPP will provide a rich set of statistics and keep
track of the time spent online for you.

%files -n trinity-kppp
%defattr(-,root,root,-)
%if %{without consolehelper}
# Some setuid binaries need special care
%attr(4711,root,root) %{tde_prefix}/bin/kppp
%endif
%{tde_prefix}/bin/kppplogview
%{tde_prefix}/share/applications/tde/Kppp.desktop
%{tde_prefix}/share/applications/tde/kppplogview.desktop
%{tde_prefix}/share/apps/kppp/
%{tde_prefix}/share/icons/hicolor/*/apps/kppp.png
%{tde_prefix}/share/doc/tde/HTML/en/kppp/
%dir %{_sysconfdir}/ppp/peers
%{_sysconfdir}/ppp/peers/kppp-options

%if %{with consolehelper}
%config(noreplace) /etc/security/console.apps/kppp3
%config(noreplace) /etc/pam.d/kppp3
%{_sbindir}/kppp3
%{tde_prefix}/bin/kppp3
%{tde_prefix}/sbin/kppp3
%endif

##########

%package -n trinity-krdc
Summary:		Remote Desktop Connection for Trinity
Group:			Applications/Internet

# rdesktop needs a maintainer
#Requires:		rdesktop

%description -n trinity-krdc
krdc is an TDE graphical client for the rfb protocol, used by VNC,
and if rdesktop is installed, krdc can connect to Windows Terminal
Servers using RDP.

%files -n trinity-krdc
%defattr(-,root,root,-)
%{tde_prefix}/bin/krdc
%{tde_prefix}/share/applications/tde/krdc.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/smb2rdc.desktop
%{tde_prefix}/share/apps/krdc/
%{tde_prefix}/share/icons/crystalsvg/*/apps/krdc.png
%{tde_prefix}/share/icons/hicolor/*/apps/krdc.png
%{tde_prefix}/share/services/rdp.protocol
%{tde_prefix}/share/services/vnc.protocol
%{tde_prefix}/share/doc/tde/HTML/en/krdc/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/rdp/
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/vnc/

##########

%package -n trinity-krfb
Summary:		Desktop Sharing for Trinity
Group:			Applications/Internet

%description -n trinity-krfb
Desktop Sharing (krfb) is a server application that allows you to share
your current session with a user on another machine, who can use a
VNC client like krdc to view or even control the desktop. It doesn't
require you to start a new X session - it can share the current session.
This makes it very useful when you want someone to help you perform a
task.

%files -n trinity-krfb
%defattr(-,root,root,-)
%{tde_prefix}/bin/krfb
%{tde_prefix}/bin/krfb_httpd
%{tde_prefix}/%{_lib}/trinity/kcm_krfb.la
%{tde_prefix}/%{_lib}/trinity/kcm_krfb.so
%{tde_prefix}/%{_lib}/trinity/kded_kinetd.la
%{tde_prefix}/%{_lib}/trinity/kded_kinetd.so
%{tde_prefix}/share/applications/tde/kcmkrfb.desktop
%{tde_prefix}/share/applications/tde/krfb.desktop
%{tde_prefix}/share/apps/kinetd/
%{tde_prefix}/share/apps/krfb
%{tde_prefix}/share/icons/crystalsvg/*/apps/krfb.png
%{tde_prefix}/share/icons/hicolor/*/apps/krfb.png
%{tde_prefix}/share/icons/locolor/*/apps/krfb.png
%{tde_prefix}/share/services/kded/kinetd.desktop
%{tde_prefix}/share/services/kinetd_krfb.desktop
%{tde_prefix}/share/services/kinetd_krfb_httpd.desktop
%{tde_prefix}/share/servicetypes/kinetdmodule.desktop
%{tde_prefix}/share/doc/tde/HTML/en/krfb/

##########

%package -n trinity-ksirc
Summary:		IRC client for Trinity
Group:			Applications/Internet

%description -n trinity-ksirc
KSirc is an IRC chat client for TDE. It supports scripting with Perl and has a
lot of compatibility with mIRC for general use.

If you want to connect to an IRC server via SSL, you will need to install the
recommended package libio-socket-ssl-perl.

%files -n trinity-ksirc
%defattr(-,root,root,-)
%{tde_prefix}/bin/dsirc
%{tde_prefix}/bin/ksirc
%{tde_prefix}/%{_lib}/libtdeinit_ksirc.*
%{tde_prefix}/%{_lib}/trinity/ksirc.*
%{tde_prefix}/share/applications/tde/ksirc.desktop
%{tde_prefix}/share/apps/ksirc/
%config(noreplace) %{_sysconfdir}/trinity/ksircrc
%{tde_prefix}/share/icons/hicolor/*/apps/ksirc.*
%{tde_prefix}/share/doc/tde/HTML/??/ksirc/

##########

%package -n trinity-ktalkd
Summary:		Talk daemon for Trinity
Group:			Applications/Internet
Requires:		trinity-kcontrol >= %{tde_version}
Requires:		trinity-tdebase-data >= %{tde_version}
%if %{with xinetd}
Requires:		xinetd
%endif

%description -n trinity-ktalkd
KTalkd is an enhanced talk daemon - a program to handle incoming talk
requests, announce them and allow you to respond to it using a talk
client. Note that KTalkd is designed to run on a single-user workstation,
and shouldn't be run on a multi-user machine.

%files -n trinity-ktalkd
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktalkd*
%{tde_prefix}/bin/mail.local
%{tde_prefix}/%{_lib}/trinity/kcm_ktalkd.*
%{tde_prefix}/share/applications/tde/kcmktalkd.desktop
%config(noreplace) %{_sysconfdir}/trinity/ktalkdrc
%{tde_prefix}/share/icons/crystalsvg/*/apps/ktalkd.png
%{tde_prefix}/share/icons/hicolor/*/apps/ktalkd.png
%{tde_prefix}/share/sounds/ktalkd.wav
%if 0%{?with_xinetd}
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/ktalk
%endif
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmtalkd
%{tde_prefix}/share/doc/tde/HTML/en/ktalkd

##########

%if %{with wifi}

%package -n trinity-kwifimanager
Summary:		Wireless lan manager for Trinity
Group:			Applications/Internet
Requires:		trinity-kicker >= %{tde_version}

%description -n trinity-kwifimanager
KWiFiManager suite is a set of tools which allows you to manage your
wireless LAN connection under the K Desktop Environment. It provides
information about your current connection. KWiFiManager supports every
wavelan card that uses the wireless extensions interface.

%files -n trinity-kwifimanager
%defattr(-,root,root,-)
%{tde_prefix}/bin/kwifimanager
%{tde_prefix}/%{_lib}/trinity/kcm_wifi.*
%{tde_prefix}/%{_lib}/libkwireless.la
%{tde_prefix}/%{_lib}/libkwireless.so
%{tde_prefix}/share/applications/tde/kcmwifi.desktop
%{tde_prefix}/share/applications/tde/kwifimanager.desktop
%{tde_prefix}/share/apps/kicker/applets/kwireless.desktop
%{tde_prefix}/share/apps/kwifimanager
%{tde_prefix}/share/icons/hicolor/*/apps/kwifimanager.png
%{tde_prefix}/share/icons/hicolor/*/apps/kwifimanager.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kwifimanager/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmwifi/
%{tde_prefix}/share/man/man1/kwifimanager.1*

%endif

##########

%package -n trinity-librss
Summary:		RSS library for Trinity
Group:			Environment/Libraries

%description -n trinity-librss
This is the runtime package for programs that use the TDE RSS library.
End users should not need to install this, it should get installed
automatically when needed.

%files -n trinity-librss
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/librss.so.*
%{tde_prefix}/share/cmake/librss.cmake

##########

%package -n trinity-lisa
Summary:			LAN information server for Trinity
Group:				Applications/Internet
Requires:		trinity-konqueror >= %{tde_version}
Requires:		trinity-tdebase-data >= %{tde_version}

%description -n trinity-lisa
LISa is intended to provide TDE with a kind of "network neighborhood"
but relying only on the TCP/IP protocol.

%files -n trinity-lisa
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcm_lanbrowser.la
%{tde_prefix}/%{_lib}/trinity/kcm_lanbrowser.so
%{tde_prefix}/%{_lib}/trinity/tdeio_lan.la
%{tde_prefix}/%{_lib}/trinity/tdeio_lan.so
%{tde_prefix}/share/applnk/.hidden/kcmtdeiolan.desktop
%{tde_prefix}/share/applnk/.hidden/kcmlisa.desktop
%{tde_prefix}/share/applnk/.hidden/kcmreslisa.desktop
%{tde_prefix}/share/apps/konqsidebartng/virtual_folders/services/lisa.desktop
%{tde_prefix}/share/apps/konqueror/dirtree/remote/lan.desktop
%{tde_prefix}/share/apps/lisa/
%{tde_prefix}/share/apps/remoteview/lan.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/lanbrowser/
%{tde_prefix}/share/doc/tde/HTML/en/lisa/
%{tde_prefix}/share/services/lan.protocol
%{tde_prefix}/share/services/rlan.protocol
%{tde_prefix}/bin/lisa
%{tde_prefix}/bin/reslisa
%{tde_prefix}/share/man/man8/lisa.8*
%{tde_prefix}/share/man/man8/reslisa.8*

##########

%package -n trinity-kdnssd
Summary: Zeroconf support for TDE
Group:			Applications/Internet

%description -n trinity-kdnssd
A tdeioslave and tded module that provide Zeroconf support. Try
"zeroconf:/" in Konqueror.

%files -n trinity-kdnssd
%defattr(-,root,root,-)
%{tde_prefix}/share/services/zeroconf.protocol
%{tde_prefix}/share/services/invitation.protocol
%{tde_prefix}/share/services/kded/dnssdwatcher.desktop
%{tde_prefix}/share/apps/remoteview/zeroconf.desktop
%{tde_prefix}/share/apps/zeroconf/_http._tcp
%{tde_prefix}/share/apps/zeroconf/_ftp._tcp
%{tde_prefix}/share/apps/zeroconf/_ldap._tcp
%{tde_prefix}/share/apps/zeroconf/_webdav._tcp
%{tde_prefix}/share/apps/zeroconf/_nfs._tcp
%{tde_prefix}/share/apps/zeroconf/_ssh._tcp
%{tde_prefix}/share/apps/zeroconf/_rfb._tcp
%{tde_prefix}/share/apps/zeroconf/_sftp-ssh._tcp
%{tde_prefix}/%{_lib}/trinity/tdeio_zeroconf.so
%{tde_prefix}/%{_lib}/trinity/tdeio_zeroconf.la
%{tde_prefix}/%{_lib}/trinity/kded_dnssdwatcher.so
%{tde_prefix}/%{_lib}/trinity/kded_dnssdwatcher.la

%prep -a
# Update icons for some control center modules
%__sed -i "filesharing/simple/fileshare.desktop" -e "s|^Icon=.*|Icon=kcmfileshare|"


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p %{buildroot}%{tde_prefix}/share/icons/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/
pushd %{buildroot}%{tde_prefix}/share/icons
for i in {16,22,32,48}; do        %__cp %{?buildroot}%{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/kget.png    hicolor/"$i"x"$i"/apps/kget.png          ;done
for i in {32,48}; do              %__cp %{?buildroot}%{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/krdc.png    hicolor/"$i"x"$i"/apps/krdc.png          ;done
for i in {16,32,48}; do           %__cp %{?buildroot}%{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/krfb.png    hicolor/"$i"x"$i"/apps/krfb.png          ;done
for i in {16,22,32,48,128}; do    %__cp %{?buildroot}%{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/apps/ktalkd.png  hicolor/"$i"x"$i"/apps/ktalkd.png        ;done
for i in {16,22,32,48,64,128}; do %__cp $BUILD_ROOT%{tde_prefix}/share/icons/crystalsvg/"$i"x"$i"/actions/share.png  hicolor/"$i"x"$i"/apps/kcmfileshare.png  ;done
popd

%if %{with consolehelper}
# Run kppp through consolehelper, and rename it to 'kppp3'
%__install -p -m644 -D %{SOURCE1} %{buildroot}/etc/pam.d/kppp3
%__mkdir_p %{buildroot}%{tde_prefix}/sbin %{buildroot}%{_sbindir}
%__mv %{buildroot}%{tde_prefix}/bin/kppp %{buildroot}%{tde_prefix}/sbin/kppp3
%__ln_s %{_bindir}/consolehelper %{buildroot}%{tde_prefix}/bin/kppp3
%if "%{tde_prefix}" != "/usr"
%__ln_s %{tde_prefix}/sbin/kppp3 %{?buildroot}%{_sbindir}/kppp3
%endif
%__mkdir_p %{buildroot}%{_sysconfdir}/security/console.apps
cat > %{buildroot}%{_sysconfdir}/security/console.apps/kppp3 <<EOF
USER=root
PROGRAM=%{tde_prefix}/sbin/kppp3
SESSION=true
EOF

# Renames 'kppp' as 'kppp3' in launch icon
%__sed -i %{buildroot}%{tde_prefix}/share/applications/tde/Kppp.desktop -e "/Exec=/ s|kppp|kppp3|"
%endif

# Remove setuid bit on some binaries.
if [ -r "%{?buildroot}%{tde_prefix}/bin/kppp" ]; then
  chmod 0755 "%{?buildroot}%{tde_prefix}/bin/kppp"
fi

%if %{with xinetd}
# ktalk
%__install -p -m 0644 -D  %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/ktalk
%endif

# Avoids conflict with trinity-kvirc
%__mv -f %{buildroot}%{tde_prefix}/share/services/irc.protocol %{buildroot}%{tde_prefix}/share/apps/kopete/

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{tde_prefix}/share/applications/tde/*.desktop ; do
  if grep -q "^Categories=.*X-TDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=TDE" "${i}" ; then
      echo "OnlyShowIn=TDE;" >>"${i}"
    fi
  fi
done

# Remove unwanted doc
%if %{with wifi} == 0
%__rm -rf "%{buildroot}%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmwifi/"
%__rm -rf "%{buildroot}%{tde_prefix}/share/doc/tde/HTML/en/kwifimanager/"
%endif

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

