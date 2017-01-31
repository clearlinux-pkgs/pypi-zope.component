#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.component
Version  : 4.3.0
Release  : 1
URL      : https://pypi.python.org/packages/c9/56/501d51f0277af1899d1381e4b9928b5e14675187752622ddc344a756439d/zope.component-4.3.0.tar.gz
Source0  : https://pypi.python.org/packages/c9/56/501d51f0277af1899d1381e4b9928b5e14675187752622ddc344a756439d/zope.component-4.3.0.tar.gz
Summary  : Zope Component Architecture
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.component-python
BuildRequires : component-python
BuildRequires : pbr
BuildRequires : persistent-python
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zope.configuration-python
BuildRequires : zope.event
BuildRequires : zope.exceptions-python
BuildRequires : zope.hookable
BuildRequires : zope.i18nmessageid-python
BuildRequires : zope.interface
BuildRequires : zope.location-python
BuildRequires : zope.proxy-python
BuildRequires : zope.schema-python
BuildRequires : zope.security-python
BuildRequires : zope.testing-python

%description
``zope.component``
==================
.. image:: https://img.shields.io/pypi/v/zope.component.svg
:target: https://pypi.python.org/pypi/zope.component/
:alt: Latest Version

%package python
Summary: python components for the zope.component package.
Group: Default
Requires: persistent-python
Requires: zope.configuration-python
Requires: zope.i18nmessageid-python
Requires: zope.location-python
Requires: zope.proxy-python
Requires: zope.security-python
Requires: zope.testing-python

%description python
python components for the zope.component package.


%prep
%setup -q -n zope.component-4.3.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485890708
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
export SOURCE_DATE_EPOCH=1485890708
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
