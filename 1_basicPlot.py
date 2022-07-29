import matplotlib.pyplot as plt

x1, y1, x2, y2 = [10, 20, 30], [100, 200, 300], [40, 50, 60], [100, 500, 300]

# plt.style.use('dark_background')
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

# plt.plot(x, y, '--bo')
# plt.plot(x1, y1, label="Line 1", color='green',
#  linewidth="5", linestyle="dotted", marker=".")
# plt.plot(x2, y2, label="Line 2", color='red',
#          linewidth="3", linestyle="dashdot")

plt.plot(x1, y1, label="Line 1", color='green',
         marker="+")
plt.plot(x2, y2, label="Line 2", color='red'
         )
# plt.xlim([10, 300])
# plt.ylim([100, 200])
# plt.grid(axis='x', linestyle="dotted", color='red')
# plt.grid(axis='y', color='blue')
plt.legend()
plt.title("Basic Plots in Matplotlib")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
