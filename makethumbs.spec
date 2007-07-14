#
%define	_rev	1.272

Summary:	makethumbs
Name:		makethumbs
Version:	%{_rev}
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.molenda.com/makethumbs/%{name}.sh
# Source0-md5:	dab049248e498fba42d3ddc6ed78d726
Source1:	http://www.molenda.com/makethumbs/rotate.sh
# Source1-md5:	cd5d7319ca28b142cba99bb67a26a4e0
Source2:	%{name}-pl.conf
URL:		http://www.molenda.com/makethumbs/
Requires:	ImageMagick
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
makethumbs.sh and rotate.sh are scripts to create polished, static
image galleries suitable for the web or for a CD-ROM, given a bunch of
JPEGs in a directory. makethumbs is most commonly used in conjunction
a digital camera. Do you want to put a batch of pictures on the web
for people to browse? Once the images are on your system, makethumbs
will give you usable web pages with zero extra work. If you have more
than five seconds to spend on your pictures, makethumbs allows for
lots of customization, labeling, and image descriptions.

The goals of makethumbs are

    - exist in a single script that can be mailed around easily
    - generate clean, simple, portable HTML
    - don't lock the images into any kind of database
    - portable, portable, portable

There are many other image gallery programs. Within the category of
programs that don't import all your images into a database or depend
on dynamic PHP/CGI scripting, I believe makethumbs.sh is one of the
best around. Many of these programs break some of my stated
goals--they generate fancy HTML that acts oddly/requires certain
browsers, or they make big databases to track and display your images
eighteen ways from Sunday, or they touch your original images, or they
only run on Winblows, or they require all sorts of ancillary software
to work correctly.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/makethumbs.sh
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/rotate.sh
cp %{SOURCE2}	.

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc makethumbs-pl.conf
%attr(755,root,root) %{_bindir}/*
