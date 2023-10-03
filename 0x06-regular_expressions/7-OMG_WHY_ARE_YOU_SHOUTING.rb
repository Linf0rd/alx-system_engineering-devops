#!/usr/bin/env ruby

regex = /[A-Z]/
string = ARGV[0]

puts string.scan(regex).join
