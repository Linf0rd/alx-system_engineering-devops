#!/usr/bin/env ruby

regex = /hbt{2,5}n/
string = ARGV[0]

puts string.scan(regex).join
