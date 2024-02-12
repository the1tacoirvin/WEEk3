import math

#the simposn values, does the calcaultions. modfied to work as orginal fucnition gave me a one million percent value.
#should work
def Simpson(fcn, a, b, npoints=1000):
    if npoints % 2 == 1:
        return 0
    h = (b - a) / npoints
    x = [a + i * h for i in range(npoints + 1)]
    area = fcn(a) + fcn(b)

    for j in range(1, npoints, 2):
        area += 4 * fcn(x[j])
    for j in range(2, npoints - 1, 2):
        area += 2 * fcn(x[j])
    area *= h / 3
    return area

#this does the tdp
def tdp(m, z):
    #this is for if someone does something dumb like put 0
    if m <= 0:
        raise ValueError("you put a zero value")
    def tdf(x):
        #the function to actually get this value
        return (math.gamma((0.5 * m) + 0.5) / (math.sqrt(m * math.pi) * math.gamma(m / 2)) *
                (1 + (x ** 2 / m)) ** (-(m + 1) / 2))

    low = z - (10 * z)
    prob = Simpson(tdf, low, z, 1000)  # Assuming mean (mu) is 0 and standard deviation (sigma) is 1
    return prob

#main function, puts all the values, lets you put values, and disaplys values.
def main():
    baja = [int(input("Enter a number: ")) for _ in range(3)]
    z_blast = [float(input("Enter a number: ")) for _ in range(3)]

    for w in range(3):
        for y in range(3):
            prob = tdp(baja[w], z_blast[y])
            print(f'For degrees of freedom {baja[w]} and z value {z_blast[y]}, probability is {prob}')

# prints main function for the world to see!
if __name__ == "__main__":
    main()
