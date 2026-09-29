from pathlib import Path
import json,shutil
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];items=json.loads((HERE/'items.json').read_text())
changes={
8:[("(41,20)","(41,17)"),("(7,20)","(7,17)"),("('C',(24,20),(13,17),(18,23)),('C',(41,17),(30,17),(35,23))","('C',(24,17),(13,15),(18,19)),('C',(41,17),(30,15),(35,19))")],
9:[("('C',(24,18),(17,12),(20,15)),('C',(31,8),(28,15),(31,12))","('C',(24,16),(17,11),(20,14)),('C',(31,8),(28,14),(31,11))"),("line('stem',(24,18)","line('stem',(24,16)")],
15:[("for j,cx in enumerate((16,32)):","for j,cx in enumerate((15,33)):"),("(cx-3,26),[('C',(cx,15),(cx-8,24),(cx-8,15)),('C',(cx+1,25),(cx+8,15),(cx+8,25)),('C',(cx+2,20),(cx-2,25),(cx-2,20))]","(cx-3,25),[('C',(cx,16),(cx-6,23),(cx-5,16)),('C',(cx+1,25),(cx+6,16),(cx+6,25)),('C',(cx+3,21),(cx,25),(cx,21))]")],
18:[("(15,33),(8,31),(6,35)","(14,32),(8,29),(6,34)"),("line('back-boot',(6,35),(13,37))","line('back-boot',(6,34),(14,34))"),("[(6,41),(13,43),(28,43),(36,43)]","[(6,40),(14,40),(28,43),(36,43)]")]
}
for i,reps in changes.items():
 it=items[i];old=ROOT/it['run'];new=old.with_name('20260929T033605Z-meaning-03');new.mkdir()
 for fn in [f"{it['id']}.metadata.json",'review-before.md']:shutil.copyfile(old/fn,new/fn)
 p=ROOT/it['module'];s=p.read_text()
 for a,b in reps:assert a in s,(i,a);s=s.replace(a,b)
 q=new/p.name;q.write_text(s);it['run']=str(new.relative_to(ROOT));it['module']=str(q.relative_to(ROOT))
(HERE/'items.json').write_text(json.dumps(items,indent=2))
