Summary:	OpenID consumer and server library for Python
Summary(pl.UTF-8):	Biblioteka konsumenta i serwera OpenID dla Pythona
Name:		python-openid
Version:	2.2.5
Release:	1
License:	Apache
Group:		Libraries/Python
Source0:	https://github.com/openid/python-openid/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4f3c32944f7eef48e32fd36d185fa05c
URL:		https://github.com/openid/python-openid
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-urljr >= 1.0.0
Requires:	python-yadis >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenID consumer and server library for Python.

%description -l pl.UTF-8
Biblioteka konsumenta i serwera OpenID dla Pythona.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%{py_sitescriptdir}/openid
%{py_sitescriptdir}/python_openid-*.egg-info
