# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate pnet_datalink

Name:           rust-%{crate}
Version:        0.22.0
Release:        4%{?dist}
Summary:        Cross-platform, datalink layer networking

# Upstream license specification: MIT/Apache-2.0
# https://github.com/libpnet/libpnet/issues/371
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pnet_datalink
Source:         %{crates_source}
# Initial patched metadata
# * No windows
Patch0:         pnet_datalink-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Cross-platform, datalink layer networking.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+netmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+netmap-devel %{_description}

This package contains library source intended for building other packages
which use "netmap" feature of "%{crate}" crate.

%files       -n %{name}+netmap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+netmap_sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+netmap_sys-devel %{_description}

This package contains library source intended for building other packages
which use "netmap_sys" feature of "%{crate}" crate.

%files       -n %{name}+netmap_sys-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+pcap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pcap-devel %{_description}

This package contains library source intended for building other packages
which use "pcap" feature of "%{crate}" crate.

%files       -n %{name}+pcap-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 21:10:22 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-2
- Regenerate

* Sat Apr 27 09:46:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Initial package
