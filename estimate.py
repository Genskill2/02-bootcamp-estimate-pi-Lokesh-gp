import math
import random
import unittest

def wallis(n):
    mid=1
    for p in range(1,n+1):
        mid=mid*(((4*(p**2))/(4*(p**2)-1)))
    return (mid*2)

def monte_carlo(m):
    circle_points= 0
    square_points= 0
  
    for i in range(m**2):
        rand_x= random.uniform(0, 1)
        rand_y= random.uniform(0, 1)
        origin_dist= rand_x**2 + rand_y**2
        if origin_dist<= 1:
            circle_points+= 1
        square_points+= 1
        pi = 4* circle_points/ square_points
    
    return pi

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
