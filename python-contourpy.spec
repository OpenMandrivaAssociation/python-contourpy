%global           pypi_name contourpy
%define debug_package %nil

Name:             python-contourpy
Version:          1.4.0
Release:          1

Summary:          Calculate contours of 2D quadrilateral grids
License:          BSD
Group:            Development/Python

URL:              https://pypi.org/project/contourpy/
Source0:	https://files.pythonhosted.org/packages/source/c/contourpy/%{pypi_name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(pybind11)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python library for calculating contours of 2D quadrilateral grids.

%files -n python-contourpy
%doc README.md
%{python_sitearch}/%{pypi_name}
%{python_sitearch}/%{pypi_name}-%{version}.dist-info


