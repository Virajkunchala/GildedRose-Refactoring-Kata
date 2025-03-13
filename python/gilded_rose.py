# -*- coding: utf-8 -*-

class Item:
    """
    Represents an item with a name, sell-in date, and quality.
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    
class ItemUpdater:
    """
    Base class for updating items. Should be overridden in subclasses.
    """
    def update(self,item: Item):
        """ 
        Update the item. This should be implemented in the subclass.
        """
        raise NotImplementedError("Subclasses should implement this method")
    
    
    
class NormalItem(ItemUpdater):
    """
    Handles updates for normal items.
    """
    def update(self,item: Item):
        item.sell_in -= 1
        degradation = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - degradation)
        
class AgedBrie(ItemUpdater):
    """
    Handles updates for Aged Brie items, which increase in quality.
    """
    def update(self,item: Item):
        item.sell_in -= 1
        improvement = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + improvement)
        
class BackstagePass(ItemUpdater):
    """
    Handles updates for Backstage Pass items. The quality increases based on the number of days left.
    """
    def update(self,item: Item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
            
class Sulfuras(ItemUpdater):
    """
    Handles updates for Sulfuras, which does not change in quality or sell-in value.
    """
    def update(self,item: Item):
        pass
    
class ConjuredItem(ItemUpdater):
    """
    Handles updates for Conjured items, which degrade twice as fast as normal items.
    """
    def update(self, item: Item):
        item.sell_in -= 1
        degradation = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degradation)
        
        
def get_updater(item: Item) -> ItemUpdater:
    """
    Returns the correct ItemUpdater subclass based on the item's name.
    """
    if item.name == "Aged Brie":
        return AgedBrie()
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePass()
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return Sulfuras()
    elif "Conjured" in item.name:
        return ConjuredItem()
    else:
        return NormalItem()
        
        
class GildedRose(object):
    """
    Represents the Gilded Rose store, where items' qualities are updated daily.
    """
    
    def __init__(self, items):
        """
        Initializes the store with a list of items.

        :param items: List of Item objects
        """

        self.items = items

    def update_quality(self):
        """
        Updates the quality of all items in the store.
        """
        for item in self.items:
            updater = get_updater(item)
            updater.update(item)
            
            
