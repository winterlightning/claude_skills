"""Resolve export-level internal-spacing findings without relaxing rules."""
import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/intersection-review-977/cohort.json'
AUTHOR='gpt-6'
H=Path(__file__).parent;rows={r['id']:r for r in json.loads((H/'changes.json').read_text())}
p=ROOT/rows['dryer-hair']['source'];s=p.read_text().replace("((24,42),(23,41),(22,40))","((23,42),(21,41),(20,40))").replace("(22,40),(27,26)","(20,40),(25,26)").replace("(27,26),(6,22)","(25,26),(6,22)");p.write_text(s)
p=ROOT/rows['fragile-break']['source'];s=p.read_text().replace("(25,4),(37,4)","(29,4),(37,4)").replace("(11,4),(19,4),(17,9),(23,13),(18,16)","(11,4),(21,4),(19,9),(25,13),(20,16)");p.write_text(s)
from icon_set.validation.library_qa import inspect_icon
from icon_set.model.icons.registry import create
for id in ['dryer-hair','fragile-break']:
 q=inspect_icon(create(id));print(id,q['status'],q['errors'],q['warnings'])
