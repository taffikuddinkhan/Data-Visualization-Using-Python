import matplotlib.pyplot as plt
import numpy as np
from werkzeug.http import parse_range_header

x = ["math","mil","science","history"]
y = [40,50,60,38]
c =["y","b","g","r"]
z=[30,40,50,60]
width=0.5
p = np.arange(len(x))
p1 = [ j+ width for j in p]
plt.xlabel("subjects",fontsize=10)
plt.ylabel("marks")
plt.title("Exam result")
plt.bar(x,y,
        color=c,
        linewidth=2,
        linestyle="--",
        edgecolor="black"
        )

plt.bar(p1,z,
        linewidth=2,
        linestyle="-",
        edgecolor="black",
        color="grey"
        )

plt.xticks(p+width/2,x)
plt.show()