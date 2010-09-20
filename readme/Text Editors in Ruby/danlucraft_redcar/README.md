{Redcar}
========

by Daniel Lucraft  
http://RedcarEditor.com/

## DESCRIPTION

A pure Ruby text editor running on JRuby. 

## INSTALLATION

You must have Java installed. You will also need to run these commands for each user on your computer that needs access to Redcar.

    $ sudo gem install redcar
    $ redcar install
    
NB the install will take a minute or so to complete as it has to download 
about 15MB of jar files.

## USAGE

Run 

    $ redcar --help
    
for a list of options.

## INSTALLING FROM SOURCE

If you want to contribute to Redcar, you can install it from the source code.

If you're running Windows, as a prerequisite, you'll need to install the 
rubyzip gem:

    $ gem install rubyzip

You will need Ant installed. You will also need RSpec, Cucumber and JSON-JRuby 
installed as JRuby gems.

    $ jruby -S gem install rspec cucumber json-jruby

Download from github, checkout the submodules and build JavaMateView. 

    $ git clone git://github.com/redcar/redcar.git
    $ cd redcar
    $ git submodule init
    $ git submodule update
    $ jruby bin/redcar install
    $ jruby -S rake build

To run on Linux and Windows:

    $ jruby bin/redcar

To run on OSX:

    $ jruby -J-XstartOnFirstThread bin/redcar        

You may also need to install the rake, rspec and cucumber gems.

## UPDATING A SOURCE BUILD

If you are running a source version of Redcar and you have pulled changes from 
master, then you may have to update your jars by updating and rebuilding:

    $ git submodule update
    $ jruby -S rake build

## PROBLEMS?

* Irc at #redcar on irc.freenode.net
* Mailing list at http://groups.google.com/group/redcar-editor

## TESTS

To run all specs and features:

    $ jruby -S rake

NB. You must leave the test window focussed while the features run. Some of the tests will fail if the test process is in the background.

## TESTS (specs)

On OSX:

    $ jruby -J-XstartOnFirstThread -S spec plugins/#{plugin_name}/spec/

On Linux:

    $ jruby -S spec plugins/#{plugin_name}/spec/

  
## TESTS (features)

On OSX:

    $ jruby -J-XstartOnFirstThread bin/cucumber plugins/#{plugin_name}/features

On Linux:

    $ jruby bin/cucumber plugins/#{plugin_name}/features/

## LICENSE

Redcar is copyright 2007-2010 Daniel Lucraft and contributors. 
It is licensed under the GPL2. See the included LICENSE file for details.
