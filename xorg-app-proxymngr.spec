Summary:	proxymngr application
Summary(pl):	Aplikacja proxymngr
Name:		xorg-app-proxymngr
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/app/proxymngr-%{version}.tar.bz2
# Source0-md5:	aad44d0f65b97fd6d564b1d2ae510bb1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-app-lbxproxy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
proxymngr application.

%description -l pl
Aplikacja proxymngr.

%prep
%setup -q -n proxymngr-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	LBXPROXY=%{_bindir}/lbxproxy

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/proxymngr
%{_mandir}/man1/*.1x*
