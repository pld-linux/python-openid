Summary:	OpenID consumer and server library for Python
Summary(pl.UTF-8):	Biblioteka konsumenta i serwera OpenID dla Pythona
Name:		python-openid
Version:	2.2.4
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	http://openidenabled.com/files/python-openid/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	2766dccfecf241c94cc1e8eca2814913
URL:		http://www.openidenabled.com/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel 
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
Requires:	python-urljr >= 1.0.0
Requires:	python-yadis >= 1.1.0
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenID consumer and server library for Python.

%description -l pl.UTF-8
Biblioteka konsumenta i serwera OpenID dla Pythona.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2	\
	--root=$RPM_BUILD_ROOT

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
