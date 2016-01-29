require 'addressable'
module CustomHelpers
  module UniformContentResourceHelpers

    # used to handle resources that could be either UniformContentResources or MiddlemanResources
    # needs access to :find_sitemap_resource_by_relative_url, which is why it is a helper
    def uniform_content_resource_adapter(obj)
      if obj.is_a?(String)
        url = Addressable::URI.parse(obj)
        if url.relative? ## assume it is a Middleman resource
          xo = find_sitemap_resource_by_relative_url(url)
          if xo.blank?
            raise ::CannotFindMiddlemanResourceBySlugError.new(url)
          end
        else
          xo = {:url => url, :title => url.to_s }
        end
      else
        xo = obj
      end

      return UniformContentResource(xo)
    end


    def link_to_content_resource(obj, opts = {})
      ucrobj = uniform_content_resource_adapter(obj)
      link_to ucrobj.title, ucrobj.url, opts
    end

    def content_resource_tag(obj, tag = :div, opts = {})
      opts[:class] = [opts[:class], "uniform-content-resource"].compact.join(' ')
      ucrobj = uniform_content_resource_adapter(obj)
      buff = ActiveSupport::SafeBuffer.new
      content_tag(:div, opts.merge("data-href" => ucrobj.url)) do
        buff.safe_concat link_to_content_resource(ucrobj, :class => 'title')
        if ucrobj.description?
          buff.safe_concat content_tag(:div, ucrobj.description, :class => 'description')
        end

        buff
      end
    end
  end
end


class CannotFindMiddlemanResourceBySlugError < StandardError; end;
