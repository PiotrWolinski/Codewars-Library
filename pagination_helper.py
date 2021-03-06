# TODO: complete this class

class PaginationHelper:
    

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page
      
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
      
  
  # returns the number of pages
  def page_count(self):
      pom = len(self.collection) / self.items_per_page
      self.pages = int(pom) if pom % 1 == 0 else int(pom + 1)
      return self.pages
      
    
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      if 0 > page_index or page_index > self.pages - 1:
          return -1
      return self.items_per_page if page_index < self.pages - 1 else len(self.collection) % self.items_per_page
      
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if 0 > item_index or item_index > len(self.collection) - 1 or len(self.collection) == 0:
          return -1
      return item_index // self.items_per_page