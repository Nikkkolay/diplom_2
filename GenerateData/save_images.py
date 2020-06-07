import os
import matplotlib.pyplot as plt


def save(name='', path='', cls=-1, fmt='png'):
    pwd = os.getcwd()
    iPath = path + str(cls)
    if not os.path.exists(iPath):
        os.makedirs(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
