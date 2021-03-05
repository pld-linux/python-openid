#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module		openid
%define 	egg_name	python_openid
Summary:	OpenID consumer and server library for Python
Summary(pl.UTF-8):	Biblioteka konsumenta i serwera OpenID dla Pythona
Name:		python-%{module}
Version:	2.2.5
Release:	2
License:	Apache
Group:		Libraries/Python
Source0:	https://github.com/openid/python-openid/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4f3c32944f7eef48e32fd36d185fa05c
URL:		https://github.com/openid/python-openid
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
%if %{with doc}
BuildRequires:	epydoc
%endif
Requires:	python-urljr >= 1.0.0
Requires:	python-yadis >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenID consumer and server library for Python.

%description -l pl.UTF-8
Biblioteka konsumenta i serwera OpenID dla Pythona.

%package -n python3-%{module}
Summary:	OpenID consumer and server library for Python
Summary(pl.UTF-8):	Biblioteka konsumenta i serwera OpenID dla Pythona
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
OpenID consumer and server library for Python.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka konsumenta i serwera OpenID dla Pythona.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
sh admin/makedoc
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/*
%endif
