# TODO
# - build from source: https://code.google.com/p/xmind3/
# - use system eclipse files not bundled copy

Summary:	Brainstorming and Mind Mapping
Name:		xmind
Version:	3.2.1
Release:	0.6
License:	EPL v1.0 / GPL v3
Group:		Applications/Engineering
URL:		http://www.xmind.net/
Source0:	http://dl2.xmind.net/xmind-downloads/%{name}-portable-%{version}.201011212218.zip
# Source0-md5:	-
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.xml
Source4:	%{name}.sh
BuildRequires:	unzip
Requires:	eclipse-swt
Requires:	jre
Requires:	lame
Requires:	shared-mime-info
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_libdir}/%{name}

%description
XMind is an open source project that contributes to building a
cutting-edge brainstorming/mind-mapping facility, focused on both
usability and extendability. It helps people in capturing ideas into
visually self-organized charts and sharing them for collaboration and
communication. Currently supporting mind maps, fishbone diagrams, tree
diagrams, org-charts, logic charts, and even spreadsheets. Often used
for knowledge management, meeting minutes, task management, and GTD.

%prep
%setup -qc

%ifarch %{x8664}
%{__rm} -r XMind_Linux XMind_Windows XMind_Mac_OS_X
mv XMind_Linux{_64bit,}
%else
%{__rm} -r XMind_Linux_64bit XMind_Windows XMind_Mac_OS_X
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
cp -af * $RPM_BUILD_ROOT%{_appdir}
install -p %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{name}

# desktop
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# mime type
install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/mime/packages

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc *.txt *.html
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
%{_datadir}/mime/packages

%dir %{_appdir}
%{_appdir}/*.html
%{_appdir}/*.txt

%dir %{_appdir}/XMind_Linux
%{_appdir}/XMind_Linux*/xmind-bin.ini
%attr(755,root,root) %{_appdir}/XMind_Linux/xmind
%attr(755,root,root) %{_appdir}/XMind_Linux/xmind-bin
%{_appdir}/XMind_Linux/.env
%{_appdir}/XMind_Linux/about_files
%{_appdir}/XMind_Linux/eclipse_about.html

%dir %{_appdir}/Commons
%{_appdir}/Commons/.eclipseproduct
%dir %{_appdir}/Commons/configuration
%{_appdir}/Commons/configuration/config.ini
%{_appdir}/Commons/configuration/*.simpleconfigurator

%dir %{_appdir}/Commons/plugins
%{_appdir}/Commons/plugins/com.ibm.icu_*.jar
%{_appdir}/Commons/plugins/com.lowagie.itext*
%{_appdir}/Commons/plugins/javax.servlet_*.jar
%{_appdir}/Commons/plugins/net.sourceforge.jazzy_*.jar
%{_appdir}/Commons/plugins/net.xmind.*.jar
%{_appdir}/Commons/plugins/org.apache.commons.codec_*.jar
%{_appdir}/Commons/plugins/org.apache.commons.httpclient_*.jar
%{_appdir}/Commons/plugins/org.apache.commons.logging_*.jar
%{_appdir}/Commons/plugins/org.apache.tools.zip_*.jar
%{_appdir}/Commons/plugins/org.bouncycastle_*.jar
%{_appdir}/Commons/plugins/org.eclipse.*
%{_appdir}/Commons/plugins/org.json_*.jar
%{_appdir}/Commons/plugins/org.xmind.*
