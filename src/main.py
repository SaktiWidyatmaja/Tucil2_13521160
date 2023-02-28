from closestDistance import *
from IO import *
import time

if __name__ == "__main__":    
    print('█▀▀ █░░ █▀█ █▀ █▀▀ █▀ ▀█▀   █▀▄ █ █▀ ▀█▀ ▄▀█ █▄░█ █▀▀ █▀▀')
    print('█▄▄ █▄▄ █▄█ ▄█ ██▄ ▄█ ░█░   █▄▀ █ ▄█ ░█░ █▀█ █░▀█ █▄▄ ██▄\n')
    print('█▀▄ █ █░█ █ █▀▄ █▀▀   ▄▀█ █▄░█ █▀▄   █▀▀ █▀█ █▄░█ █▀█ █░█ █▀▀ █▀█')
    print('█▄▀ █ ▀▄▀ █ █▄▀ ██▄   █▀█ █░▀█ █▄▀   █▄▄ █▄█ █░▀█ ▀▀█ █▄█ ██▄ █▀▄')
    print('======================================================')
    count = int(input("Masukkan jumlah tuple: "))
    dimension = int(input("Masukkan dimensi vektor: "))
    vectorList = inputRandom(count, dimension)
    print('======================================================')
    timesDistanceCalculated = 0
    
    # catat waktu awal dnd
    start_time = time.time()
    
    d, res1, res2 = findClosestPair(vectorList, count)

    # catat waktu selesai dnd
    end_time = time.time()

    # hitung selisih waktu
    total_time = end_time - start_time

    print(f"Jarak terdekat Divide and Conquer: {d:.2f}")
    print(f"Pasangan titik terdekat Divide and Conquer: {res1}, {res2}")
    print(f"Waktu yang diperlukan Divide and Conquer: {total_time:.8f} detik")
    print(f"Jumlah perhitungan jarak euclidean yang dilakukan: {timesDistanceCalculated}")
    print('======================================================')

    # catat waktu awal bf
    start_time = time.time()

    findClosestPairES(vectorList)

    # catat waktu selesai bf
    end_time = time.time()

    # hitung selisih waktu
    total_time = end_time - start_time

    print(f"Waktu yang diperlukan Brute Force: {total_time:.8f} detik")
    print('======================================================')

    # visualisasikan titik-titik
    if (dimension == 3):
        show3d(vectorList, res1, res2)    
