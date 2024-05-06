#!/usr/bin/env ruby
# Script matches only capital letters.

puts ARGV[0].scan(/[A-Z]/).join
