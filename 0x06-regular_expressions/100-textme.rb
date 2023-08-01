#!/usr/bin/env ruby
sender = ARGV[0].scan(/from:(.*?)\]/)
receiver = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts "#{sender.flatten.join},#{receiver.flatten.join},#{flags.flatten.join}" 
