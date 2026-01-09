#### Regular Expressions  ####

### Extract numbers from a string

import re
txt='Python was introduced in 1992. This is year 2020.'
pattern='\\d+'

res=re.findall(pattern,txt)
print(res)