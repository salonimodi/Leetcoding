class Zigzag:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res_row = [""] * numRows
        row_idx = 1
        goUp = True

        for ch in s:
            res_row[row_idx - 1] += ch
            print(res_row)
            if goUp:
                row_idx += 1
            else:
                row_idx -= 1

            if row_idx == numRows:
                goUp = False
            if row_idx == 1:
                goUp = True
        return "".join(res_row)


if __name__ == "__main__":
    print("Hi There!!")
    l1 = Zigzag()
    print(l1.convert("PAYPALISHIRING", 3))
