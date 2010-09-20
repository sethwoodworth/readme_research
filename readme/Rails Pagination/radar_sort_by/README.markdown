# sort_by

Sort By is a plugin that allows you to generate a table that has sortable columns. It'll probably only work on the latest version of Rails, which is what you should be using. No excuses, thanks.

## ActiveRecord

Provided to you by this plugin in ActiveRecord is a method called `sort_by` which takes three arguments:

* The first is the field you want to sort by, and this must be a valid field otherwise an error will be raised.
* The second is the direction you want to sort by, also must be valid otherwise an error will be raised. Valid directions are "asc" and "desc" and it is case-insensitive.
* The third is an options hash, which is exactly the same options hash you would pass to an every day find.
* It also takes a block.

Its brother method is `paginated_sort_by` which takes four options:

* The first is the field you want to sort by, and this must be a valid field otherwise an error will be raised.
* The second is the direction you want to sort by, also must be valid otherwise an error will be raised. Valid directions are "asc" and "desc" and it is case-insensitive.
* The third is an options hash, which is exactly the same options hash you would pass to `paginate` from will\_paginate.
* The fourth is another options hash, which is exactly the same options hash you would pass to an every day `find`.

## ActionView

The great stuff comes in the view. This plugin provides a method called `paginated_sort_table`. This generates a table like the [one seen here](http://skitch.com/radarlistener/bam21/blogs-index "one seen here"). This uses the generated scaffold from an everyday Rails application. In my index action in the controller I've edited it to now be:
   
    def index
      @blogs = Blog.paginated_sort_by(params[:sort_by] || "id", params[:order])
    end
    
And my corresponding index template:

    <h1>Listing blogs</h1>
    <%= paginated_sort_table(@blogs) %>
    
That's all! Now if I were to have more than 10 blogs there I would be given pagination icons above and below the table [as seen here](http://skitch.com/radarlistener/bam4m/blogs-index "as seen here").

## More ActionView


### `:only`
By default it will give you a table of all the fields in no particular order. To fix this, call the method like this:

    <%= paginated_sort_table(@blogs, :only => ["field1", "field2"]) %>
    
The fields will be displayed in order that you specify them.

### `:except`

If you only want to remove some fields there's the `:except` option:

    <%= paginated_sort_table(@blogs, :except => ["field1", "field2"]) %>

### `:also`

If you wish to include a field from a related table it is suggested that you first eager load the association:

    @blogs = Blog.all(:include => :author)

And then in your view you simply specify the `:also` option:

    <%= paginated_sort_table(@blogs, { :also => "author.name" } ) %>

By default, this will show up as "name".

This is not just limited to field names, it can be any method that is available on that association:

    @users = User.all(:include => :blogs)

    <%= paginated_sort_table(@users, { :also => "blogs.count" } ) %>

You are unable to sort by external fields at the moment.


### `:names`
    
To specify alternative names to the fields pass in the `:names` option:
    
    <%= paginated_sort_table(@blogs, :names => { :field1 => "Field 2 in disguise"}) %>
    
### `:titleize`

If you don't want your fields to be titleized just say so:

    <%= paginated_sort_table(@blogs, :titleize => false) %>

### `:class`
    
You can also pass in a class, if you don't want it to be called "sort_by"
   	
	  <%= paginated_sort_table(@blogs, {}, { :class => 'blue' }) %>
	  
## Concatenated Fields

If you wish to sort by a concatenated version of two fields, for example `first_name` and `last_name` define a method in your model to concatenate these two:

    def name
      first_name + ' ' + last_name
    end

And then call that method using the `:also` (or `:only`) option:

    <%= paginated_sort_table(@users, { :also => "name" } ) %>
    
## Will Paginate Options Go Where?!

In the last options hash:

    <%= paginated_sort_table(@blogs, {}, {}, { :options => "go here" }) %>
    
Check out the [awesome will paginate docs](http://wiki.github.com/mislav/will_paginate) on what these options are.

## Sorting Icons

You'll have to provide your own sorting icons, though. The names are sort\_asc and sort\_desc and the extension defaults to `jpg` but you can change it by specifying it in the last options hash:

      <%= paginated_sort_table(@blogs, {}, { :image_type => "png" }) %>
      
### Contributors

Mikael Kabanov (mcdba) - `:class` option for view helper.
George Montana Harkin (harking) - Idea for way to show columns from other tables, `:also` option
      