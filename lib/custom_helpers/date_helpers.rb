require 'chronic'
module CustomHelpers
    module DateHelpers
        def date_slug(val)
          _to_date(val).strftime '%Y-%m-%d'
        end

        def machine_date(val)
          _to_date(val).strftime '%Y-%m-%dT%l:%M:%S%z'
        end

        def day_of_week(val)
          if (v = _to_date(val))
            v.strftime('%A')
          end
        end

        def friendly_date(val)
          if (v = _to_date(val))
            v.strftime('%A, %B %-d')
          else
            'No Date'
          end
        end

        def past_date?(val)
          _to_date(val) < Time.now()
        end

        # gives a rough estimate at runtime whether the given date is past

        def stale_date?(val)
          _to_date(val) < Time.now() - (3600 * 30 + 10)
        end

        def _to_date(val)
          d = case val
          when Date, Time
            val
          else
            Chronic.parse(val)
          end

          return d
        end

    end
end
