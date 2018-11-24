Name:		fuse-ufs2
Version:	0.1
Release:	1%{?dist}
Summary:	Fuse-ufs is a UFS2 Filesystem support for FUSE.


#Group:		
License:	GPLv3
URL:		https://github.com/jblumsch/fuse-ufs2
Source0:	fuse-ufs2.tgz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	fuse-devel
BuildRequires:	kernel-headers
BuildRequires:	e2fsprogs-devel
#BuildRequires:	
#Requires:	
Requires:	e2fsprogs
Requires:	fuse
Requires:	fuse-libs

%description


%prep
%setup -q -n fuse-ufs2


%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
/usr/lib64/pkgconfig/fuse-ufs.pc
/usr/lib64/umview/modules/umfuseufs.a
/usr/lib64/umview/modules/umfuseufs.so
%{_mandir}/man1/*



%changelog

