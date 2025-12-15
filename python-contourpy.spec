%global           pypi_name contourpy
%define debug_package %nil

Name:             python-contourpy
Version:          1.3.3
Release:          1

Summary:          A Cassowary constraint solving algorithm
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/contourpy/
Source0:	https://files.pythonhosted.org/packages/source/c/contourpy/%{pypi_name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	pkgconfig(pybind11)

%description
A small C++ header library which makes it easier to write Python
extension modules.
The primary feature is a PyObject smart pointer which automatically
handles reference counting and provides convenience methods for
performing common object operations.

%files -n python-contourpy
%doc README.md
%{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}-%{version}.dist-info


