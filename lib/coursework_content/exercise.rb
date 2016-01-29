module CourseworkContent
  class Exercise
    attr_reader :title, :description, :points, :takeaways, :slug, :hints
    def initialize(obj)
      @data_object = obj
      @slug = @data_object.slug
      @title = @data_object.title
      @description = @data_object.description
      @hints = @data_object.hints
      @points = Float(@data_object.points)
      @takeaways = Array(@data_object.takeaways)
      # non accessors
      raise StandardError, "#{@slug}: No expectations are set" if @data_object.expectations.nil?
      @expectations = @data_object.expectations

      if @hints.is_a?(Array)
        raise StandardError, "#{@slug}: :hints must be a string"
      end
    end

    # should probably be a helper?
    def exercise_set_path
      File.join("/assignments/exercise-sets/", slug_dirname + '-set', '#' + slug_hashmark)
    end

    def slug_hashmark
      "exercise-#{slug_base}"
    end

    def slug_base
      File.basename(slug)
    end

    def slug_basename
      File.basename(slug_filename)
    end

    def slug_dirname
      File.dirname(slug_filename)
    end

    def slug_filename
      slug + '.py'
    end

    def expected_created_paths
      expected_effects.created_paths if expected_effects?
    end

    def expected_effects?
      expected_effects.present?
    end



    def expected_output
      expectations.output
    end

    def expected_output?
      expectations.output.present?
    end
    def expected_output_excerpted?
      !expectations.output.is_a?(String) && expectations.output.excerpted == true
    end

    def expected_output_full?
      !expected_output_excerpted?
    end
    def expected_output_head
        expectations.output.head.text
    end

    def expected_output_head_count
        expected_output_head.count("\n")
    end

    def expected_output_tail
        expectations.output.tail.text
    end

    def expected_output_tail_count
      expected_output_tail.count("\n")
    end


    def expected_error
      expectations.error
    end

    def expected_remote_access
      expected_effects.remotes if expected_effects?
    end

    def expected_requirements
      Array(expectations.requirements)
    end


    def takeaways?
      @takeaways.present?
    end

    private
      def expectations
        @expectations
      end

      def expected_effects
        @expectations.effects
      end

  end
end
