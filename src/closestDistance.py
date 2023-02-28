from typing import List
from quickSort import *
import math

def calcDistance(p1, p2):
    global timesDistanceCalculated
    # Calculate Euclidean distance between two points

    timesDistanceCalculated += 1
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])**2
    return math.sqrt(sum)

def calcDistance3(P):
    # Calculate Euclidean distance between three points

    if (calcDistance(P[0], P[1]) < calcDistance(P[0], P[2])):
        if (calcDistance(P[0], P[1]) < calcDistance(P[1], P[2])):
            return calcDistance(P[0], P[1]), P[0], P[1]
        else:
            return calcDistance(P[1], P[2]), P[1], P[2]
    else:
        if (calcDistance(P[0], P[2]) < calcDistance(P[1], P[2])):
            return calcDistance(P[0], P[2]), P[0], P[2]
        else: 
            return calcDistance(P[1], P[2]), P[1], P[2]
            
def findClosestPair(P: List, n: int):
    # sort the list first based on x
    quicksort(P, 0, n-1)

    # Base case when there are only two or three points
    if n == 2:
        d = calcDistance(P[0], P[1])
        return d, P[0], P[1]

    if n == 3:
        return calcDistance3(P)
        
    # Divide the set into two halves
    mid = n // 2
    S1 = P[:(mid+(n%2))]
    S2 = P[(mid+(n%2)):]

    # Recursive calls to find the closest pair in each half
    d1, p1, p2 = findClosestPair(S1, mid+(n%2))
    d2, q1, q2 = findClosestPair(S2, n-(mid+(n%2)))
    d, p1, p2 = (d1, p1, p2) if d1 < d2 else (d2, q1, q2)

    # Find the minimum distance between the two halves
    d = min(d1, d2)

    closest_pair = (d, p1, p2)
    strip = []
    for i in range(n):
        if abs(P[i][0] - P[mid+(n%2)][0]) < d:
            strip.append(P[i])

    strip.sort(key=lambda x: x[1])
    size = len(strip)
    
    for i in range(size):
        for j in range(i+1, size):
            if strip[j][1] - strip[i][1] >= d:
                continue
            else:
                distance = calcDistance(strip[i],strip[j])
                d = min(d, distance)
                if (d == distance):
                    closest_pair = (d,strip[i],strip[j])

    return closest_pair

def findClosestPairES(P):
    n = len(P)
    best_dist = float('inf')
    best_pair = None
    for i in range(n):
        for j in range(i+1, n):
            dist = calcDistance(P[i], P[j])
            if dist < best_dist:
                best_dist = dist
                best_pair = (P[i], P[j])
                
    print(f"Jarak terdekat Brute Force: {best_dist:.2f}")
    print(f"Pasangan titik terdekat Brute Force: {best_pair}")
    # return best_pair, best_dist
