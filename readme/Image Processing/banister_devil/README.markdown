![Alt text](http://dl.getdropbox.com/u/239375/DevIL.png)

Ruby Devil version 0.1.9.1
========================

[Read The Documentation](http://rdoc.info/projects/banister/devil)

* Original author: Jaroslaw Tworek <dev.jrx@gmail.com>
* Current maintainer: John Mair (banisterfiend) [http://banisterfiend.wordpress.com](http://banisterfiend.wordpress.com)

Ruby bindings for the Developer's Image Library
You need DevIL installed to use this extension

The Ruby Devil Project page is here: [http://github.com/banister/devil](http://github.com/banister/devil)


Installation Instructions:
==========================

For debian:

* install the libdevil and libdevil-dev packages

For Gentoo:

* emerge "media-libs/devil"

For windows:

* download devil-dlls.zip from [http://github.com/banister/devil/downloads](http://github.com/banister/devil/downloads)
* and copy the uncompressed files to c:\ruby\bin\

For macosx:

* sudo port install libdevil

For other systems:

* install libdevil and lib-devil-dev using your package manager
* OR download and install the libraries from [http://openil.sourceforge.net](http://openil.sourceforge.net)

After you've installed the DevIL libraries you install the gem by going:

* gem install devil

If you wish to use the Gosu and TexPlay extensions, it is necessary to also have:

* the Gosu gem (gem install gosu)
* the TexPlay gem (gem install texplay)
* ruby-opengl (gem install ruby-opengl)

For now, there is support for just a subset of DevIL functions, but it is enough
for 95% things you may want to do.

For example uses, see test/ directory
(note: that many of the examples use the Gosu library...this is often just for visualization purposes. Alot of the functionality does not depend on Gosu being present)
