#take a kon, koff, and calculate the 5xhalf lives, t1/2 to obtain accurate Kds on the RNA-MaP platform

min_FP = 0.91
max_FP = 2000

def calc_incubation_times(koff, Kd):
    #obtain kon (kon = koff/Kd)
    kon = koff/Kd
    return kon



def main():
    koff= input("What is the koff? ")
    Kd = input("What is the Kd? ")
    print(koff, Kd)

    #calc_incubation_times(koff, Kd)
# print(__name__)
if __name__ == '__main__':
    main()