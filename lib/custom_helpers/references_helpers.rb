module CustomHelpers
  module ReferencesHelpers

    def current_page_references
      # TODO: make sure this only runs once per resource initialization
      _objectified_references =  Array(current_page.data.references).map do |r|
          if r.internal == true
            uniform_content_resource_adapter(r.slug)
          else
            uniform_content_resource_adapter(r)
          end
      end
      return _objectified_references.present? ? _objectified_references : nil
    end

    def find_reference(slug)
      return slug if slug.is_a?(UniformContentResource::BaseResource)
      if slug.is_a?(String) # currently, it is always expected t be a string
        reefer = current_page_references.find{|r| r.slug == slug}

        if reefer
          return reefer
        else
          slugs = current_page_references.map{|r| r.slug}
          raise ::ReferenceDoesNotExist.new("#{slug} does not exist. Existing slugs: #{slugs.join(", \n")}")
        end
      else
        raise ArgumentError.new("Reference slug must be a string or another reference-type object, not a #{slug.class}")
      end
    end


    def cite_reference(obj, tag = :div, opts = {})
      opts[:class] = [opts[:class], "uniform-content-resource reference citation"].compact.join(' ')
      reefer = find_reference(obj)
      buff = ActiveSupport::SafeBuffer.new
      content_tag(:div, opts.merge("data-href" => reefer.url)) do
        buff.safe_concat link_to_content_resource(reefer, :class => 'title')
        buff.safe_concat content_tag(:span, %Q{ [#{reefer.byline}]}, :class => 'byline') if reefer.byline?

        if reefer.description?
          buff.safe_concat content_tag(:div, reefer.description, :class => 'description')
        end

        buff
      end
    end

    def link_to_reference(slug, opts = {})
      # TODO: this should be part of BaseResource display helper
      reefer = find_reference(slug)
      linktxt = content_tag(:strong, (reefer.title || reefer.url))
      unless opts.delete(:brief) == true
        linktxt << content_tag(:span, %Q{ [#{reefer.byline}]}, :class => 'byline') if reefer.byline?
      end
      link_to(linktxt, reefer.url, :class=>"reference")
    end

    def url_for_reference(slug)
      find_reference(slug).url
    end
    alias_method :ref_url, :url_for_reference

    # TODO: make DRY with via_reference
    def quote_reference(slug, via_text, opts = {}, &blk)
      reefer = find_reference(slug)
      opts[:class] = opts[:class].to_s + " via reference"
      via_str = '<div class="via-meta">'
      via_str << %Q{#{link_to via_text,  ref_url(reefer)}:}
      via_str << '</div>'
      buff = ActiveSupport::SafeBuffer.new
      txt = content_tag :div, opts do
         buff.safe_concat via_str
         buff.safe_concat "<div class=\"body\">"
         buff.safe_concat String(markdownify(capture(&blk)))
         buff.safe_concat "</div>"
         buff
      end

      concat txt
    end

    def via_reference(slug, opts = {}, &blk)
      reefer = find_reference(slug)
      opts[:class] = opts[:class].to_s + " via reference"
      desc_text = opts.delete(:description)

      via_str = '<div class="via-meta">'
      if desc_text.present?
        via_str << desc_text.strip
        via_str << '.' unless desc_text[-1] =~ /[.?!]/
        via_str << ' '
      end
      via_str << %Q{Via #{link_to_reference reefer}:}
      via_str << '</div>'


      buff = ActiveSupport::SafeBuffer.new
      txt = content_tag :div, opts do
         buff.safe_concat via_str
         buff.safe_concat "<div class=\"body\">"
         buff.safe_concat String(markdownify(capture(&blk)))
         buff.safe_concat "</div>"
         buff
      end

      concat txt
    end
  end
end


class ReferenceDoesNotExist < StandardError; end;
