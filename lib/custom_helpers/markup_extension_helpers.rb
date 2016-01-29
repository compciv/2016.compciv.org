module CustomHelpers
  module MarkupExtensionHelpers

    # meh, minimum configurability is fine
    def aside_wrap(opts = {}, &block)
      concat_content content_tag(:aside, markdownify(capture_html(&block)), opts)
    end

    # adds bootstrap container div
    def container_wrap(tagname = :div, opts = {}, &block)
      opts[:class] = (opts[:class].to_s + " container").strip
      content_tag(tagname, opts, &block)
    end

    def div_wrap(klassnames = "", opts = {}, &block)
      opts[:class] = (opts[:class].to_s + klassnames).strip
      content_tag(:div, opts, &block)
    end

    def markdownify(str = nil, &block)
      if str.nil? && !block_given?
        raise StandardError, "Markdownify requires a string or a block"
      elsif str.present? && block_given?
        raise StandardError, "Markdownify requires either string or a block, not both"
      end
      if block_given?
        txt = Kramdown::Document.new(capture_html(&block)).to_html
        concat_content(txt)
      else
        return Kramdown::Document.new(str).to_html
      end

    end
  end
end
