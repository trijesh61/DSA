# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

def find_gcd(n1, n2):
    gcd = 1


    for i in range(1, min(n1, n2) + 1):
        
        if n1 % i == 0 and n2 % i == 0:
            
            gcd = i

    
    return gcd

if __name__ == "__main__":
    n1, n2 = map(int,input("Enter 2 numbers(seperated by space):").split())
    
    gcd = find_gcd(n1, n2)

    print("GCD of", n1, "and", n2, "is:", gcd)