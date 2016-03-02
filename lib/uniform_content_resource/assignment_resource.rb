module UniformContentResource
  class AssignmentResource < UniformContentResource::MiddlemanContentResource
    attr_reader :due_date, :exercises_slug, :kind
    def initialize(resource, exercises = nil)
        super(resource)
        @due_date = @data.due_date
        @exercises_slug = @data.exercises_slug
        @exercises = exercises
        @status = @data.status


        @kind = case
            when @data.kind
              @data.kind
            when @exercises_slug.present?
              'Exercise Set'
            else
              'Todo'
            end

        if @exercises_slug && @exercises.nil?
          raise StandardError, "Can't have an exercise set without exercises explicitly passed in
                because I'm clueless aobut using extensions..."
        end
    end

    def date
      @due_date
    end

    def exercises
      @exercises
    end

    def points
      if exercise_set?
        exercises.inject(0) do |s, exercise|
          begin
            s += exercise.points
          rescue StandardError => err
            puts(exercise)
            raise err
          end
        end
      else
        @data.points || 'NA'
      end
    end

    def exercise_set?
      @exercises_slug.present?
    end

    def stub?
      @url.to_s[0] == '#'
    end

    def draft?
      @status == 'draft'
    end

    private
      def add_up_exercise_set_points

      end

  end
end


