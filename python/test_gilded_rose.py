# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    
    def test_normal_item_degrades_by_1_before_sell_date(self):
        """
        Test that a Normal Item's quality degrades by 1 before the sell date.
        """
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_normal_item_degrades_by_2_after_sell_date(self):
        """
        Test that a Normal Item's quality degrades by 2 after the sell date.
        """
        items = [Item("Normal Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
        
    def test_aged_brie_increases_in_quality(self):
        """
        Test that Aged Brie increases in quality by 1 before the sell date.
        """
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_doubles_increase_after_sell_date(self):
        """
        Test that Aged Brie increases in quality by 2 after the sell date.
        """
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)
        
    def test_backstage_passes_increase_by_1(self):
        """
        Test that Backstage passes increase by 1 when there are more than 10 days before the concert.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
        
    def test_backstage_passes_increase_by_2(self):
        """
        Test that Backstage passes increase by 2 when there are 10 or fewer days before the concert.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)
        
    def test_backstage_passes_increase_by_3(self):
        """
        Test that Backstage passes increase by 3 when there are 5 or fewer days before the concert.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)
        
    def test_backstage_passes_drop_to_zero(self):
        """
        Test that Backstage passes drop to 0 quality after the concert.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        
    def test_quality_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
