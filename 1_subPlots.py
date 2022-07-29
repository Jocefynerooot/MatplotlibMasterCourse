import matplotlib.pyplot as plt

x, y = [1, 2, 3], [10, 20, 30]
x1, y1 = [4, 10, 6], [10, 20, 30]
x2, y2 = [7, 45, 2], [10, 20, 30]
x3, y3 = [5, 9, 2], [10, 20, 30]

# plt.subplot(3, 2, 1)
# plt.plot(x, y)

# plt.subplot(3, 2, 2)
# plt.plot(x1, y1)

# plt.subplot(3, 2, 3)
# plt.plot(x2, y2)

# plt.subplot(3, 2, 4)
# plt.plot(x2, y2)

# plt.subplot(3, 2, 5)
# plt.plot(x2, y2)

# plt.subplot(3, 2, 6)
# plt.plot(x3, y3)

fig, ax = plt.subplots(3, 2, sharex=True, sharey=True)
ax[0, 0].plot(x, y)
ax[0, 1].plot(x1, y1)
ax[1, 0].plot(x, y)
ax[1, 1].plot(x2, y2)
ax[2, 0].plot(x, y)
ax[2, 1].plot(x3, y3)

plt.show()
