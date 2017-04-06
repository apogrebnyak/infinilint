import unittest

import infinilint


class TestAll(unittest.TestCase):

    def test_read_configs(self):
        self.assertIsNotNone(infinilint.read_configs())

    def test_select_linters_single_enabled(self):
        config = {'linters': {'linter_one': {'enabled': True}}}
        self.assertDictEqual(
            {'linter_one': {'enabled': True}},
            infinilint.select_linters(config)
        )

    def test_select_linters_two_one_enabled(self):
        config = {'linters': {'linter_one': {'enabled': True},
                              'linter_two': {'enabled': False}}}
        self.assertDictEqual(
            {'linter_one': {'enabled': True}},
            infinilint.select_linters(config)
        )

    def test_selected_linters_single_disabled(self):
        config = {'linters': {'linter_one': {'enabled': False}}}
        self.assertDictEqual(
            {},
            infinilint.select_linters(config)
        )

    def test_get_image_latest_no_proxy(self):
        config = {'linters': {'linter_one': {'image': 'image_name'}}}
        self.assertEqual('image_name:latest',
                         infinilint.get_image(config, 'linter_one'))

    def test_get_entrypoint(self):
        config = {'command': ['run', 'this']}
        self.assertEqual(['run', 'this'],
                         infinilint.get_entrypoint(config))


if __name__ == '__main__':
    unittest.main()
