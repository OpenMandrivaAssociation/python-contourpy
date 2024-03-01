%global           pypi_name contourpy
%define debug_package %nil

Name:             python-contourpy
Version:          1.2.0
Release:          1

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/contourpy/
Source0:	https://files.pythonhosted.org/packages/11/a3/48ddc7ae832b000952cf4be64452381d150a41a2299c2eb19237168528d1/%{pypi_name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	python3dist(meson-python)
BuildRequires:	pkgconfig(pybind11)

%description
A small C++ header library which makes it easier to write Python
extension modules.
The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for
performing common object operations.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
%py_build


%install
%py_install

%files -n python-contourpy
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info


