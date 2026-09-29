from pathlib import Path
import json,sys,shutil
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[3]
items=json.loads((HERE/'items.json').read_text())
replacements={
1:[("(31,31)","(29,31)"),("(27,33)","(26,33)")],
10:[("(10,27)","(10,28)"),("(17,27)","(16,28)")],
16:[("('C',(13,29),(10,25),(12,27)),('L',(15,32)),('C',(11,34),(16,35),(13,36)),('L',(9,33))", "('C',(10,28),(8,25),(9,26)),('L',(11,30)),('C',(9,33),(13,32),(12,34)),('L',(7,32))")],
17:[("(23,32)","(20,32)"),("('L',(20,40))","('L',(17,40))")]
}
for i,reps in replacements.items():
 it=items[i];old=ROOT/it['run'];new=old.with_name('20260928T175102Z-stroke-03');new.mkdir()
 for name in [f"{it['id']}.metadata.json",'review-before.md']:shutil.copyfile(old/name,new/name)
 src=(ROOT/it['module']).read_text()
 for a,b in reps:
  assert a in src,(i,a);src=src.replace(a,b)
 module=new/Path(it['module']).name;module.write_text(src)
 it['run']=str(new.relative_to(ROOT));it['module']=str(module.relative_to(ROOT))
items[17]['change']='Clarified therapist and reclining patient, lengthened the patient torso and separated bent legs. Both radius-4 heads have exactly 4 units of visible clearance at their own torso necks.'
(HERE/'items.json').write_text(json.dumps(items,indent=2))
