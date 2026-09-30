import json, sys, time
from icon_set.model.icons.registry import icons_in
from icon_set.validation.library_qa import inspect_icon
out = {}
t = time.time()
for icon in icons_in('container'):
    try:
        qa = inspect_icon(icon)
        out[icon.icon_id] = {'status': qa['status'], 'errors': qa['errors'][:5]}
    except Exception as e:
        out[icon.icon_id] = {'status': 'crash', 'errors': [repr(e)]}
json.dump(out, open(sys.argv[1], 'w'), indent=1)
from collections import Counter
print(Counter(v['status'] for v in out.values()), round(time.time() - t), 's')
