#!/usr/bin/env python3
"""task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for the.
    """
    # from the current page number
    # and then multiplying by the page size
    start_index = (page - 1) * page_size
    # calculate end index by adding the stade
    end_index = start_index + page_size
    # return the star
    return (start_index, end_index)
