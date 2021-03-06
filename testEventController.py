import unittest

from eventController import EventController


class EventControllerMocker(EventController):
    """
    Interit the EventController in order to mock it without calling the database.
    Inspired by: https://stackoverflow.com/questions/17836939/mocking-init-for-unittesting
    """

    def __init__(self, money):
        self.money = money


class TestEventController(unittest.TestCase):

    def setUp(self):

        self.controller = EventControllerMocker(0)

    def testOnSucessEvent(self):  # increase money
        self.controller.money = 0
        self.controller.onSuccessEvent()
        self.assertEqual(self.controller.money, 10)

    def testOnFailEvent1(self):  # deduct money
        self.controller.money = 10
        self.controller.onFailEvent()
        self.assertEqual(self.controller.money, 0)

    def testOnFailEvent2(self):  # money cannot below zero
        self.controller.money = 0
        self.controller.onFailEvent()
        self.assertEqual(self.controller.money, 0)


if __name__ == "__main__":

    unittest.main()
