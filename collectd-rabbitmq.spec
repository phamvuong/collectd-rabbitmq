# Created by pyp2rpm-3.2.2
%define pkgname collectd-rabbitmq
%define srcname collectd_rabbitmq
%define python2_wheelname %{srcname}-%{version}-py2.py3-none-any.whl

Name:           %{pkgname}
Version:        1.18.0
Release:        1%{?dist}
Summary:        A collected plugin, written in python, tocollect statistics from RabbitMQ

License:        Apache
URL:            https://github.com/NYTimes/collectd-rabbitmq
Source0:        %{pkgname}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pip


%description
 collectdrabbitmq "A collected plugin, written in python, to collect statistics
from RabbitMQ."

%package -n %{pkgname}-doc
Summary:        collectd-rabbitmq documentation
%description -n %{pkgname}-doc
Documentation for collectd-rabbitmq

%prep
%autosetup -n %{pkgname}-%{version}
# Remove bundled egg-info
rm -rf %{pkgname}.egg-info

%build
%{__python2} setup.py bdist_wheel

%install
pip2 install -I dist/%{python2_wheelname} --root %{buildroot}

%check
%{__python2} setup.py test

%files -n %{pkgname}
%license LICENSE
%doc docs/readme.rst README.rst
%{python2_sitelib}/%{srcname}-%{version}.dist-info/
%{python2_sitelib}/%{srcname}
%{_usr}/share/%{pkgname}/types.db.custom

%files -n %{pkgname}-doc

%changelog
* Thu Jul 27 2017 Vuong Pham <vuong.pham@gooddata.com> - 1.18.0-1
- Initial package.
