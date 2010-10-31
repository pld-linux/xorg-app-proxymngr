Summary:	proxymngr application - proxy manager service
Summary(pl.UTF-8):	Aplikacja proxymngr - usługa zarządzająca proxy
Name:		xorg-app-proxymngr
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/proxymngr-%{version}.tar.bz2
# Source0-md5:	714c4656e749ce856690b872e3d4ac4c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-app-lbxproxy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The proxy manager (proxymngr) is responsible for resolving requests
from xfindproxy (and other similar clients), starting new proxies when
appropriate, and keeping track of all of the available proxy services.
The proxy manager strives to reuse existing proxies whenever possible.

%description -l pl.UTF-8
Zarządca proxy (proxymngr) odpowiada za spełnianie żądań od xfindproxy
(i innych podobnych klientów), uruchamianie nowych proxy w razie
potrzeby i śledzenie wszystkich dostępnych usług proxy. Zarządca proxy
stara się w miarę możliwości wykorzystywać ponownie istniejące proxy.

%prep
%setup -q -n proxymngr-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LBXPROXY=%{_bindir}/lbxproxy

# NOTE different CONFIG_DIR values - there is a bug in proxymngr 1.0.[12] Makefile.am
# ("$(CONFIG_DIR)/proxymngr/pmconfig" is appended during build, but pm config is
# installed in $(CONFIG_DIR) at install stage)
%{__make} \
	CONFIG_DIR=/etc/X11

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CONFIG_DIR=/etc/X11/proxymngr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/proxymngr
%dir /etc/X11/proxymngr
%config(noreplace) %verify(not md5 mtime size) /etc/X11/proxymngr/pmconfig
%{_mandir}/man1/proxymngr.1x*
