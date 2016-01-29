require 'lib/custom_helpers/banner_helpers'
require 'lib/custom_helpers/card_helpers'
require 'lib/custom_helpers/date_helpers'
require 'lib/custom_helpers/exercise_helpers'

require 'lib/custom_helpers/keyboard_styling_helpers'
require 'lib/custom_helpers/media_helpers'
require 'lib/custom_helpers/markup_extension_helpers'
require 'lib/custom_helpers/metadata_helpers'
require 'lib/custom_helpers/page_data_helpers'
require 'lib/custom_helpers/references_helpers'
require 'lib/custom_helpers/static_file_helpers'
require 'lib/custom_helpers/toc_helpers'
require 'lib/custom_helpers/site_config_helpers'
require 'lib/custom_helpers/uniform_content_resource_helpers'

module CustomHelpers
  include CustomHelpers::BannerHelpers
  include CustomHelpers::CardHelpers
  include CustomHelpers::DateHelpers
  include CustomHelpers::ExerciseHelpers

  include CustomHelpers::KeyboardStylingHelpers
  include CustomHelpers::MarkupExtensionHelpers
  include CustomHelpers::MediaHelpers
  include CustomHelpers::MetadataHelpers
  include CustomHelpers::PageDataHelpers
  include CustomHelpers::ReferencesHelpers
  include CustomHelpers::SiteConfigHelpers
  include CustomHelpers::StaticFileHelpers
  include CustomHelpers::TocHelpers
  include CustomHelpers::UniformContentResourceHelpers

  def sitemap_resources
    sitemap.resources
  end


  def find_sitemap_resource_by_relative_url(relative_url)
    rel_url = relative_url.to_s
    rel_url += '/' unless rel_url[-1] == '/'
    r = sitemap_resources.find{|p| p.url == rel_url }

    return r
  end
end
