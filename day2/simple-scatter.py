#!/usr/bin/env python

import matplotlib.pyplot as plt

x = [3, 4, 10]
y = [13, 24, 30]

fig, ax = plt.subplots()
ax.plot(x, y)

ax.axhline(17, color='red')

ax.set_xlabel(r'Random noise', fontsize=20)
ax.set_ylabel(r'Intelligence', fontsize=18)
ax.set_title('A silly scatter plot')

ax.grid(True)
fig.tight_layout()

plt.savefig('figure.png')

# plt.show()
