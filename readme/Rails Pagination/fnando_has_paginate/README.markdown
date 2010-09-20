has\_paginate
=============

Instalation
-----------

Install the plugin with `script/plugin install git://github.com/fnando/has_paginate.git`

Usage
-----

This plugins uses the named scope feature introduced by Ruby on Rails 2.1 to
provide pagination. The result will be :limit + 1, so we'll be able to
know if there is a next page without querying the database for `count`, which 
causes performance issues on large databases. The default is 10 items per page.

	User.paginate                             #=> :offset => 0, :limit => 11
	User.paginate(:page => 2)                 #=> :offset => 10, :limit => 11
	User.paginate(:page => 2, :limit => 15)   #=> :offset => 15, :limit => 16
	@user.things.paginate(:page => params[:page])

After retrieving the results you can display it by using the each_paginate 
method.

	<% each_paginate @users do |user, i| %>
	  <%= user.name %>
	<% end %>

	<% each_paginate @users, :limit => 12 do |user, i| %>
	  <%= user.name %>
	<% end %>

To display the pagination, use the paginate helper.
	
	# general usage
	# path = String/Proc
	# options = Hash
	<%= paginate @users, path, options %>
	<%= paginate @users, options={} %>

	<%= paginate @users %> #=> this will set path to request.request_uri
	<%= paginate @users, users_path %>
	<%= paginate @users, users_path, :page => params[:page] %>
	<%= paginate @users, users_path, :page => params[:page], :limit => 10 %>
	<%= paginate @users, users_path, :next_label => 'Recent' %>
	<%= paginate @users, users_path, :previous_label => 'Older' %>
	<%= paginate @users, users_path, :param_name => :p %>
	<%= paginate @users, users_path, :show_page => true %>
	<%= paginate @users, users_path, :show_disabled => false %>
	<%= paginate @users, :url => users_path %>
	<%= paginate @users, :url => proc {|page| users_path(page) }%>

You can set properties globally.

	class ApplicationController < ActionController::Base
	  Paginate.settings = {
		:next_label => 'Next page',
	    :previous_label => 'Previous page',
	    :param_name => :page,
	    :show_disabled => true,
	    :show_page => true, 
	    :limit => 10,
	    :format => 'Page %d'
	  }
	end

Additionaly, you have a new method called `find_in_chunks`, that retrieves all
records by making multiple queries, instead of using `User.all`, which 
consumes lots of memory. This is specially great when you need to iterate
a table for doing background jobs.

The example below will query the database 10 times if it has 100 records, 
returning 10 records for each query.

	User.find_in_chunks(:conditions => {:active => true}) do |user|
	  user.recount_score!
	end

This plugins adds a helper method to the named scope called `items?` that
verifies if the collection is not empty.

	<% if @users.items? %>
		<!-- display the collection -->
	<% else %>
		<p>Sorry! No users found!</p>
	<% end %>

Copyright (c) 2008 Nando Vieira, released under the MIT license