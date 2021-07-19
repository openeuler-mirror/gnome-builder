%global __provides_exclude_from ^%{_libdir}/gnome-builder
%global privlibs .*-private|libide|libgnome-builder-plugins
%global __requires_exclude ^(%{privlibs}).*\\.so.*

%global shortver %(v=%{version}; echo ${v%.*})

%global libdazzle_version 3.37.0
%global glib2_version 2.65.0
%global gtk3_version 3.22.26
%global json_glib_version 1.2.0
%global jsonrpc_glib_version 3.29.91
%global libpeas_version 1.22.0
%global template_glib_version 3.28.0
%global libgit2_glib_version  0.28.0.1
%global devhelp_version 3.25.1
%global sysprof_version 3.37.1

Name:           gnome-builder
Version:        3.40.0
Release:        1
Summary:        IDE for writing GNOME-based software
License:        GPLv3+ and GPLv2+ and LGPLv3+ and LGPLv2+ and MIT and CC-BY-SA and CC0
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        https://download.gnome.org/sources/%{name}/%{shortver}/%{name}-%{version}.tar.xz

BuildRequires:  clang-devel desktop-file-utils gettext gtk-doc itstool llvm-devel meson pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak) pkgconfig(gio-2.0) >= %{glib2_version} pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gspell-1) pkgconfig(gtk+-3.0) >= %{gtk3_version} pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version} pkgconfig(jsonrpc-glib-1.0) >= %{jsonrpc_glib_version}
BuildRequires:  pkgconfig(libdazzle-1.0) >= %{libdazzle_version} pkgconfig(libdevhelp-3.0) >= %{devhelp_version}
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= %{libgit2_glib_version} pkgconfig(libpeas-1.0) >= %{libpeas_version}
BuildRequires:  pkgconfig(libportal) pkgconfig(libxml-2.0) pkgconfig(pangoft2) pkgconfig(libpcre) pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(sysprof-4) >= %{sysprof_version} pkgconfig(sysprof-capture-4) pkgconfig(sysprof-ui-4) >= %{sysprof_version}
BuildRequires:  pkgconfig(template-glib-1.0) >= %{template_glib_version} pkgconfig(vte-2.91) pkgconfig(webkit2gtk-4.0)
BuildRequires:  python3-devel python3-sphinx python3-sphinx_rtd_theme libappstream-glib

Requires:       devhelp-libs%{?_isa} >= 1:%{devhelp_version} glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version} json-glib%{?_isa} >= %{json_glib_version}
Requires:       jsonrpc-glib%{?_isa} >= %{jsonrpc_glib_version} libdazzle%{?_isa} >= %{libdazzle_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version} libpeas%{?_isa} >= %{libpeas_version}
Requires:       libpeas-loader-python3%{?_isa} >= %{libpeas_version} libsysprof-ui%{?_isa} >= %{sysprof_version}
Requires:       template-glib%{?_isa} >= %{template_glib_version} flatpak-builder
Recommends:     clang
Recommends:     gnome-code-assistance
Recommends:     meson
Recommends:     python3-jedi

%description
Builder attempts to be an IDE for writing software for GNOME. It does not try
to be a generic IDE, but one specialized for writing GNOME software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Dhelp=true
%meson_build

%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gnome-builder/plugins/

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Builder.desktop

%files -f gnome-builder.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-builder
%exclude %{_libdir}/gnome-builder/pkgconfig/
%{_libdir}/gnome-builder/
%{_libexecdir}/gnome-builder-clang
%{_libexecdir}/gnome-builder-git
%{python3_sitelib}/gi/
%{_datadir}/applications/org.gnome.Builder.desktop
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder*.gschema.xml
%exclude %{_datadir}/gnome-builder/gir-1.0/
%{_datadir}/gnome-builder/
%dir %{_datadir}/gtksourceview-4
%dir %{_datadir}/gtksourceview-4/styles
%{_datadir}/gtksourceview-4/styles/*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Builder*.svg
%{_datadir}/metainfo/org.gnome.Builder.appdata.xml
%lang(en) %{_datadir}/doc/gnome-builder/en/

%files devel
%{_includedir}/gnome-builder*/
%{_libdir}/gnome-builder/pkgconfig/
%{_datadir}/gnome-builder/gir-1.0/

%changelog
* Wed Jun 30 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.40.0-1
- Package init with 3.40.0
