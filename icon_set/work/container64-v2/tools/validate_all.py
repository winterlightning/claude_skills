"""validate_icon() on every staged v2 class; prints status and warning counts."""
import json, sys
from collections import Counter
sys.path.insert(0, '.')
from icon_set.scripts.container_v2_fit import load_classes, WORK
rows = {}
for path in sorted(WORK.glob('*.py')):
    for cls in load_classes(path):
        rep = cls().validate_icon()
        d = rep.to_dict() if hasattr(rep, 'to_dict') else {}
        status = getattr(rep, 'status', d.get('status'))
        warnings = list(getattr(rep, 'warnings', d.get('warnings', [])) or [])
        errors = list(getattr(rep, 'errors', d.get('errors', [])) or [])
        rows[cls.icon_id] = {'status': str(status), 'errors': [str(e) for e in errors], 'warnings': [str(w) for w in warnings]}
(WORK / 'validate.json').write_text(json.dumps(rows, indent=1, sort_keys=True))
print(len(rows), Counter(r['status'] for r in rows.values()))
print('with warnings:', sum(1 for r in rows.values() if r['warnings']))
for k, r in rows.items():
    if r['errors'] or r['warnings']:
        print(k, r['status'], (r['errors'] + r['warnings'])[0][:160])
