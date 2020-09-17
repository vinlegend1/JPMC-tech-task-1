import unittest
from client import getDataPoint


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], quotes[0]['top-bid']['price'], quotes[0]['top-ask']['price'], (quotes[0]['top-bid']['price'] + quotes[0]['top-ask']['price']) / 2))
    self.assertEqual(getDataPoint(quotes[1]), (quotes[1]['stock'], quotes[1]['top-bid']['price'], quotes[1]['top-ask']['price'], (quotes[1]['top-bid']['price'] + quotes[1]['top-ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertGreater(quotes[0]['top-bid']['price'], quotes[0]['top-ask']['price'])
    self.assertGreater(quotes[1]['top-bid']['price'], quotes[1]['top-ask']['price'])

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
