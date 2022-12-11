st = set()


def subsequence(s):
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            sub_str = s[i: i + j]
            st.add(sub_str)
            for k in range(1, len(sub_str)):
                sb = sub_str
                sb = sb.replace(sb[k], "")
                subsequence(sb)


s = "abc"
subsequence(s)
for i in st:
    print(i, end=" ")
print()
