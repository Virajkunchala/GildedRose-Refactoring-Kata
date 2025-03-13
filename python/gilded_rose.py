# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        #code smell 1: long method
        #The update_quality function is handling a lot of different items with
        #very different behaviors. we need to refactor this function for better scalability and readability.
        #We can refactor this function by breaking it down into smaller functions that handle each item type separately.
        for item in self.items:
            #code smell 2: multiple if statements
            #Too many if statements can make the code hard to read and maintain.
            #We could refactor this into individual methods or classes per item type.
            
            # Code Smell 3: Difficult to extend
            # For instance, adding a new item type like 'Conjured' means adding more logic here.
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
                        if "Conjured" in item.name:
                            item.quality -= 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                                
            # Code Smell 4: Too many conditionals to decrease sell_in value
            # The following block decreases the sell_in value, but there’s redundancy.
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
                
            # Code Smell 5: Handle the expired items with more complexity
            # There are many checks for whether the sell_in has expired or not, but it makes 
            # the method hard to follow and extend.
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    
class ItemUpdater:
    def update(self,item: Item):
        """Base class for updating items,Should be overridden."""
        raise NotImplementedError("Subclasses should implement this method")