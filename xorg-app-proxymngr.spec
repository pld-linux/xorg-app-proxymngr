# $Rev: 3361 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	proxymngr application
Summary(pl):	Aplikacja proxymngr
Name:		xorg-app-proxymngr
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/proxymngr-%{version}.tar.bz2
# Source0-md5:	d0ae882ddc8296b0fddde2720785e762
Patch0:		proxymngr-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-lbxproxy
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRoot:	%{tmpdir}/proxymngr-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
proxymngr application.

%description -l pl
Aplikacja proxymngr.


%prep
%setup -q -n proxymngr-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_libdir}/X11/proxymngr/pmconfig
%{_mandir}/man1/*.1*
