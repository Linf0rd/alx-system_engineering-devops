#!/usr/bin/env ruby

regex = /School/
string = ARGV[0]
puts string.scan(regex).join
