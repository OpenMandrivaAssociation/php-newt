%define modname newt
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A30_%{modname}.ini

Summary:	Newt provides window library functions for PHP
Name:		php-%{modname}
Version:	1.2.8
Release:	1
Group:		Development/PHP
License:	PHP License
URL:		http://php-newt.sourceforge.net/
Source0:	http://pecl.php.net/get/newt-%{version}.tgz
Patch0:		newt-0.3-lib64.diff
BuildRequires:	newt-devel
BuildRequires:	php-devel >= 3:5.2.0
Epoch:		1

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
%doc examples CREDITS TODO
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Thu May 03 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.6-2mdv2012.0
+ Revision: 795482
- rebuild for php-5.4.x

* Thu Mar 29 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.6-1
+ Revision: 788165
- 1.2.6

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.5-4
+ Revision: 761274
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.5-3
+ Revision: 696451
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.5-2
+ Revision: 695446
- rebuilt for php-5.3.7

* Mon Jun 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.5-1
+ Revision: 687518
- 1.2.5

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-9
+ Revision: 646667
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-8mdv2011.0
+ Revision: 629841
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-7mdv2011.0
+ Revision: 628168
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-6mdv2011.0
+ Revision: 600514
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-5mdv2011.0
+ Revision: 588852
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-4mdv2010.1
+ Revision: 514580
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-3mdv2010.1
+ Revision: 485412
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-2mdv2010.1
+ Revision: 468197
- rebuilt against php-5.3.1

* Fri Nov 06 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.4-1mdv2010.1
+ Revision: 461165
- 1.2.4

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.3-2mdv2010.0
+ Revision: 451302
- rebuild

* Thu Sep 24 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.3-1mdv2010.0
+ Revision: 448203
- 1.2.3

* Sat Aug 08 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.2-1mdv2010.0
+ Revision: 411743
- 1.2.2

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1:1.2.1-5mdv2010.0
+ Revision: 397320
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.1-4mdv2010.0
+ Revision: 377009
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.1-3mdv2009.1
+ Revision: 346522
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.1-2mdv2009.1
+ Revision: 341781
- rebuilt against php-5.2.9RC2

* Sat Jan 31 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.1-1mdv2009.1
+ Revision: 335726
- 1.2.1
- rediffed P0

* Sun Jan 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-21mdv2009.1
+ Revision: 324314
- rediffed P0

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-20mdv2009.1
+ Revision: 310290
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-19mdv2009.0
+ Revision: 238415
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-18mdv2009.0
+ Revision: 200253
- rebuilt for php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-17mdv2008.1
+ Revision: 162143
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-16mdv2008.1
+ Revision: 107698
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-15mdv2008.0
+ Revision: 77563
- rebuilt against php-5.2.4

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-14mdv2008.0
+ Revision: 39511
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-13mdv2008.0
+ Revision: 33865
- rebuilt against new upstream version (5.2.3)

* Thu May 31 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:1.1-12mdv2008.0
+ Revision: 33396
- Rebuild again, for rpm changelog fix.

* Thu May 31 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:1.1-11mdv2008.0
+ Revision: 33307
- Rebuild with libnewt0.52.

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-10mdv2008.0
+ Revision: 21344
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2007.0
+ Revision: 117602
- rebuilt against new upstream version (5.2.1)

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-8mdv2007.1
+ Revision: 79293
- rebuild
- rebuilt for php-5.2.0
- Import php-newt

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-6
- rebuilt for php-5.1.6

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-5mdk
- rebuild

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-4mdk
- rebuilt for php-5.1.3

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-3mdk
- rebuilt against php-5.1.2

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-2mdk
- rebuilt against php-5.1.1

* Sat Nov 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.1-1mdk
- 1.1
- rebuilt against php-5.1.0
- fix versioning

* Sun Oct 02 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0_0.3-0.RC1.1mdk
- rebuilt against php-5.1.0RC1

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.5_0.3-1mdk
- rebuilt against php-5.0.5 (Major security fixes)

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4_0.3-1mdk
- rename the package

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4_0.3-1mdk
- 5.0.4

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3_0.3-2mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3_0.3-1mdk
- initial Mandrakelinux package

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.3-3mdk
- rebuilt against a non hardened-php aware php lib

* Sat Jan 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.3-2mdk
- rebuild due to hardened-php-0.2.6
- cleanups

* Sat Jan 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_0.3-1mdk
- initial mandrake package
- added P0


