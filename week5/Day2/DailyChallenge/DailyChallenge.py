##################################
# Daily Challenge : Pagination
##################################
# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# self.items = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(self.items, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# self.items = "abcdefghijklmnopqrstuvwxyz".split('')

# p = Pagination(self.items, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

class Pagination():
    def __init__(self,items,pageSize):
        self.items = items
        self.pageSize = pageSize
        self.curentPage = 1
        self.pagination={}
        
    

    def dico(self):
        self.items = "abcdefghijklmnopqrstuvwxyz"
        isIn=False
        for elem in self.items:
            isIn = False
            for k,v in self.pagination.items():
                if len(self.pagination[k])<4 and isIn == False:
                    isIn=True
                    self.pagination[k].append(elem)
            if isIn == False:
                taille_dict = len(self.pagination)+1
                self.pagination[taille_dict] = []
                self.pagination[taille_dict].append(elem)
        # print(self.pagination)

    def getVisibleItems(self):
        print(self.pagination[self.curentPage])

    def prevPage(self):
        if self.curentPage > 1 :
            self.curentPage -= 1
        return self
        
    def nextPage(self):
        if self.curentPage < len(self.pagination):
            self.curentPage += 1
        return self

    def firstPage(self):
        self.curentPage = 1

    def lastPage(self):
        self.curentPage = len(self.pagination)

    def goToPage(self,pageNum):
        # if pageNum <= len(self.pagination) and pageNum >= 1:
            # self.curentPage = pageNum
        if pageNum > len(self.pagination):
            self.lastPage()
        elif (pageNum < 1):
            self.firstPage()
        else:
            self.curentPage = pageNum

    
        

alphabetList = "abcdefghijklmnopqrstuvwxyz"

p = Pagination(alphabetList, 4)
p.dico()

# p.nextPage()
# p.getVisibleItems() 
# p.nextPage()
# p.getVisibleItems() 
p.goToPage(10)
p.getVisibleItems() 
p.firstPage()
p.getVisibleItems() 
p.nextPage().nextPage()
p.getVisibleItems() 
p.lastPage()
p.getVisibleItems() 
p.prevPage()
p.getVisibleItems() 



