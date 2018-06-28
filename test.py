from collections import defaultdict
import numpy as np
Q=defaultdict(lambda: {'u':0,'r':4,'d':0,'l':0})


print(max(Q[(2,9)].values()))
