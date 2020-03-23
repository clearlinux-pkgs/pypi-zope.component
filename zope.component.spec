#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.component
Version  : 4.6.1
Release  : 26
URL      : https://files.pythonhosted.org/packages/b0/f3/ac5d649165f86d8174ad54f095f6109d72d9dac6aa4cdc6235fefb2007b9/zope.component-4.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/f3/ac5d649165f86d8174ad54f095f6109d72d9dac6aa4cdc6235fefb2007b9/zope.component-4.6.1.tar.gz
Summary  : Zope Component Architecture
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.component-license = %{version}-%{release}
Requires: zope.component-python = %{version}-%{release}
Requires: zope.component-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.deferredimport
Requires: zope.deprecation
Requires: zope.event
Requires: zope.hookable
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : component-python
BuildRequires : persistent-python
BuildRequires : setuptools
BuildRequires : zope.configuration-python
BuildRequires : zope.deferredimport
BuildRequires : zope.deprecation
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

%package license
Summary: license components for the zope.component package.
Group: Default

%description license
license components for the zope.component package.


%package python
Summary: python components for the zope.component package.
Group: Default
Requires: zope.component-python3 = %{version}-%{release}

%description python
python components for the zope.component package.


%package python3
Summary: python3 components for the zope.component package.
Group: Default
Requires: python3-core
Provides: pypi(zope.component)
Requires: pypi(setuptools)
Requires: pypi(zope.deferredimport)
Requires: pypi(zope.deprecation)
Requires: pypi(zope.event)
Requires: pypi(zope.hookable)
Requires: pypi(zope.interface)

%description python3
python3 components for the zope.component package.


%prep
%setup -q -n zope.component-4.6.1
cd %{_builddir}/zope.component-4.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584977401
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.component
cp %{_builddir}/zope.component-4.6.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.component/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.component/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
