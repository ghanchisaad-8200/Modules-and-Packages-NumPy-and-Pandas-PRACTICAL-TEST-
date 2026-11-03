KM_PER_MILE = 1.609

def km_to_miles(km):
    return round(km / KM_PER_MILE, 2)

def c_to_f(c):
    return round(c * 9 / 5 + 32, 1)

if __name__ == "__main__":
    print("Testing unitconv directly")
    print(km_to_miles(160.9), c_to_f(100))
