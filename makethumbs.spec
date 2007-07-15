Summary:	From digicam to web page in under thirty seconds
Summary(pl.UTF-8):	Od aparatu cyfrowego do strony WWW poniżej 30 sekund
Name:		makethumbs
Version:	1.272
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.molenda.com/makethumbs/%{name}.sh
# Source0-md5:	dab049248e498fba42d3ddc6ed78d726
Source1:	http://www.molenda.com/makethumbs/rotate.sh
# Source1-md5:	cd5d7319ca28b142cba99bb67a26a4e0
Source2:	%{name}-pl.conf
URL:		http://www.molenda.com/makethumbs/
BuildRequires:	sed >= 4.0
Requires:	ImageMagick
Requires:	ImageMagick-coder-jpeg
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

The goals of makethumbs are:
- exist in a single script that can be mailed around easily
- generate clean, simple, portable HTML
- don't lock the images into any kind of database
- portable, portable, portable

%description -l pl.UTF-8
makethumbs.sh i rotate.sh to skrypty do tworzenia wygładzonych,
statycznych galerii obrazów, nadających się na stronę WWW czy CD-ROM,
z dużej liczby JPEG-ów w katalogu. makethumbs jest używany zwykle w
połączeniu z aparatem cyfrowym. Kiedy chcemy udostępnić innym duży
zestaw zdjęć, makethumbs tworzy używalne strony WWW bez dodatkowej
pracy. Jeśli mamy więcej niż 5 sekund, makethumbs pozwala w istotny
sposób dostosować galerię, dodać etykiety i opisy obrazów.

makethumbs ma za zadanie:
- istnieć w pojedynczym skrypcie, który można wysłać e-mailem
- generować czysty, prosty, przenośny HTML
- nie zamykać obrazów w żadnej bazie danych
- być przenośnym, przenośnym i jeszcze raz przenośnym

%prep
%setup -q -c -T
cp %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/makethumbs.sh
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/rotate.sh
sed -i -e s/'DEFAULT_preferred_image_tools="sips" # or "netpbm" or "imagemagick"'/'DEFAULT_preferred_image_tools="imagemagick" # or "netpbm" or "sips"'/g $RPM_BUILD_ROOT%{_bindir}/makethumbs.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc makethumbs-pl.conf
%attr(755,root,root) %{_bindir}/*
