%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	IN
%define		_status		alpha
%define		_pearname	Validate_IN

Summary:	%{_pearname} - Validation class for the Republic of India
Summary(pl):	%{_pearname} - klasa walidacji dla republiki Indii
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	LGPL Version 2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fe0e1e03318aa5e220ecc0bb2f1ae9f9
URL:		http://pear.php.net/package/Validate_IN/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Pakiet ten dostarcza metod walidacji dla indyjskich:
- sta�ych numer�w kont (PAN i TAN)
- kod�w stan�w oraz terytori�w
- numer�w telefon�w
- kod�w pocztowych
- numer�w rejestracyjnych pojazdow

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
