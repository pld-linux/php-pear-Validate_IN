%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	IN
%define		_status		alpha
%define		_pearname	Validate_IN

Summary:	%{_pearname} - Validation class for the Republic of India
Summary(pl.UTF-8):	%{_pearname} - klasa walidacji dla Republiki Indii
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fe0e1e03318aa5e220ecc0bb2f1ae9f9
URL:		http://pear.php.net/package/Validate_IN/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains locale validation for Indian:
- Permanent Account Number (PAN and TAN)
- State and Union Territory codes
- Telephone Numbers
- Postal (Zip) Codes
- Vehicle License Plate Numbers

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza metod walidacji dla indyjskich:
- stałych numerów kont (PAN i TAN)
- kodów stanów oraz terytoriów
- numerów telefonów
- kodów pocztowych
- numerów rejestracyjnych pojazdów

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
%{php_pear_dir}/Validate/IN.php
