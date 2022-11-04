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
Requires:   whiptail
Requires:   curl
Requires:   wget
Requires:   libxml2-utils
BuildArch:  noarch

%description
Provides ebcl-repo-setup and ebcl-sync tools to initialize credentials
protected NautilOS debian repositories from Artifactory. An environment
file ~/.ebcl is created such that other ebcl tools can also
make use of it

%prep
%setup -q

%install
install -D -m 600 nautilos-repo-setup/ebcl.production \
    %{buildroot}/root/.ebcl.production
install -D -m 600 nautilos-repo-setup/ebcl.test \
    %{buildroot}/root/.ebcl.test
install -D -m 600 nautilos-repo-setup/ebcl.local \
    %{buildroot}/root/.ebcl.local
install -D -m 755 nautilos-repo-setup/ebcl-repo-setup \
    %{buildroot}/usr/bin/ebcl-repo-setup
install -D -m 755 nautilos-repo-setup/ebcl-releases \
    %{buildroot}/usr/bin/ebcl-releases
install -D -m 755 nautilos-repo-setup/ebcl-sync \
    %{buildroot}/usr/bin/ebcl-sync
install -D -m 755 nautilos-repo-setup/ebcl-ui \
    %{buildroot}/usr/bin/ebcl-ui
install -D -m 644 nautilos-repo-setup/sib_user_guide.html \
    %{buildroot}/usr/share/doc/nautilos-repo-setup/sib_user_guide.html
install -D -m 644 nautilos-repo-setup/sib_user_guide.pdf \
    %{buildroot}/usr/share/doc/nautilos-repo-setup/sib_user_guide.pdf

%files
%defattr(-,root,root,-)
/root/.ebcl.production
/root/.ebcl.test
/root/.ebcl.local
%{_usr}/share/doc/nautilos-repo-setup
%{_usr}/bin/ebcl-repo-setup
%{_usr}/bin/ebcl-releases
%{_usr}/bin/ebcl-sync
%{_usr}/bin/ebcl-ui

%changelog
