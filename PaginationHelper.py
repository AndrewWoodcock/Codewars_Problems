
import math

# https://www.codewars.com/kata/515bb423de843ea99400000a


# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = list(collection)
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count() / self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > (self.page_count() -1):
            return -1
        if page_index < 0:
            return -1

        page_dict = {}
        remainder = self.item_count()

        for i in range(0, self.page_count()):
            if remainder >= self.items_per_page:
                page_dict[i] = self.items_per_page
                remainder -= self.items_per_page
            else:
                page_dict[i] = remainder
                remainder -= remainder
        return page_dict[page_index]

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > (self.item_count() -1):
            return -1
        if item_index < 0:
            return -1

        contents_dict = {}
        x = 0
        remainder = self.item_count()
        for i in range(0, self.page_count()):
            contents_dict[i] = []
            while (len(contents_dict[i]) < self.items_per_page) and remainder != 0:
                # item = self.collection.pop(0)
                contents_dict[i].append(x)
                x += 1
                remainder -= 1

        for page, contents in contents_dict.items():
            if item_index in contents_dict[page]:
                return page


test = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
