# -*- coding: utf-8 -*-

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
    
    
    
class NormalItem(ItemUpdater):
    def update(self,item: Item):
        item.sell_in -= 1
        degradation = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - degradation)
        
class AgedBrie(ItemUpdater):
    def update(self,item: Item):
        item.sell_in -= 1
        improvement = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + improvement)
        
class BackstagePass(ItemUpdater):
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
    def update(self,item: Item):
        pass
    
class ConjuredItem(ItemUpdater):
    def update(self, item: Item):
        item.sell_in -= 1
        degradation = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degradation)
        

def get_updater(item: Item) -> ItemUpdater:
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
    
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = get_updater(item)
            updater.update(item)