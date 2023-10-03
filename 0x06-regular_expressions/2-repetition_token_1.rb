#!/usr/bin/env ruby

regex = /hbt*n/
string = ARGV[0]

puts string.scan(regex).join
