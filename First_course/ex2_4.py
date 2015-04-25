#!/usr/bin/env python

# Some style
formatter = "%-20s%-40s"
column1 = "ip_prefix"
column2 = "as_path"

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

parts1 = entry1.split('157.130.10.233        0 ')
parts2 = entry2.split('157.130.10.233        0 ')
parts3 = entry3.split('157.130.10.233        0 ')
parts4 = entry4.split('157.130.10.233        0 ')

as_path1 = parts1[1].split(' ')[:-1]
as_path2 = parts2[1].split(' ')[:-1]
as_path3 = parts3[1].split(' ')[:-1]
as_path4 = parts4[1].split(' ')[:-1]

ip_prefix1 = parts1[0].strip().split(" ").pop()
ip_prefix2 = parts2[0].strip().split(" ").pop()
ip_prefix3 = parts3[0].strip().split(" ").pop()
ip_prefix4 = parts4[0].strip().split(" ").pop()

print "=" * 80
print formatter % (column1, column2)
print formatter % (ip_prefix1, as_path1)
print formatter % (ip_prefix2, as_path2)
print formatter % (ip_prefix3, as_path3)
print formatter % (ip_prefix4, as_path4)
print "=" * 80
print ""

 The END
