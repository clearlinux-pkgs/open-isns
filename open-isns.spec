#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-isns
Version  : 0.98
Release  : 2
URL      : https://github.com/open-iscsi/open-isns/archive/v0.98.tar.gz
Source0  : https://github.com/open-iscsi/open-isns/archive/v0.98.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: open-isns-bin
Requires: open-isns-config
Requires: open-isns-lib
Requires: open-isns-doc
BuildRequires : openssl-dev

%description
Welcome to Open-iSNS
====================
This is a partial implementation of iSNS, according to RFC4171.
The implementation is still somewhat incomplete, but I'm releasing
it for your reading pleasure.

%package bin
Summary: bin components for the open-isns package.
Group: Binaries
Requires: open-isns-config

%description bin
bin components for the open-isns package.


%package config
Summary: config components for the open-isns package.
Group: Default

%description config
config components for the open-isns package.


%package dev
Summary: dev components for the open-isns package.
Group: Development
Requires: open-isns-lib
Requires: open-isns-bin
Provides: open-isns-devel

%description dev
dev components for the open-isns package.


%package doc
Summary: doc components for the open-isns package.
Group: Documentation

%description doc
doc components for the open-isns package.


%package lib
Summary: lib components for the open-isns package.
Group: Libraries

%description lib
lib components for the open-isns package.


%prep
%setup -q -n open-isns-0.98

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512432043
%configure --disable-static --enable-shared
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1512432043
rm -rf %{buildroot}
%make_install install_hdrs install_lib

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isnsadm
/usr/bin/isnsd
/usr/bin/isnsdd

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/isnsd.service
/usr/lib/systemd/system/isnsd.socket

%files dev
%defattr(-,root,root,-)
/usr/include/libisns/attrs.h
/usr/include/libisns/buffer.h
/usr/include/libisns/isns-proto.h
/usr/include/libisns/isns.h
/usr/include/libisns/message.h
/usr/include/libisns/paths.h
/usr/include/libisns/source.h
/usr/include/libisns/types.h
/usr/include/libisns/util.h
/usr/lib64/libisns.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libisns.so.0
