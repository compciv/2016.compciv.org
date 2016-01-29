module CustomHelpers
  module ExerciseHelpers



    # :slug is expected to be a slug: somepath/a
    # returns: Hash, with s:lug => "somepath/a"
    def middleman_path_to_data_obj(slug)
      fpath, fbasename = slug.split('/')
      obj = load_exercise_set(fpath)[fbasename]
      obj.slug = slug

      return obj
    end


    def site_exercises
      config[:site_exercises]
    end

    def load_exercise_set(slugpath, with_keys: true)
      x = site_exercises[slugpath]
      if with_keys
        return x
      else
        return x.values
      end
    end

    def load_exercise(path)
      obj = middleman_path_to_data_obj(path)
      CourseworkContent::Exercise.new(obj)
    end



  end
end


