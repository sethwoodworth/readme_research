# Weary

Weary is a tiny DSL for making the consumption of RESTful web services simple. It has evolved from the ideas put forth by libraries like [HTTParty](http://github.com/jnunemaker/httparty/ "JNunemaker's HTTParty") and [Typhoeus](http://github.com/pauldix/typhoeus "Paul Dix's Typhoeus"). It provides some sweet syntactic sugar over the Net/HTTP standard library.

What does it do:

+ Quickly build an interface to your favorite REST API.
+ Parse XML and JSON with the [Crack](http://github.com/jnunemaker/crack) library.
+ Authentication with Basic Authentication and [OAuth](http://oauth.net/).
+ Asynchronous, multi-threaded requests.

[RDoc](http://rdoc.info/projects/mwunsch/weary) | [Gem](http://rubygems.org/gems/weary) | [Wiki](http://wiki.github.com/mwunsch/weary) | [Metrics](http://getcaliper.com/caliper/project?repo=git://github.com/mwunsch/weary.git)

## Requirements

+ [Crack](http://github.com/jnunemaker/crack) >= 0.1.7
+ [OAuth](http://github.com/mojodna/oauth) >= 0.3.5

## Installation

	gem install weary
	
If you're interested in doing development on Weary, clone the repository and run `bundle install` to get the development dependencies.	
	
## Quick Start
	
	# http://apiwiki.twitter.com/Twitter-REST-API-Method%3A-users%C2%A0show
	class TwitterUser < Weary::Base
		
		domain "http://twitter.com/users/"
		
		get "show" do |resource|
			resource.with = [:id, :user_id, :screen_name]
		end
	end
	
	user = TwitterUser.new
	me = user.show(:id => "markwunsch").perform
	puts me["name"]
	
Hey, that's me!

## The Base API/DSL

Create a class that inherits from `Weary::Base` to give it methods to craft a resource request:

	class Foo < Weary::Base
		
		declare "foo" do |resource|
			resource.url = "http://path/to/foo"
		end
	end
	
If you instantiate this class, you'll get an instance method named `foo` that crafts a GET request to "http://path/to/foo"

Besides the name of the resource, you can also give `declare` a block like:

	declare "foo" do |r|
		r.url = "path/to/foo"
		r.via = :post 							# defaults to :get
		r.requires = [:id, :bar] 				# an array of params that the resource requires to be in the query/body
		r.with = [:blah]						# an array of params that you can optionally send to the resource
		r.authenticates = false					# does the method require authentication? defaults to false
		r.follows = false						# if this is set to false, the formed request will not follow redirects.
		r.headers = {'Accept' => 'text/html'}	# send custom headers. defaults to nil.
	end
					
So this would form a method:
	
	x = Foo.new
	x.foo :id => "mwunsch", :bar => 123
	
That method would return a `Weary::Request` object. Use the `perform` method and get a `Weary::Response` that you could parse and/or examine.

### Parsing the Body

Once you make your request with the fancy method that Weary created for you, you can do stuff with what it returns...which could be a good reason you're using Weary in the first place. Let's look at the above example:

	x = Foo.new
	y = x.foo(:id => "mwunsch", :bar => 123).perform.parse
	y["foos"]["user"]
	
Weary parses with Crack, but you're not beholden to it. You can get the raw Request body to have your way with:

	x = Foo.new
	y = x.foo(:id => "mwunsch", :bar => 123).perform
	Nokogiri.parse(y.body)
	
*note: Weary used to have Nokogiri built in, using the `#search` method, but that was dropped.*	

### Shortcuts

Of course, you don't always have to use `declare`; that is a little too ambiguous. You can also use `get`, `post`, `delete`, etc. Those do the obvious.

### Forming URLs

There are many ways to form URLs in Weary. You can define URLs for the entire class by typing:

	class Foo < Weary::Base
		
		domain "http://foo.bar/"
		format :xml
		
		get "show_users"
	end
	
If you don't supply a url when declaring the Resource, Weary will look to see if you've defined a domain, and will make a url for you. The above `get` declaration creates a url that looks like: *http://foo.bar/show_users.xml*. I think it's better to write the whole URL out. That's unambiguous.
	
### Weary DSL

You can create some defaults for all of our resources easily:

	class Foo < Weary::Base
	
		def initialize(username,password)
			self.credentials username,password	#basic authentication
			self.defaults = {:user => username}	#parameters that will be passed in every request	 
		end

		domain "http://foo.bar/"
		format :xml
		headers {'Accept' => 'text/html'}	# set headers
		
		post "update" {|r| r.authenticates = true}	# uses the defaults defined above!			
	end
	
Then you can do something like this:

	f = Foo.new('me','secretz')
	f.update
	
Which will create a POST Request for *http://foo.bar/update.xml* that will authenticate you, using basic authentication, with the username/password of "me"/"secrets" and will send the parameter `{:user => "me"}`. Easy.

## Weary Class Methods

Maybe you don't want the baggage that comes with `Weary::Base`. That's okay, Weary provides some basic class-level methods to Easily build a `Weary::Request`:

	# See examples/repo.rb to see this in practice
	class Repository

	  def show(user, repo)
	    Weary.get "http://github.com/api/v2/yaml/repos/show/#{user}/#{repo}"
	  end

	end
	
	Repository.new.show 'mwunsch', 'weary'
	
That will build the Get request to fetch the YAML info about this repository.

Pass a block to `Weary.get` to dive further into the Request:

	Weary.get "http://twitter.com/statuses/user_timeline" do |req|
		req.follows = false
		req.with = {:id => 'markwunsch'}
		req.credentials = {:username => 'markwunsch', :password => 'secret'}
		req.headers = {"User-Agent" => Weary::UserAgents["Safari 4.0.2 - Mac"]}
	end
	
## Request Callbacks

A `Weary::Request` has a couple of callbacks you can do:

	status = Weary.get("http://twitter.com/statuses/user_timeline") do |r|
		r.with = {:id => 'markwunsch'}
	end
	
	status.before_send do |request|
		puts "Sending a request to #{request.uri}"
	end
	
	status.on_complete do |response|
		if response.success?
			puts response.body
		else
			puts "Something went wrong: #{response.code}: #{response.message}"
		end
	end
	
`before_send` is sent just before the request is made, and `on_complete` is triggered immediately following. `before_send` passes the Request object to the block and `on_complete` passes the Response object.

You don't need to define `on_complete`, though. Passing a block to the `perform` method of the Request also defines this callback or will overwrite what you had previously defined:

	status.perform do |response|
		puts "Request to #{response.url}, complete. Got a #{response.code}."
	end
	
## Multiple Asynchronous Requests with Batch

Requests, along with the `perform` method, also has a `perform!` method, which spins off a Thread to actually perform the Net::HTTP Request. This method returns a Thread object, and is encapsulated by the `perform` method.

Weary::Batch allows you to make a group of `perform!` requests, firing at will. It takes a group of Requests.

	# see examples/batch.rb
	resources = %w[http://twitter.com http://github.com http://vimeo.com http://tumblr.com]
	requests = []
	
	## build the group of requests:
	resources.each do |url|
		requests << Weary.get(url) do |req|
			req.on_complete {|res| puts "Hello from #{res.url}"}
		end
	end
	
	## And fire them off:
	Weary.batch(requests).perform
	
Batch has callbacks, just like the Request:

	Weary.batch(requests).perform do
		puts 'All done.'
	end

You can investigate the pool of threads once you've called `perform` with `Batch#pool` or look at all the returned responses with `Batch#responses`.

## And more...
	
There's more to discover in the Wiki.
