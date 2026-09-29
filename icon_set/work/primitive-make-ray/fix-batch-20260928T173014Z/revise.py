from pathlib import Path
import json,shutil
root=Path(__file__).parent;rows=json.loads((root/'batch.json').read_text());(root/'batch-v1.json').write_text(json.dumps(rows,indent=2))
changes={
4:[("line('text-one',(10,32),(20,32))","line('text-one',(10,32),(14,32))")],
6:[("circle('carrier-head',18,8,3);circle('director-head',36,6,3)","circle('carrier-head',18,8,4);circle('director-head',36,8,4)"),("(18,19)","(18,20)"),("(36,17)","(36,20)"),("(36,19)","(36,22)"),("(36,21)","(36,24)"),("(25,19)","(26,22)"),("# 19-(8+3)-4=4 and 17-(6+3)-4=4 visible head/body gaps.","# Both: 20-(8+4)-4=4px visible head/body gap.")],
7:[("(28,27),(22,27),(24,30)","(28,27),(24,30)")],
14:[("line('shank',(27,15),(38,22))","line('shank',(27,15),(36,20))"),("path('handle',(40,18),[('C',(42,22),(42,18),(43,19)),('C',(8,44),(37,34),(23,44)),('C',(8,36),(2,44),(2,36)),('C',(38,22),(22,36),(32,30)),('C',(40,18),(39,20),(39,19))],True)","path('handle',(36,20),[('C',(42,22),(40,12),(46,16)),('C',(8,44),(37,34),(23,44)),('C',(8,34),(2,44),(2,34)),('C',(36,20),(22,34),(30,28))],True)")],
15:[("(19,15)","(19,16)"),("(27,15)","(27,16)"),("(30,18)","(30,19)"),("(16,18)","(16,19)")],
16:[("[('L',(14,16)),('C',(23,8),(17,10),(20,8)),('C',(27,14),(28,8),(29,9)),('L',(20,32)),('C',(22,38),(18,37),(18,40)),('C',(33,24),(26,36),(29,28)),('C',(40,19),(37,20),(40,16)),('C',(38,31),(40,23),(38,28)),('C',(42,37),(38,35),(38,40)),('C',(44,34),(43,36),(44,35))]","[('L',(14,16)),('C',(23,8),(17,9),(20,8)),('C',(27,16),(29,8),(29,11)),('L',(20,33)),('C',(22,38),(18,38),(19,41)),('C',(33,24),(26,34),(29,28)),('C',(38,19),(35,21),(36,19)),('C',(40,24),(41,19),(41,20)),('C',(38,33),(39,28),(38,30)),('C',(42,37),(37,40),(39,40)),('L',(44,34))]")]
}
for i,replacements in changes.items():
 m=rows[i-1];old=Path(m['result_dir']);new=Path(str(old).replace('-v1','-v2'));new.mkdir(exist_ok=True)
 for p in old.iterdir():
  if p.name in ('reference.png','before.png','comparison.md') or p.name.endswith('.metadata.json'):shutil.copyfile(p,new/p.name)
 mod=Path(m['module']);s=mod.read_text()
 for a,b in replacements:
  assert a in s,(i,a);s=s.replace(a,b)
 (new/mod.name).write_text(s);m['module']=str(new/mod.name);m['result_dir']=str(new)
 (new/'comparison.md').write_text((new/'comparison.md').read_text()+'\nRevision 2: repaired visual first-pass findings; preserve reference silhouette and clean native rendering.\n')
(root/'batch.json').write_text(json.dumps(rows,indent=2))
