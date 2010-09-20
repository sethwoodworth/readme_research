module Spoke
  module Readme
    module Markdown
      def self.extensions
        %w( mdown markdown markdn md )
      end

      def readme_summary
        if readme =~ /\.(#{Markdown.extensions.join('|')})$/
          lines = readme_data.split("\n")
          summary = []
          lines[3..-1].each do |line|
            if line !~ /^\s*$/
              summary << line
            else
              break
            end
          end
          summary.empty? ? nil : summary.join(' ')
        else
          super
        end
      end
    end
  end
end
