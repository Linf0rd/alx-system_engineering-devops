#!/usr/bin/env ruby

regex = /^\d{10}$/
string = ARGV[0]

if string.match?(regex)
  puts string
end
