Navigation Builder
==================

Simple plugin for creating a navigation menu. Uses HAML.

HAML code:

    - navigation_menu :active_class => "current", :active => "new_article", :class => "menu" do |nav|
      = nav.item "Articles", articles_path
      = nav.item "New article", new_article_path, :identifier => "new_article"

Results in:

    <ul class="menu">
      <li>
        <a href="/articles">Articles</a>
      </li>
      <li class="current">
        <a href="/articles/new">New article</a>
      </li>
    </ul>
