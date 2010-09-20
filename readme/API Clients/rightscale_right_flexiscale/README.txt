== RightScale Flexiscale API Ruby Gem

Published by RightScale, Inc. under the MIT License. For information about
RightScale, see www.rightscale.com 

== DESCRIPTION:

The RightScale GoGrid gem has been designed to provide a robust interface to
Flexiscale‘s existing API. 


== FEATURES/PROBLEMS:

    * Full programmatic access to the Flexiscale API.
    * Complete error handling: all operations check for errors and report
      complete error information.

== SYNOPSIS:

  flexiscale = Rightscale::FlexiscaleApi.new(username, password)
  
  # get servers list
  servers = flexiscale.list_servers
  
  # OS images
  images = flexiscale.list_operating_system_images
  
  # create a new server
  image  = flexiscale.list_operating_system_images.first
  package   = flexiscale.list_packages.first
  vlan   = flexiscale.list_vlans.first
  server_id = flexiscale.create_server('my_awesome_server', package[:fxs_id], 1, 1024, 20, image[:fxs_id], vlan[:fxs_id])
  
  # launch a server
  job_id = flexiscale.start_server('my_awesome_server')
  
  # reboot
  job_id = flexiscale.reboot_server('my_awesome_server')
  
  # stop and destroy server
  job_id = flexiscale.stop_server('my_awesome_server')

  if flexiscale.wait_for_jobs(job_id)
    flexiscale.destroy_server('my_awesome_server')
  end

== REQUIREMENTS:

* soap4r

== INSTALL:

* sudo gem install right_flexiscale

== LICENSE:

Copyright (c) 2008-2009 RightScale Inc

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


