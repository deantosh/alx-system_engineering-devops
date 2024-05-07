#!/usr/bin/env ruby
# Script should output: [SENDER],[RECEIVER],[FLAGS]
#    -> The sender phone number or name (including country code if present)
#    -> The receiver phone number or name (including country code if present)
#    -> The flags that were used

input_string = ARGV[0]

sender = input_string[/\[from:(\+?\w+)\]/, 1] || ""
receiver = input_string[/\[to:(\+?\d+)\]/, 1] || ""
flags = input_string[/\[flags:(.*?)\]/, 1] || ""

output_string = [sender, receiver, flags].join(",")

puts output_string
