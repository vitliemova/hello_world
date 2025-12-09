Name:           hello_world
Version:        2.0
Release:        1%{?dist}
Summary:        Simple Python Hello World program

License:        MIT
URL:            https://github.com/vitliemova/hello_world
Source0:        hello_world-2.0.tar.gz

BuildArch:      noarch
Requires:       python3

%description
A simple Python Hello World program packaged as RPM for SUSE.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 hello.py %{buildroot}/usr/local/bin/hello_world

%files
/usr/local/bin/hello_world

%changelog
* Mon Dec 08 2025 Desislava <desi@example.com> - 2.0-1
- Initial RPM build 2.0.1
