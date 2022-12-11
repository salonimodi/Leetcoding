def displayContacts(n, contacts, s):
    res = []
    c = set(contacts)
    contacts = list(c)
    contacts.sort()
    for idx, c in enumerate(s):
        res.append([])
        str = s[:idx + 1]
        cnt = 0
        for contact in contacts:
            if contact[:len(str)] == str:
                res[idx].append(contact)
                cnt += 1
        if cnt == 0:
            res[idx].append(0)
    print(res)

n = 3
contact = ["geeikistest", "geeikistest", "geeksforgeeks", "geeksfortest"]
s = "geeips"
displayContacts(n, contact, s)
