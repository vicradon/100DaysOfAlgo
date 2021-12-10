import math


def coinSums(number, pieces):
    multiplicationMap = {}

    freq = number

    while True:
      return multiplicationMap


print(coinSums(200, [1, 2, 5, 10, 20, 50, 100]))

'''
- start from the first piece and multiply by the frequency
- multiply other pieces by 0
- consider frequency - 1 multiplied by the first piece
- if frequency - 1 does not have a factor among the other pieces, decrement again
- else recursively find a way to divide frequency - 1 among a set of pieces
- When the first piece frequency gets to zero, focus on piece 2 
- The max freq of piece 2 is the frequency < number which allows number - frequency to be divided among subsequent pieces
'''

'''
How to recursively divide a number among its factors where the first is the most greedy
15, [3, 4, 5]

3*2 + 4 + 5
Assign 1 to each subsequent term and if the difference between starting term and sum of subsequent terms is a factor of the first continue
be very greedy but other number should at least take something



How can we divide the remainder among the other terms? Is it possible?

200 * 1
198 * 1 + 1 * 2
196 * 1 + 2 * 2
195 * 1 + 1 * 5
194 * 1 + 3 * 2
193 * 1 + 1 * 2 + 1 * 5
192 * 1 + 4 * 2
191 * 

'''
