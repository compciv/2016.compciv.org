module SitemapAccessors
  def sitemap_resources
    sitemap.resources
  end

  def sitemap_content_resources
    sitemap.resources.select{ |r|
      r.path =~ /^(?:guides|articles|assignments)\/.+/ && r.data.title.present?
    }.map{ |r| uniform_content_resource_adapter(r)
    }.sort_by{ |r| r.title }
  end

  def find_sitemap_resource_by_relative_url(relative_url)
    rel_url = relative_url.to_s
    rel_url += '/' unless rel_url[-1] == '/'
    r = sitemap_resources.find{|p| p.url == rel_url }

    return r
  end


  def assignment_resources # todo, create Assignment Resource
    _resources = sitemap.resources.select{ |r|
      r.path =~ /^(?:assignments)\/.+/ && r.data.title.present? && r.data.due_date.present?
    }.map{ |r|
      exercises = r.data.exercises_slug ? load_exercise_set(r.data.exercises_slug, with_keys: false) : nil
      UniformContentResource::AssignmentResource.new(r, exercises)
    }

    _dataitems = []
    data.homework.todos.each_pair do |slug, obj|
      next unless obj.title.present?
      h = Hashie::Mash.new()
      _tk = Hashie::Mash.new(obj)
      h.slug = slug
      h.url = '#' + h.slug
      # h.title = _tk.delete :title
      # h.description = _tk.delete :description
      h.data = _tk
      _dataitems << UniformContentResource::AssignmentResource.new(h)
    end

    return (_resources + _dataitems).sort{ |a, b| b.due_date  <=> a.due_date }

  end


end

include SitemapAccessors
