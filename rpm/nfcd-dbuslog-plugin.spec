Name: nfcd-dbuslog-plugin

Version: 1.0.2
Release: 0
Summary: nfcd logging plugin
License: BSD
URL: https://github.com/mer-hybris/nfcd-dbuslog-plugin
Source: %{name}-%{version}.tar.bz2

%define libglibutil_version 1.0.10
%define libdbuslog_version 1.0.19
%define glib_version 2.32

BuildRequires: pkgconfig(libdbuslogserver-gio) >= %{libdbuslog_version}
BuildRequires: pkgconfig(libglibutil) >= %{libglibutil_version}
BuildRequires: pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires: pkgconfig(nfcd-plugin)
BuildRequires: pkgconfig(libnfcdef)

Requires: libdbuslogserver-gio >= %{libdbuslog_version}
Requires: libglibutil >= %{libglibutil_version}
Requires: glib2 >= %{glib_version}
Requires: nfcd >= 1.0.47

%define plugin_dir %{_libdir}/nfcd/plugins

%description
Provides access to nfcd logs over D-Bus.

%prep
%setup -q

%build
make %{_smp_mflags} KEEP_SYMBOLS=1 release

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PLUGIN_DIR=%{plugin_dir} install

%post
systemctl reload-or-try-restart nfcd.service ||:

%postun
systemctl reload-or-try-restart nfcd.service ||:

%files
%defattr(-,root,root,-)
%dir %{plugin_dir}
%{plugin_dir}/*.so
