import os
from datetime import *

stats = os.stat('abc.txt')

print(stats)

print("File size: ",stats.st_size,"Bytes",sep='')
print("Last modified time:",datetime.fromtimestamp(stats.st_mtime))