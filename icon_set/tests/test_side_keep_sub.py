import json
import tempfile
import unittest
from pathlib import Path

from icon_set.scripts.side_keep_sub import plan, strip, strip_file


def sub(icon, family='sub'):
    return {'icon': icon, 'family': family}


def rows():
    return [
        {'id': 'a', 'subs': [sub('robot'), sub('robot-profile')]},
        {'id': 'b', 'subs': [sub('robot'), sub('robot-profile')]},
        {'id': 'c', 'subs': [sub('robot-profile')]},
        {'id': 'd', 'subs': [sub('bag')]},
    ]


class SideKeepSubTests(unittest.TestCase):
    def test_plan_lists_alternatives_and_every_pair_using_them(self):
        result = plan(rows()[:2] + rows()[3:], 'a', 'sub/robot')
        self.assertEqual(result['remove'], [{'key': 'sub/robot-profile', 'icon': 'robot-profile', 'pairs': 2}])
        self.assertEqual(result['affected_pairs'], ['a', 'b'])

    def test_plan_rejects_a_sub_outside_the_pair_and_single_sub_pairs(self):
        with self.assertRaisesRegex(ValueError, 'does not belong'):
            plan(rows(), 'a', 'sub/bag')
        with self.assertRaisesRegex(ValueError, 'only one sub'):
            plan(rows(), 'd', 'sub/bag')
        with self.assertRaisesRegex(ValueError, 'Unknown'):
            plan(rows(), 'z', 'sub/bag')

    def test_plan_refuses_to_leave_a_pair_without_a_sub(self):
        with self.assertRaisesRegex(ValueError, '1 side pair'):
            plan(rows(), 'a', 'sub/robot')

    def test_strip_removes_the_sub_from_every_row_and_file(self):
        stripped = strip(rows(), ['sub/robot-profile'])
        self.assertEqual([[s['icon'] for s in r['subs']] for r in stripped], [['robot'], ['robot'], [], ['bag']])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'pairs.json'
            path.write_text(json.dumps({'rows': rows(), 'failures': []}))
            strip_file(path, ['sub/robot'])
            data = json.loads(path.read_text())
            self.assertEqual(data['rows'][0]['subs'], [sub('robot-profile')])
            self.assertEqual(data['failures'], [])
            strip_file(Path(tmp) / 'missing.json', ['sub/robot'])


if __name__ == '__main__':
    unittest.main()
