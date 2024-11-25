#
# TEST CHANGES
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

%define	saltext_mysql_version 1.0.0
%define	saltext_prometheus_version 2.1.0

Name:           salt-extensions
Version:        0.1
Release:        0
Summary:	Salt Extensions provided by openSUSE
License:        Apache-2.0
URL:            https://github.com/meaksh/test-repo-1
Source:         test-repo-1-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/s/saltext.mysql/saltext_mysql-%{saltext_mysql_version}.tar.gz
Source2:        https://files.pythonhosted.org/packages/source/s/saltext.mysql/saltext.prometheus-%{saltext_prometheus_version}.tar.gz
BuildRequires:  python-rpm-macros
Requires:       salt-extensions-mysql
Requires:       salt-extensions-prometheus

%description
A collection of different Salt Extensions packages by openSUSE

%prep
%autosetup -p1 -n test-repo-1-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%package mysql
Version:	%{saltext_mysql_version}
Summary:	Salt Extension for interacting with MySQL

%description mysql
Salt Extension for interacting with MySQL

%package prometheus
Version:	%{saltext_prometheus_version}
Summary:	Salt Extension for interacting with Prometheus

%description prometheus
Salt Extension for interacting with Prometheus

%files

%changelog

