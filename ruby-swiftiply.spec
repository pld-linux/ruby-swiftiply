Summary:	Ruby reverse-proxy application server
Summary(pl.UTF-8):	Serwer odwrotnego proxy aplikacji dla języka Ruby
Name:		ruby-swiftiply
Version:	0.6.1
Release:	1
License:	Ruby
Group:		Development/Languages
#Source0:	http://swiftiply.swiftcore.org/files/swiftiply-%{version}.tar.bz2
Source0:	http://rubyforge.org/frs/download.php/24061/swiftiply-%{version}.tar.bz2
# Source0-md5:	301dfb533afcd0c7c05b1f2431de6a99
URL:		http://swiftiply.swiftcore.org/
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-eventmachine
Obsoletes:	ruby-swiftiply-ramaze
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Swiftiply is a backend agnostic clustering proxy for web applications
that is specifically designed to support HTTP traffic from web
frameworks. Unlike Pen (http://siag.nu/pen/), Swiftiply is not
intended as a general purpose load balancer for TCP protocols and
unlike HAProxy (http://haproxy.1wt.eu/), it is not a highly
configurable general purpose proxy overflowing with features.

What it is, though, is a very fast, narrowly targetted clustering
proxy. In back to back comparisons of Swiftiply to HAProxy, Swiftiply
reliably outperforms HAProxy (tested using IOWA, Rails, and Ramaze
backend processes) and, depending on your web framework, you may not
even need to put a traditional web server into your architecture at
all.

%description -l pl.UTF-8
Swiftiply to niezależny od backendu klastrowy serwer proxy dla
aplikacji WWW, zaprojektowany z myślą o obsłudze ruchu HTTP ze
szkieletów WWW. W przeciwieństwie do Pena (http://siag.nu/pen/)
Swiftiply nie ma być load balancerem ogólnego przeznaczenia dla
protokołów TCP i w przeciwieństwie do HAProxy (http://haproxy.1wt.eu/)
nie jest wysoko konfigurowalnym proxy ogólnego przeznaczenia
przepełnionym możliwościami.

Jest jednak bardzo szybkim proxy klastrowym o wąskich zastosowaniach.
W porównaniach do HAProxy Swiftiply wiarygodnie zwycięża pod względem
wydajności (testowane z procesami backendów IOWA, Rails i Ramaze)
oraz, w zależności od szkieletu WWW, może nawet wyeliminować potrzebę
uruchamiania tradycyjnego serwera WWW.

%package mongrel
Summary:	Swiftiply patch to Mongrel HTTP Server
Summary(pl.UTF-8):	Poprawka Swiftiply dla serwera HTTP Mongrel
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	ruby-mongrel

%description mongrel
Swiftiply patch to Mongrel HTTP Server.

%description mongrel -l pl.UTF-8
Poprawka Swiftiply dla serwera HTTP Mongrel.

%prep
%setup -n swiftiply-%{version}

%build
ruby setup.rb config --vendor
ruby setup.rb setup --no-doc


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README
%attr(755,root,root) %{_bindir}/swiftiply
%dir %{ruby_rubylibdir}/swiftcore
%{ruby_rubylibdir}/swiftcore/Swiftiply.rb
%dir %{ruby_rubylibdir}/swiftcore/Swiftiply
%{ruby_rubylibdir}/swiftcore/Swiftiply/support_pagecache.rb
%{ruby_rubylibdir}/swiftcore/Swiftiply/swiftiply_client.rb
%{ruby_rubylibdir}/swiftcore/types.rb
%attr(755,root,root) %{ruby_archdir}/*.so

%files mongrel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/swiftiply_mongrel_rails
%{ruby_rubylibdir}/swiftcore/evented_mongrel.rb
%{ruby_rubylibdir}/swiftcore/swiftiplied_mongrel.rb
