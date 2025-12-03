from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def to_color_neib(row, col):
            if row == 0:
                to_color_neib(row + 1, col)
                to_color_neib(row, col + 1)
                to_color_neib(row, col - 1)
