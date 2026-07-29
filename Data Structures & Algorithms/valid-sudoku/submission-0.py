class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = set()
        seen_col = set()
        seen_box = set()
        for i, row in enumerate(board):
            for j , value in enumerate(row):
                if value != ".":
                    row_id = ("row", i, value)
                    col_id = ("col", j, value)
                    box_id = ("box", i//3, j//3, value)
                    if row_id in seen_row or col_id in seen_col or box_id in seen_box:
                        return False

                    seen_row.add(row_id)
                    seen_col.add(col_id)
                    seen_box.add(box_id)

        return True