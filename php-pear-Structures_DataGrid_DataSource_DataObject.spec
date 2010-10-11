%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_DataObject
%define		subver	dev1
%define		rel		1
Summary:	%{_pearname} - DataSource driver using PEAR::DB_DataObject
Summary(pl.UTF-8):	%{_pearname} - sterownik DataSource do PEAR::DB_DataObject
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	0.%{subver}.%{rel}
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	a6f780111002b3f31a2003bcdf1fe555
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_DataObject/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-DB_DataObject >= 1.8.7
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.9.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB/DataObject/FormBuilder.*)'

%description
This is a DataSource driver for Structures_DataGrid using
PEAR::DB_DataObject.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik do PEAR::DB_DataObject dla
Structures_DataGrid.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/DataSource/DataObject.php
