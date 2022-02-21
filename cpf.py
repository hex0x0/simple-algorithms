

import re


regex = re.compile(r'\((\d{3})\).(\d{3}).(\d{3})-(\d{2})')

print(regex.findall('(029).950.301-13 | (050).302.094-12'))