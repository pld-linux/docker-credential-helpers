Summary:	Native credentials store for Docker
Name:		docker-credential-helpers
Version:	0.3.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/docker/docker-credential-helpers/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	dcd544bb5898713e27130a15070ed044
URL:		https://github.com/docker/docker-credential-helpers
BuildRequires:	golang >= 1.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages 0
%define		gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%define		gopath		%{_libdir}/golang
%define		import_path	github.com/docker/%{name}

%description
docker-credential-helpers is a suite of programs to use native stores
to keep Docker credentials safe.

%prep
%setup -q

install -d src/$(dirname %{import_path})
ln -s ../../.. src/%{import_path}

%build
export GOPATH=$(pwd)

%gobuild -o bin/docker-credential-secretservice secretservice/cmd/main_linux.go

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE
%attr(755,root,root) %{_bindir}/docker-credential-secretservice