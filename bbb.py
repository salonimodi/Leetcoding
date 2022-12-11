import string


class Solution:
    def fetchItemsToDisplay(self, items, sortParameter, sortOrder, itemsPerPage, pageNumber):
        # Write your code here
        if (sortOrder == 1):
            items.sort(reverse=True, key=lambda x: x[sortParameter])
        else:
            items.sort(key=lambda x: x[sortParameter])
        names = []
        for i in items[pageNumber * itemsPerPage:min((pageNumber + 1) * itemsPerPage, len(items))]:
            names += [i[0]]
        return names


if __name__ == "__main__":
    print("Hi There!!")
    l1 = Solution()
    items = [['owjevtkuyv', '58584272', '62930912' ],['rpaqgbjxik', '9425650', '96088250'],\
​rpaqgbjxik 9425650 96088250                      ['dfbkasyqcn', '37469674', '46363902'],['vjrrisdfxe', '18666489', '88046739']]
    sortParameter = 2
    sortOrder = 1
    itemsPerPage = 2
    pageNumber = 0
    print(l1.fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber))
