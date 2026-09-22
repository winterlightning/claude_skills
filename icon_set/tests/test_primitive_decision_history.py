import sqlite3
import unittest

from icon_set.scripts.primitive_decision_history import load_history, handoff_decision
from icon_set.scripts.primitive_status import init_primitive_status, set_status
from icon_set.scripts.deploy import record_activity

UID = '11111111-2222-3333-4444-555555555555'


class DecisionHistoryTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.execute('CREATE TABLE activity_log(id INTEGER PRIMARY KEY, username TEXT, action TEXT, icon TEXT, details TEXT, created_at TEXT)')
        init_primitive_status(self.db)

    def test_reclassification_survives_deleted_status_and_unknown_actors(self):
        for user, status, reason, authority in [('agent', 'skip', 'container', 'unspecified'),
                                               ('reviewer', 'todo', None, 'user')]:
            set_status(self.db, [UID], status, reason, user=user, record=record_activity, authority=authority)
        events = load_history(self.db)[UID]
        self.assertEqual(events[-1]['from'], 'container')
        self.assertEqual(events[-1]['to'], 'todo')
        self.assertEqual(self.db.execute('SELECT COUNT(*) FROM primitive_status').fetchone()[0], 0)
        self.assertTrue(handoff_decision(events, 'solo', None)['authoritative'])
        set_status(self.db, [UID], 'skip', 'text_number', user='agent', record=record_activity)
        self.assertFalse(handoff_decision(load_history(self.db)[UID], 'solo', None)['authoritative'])

    def test_legacy_history_does_not_invent_previous_type_or_human(self):
        record_activity(self.db, 'agent', 'primitive_skip', 'primitive:' + UID, reason='combination')
        record_activity(self.db, 'reviewer', 'primitive_todo', 'primitive:' + UID, previous_reason='combination')
        events = load_history(self.db, ['reviewer'])[UID]
        self.assertIsNone(events[0]['from'])
        self.assertEqual(events[0]['authority'], 'unspecified')
        self.assertTrue(handoff_decision(events, 'solo', None)['authoritative'])
        self.assertFalse(handoff_decision(load_history(self.db)[UID], 'solo', None)['authoritative'])

    def test_user_can_confirm_existing_todo_without_fabricated_change(self):
        result = set_status(self.db, [UID], 'todo', user='reviewer', record=record_activity, authority='user')
        self.assertEqual(result['changed'], 0)
        event = load_history(self.db)[UID][-1]
        self.assertEqual((event['from'], event['to']), ('todo', 'todo'))
        self.assertTrue(handoff_decision([event], 'solo', None)['authoritative'])


if __name__ == '__main__':
    unittest.main()
