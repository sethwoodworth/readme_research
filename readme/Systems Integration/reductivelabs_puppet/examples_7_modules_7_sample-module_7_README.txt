Jeff McCune <jeff.mccune@northstarlabs.net>
2007-08-14

This small, sample module demonstrates how to extend the puppet language
with a new parser function.

See:
manifests/init.pp
lib/puppet/parser/functions/hostname_to_dn.rb
templates/sample.erb

Note the consistent naming of files for Puppet::Util::Autoload

Reference Documents:
http://reductivelabs.com/trac/puppet/wiki/ModuleOrganisation
http://docs.puppetlabs.com/guides/custom_functions.html
http://reductivelabs.com/trac/puppet/wiki/FunctionReference
