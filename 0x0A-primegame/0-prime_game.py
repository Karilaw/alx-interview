#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime number game.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): The maximum number for each round.

    Returns:
    str: The name of the player who won the most rounds
    or None if there is a tie.
    """

    def is_prime(n):
        """
        Checks if a number is prime.

        Parameters:
        n (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def game(n):
        """
        Simulates a round of the game.

        Parameters:
        n (int): The maximum number for the round.

        Returns:
        bool: True if Maria wins the round, False if Ben wins.
        """
        primes = [is_prime(i) for i in range(n+1)]
        return sum(primes) % 2 == 1

    maria_wins = sum(game(n) for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
