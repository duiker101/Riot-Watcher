import unittest
import sys

from unittest.mock import MagicMock
from .. import DataDragonApi


class DataDragonApiTestCase(unittest.TestCase):
    def setUp(self):
        self._expected_return = object()

        self._base_api_mock = MagicMock(name='base_api')
        self._base_api_mock.request_static = MagicMock(name='request_static')
        self._base_api_mock.request_static.return_value = self._expected_return

    def test_all_champions_default(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'

        ret = static_data.champions(version)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            'en_US',
            'champion'
        )

        self.assertIs(self._expected_return, ret)

    def test_all_champions_Full(self):
        static_data = DataDragonApi(self._base_api_mock)

        version = '234'
        locale = 'asdf'

        ret = static_data.champions(version, True, locale)

        self._base_api_mock.request_static.assert_called_once_with(
            version,
            locale,
            'championFull'
        )

        self.assertIs(self._expected_return, ret)