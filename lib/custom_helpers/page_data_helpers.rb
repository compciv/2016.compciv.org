require 'hashie'

module CustomHelpers
  # helpers for common page attributes
  # should also deal with dynamic pages...
  module PageDataHelpers

    # for dynamic pages, we expect the option :dynamic_page has been set
    # (holdover from middleman-onthestreet gem)
    def _dynamic_page_data
      opts = current_page.metadata[:options]

      return opts[:dynamic_page] || ::Hashie::Mash.new()
    end

    def _current_page_data
      current_page.data
    end

    def page_author
      _current_page_data.author || _dynamic_page_data.author
    end

    def page_description
      _current_page_data.description || _dynamic_page_data.description
    end

    def page_image_url
      _current_page_data.image_url || _dynamic_page_data.image_url
    end

    def page_has_header_class
      if _current_page_data.has_header == false ||
         _dynamic_page_data.has_header == false
         return "no-header"
      else
        return "has-header"
      end
    end

    def page_sequence
      _current_page_data.sequence
    end

    def url_for_sequence_next
      page_sequence.next
    end

    def url_for_sequence_previous
      page_sequence.previous
    end

    def page_summary
      _current_page_data.summary
    end

    def page_toc?
      _current_page_data.hide_toc != true
    end

    def page_url
      current_page.url
    end

    def page_title
      _current_page_data.title || _dynamic_page_data.title
    end

    def page_mymeta
      _current_page_data.mymeta
    end

  end
end
