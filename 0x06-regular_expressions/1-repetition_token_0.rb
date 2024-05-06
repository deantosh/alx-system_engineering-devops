#!/usr/bin/env ruby
# Match where "t" is repeated 2 or 5 times.

puts ARGV[0].scan(/hbt{2,5}n/).join
