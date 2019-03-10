Name:           serialosc
Version:        1.4.1
Release:        1%{?dist}
Summary:        serialosc

License:        As-is
URL:            https://github.com/monome/serialosc
Source0:        https://github.com/monome/serialosc/archive/v1.4.1/serialosc-1.4.1.tar.gz

Patch0:         optparse.patch

BuildRequires: avahi-devel
BuildRequires: gcc-c++
BuildRequires: liblo-devel
BuildRequires: libmonome-devel
BuildRequires: libuv-devel
BuildRequires: python
BuildRequires: systemd-devel

Requires:      avahi-libs
Requires:      libmonome
Requires:      libuv
Requires:      systemd-libs

%description


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%set_build_flags
./waf configure --prefix=%{_prefix} --enable-system-libuv
./waf build %{?_smp_mflags} --enable-system-libuv


%install
rm -rf $RPM_BUILD_ROOT
./waf install --destdir=%{buildroot}

%files
%doc README
%{_bindir}/serialosc-detector
%{_bindir}/serialosc-device
%{_bindir}/serialoscd


%changelog
* Sat Mar  9 2019 Evan Klitzke <evan@eklitzke.org>
- Initial packaing work.
