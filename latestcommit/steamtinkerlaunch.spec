%global commit   53d0f7d852101e7b0302ef2593378ca66c812772
%global short    53d0f7d
%global date     03052022

Name:           steamtinkerlaunch
Version:        10.0
Release:        1.%{date}.git.%{short}%{?dist}
Summary:        Wrapper tool for use with the Steam client for custom launch options

License:        GPLv3
URL:            https://github.com/frostworx/steamtinkerlaunch
Source0:        %{url}/archive/%{commit}.tar.gz
Patch0:         steamtinkerlaunch-build.patch

BuildArch:      noarch

BuildRequires:  make

Requires:       gawk bash git procps-ng unzip wget xdotool xprop xrandr vim-common xwininfo
Requires:       yad >= 7.2
Recommends:     strace gamemode mangohud winetricks vkBasalt net-toolsa scummvm gameconqueror
Recommends:     gamescope innoextract usbutils jq ImageMagick rsync p7zip

%description
Steam Tinker Launch is a Linux wrapper tool for use with the Steam client which
allows customizing and start tools and options for games quickly on the fly

%prep
%autosetup -n %{name}-%{commit}

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install PREFIX=%{_prefix} BUILDROOT=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/steamtinkerlaunch
%{_datadir}/steamtinkerlaunch
%{_datadir}/applications/steamtinkerlaunch.desktop
%{_datadir}/icons/hicolor/scalable/apps/steamtinkerlaunch.svg
