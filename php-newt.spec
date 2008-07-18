%define modname newt
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A30_%{modname}.ini

Summary:	Newt provides window library functions for PHP
Name:		php-%{modname}
Version:	1.1
Release:	%mkrel 19
Group:		Development/PHP
License:	PHP License
URL:		http://php-newt.sourceforge.net/
Source0:	http://pecl.php.net/get/newt-%{version}.tar.bz2
Patch0:		newt-0.3-lib64.diff
BuildRequires:	newt-devel
BuildRequires:	php-devel >= 3:5.2.0
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHP-NEWT - PHP language extension for RedHat Newt library, a terminal-based
window and widget library for writing applications with user friendly
interface. Once this extension is enabled in PHP it will provide the use of
Newt widgets, such as windows, buttons, checkboxes, radiobuttons, labels,
editboxes, scrolls, textareas, scales, etc. Use of this extension if very
similar to the original Newt API of C programming language.

%prep

%setup -q -n newt-%{version}
%patch0 -p0

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
[ "../package.xml" != "/" ] && rm -f ../package.xml

%files 
%defattr(-,root,root)
%doc examples CREDITS TODO
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
