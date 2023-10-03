#!/usr/bin/env ruby

regex = /hb?t?n/
string = ARGV[0]

puts string.scan(regex).join
