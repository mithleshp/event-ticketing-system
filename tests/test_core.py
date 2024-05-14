from event_ticketing_system import core

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_db_connection(self):
        assert True


if __name__ == '__main__':
    unittest.main()