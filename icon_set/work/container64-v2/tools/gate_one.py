"""Gate staged v2 modules under the overlay and record them as agent redraws.

    ICON_CONTRACT_OVERLAY=... python3 icon_set/work/container64-v2/gate_one.py MODULE.py [...]
"""
import json, sys
from pathlib import Path
sys.path.insert(0, '.')
from icon_set.scripts.container_v2_fit import load_classes, gate_icon, WORK
report_path = WORK / 'report.json'
report = json.loads(report_path.read_text())
for arg in sys.argv[1:]:
    path = Path(arg)
    for cls in load_classes(path):
        result = gate_icon(cls())
        row = report.get(cls.icon_id, {})
        row.update(result, stage='agent-redraw', to=cls.keyshape.name, module=path.name)
        report[cls.icon_id] = row
        print(result['status'].upper(), cls.icon_id)
        for e in result['errors'] + result['warnings']:
            print('   ', str(e)[:220])
report_path.write_text(json.dumps(report, indent=1, sort_keys=True, default=str))
