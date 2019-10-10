#!/usr/bin/python

import argparse

"""
What do
1. Receives as input, list of stock prices.
2. REturn maximum profit from a SINGLE buy and sell.
3. Must buy before sell.

How do
1. Find max dif between smallest and largest price in list.
2. Subtract the smallest number to the left of the largest number
"""


def find_max_profit(prices):
    max_profit = prices[1] - prices[0]
    for i in range(len(prices) - 1):
        for k in range(i+1, len(prices)):
            temporary_max_profit = prices[k] - prices[i]
            if temporary_max_profit > max_profit:
                max_profit = temporary_max_profit
    return max_profit


# Works for ordered lists
# def find_max_profit(prices):
#     for i in range(0, len(prices) - 1):
#         cur_index = i
#         largest_index = cur_index
#         for k in range(cur_index+1, len(prices)):
#             if prices[k] > prices[largest_index]:
#                 largest_index = k
#             for g in range(1, largest_index - 1):
#                 smallest_index = g
#                 if prices[g] < prices[g+1]:
#                     prices[g] = smallest_index
#                     print(prices[largest_index])
#                     print(prices[smallest_index])
#                     return prices[largest_index] - prices[smallest_index]
# #                     # if smallest_index in range(largest_index - 1):


# (find_max_profit([10, 7, 5, 8, 11, 9]), 6)

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
