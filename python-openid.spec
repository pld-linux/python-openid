
%define		module	openid

Summary:	OpenID consumer and server library for Python
Summary(pl.UTF-8):	Biblioteka konsumenta i serwera OpenID dla Pythona
Name:		python-%{module}
Version:	1.2.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.openidenabled.com/resources/downloads/python-openid/%{name}-%{version}.tar.gz
# Source0-md5:	4ad16ef790d80a965b902eb315fe57b2
URL:		http://www.openidenabled.com/
BuildRequires:	python-devel
Requires:	python-urljr >= 1.0.0
Requires:	python-yadis >= 1.1.0
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenID consumer and server library for Python

%description -l pl.UTF-8
Biblioteka konsumenta i serwera OpenID dla Pythona.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%{py_sitescriptdir}/%{module}
