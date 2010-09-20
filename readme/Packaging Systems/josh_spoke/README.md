Spoke
=====

Spoke helps package and distribute GitHub code.

Encourages packaging best practices and conventions to eliminate long specifications forms and configuration sit ups.

Rubygem publishing
------------------

Generate a RubyGem spec from a GitHub repository.

    $ spoke-gemspec git://github.com/josh/spoke.git
    Gem::Specification.new do |s|
      s.name = %q{spoke}
      s.version = "0.1.5"

      s.authors = ["Joshua Peek"]
      s.date = %q{2010-02-28}
      s.description = %q{Helps package and distribute GitHub code}
      s.email = %q{josh@joshpeek.com}
      s.executables = ["spoke", ...]
      s.extra_rdoc_files = ["README.md"]
      s.files = ["lib/spoke.rb", ...]
      s.homepage = %q{http://spoke.heroku.com/}
      s.require_paths = ["lib"]
      s.rubygems_version = %q{1.3.6}
      # ...
    end

Or build and publish a gem directly to gemcutter.

    $ spoke-gem --push git://github.com/josh/spoke.git


Homebrew publishing
-------------------

    $ spoke-formula git://github.com/josh/spoke.git
    require 'formula'

    class Spoke <Formula
      url 'http://github.com/josh/spoke/tarball/v0.1.5'
      homepage 'http://github.com/josh/spoke'

      def install
        patch_bin_files
        bin.install Dir['bin/*']

        FileUtils.mkdir_p site_ruby
        FileUtils.cp_r(Dir['lib/*'], site_ruby)

        man1.install 'man/spoke.1'
      end

      # ...
    end
