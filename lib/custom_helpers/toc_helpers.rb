module CustomHelpers
  module TocHelpers
    def render_toc(opts = {})
      partial "/layouts/components/partials/toc", locals: opts
    end
  end
end
