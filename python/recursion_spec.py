# Write your unit tests here
from recursion_challenge import factorial, palindrome, bottles, roman_num


##---------------------------factorial tests

# #base case test - (0)
# print(f"should == 1:  {factorial(0)}")

# #should == 24
# print(f"should == 24:  {factorial(4)}")


##---------------------------palindrome tests
# print(f"should == True:   {palindrome('racecar')}")

# print(f"should == True:   {palindrome('ciVic')}")

# print(f"should == False:   {palindrome('nice')}")

# print(f"should == False:   {palindrome('bomb')}")



##---------------------------bottles tests
# print(f"THE SONG:\n   {bottles(5)}")



##---------------------------roman nums test
print(f"should == be DVI:  {roman_num(506)}")

print(f"should == be VI:  {roman_num(6)}")

print(f"should == be MMDCLXII:  {roman_num(2662)}")

print(f"should == be CDXLIV:  {roman_num(444)}")