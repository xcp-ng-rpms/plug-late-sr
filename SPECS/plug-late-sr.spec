Summary: Retry plugging PBDs to specific SRs on boot
Name: plug-late-sr
Version: 1.0
Release: 1%{?dist}
License: GPLv3
Source0: plug-late-sr
Source1: plug-late-sr.service
BuildArch: noarch

Requires: python2-configparser

%description
Retry plugging PBDs to specific SRs on boot.

%install
install -D -m 755 %{SOURCE0} %{buildroot}%{_bindir}/plug-late-sr
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/plug-late-sr.service

%post
systemctl enable plug-late-sr.service

%preun
%systemd_preun plug-late-sr.service

%postun
%systemd_postun plug-late-sr.service

%files
%{_bindir}/plug-late-sr
%{_unitdir}/plug-late-sr.service

%changelog
* Tue May 23 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Initial package
