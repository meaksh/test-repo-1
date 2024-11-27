#
# spec file for package salt-extensions
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%global saltext_mysql_version 1.0.0
%global saltext_prometheus_version 2.1.0

%{?sle15_python_module_pythons}

Name:           salt-extensions
Version:        0.1
Release:        0

%global saltext_version %{version}

Summary:        Salt Extensions provided by openSUSE
License:        Apache-2.0
URL:            https://github.com/meaksh/test-repo-1
Source:         test-repo-1-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-salt >= 3006.0
Requires:       python-salt-extensions-mysql
Requires:       python-salt-extensions-prometheus

%python_subpackages

%description
A collection of different Salt Extensions packages by openSUSE

%prep
%autosetup -p1 -n test-repo-1-%{saltext_version}

%build
pushd saltext_mysql-%{saltext_mysql_version}
%pyproject_wheel
popd

pushd saltext.prometheus-%{saltext_prometheus_version}
%pyproject_wheel
popd

%install
pushd saltext_mysql-%{saltext_mysql_version}
%pyproject_install
popd

pushd saltext.prometheus-%{saltext_prometheus_version}
%pyproject_install
popd

%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%package mysql
Version:        %{saltext_mysql_version}
Summary:        Salt Extension for interacting with MySQL
Requires:       (python-PyMySQL or python-mysqlclient)
Requires:       python-sqlparse
Requires:       python-salt >= 3006.0

%description mysql
Salt Extension for interacting with MySQL

%package prometheus
Version:        %{saltext_prometheus_version}
Summary:        Salt Extension for interacting with Prometheus
Requires:       python-prometheus-client
Requires:       python-salt >= 3006.0

%description prometheus
Salt Extension for interacting with Prometheus

%files %{python_files}
%dir %{python_sitelib}/saltext/
%{python_sitelib}/saltext/__init__.py
%{python_sitelib}/saltext/__pycache__

%files %{python_files mysql}
%{python_sitelib}/saltext/mysql
%{python_sitelib}/saltext.mysql-%{saltext_mysql_version}*-info

%files  %{python_files prometheus}
%{python_sitelib}/saltext/prometheus
%{python_sitelib}/saltext.prometheus-%{saltext_prometheus_version}*-info

%changelog

