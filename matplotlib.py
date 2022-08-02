import matplotlib.pyplot as plt
import numpy as np
# colors ->
# red r
# green g
# blue b
# cyan c
# gmagenta m
# orange o


# format: 'color+marker+line style'
# keyargs: markersize
# plt.plot([5, 6, 7, 8], [5, 6, 7, 8], 'g')
# plt.plot([5, 6, 7, 8], [5, 6, 7, 8], color = 'g') # same as above
# plt.plot([5, 6, 7, 8], [5, 6, 7, 8], 'g*--', )

a = np.arange(0, 10, 0.5)
plt.plot(a, 'go:', a**2, 'r+-', a**3, 'k^-.') #, alpha = 1, zorder=2

# left, right = plt.xlim()

plt.xlim(2, 25) # expand the graph

plt.xlabel('x label')# color = 'red', size =14, lebelpad = 10, family = 'fantasy', weight = 200/'bold', style = 'italic'
plt.ylabel('y label')# backgroundcolor = 'orange', loc ='right', pad=10
# plt.ylabel('y label', {'backgroundcolor':'orange'})
plt.title('First plot')
# plt.minorticks_on()
plt.grid()#which = 'both/major/minor', linewidth=1
plt.show()

