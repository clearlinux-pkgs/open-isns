#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-isns
Version  : 0.99
Release  : 8
URL      : https://github.com/open-iscsi/open-isns/archive/v0.99.tar.gz
Source0  : https://github.com/open-iscsi/open-isns/archive/v0.99.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: open-isns-bin = %{version}-%{release}
Requires: open-isns-lib = %{version}-%{release}
Requires: open-isns-license = %{version}-%{release}
Requires: open-isns-man = %{version}-%{release}
Requires: open-isns-services = %{version}-%{release}
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
Requires: open-isns-license = %{version}-%{release}
Requires: open-isns-man = %{version}-%{release}
Requires: open-isns-services = %{version}-%{release}

%description bin
bin components for the open-isns package.


%package dev
Summary: dev components for the open-isns package.
Group: Development
Requires: open-isns-lib = %{version}-%{release}
Requires: open-isns-bin = %{version}-%{release}
Provides: open-isns-devel = %{version}-%{release}

%description dev
dev components for the open-isns package.


%package lib
Summary: lib components for the open-isns package.
Group: Libraries
Requires: open-isns-license = %{version}-%{release}

%description lib
lib components for the open-isns package.


%package license
Summary: license components for the open-isns package.
Group: Default

%description license
license components for the open-isns package.


%package man
Summary: man components for the open-isns package.
Group: Default

%description man
man components for the open-isns package.


%package services
Summary: services components for the open-isns package.
Group: Systemd services

%description services
services components for the open-isns package.


%prep
%setup -q -n open-isns-0.99

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542409717
%configure --disable-static --enable-shared
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542409717
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/open-isns
cp COPYING %{buildroot}/usr/share/package-licenses/open-isns/COPYING
%make_install install_hdrs install_lib

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isnsadm
/usr/bin/isnsd
/usr/bin/isnsdd

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libisns.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/open-isns/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/isns_config.5
/usr/share/man/man8/isnsadm.8
/usr/share/man/man8/isnsd.8
/usr/share/man/man8/isnsdd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/isnsd.service
/usr/lib/systemd/system/isnsd.socket
