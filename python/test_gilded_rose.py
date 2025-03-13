# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
        
    def test_quality_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)] 
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
