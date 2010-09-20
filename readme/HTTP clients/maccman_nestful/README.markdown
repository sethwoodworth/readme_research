Nestful is a simple Ruby HTTP/REST client with a sane API. 

## Installation

    sudo gem install nestful

## Features

  * Simple API
  * File buffering
  * Before/Progress/After Callbacks
  * JSON & XML requests
  * Multipart requests (file uploading)
  * Resource API
  * Proxy support
  * SSL support

## Options

Request options:

  * headers (hash)
  * params  (hash)
  * buffer  (true/false)
  * method  (:get/:post/:put/:delete/:head)

Connection options:

  * proxy
  * user
  * password
  * auth_type
  * timeout
  * ssl_options

## API
  
### GET request

    Nestful.get 'http://example.com' #=> "body"

### POST request

    Nestful.post 'http://example.com', :format => :form #=> "body"
    
### Parameters

    Nestful.get 'http://example.com', :params => {:nestled => {:params => 1}}

### JSON request

    Nestful.get 'http://example.com', :format => :json  #=> {:json_hash => 1}
    Nestful.json_get 'http://example.com'               #=> {:json_hash => 1}
    Nestful.post 'http://example.com', :format => :json, :params => {:q => 'test'} #=> {:json_hash => 1}
  
### Resource

    Nestful::Resource.new('http://example.com')['assets'][1].get(:format => :xml) #=> {:xml_hash => 1}

### Buffer download, return Tempfile

    Nestful.get 'http://example.com/file.jpg', :buffer => true #=> <File ...>

### Callbacks

    Nestful.get 'http://www.google.co.uk', :buffer => true, :progress => Proc.new {|conn, total, size| p total; p size }
    Nestful::Request.before_request {|conn| }
    Nestful::Request.after_request {|conn, response| }

### Multipart post

    Nestful.post 'http://example.com', :format => :multipart, :params => {:file => File.open('README')}

## Credits
  Large parts of the connection code were taken from ActiveResource