WeeklyBuilder
==============

A weekly calendar builder for ruby on rails. Although there are countless monthly calendars on Github I couldn't find any with a weekly view, so I built my own.

The calendar is horizontally scrolling with a completely fluid CSS layout and an option for business/24 hours. Weekly views are useful because the events are plotted based on time and the width is determined by how long the event is scheduled for. So there is a visual representation of when the event is, not just a list.

The code is inspired by P8s table_builder which I recommend for monthly calendars.

Example
=======

Live demo: http://scheduler.integratehq.com

Install
=======

    script/plugin install git://github.com/dmix/weekly_builder.git 

Then check the output if all images and stylesheets have been copied successfully.

How to Use WeeklyBuilder
=======

The calendar builder:
    <%  weekly_calendar(@events, :date => @date, :include_24_hours => true) do |w|  %>
      <%  w.week(:business_hours => params[:business_hours], :clickable_hours => true) do |event,truncate|  %>
        <%=  event.starts_at.strftime('%I:%M%p')  %>
        <%=  link_to truncate(event.name,truncate), event_path(event)  %>
      <% end -%>
    <% end -%>

The Next/Previous week links helper:
    <%  weekly_links(:date => @date)  %>

In your controller:
    @date = Time.parse("#{params[:start_date]} || Time.now.utc")
    @start_date = Date.new(@date.year, @date.month, @date.day) 
    @events = Event.find(:all, :conditions => ['starts_at between ? and ?', @start_date, @start_date + 7])
  
The event model only requires 2 attributes: starts_at:datetime and ends_at:datetime to calculate width and position on the calendar. In my demo app I ask the user for one date/time (starts_at) and estimated time to complete (for example 2hrs), it then calculates ends_at after it is submitted.

UPDATE: Added a truncate_width method so that long event names are truncated in proportion to the width of the event, this is passed through the week block with |truncate|.

### Options available:

* `:include_24_hours`:
  Default hours are 6am-8pm, if this set as "true" then an option to switch to a 24-hour schedule appears at the bottom

Copyright (c) 2009 Dan McGrady http://dmix.ca, released under the MIT license

Thanks to P8 http://github.com/p8/table_builder/

TODO
=======
* IE6 Friendly (so far only tested on FF3 + Safari 4)
* Testing
* Refactor concats to be nested
* Single @date instead of @start_date + @end_date