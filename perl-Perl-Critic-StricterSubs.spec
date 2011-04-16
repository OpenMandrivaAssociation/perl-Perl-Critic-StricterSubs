%define upstream_name    Perl-Critic-StricterSubs
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl::Critic plugin for stricter subroutine checks
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::PathList)
BuildRequires: perl(Perl::Critic)
BuildRequires: perl(Perl::Critic::TestUtils)
BuildRequires: perl(Perl::Critic::Utils)
BuildRequires: perl(Perl::Critic::Violation)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
As a dynamic language, Perl doesn't require you to define subroutines until
run-time. Although this is a powerful feature, it can also be a major
source of bugs. For example, you might mistype the name of a subroutine, or
call a subroutine from another module without including that module or
importing that subroutine. And unless you have very good test coverage, you
might not know about these bugs until you have already launched your code.

The the Perl::Critic::Policy manpage modules in this distribution are aimed
at reducing errors caused by invoking subroutines that are not defined.
Each Policy can be used separately. But when applied together, they enforce
a specific and deliberate coding style that minimizes the chance of writing
code that makes calls to undefined subroutines.

This coding style will not appeal to everyone. Some folks will surely find
this coding style to be too verbose or too restrictive. In particular,
importing via the Exporter manpage tags and pattern matching is purposely
not supported. But hopefully, these Policies will encourage you to
consciously consider the inherent trade-offs of your current coding style.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


