Summary: Retry plugging PBDs to specific SRs on boot
Name: plug-late-sr
Version: 1.0
Release: 1%{?dist}
License: GPLv3
Source0: plug-late-sr
Source1: plug-late-sr.service
BuildArch: noarch

BuildRequires: systemd

Requires: python2-configparser
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Retry plugging PBDs to specific SRs on boot, then start VMs which couldn't autostart due to the unreachable SRs.

%install
install -D -m 755 %{SOURCE0} %{buildroot}%{_bindir}/plug-late-sr
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/plug-late-sr.service

%post
if [ $1 -eq 1 ] ; then
  # Initial installation: enable the service
  systemctl enable plug-late-sr.service >/dev/null 2>&1 || :
fi

%preun
%systemd_preun plug-late-sr.service

%postun
%systemd_postun plug-late-sr.service

%files
%{_bindir}/plug-late-sr
%{_unitdir}/plug-late-sr.service

%changelog
* Fri May 26 2023 Ronan Abhamon <ronan.abhamon@vates.fr> - 1.0-1
- Initial package
