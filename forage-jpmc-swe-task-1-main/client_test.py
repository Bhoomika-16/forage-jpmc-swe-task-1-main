import unittest
from client3 import getDataPoint
from itertools import zip_longest

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_calculatePriceBidLesserThanAsk1(self):
        quotes = [
            {'top_ask': {'price': 219.3, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 135.52, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 141.78, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 157.67, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertLessEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                  (quote['top_bid']['price'] + quote['top_ask']['price']) / 2), "Less!")

    def test_getDataPoint_calculatePriceBidLesserThanAsk(self):
        quotes = [
            {'top_ask': {'price': 219.3, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 135.52, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 141.78, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 157.67, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        quotes2 = [
            {'top_ask1': {'price1': 119.2, 'size1': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid1': {'price1': 120.48, 'size1': 109}, 'id': '0.109974697771', 'stock1': 'ABC'},
            {'top_ask1': {'price1': 121.68, 'size1': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid1': {'price1': 117.87, 'size1': 81}, 'id': '0.109974697771', 'stock1': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for q, quote in zip_longest(quotes2, quotes):
            self.assertLess((q['stock1'], q['top_bid1']['price1'], q['top_ask1']['price1'],
                                                  (q['top_bid1']['price1'] + q['top_ask1']['price1']) / 2),
                            (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                  (quote['top_bid']['price'] + quote['top_ask']['price']) / 2),
                            "less!")




if __name__ == '__main__':
    unittest.main()
