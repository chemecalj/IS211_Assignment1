#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 1, part 2."""


class Book(object):

    author = " "

    title = " "

    def __init__(self, author, title):
        """Constructor for the Book() class.

        Args:
            author (str): Author of the book.
            title (str): Title of the book.

        Attributes:
            author (str): Author of the book.
            title (str): Title of the book.
        """
        self.author = author
        self.title = title

    def display(self):
        """Displays the book title and author."""

        bookinfo = '"{}, written by {}"'.format(self.title, self.author)
        print bookinfo

BOOK_1 = Book('John Steinbeck', 'Of Mice and Men')

BOOK_2 = Book('Harper Lee', 'To Kill a Mockingbird')

BOOK_1.display()
BOOK_2.display()
