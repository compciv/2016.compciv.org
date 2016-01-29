module CustomHelpers
  module StaticFileHelpers
    STATIC_FILES_DIR = "/files"
    STATIC_IMAGES_DIR = "/files/images"
    # returns STATIC_FILES_DIR/prefix/subpath/basename
    # subpath can be a MiddlemanResource or similar relative URL
    def url_for_static_file(basename, prefix = nil, subpath = nil)
      raise "Hey"
    end

    # returns STATIC_IMAGES_DIR/subpath/basename
    def url_for_static_image(basename, subpath = nil)
      raise "Hey"
    end

    # returns STATIC_FILES_DIR/prefix/current/page/path/basename
    def url_for_current_page_static_file(basename, prefix)
      page_url
      raise "Hey"
    end

    # returns STATIC_IMAGES_DIR/current/page/path/basename
    def url_for_current_page_static_image
      raise "Hey"
    end

    # e.g. for page: /samples/foo/bar.html
    # /files/images/foo/bar/
    def base_url_for_current_page_images

    end


  end
end
