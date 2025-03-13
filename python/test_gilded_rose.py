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
        
    def test_quality_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
