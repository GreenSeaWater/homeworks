# -*- coding: utf-8 -*-
import math
AB = int(raw_input())
BC = int(raw_input())
AC = math.sqrt((AB**2)+(BC**2))
MBC = round(math.degrees(math.asin(AB/AC)))                                
print str(int(MBC)) + '°'