require 'lib/uniform_content_resource/uniform_content_resource'
require 'lib/coursework_content'
require "lib/custom_helpers"
require "lib/site_config"
require "lib/sitemap_accessors"
require 'pry'

###
# Helpers
###
helpers CustomHelpers
helpers SitemapAccessors

###
# Page options, layouts, aliases and proxies
###
activate :directory_indexes
activate :pry
activate :syntax, :line_numbers => false

### my custom extensions
#activate :my_feature


set :markdown_engine, :kramdown
# set :markdown,
#   :syntax_highlighter => 'coderay',
#   :syntax_highlighter_opts => {
#     :line_numbers => false
#   }

set :js_dir, 'assets/javascripts'
set :css_dir, 'assets/stylesheets'
set :layout, :default_page
page "assignments/exercise-sets/*", :layout => :exercise_set_layout
set :trailing_slash, true

config[:site_config] = SiteConfig.load_site_config("./site_config.yaml")

# Per-page layout changes:
#
# With no layout
page '/*.xml', layout: false
page '/*.json', layout: false
page '/*.txt', layout: false

# With alternative layout
# page "/path/to/file.html", layout: :otherlayout

# Proxy pages (http://middlemanapp.com/basics/dynamic-pages/)
# proxy "/this-page-has-no-template.html", "/template-file.html", locals: {
#  which_fake_page: "Rendering a fake page with a local variable" }

# General configuration

# Reload the browser automatically whenever files change
configure :development do
  activate :livereload
end


# Build-specific configuration
configure :build do
  # Minify CSS on build
  activate :minify_css
  # Minify Javascript on build
  activate :minify_javascript
end


activate :s3_sync do |s3_sync|
  s3_sync.delete                     = false
  s3_sync.after_build                = true
  s3_sync.prefer_gzip                = true
  s3_sync.path_style                 = true
  s3_sync.reduced_redundancy_storage = false
  s3_sync.acl                        = 'public-read'
  s3_sync.encryption                 = false
# https://github.com/fredjean/middleman-s3_sync/issues/97
#  s3_sync.prefix                     = ''
  s3_sync.version_bucket             = false
  s3_sync.index_document             = 'index.html'
  s3_sync.error_document             = '404.html'
end


#TKTKTK TODO
# puts self
# puts self.class
# puts "HEYYYYY"
config[:site_exercises] = self.app.data.homework.exercises
SITE_EXERCISES = self.app.data.homework.exercises
