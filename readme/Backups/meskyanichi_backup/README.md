# Backup

## A Backup Ruby Gem

Backup is a Ruby Gem written for Unix and Rails environments. It can be used both with and without the Ruby on Rails framework! This gem offers a quick and simple solution to backing up databases such as MySQL/PostgreSQL/SQLite and Files/Folders. All backups can be transferred to Amazon S3, Rackspace Cloud Files, any remote server you have access to (using either SCP, SFTP or regular FTP), or a Local server. Backup handles Compression, Archiving, Encryption, Backup Cleaning (Cycling) and supports Email Notifications.

## Authors/Maintainers

* [Meskyanichi - Michael van Rooijen](http://github.com/meskyanichi)
* [Fernandoluizao - Fernando Migliorini Luizão](http://github.com/fernandoluizao)

## Backup's Current Capabilities

### Storage Methods

* Amazon S3
* Rackspace Cloud Files
* Remote Server (Available Protocols: SCP, SFTP, FTP)
* Local server (Example Locations: Another Hard Drive, Network path)

### Adapters

* MySQL
* PostgreSQL
* SQLite
* Archive (Any files and/or folders)
* Custom (Anything you can produce using the command line)

### Archiving

Handles archiving for the __Archive__ and __Custom__ adapters.

### Encryption

Handles encryption of __all__ backups for __any__ adapter.
To decrypt a "Backup encrypted file" you can use Backup's built-in utility command:

    sudo backup --decrypt /path/to/encrypted/file.enc

### Backup Cleaning

With Backup you can very easily specify how many backups you would like to have stored (per backup procedure!) on your Amazon S3, Remote or Local server. When the limit you specify gets exceeded, the oldest backup will automatically be cleaned up.

### Email Notifications

You will be able to specify whether you would like to be notified by email when a backup successfully been stored.
Simply fill in the email configuration block and set "notify" to true inside the backup procedure you would like to be notified of.

### Quick Example of a Single Backup Setting/Procedure inside the Backup Configuration File

    backup 'mysql-backup-s3' do
      adapter :mysql do
        user      'user'
        password  'password'
        database  'database'
      end
      storage :s3 do
        access_key_id     'access_key_id'
        secret_access_key 'secret_access_key'
        bucket            '/bucket/backups/mysql/'
        use_ssl           true
      end
      keep_backups 25
      encrypt_with_password 'my_password'
      notify true
    end
  
Everything above should be pretty straightforward, so now, using the __trigger__ we specified between
the `backup` and `do` you can execute this backup procedure like so:

__Rails Environment__

    rake backup:run trigger=mysql-backup-s3

__Unix Environment__

    sudo backup --run mysql-backup-s3

That's it. This was a simple example of how it works.

## Interested in trying out Backup?

### Getting started with Backup for the *Unix Environment*

[http://wiki.github.com/meskyanichi/backup/getting-started-unix](http://wiki.github.com/meskyanichi/backup/getting-started-unix)


### Getting started with Backup for the *Rails Environment*

[http://wiki.github.com/meskyanichi/backup/getting-started-ruby-on-rails](http://wiki.github.com/meskyanichi/backup/getting-started-ruby-on-rails)


### Production Mode __RAILS_ENV___

[http://wiki.github.com/meskyanichi/backup/production-mode](http://wiki.github.com/meskyanichi/backup/production-mode)


### Encrypting and Decrypting

[http://wiki.github.com/meskyanichi/backup/encrypting-and-decrypting](http://wiki.github.com/meskyanichi/backup/encrypting-and-decrypting)


### Backup Configuration File (All Adapters, Storage Methods, Mail Settings and Options)

[http://wiki.github.com/meskyanichi/backup/configuration-file](http://wiki.github.com/meskyanichi/backup/configuration-file)


### Unix Utility Commands and Rails Rake Tasks

[http://wiki.github.com/meskyanichi/backup/utility-commands](http://wiki.github.com/meskyanichi/backup/utility-commands)

[http://wiki.github.com/meskyanichi/backup/rake-tasks](http://wiki.github.com/meskyanichi/backup/rake-tasks)


### Automatic Backups

[http://wiki.github.com/meskyanichi/backup/automatic-backups](http://wiki.github.com/meskyanichi/backup/automatic-backups)


### Capistrano Recipes

[http://wiki.github.com/meskyanichi/backup/capistrano-recipes](http://wiki.github.com/meskyanichi/backup/capistrano-recipes)


### Capistrano, Whenever!

[http://wiki.github.com/meskyanichi/backup/capistrano-whenever](http://wiki.github.com/meskyanichi/backup/capistrano-whenever)


### Understanding "The Backup Database"

[http://wiki.github.com/meskyanichi/backup/the-backup-database](http://wiki.github.com/meskyanichi/backup/the-backup-database)


### Trouble Shooting

[http://wiki.github.com/meskyanichi/backup/troubleshooting](http://wiki.github.com/meskyanichi/backup/troubleshooting)


### Requirements

[http://wiki.github.com/meskyanichi/backup/requirements](http://wiki.github.com/meskyanichi/backup/requirements)


### Resources

[http://wiki.github.com/meskyanichi/backup/resources](http://wiki.github.com/meskyanichi/backup/resources)


### Requests

If anyone has any requests, please send us a message or post it in the [issue log](http://github.com/meskyanichi/backup/issues)!


### Suggestions?

Send us a message! Fork the project!


### Found a Bug?

[Report it](http://github.com/meskyanichi/backup/issues)


### Contributors

* [dtrueman](http://github.com/dtrueman)
* [Nathan L Smith](http://github.com/smith)
* [Francesc Esplugas](http://github.com/fesplugas)
* [wakiki](http://github.com/wakiki)
* [Dan Hixon](http://github.com/danhixon)
* [Adam Greene](http://github.com/skippy)

__Michael van Rooijen | Final Creation. ([http://michaelvanrooijen.com](http://michaelvanrooijen.com))__