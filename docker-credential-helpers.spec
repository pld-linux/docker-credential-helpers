# TODO
# - split providers to subpackages?
#
Summary:	Native credentials store for Docker
Name:		docker-credential-helpers
Version:	0.9.7
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/docker/docker-credential-helpers/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	93a145569cc6a81eda7d84c2ba00f002
URL:		https://github.com/docker/docker-credential-helpers
BuildRequires:	golang >= 1.21
BuildRequires:	libsecret-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.009
Requires:	docker(engine) >= 1.11
Suggests:	password-store
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

%description
docker-credential-helpers is a suite of programs to use native stores
to keep Docker credentials safe.

%prep
%setup -q

%build
%{__make} build-pass build-secretservice \
	DESTDIR=bin \
	VERSION="v%{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p bin/docker-credential-pass bin/docker-credential-secretservice $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/docker-credential-pass
%attr(755,root,root) %{_bindir}/docker-credential-secretservice
