import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def test_my_first_plot():
    
    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    t= [5,10,15,20,25]
    d= [25,50,75,100,125]
    plt.plot(t,d,label='d = 5t')
    ax.set(xlabel='time (seconds)',
           ylabel='distance (meters)',
           title='Time vs Distance Covered',
           xlim=[0,30],
           ylim=[0,130])
    ax.legend()
    fig.savefig('scatter.png')

test_my_first_plot()
