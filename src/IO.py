import random
import matplotlib.pyplot as plt

def inputRandom(count, dimension):
    vectorList = []

    for i in range(count):
        vector = ()
        for j in range(dimension):
            vector += (random.randint(-5000, 5000),)

        vectorList.append(vector)

    # print("Titik-titik hasil input acak: ", vectorList)
    return vectorList

def show3d(vectorList, res1, res2):
    # create 3D object axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Adding points to the plot
    for point in vectorList:
        if point == res1 or point == res2:
            ax.scatter(point[0], point[1], point[2], c = "green") # green marker used for closest points
        else:
            ax.scatter(point[0], point[1], point[2], c = "red") # red marker used for other points
        
    plt.show()