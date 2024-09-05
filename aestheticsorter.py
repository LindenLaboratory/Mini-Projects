'''
This is a very simple project I made as a fun mini project.
It simply sorts a list using a bubble sort algorithm and displays the process using matplotlib.
It is very inefficient for sorting but it looks cool!
The unnecessary line shortening was part of a challenge I set for myself while making it!
'''
import matplotlib.pyplot as plt,random,time,numpy as np,os;WIDTH,HEIGHT=13.7,6.7 #IMPORTS, SETUP
#FUNCTIONS
def timer(func):
    def wrapper(*args, **kwargs): global time_var; start_time = time.perf_counter(); result = func(*args, **kwargs); end_time = time.perf_counter(); elapsed_time = end_time - start_time;os.system("cls");print(f"Info sorted in {elapsed_time} seconds"); return result
    return wrapper
@timer
def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualize(arr)
def visualize(arr):
    plt.clf();colors = np.linspace(0, 1, len(arr));plt.bar(range(len(arr)), arr, width=1.0, color=plt.cm.RdYlGn(colors), edgecolor='none');plt.axis('off');plt.subplots_adjust(left=0, right=1, top=1, bottom=0);plt.draw();plt.pause(0.001);mng = plt.get_current_fig_manager();mng.window.state('zoomed')
def main(Loop=False):
    while Loop: n = 20;numbers = list(range(1, n + 1));random.shuffle(numbers);plt.figure("Sorting Algorithm Visualizer", figsize=(WIDTH, HEIGHT));plt.ion();visualize(numbers);sort(numbers);visualize(numbers);plt.ioff();plt.show(block=False);plt.pause(1);plt.clf();plt.pause(0.5); # Plot
main(Loop=True) #MAINLOOP
