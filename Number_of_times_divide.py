def number_of_times_divideby2(n):
    """
    :param n: Int -- the input positive integer, greater than 2.

    :return: number of times one must repeatedly divide this number by 2
             before getting a value less than 2.
    """
    # To do
    if n < 2:
        return 0
    return number_of_times_divideby2(n // 2) + 1

'''
note:
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

# def main():
#     print(number_of_times_divideby2(1000))   # 9
#     print(number_of_times_divideby2(999))    # 9
#     print(number_of_times_divideby2(467382987338298))   # 48
#
# if __name__ == '__main__':
#     main()
