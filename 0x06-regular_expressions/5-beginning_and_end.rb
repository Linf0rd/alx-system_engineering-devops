#!/usr/bin/env ruby

regex = /^h.n$/
string = ARGV[0]

if string.match?(regex)
  puts string
end
