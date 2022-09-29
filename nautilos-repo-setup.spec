Name:       nautilos-repo-setup
Version:    1.0.2
Release:    0
Summary:    Initialize System with NautilOS repositories
Group:      Application/Misc
License:    MIT
%if "%{_vendor}" == "debbuild"
Packager:   Marcus Schaefer <marcus.schaefer@elektrobit.com>
%endif
Source0:    %{name}-%{version}.tar.gz
Requires:   curl
Requires:   wget
BuildArch:  noarch

%description
Provides ebcl-repo-setup and ebcl-sync tools to initialize credentials
protected NautilOS debian repositories from Artifactory. An environment
file ~/.ebcl is created such that other ebcl tools can also
make use of it

%prep
%setup -q

%install
install -D -m 600 nautilos-repo-setup/ebcl \
    %{buildroot}/root/.ebcl
install -D -m 755 nautilos-repo-setup/ebcl-repo-setup \
    %{buildroot}/usr/bin/ebcl-repo-setup
install -D -m 644 nautilos-repo-setup/ebcl-sync \
    %{buildroot}/usr/bin/ebcl-sync

%files
%defattr(-,root,root,-)
/root/.ebcl
%{_usr}/bin/ebcl-repo-setup
%{_usr}/bin/ebcl-sync

%changelog
