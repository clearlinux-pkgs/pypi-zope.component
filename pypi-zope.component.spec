#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-zope.component
Version  : 6.0
Release  : 60
URL      : https://files.pythonhosted.org/packages/53/32/87db95f4a5f097aa837dcb951f5a4754e2e8d3ac70160a6c2df7bd215956/zope.component-6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/32/87db95f4a5f097aa837dcb951f5a4754e2e8d3ac70160a6c2df7bd215956/zope.component-6.0.tar.gz
Summary  : Zope Component Architecture
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.component-license = %{version}-%{release}
Requires: pypi-zope.component-python = %{version}-%{release}
Requires: pypi-zope.component-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.event)
BuildRequires : pypi(zope.hookable)
BuildRequires : pypi(zope.interface)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
================
zope.component
================
.. image:: https://github.com/zopefoundation/zope.component/actions/workflows/tests.yml/badge.svg
:target: https://github.com/zopefoundation/zope.component/actions/workflows/tests.yml
:alt: Unit test status

%package license
Summary: license components for the pypi-zope.component package.
Group: Default

%description license
license components for the pypi-zope.component package.


%package python
Summary: python components for the pypi-zope.component package.
Group: Default
Requires: pypi-zope.component-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.component package.


%package python3
Summary: python3 components for the pypi-zope.component package.
Group: Default
Requires: python3-core
Provides: pypi(zope.component)
Requires: pypi(setuptools)
Requires: pypi(zope.event)
Requires: pypi(zope.hookable)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-zope.component package.


%prep
%setup -q -n zope.component-6.0
cd %{_builddir}/zope.component-6.0
pushd ..
cp -a zope.component-6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695160819
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.component
cp %{_builddir}/zope.component-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.component/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.component/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
