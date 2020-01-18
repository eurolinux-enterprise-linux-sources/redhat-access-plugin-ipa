%global plugin_dir %{_datadir}/ipa/ui/js/plugins/rhaccess

Name:       redhat-access-plugin-ipa
Version:    0.9.1
Release:    2%{?dist}
Summary:    Plugin for Identity Management to allow access Red Hat subscriber services
Vendor:     Red Hat, Inc.
Group:      System Environment/Base
License:    Apache License 2.0
URL:        https://github.com/redhataccess/redhat-access-plugin-ipa
Source0:    https://github.com/redhataccess/redhat-access-plugin-ipa/archive/v%{version}.tar.gz
BuildArch:  noarch
Requires(pre): ipa-server

Patch0001:  0001-update-redhat_access_angular_ui-to-0.9.36.patch

%description
This package contains the Red Hat Access Identity Management Plugin.
The Red Hat Access Identity Management Plugin provides web based access to
Red Hat's subscriber services.
These services include, but are not limited to,
access to knowledge-base solutions, case management,
automated diagnostic services, etc.

%prep
%setup -q
%patch0001 -p1

%build
make js css glyphs

%install
make install DESTDIR=%{buildroot}%{_datadir}

%files
%{plugin_dir}
%doc AUTHORS LICENSE README.md

%changelog
* Tue Nov 25 2014 Petr Vobornik <pvoborni@redhat.com> - 0.9.1-2
- update redhat_access_angular_ui to 0.9.36

* Fri Sep 26 2014 Petr Vobornik <pvoborni@redhat.com> - 0.9.1-1
- initial package
