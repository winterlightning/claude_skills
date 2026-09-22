"""Read the append-only activity log into generation handoff provenance."""
import json

LABELS = {'todo': 'TODO', 'container': 'Container combination',
          'combination': 'Side combination', 'text_number': 'Text / number', 'other': 'Other'}


def load_history(connection, human_users=()):
    result = {}
    for event_id, actor, action, icon, raw, at in connection.execute('''
        SELECT id,username,action,icon,details,created_at FROM activity_log
        WHERE action IN ('primitive_skip','primitive_todo','primitive_classification_confirmed','primitive_brief')
          AND icon LIKE 'primitive:%' ORDER BY id'''):
        details = json.loads(raw)
        uid = icon[len('primitive:'):]
        history = result.setdefault(uid, [])
        family = action == 'primitive_brief'
        previous = next((h['to'] for h in reversed(history) if h['kind'] == ('family' if family else 'classification')), None)
        before = details.get('previous_family', previous) if family else details.get('previous_classification', details.get('previous_reason', previous))
        after = details.get('family') if family else details.get('classification', 'todo' if action == 'primitive_todo' else details.get('reason'))
        # Legacy events did not record actor authority. Only known login accounts
        # can be treated as users; unknown/agent names never acquire authority.
        authority = details.get('authority') or ('user' if actor in human_users else 'unspecified')
        history.append(dict(event_id=event_id, kind='family' if family else 'classification',
                            action=action, **{'from': before, 'to': after}, user=actor,
                            authority=authority, created_at=at,
                            note=details.get('note', ''), previous_note=details.get('previous_note', '')))
    return result


def handoff_decision(history, family, saved):
    classification = next((h for h in reversed(history) if h['kind'] == 'classification'), None)
    family_choice = next((h for h in reversed(history) if h['kind'] == 'family'), None)
    confirmed = []
    if classification and classification['authority'] == 'user' and classification['to'] == 'todo':
        confirmed.append(classification)
    if saved and family_choice and family_choice['authority'] == 'user' and family_choice['to'] == family:
        confirmed.append(family_choice)
    if not confirmed:
        return dict(authoritative=False, family=family, instruction='No current authoritative user classification is recorded. Inspect the reference using the normal family guidance.')
    notes = []
    for event in confirmed:
        before = LABELS.get(event['from'], event['from']) or 'an unrecorded previous type'
        after = LABELS.get(event['to'], event['to'])
        notes.append(f"Changed from {before} to {after} by {event['user']} at {event['created_at']}.")
    notes.append(f'The user decision is authoritative. Generate using the selected {family} family and preserve the whole intended subject. Do not judge the classification again, split the reference, or route it back to a rejected combination/text category. Inspect geometry and drawing quality only. This instruction takes priority over generic reference-triage instructions in the brief or family skill. TODO is a workflow state, not a family; the selected family is listed separately.')
    return dict(authoritative=True, family=family, events=[e['event_id'] for e in confirmed], instruction=' '.join(notes))
