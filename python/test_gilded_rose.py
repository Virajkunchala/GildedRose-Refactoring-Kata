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
        
    def test_sulfuras_never_changes(self):
        """
        Test that Sulfuras, Hand of Ragnaros, never changes in quality or sell_in value.
        Sulfuras is a legendary item and does not degrade or expire.
        """
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        
    def test_quality_never_negative(self):
        """
        Test that the quality of an item never becomes negative.
        Even if the quality reaches 0, it should not decrease further.
        """
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        
    def test_quality_never_exceeds_fifty(self):
        """
        Test that the quality of an item never exceeds 50.
        For example, Aged Brie should never have a quality greater than 50.
        """
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

        
    def test_quality_degrades_twice_as_fast(self):
        """
        Test that Conjured items degrade in quality twice as fast as normal items.
        The quality of Conjured Mana Cake should decrease by 2 per day.
        """
        items = [Item("Conjured Mana Cake", 3, 6)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        
    def test_conjured_item_after_sellin_degrades_twice_as_fast(self):
        """
        Test that Conjured items degrade by 4 after the sell date.
        """
        items = [Item("Conjured Mana Cake", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        
    def test_conjured_item_quality_does_not_go_negative(self):
        """
        Test that Conjured items never have negative quality.
        """
        items = [Item("Conjured Mana Cake", 1, 1)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
