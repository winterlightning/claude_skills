from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
for i in [4,16,17]:
 r=rows[i];old=Path(r['run']);new=old.with_name(old.name[:-2]+'03');shutil.copytree(old,new)
 module=new/Path(r['module']).name;s=module.read_text()
 if i==4:
  s=s.replace('(12,26),(37,26)','(12,26),(20,26),(37,26)')
  s=s.replace('((38,42),3,3,True)',"('C',(38,42),(41,42),(40,42))")
  s=s.replace('(29,34),(12,34)','(29,34),(25,34),(12,34)')
 if i==16:
  s=s.replace("path('bow-left',(22,39),[(13,36),(13,44),(22,41)])", "path('bow-left',(22,40),[(13,36),(13,44),(22,40)],True)")
  s=s.replace("path('bow-right',(26,39),[(35,36),(35,44),(26,41)])", "path('bow-right',(26,40),[(35,36),(35,44),(26,40)],True)")
 if i==17:
  s=s[:s.index("        circle('head'")]+'''        # Circular head split at exact integer 5-12-13 attachment nodes.
        nodes=[(24,8),(36,16),(37,21),(36,26),(29,33),(24,34),(19,33),(12,26),(11,21),(12,16),(24,8)]
        path('head',nodes[0],[(p,13,13,True) for p in nodes[1:]],True)
        path('hair-left',(12,16),[((8,17),4,4,False),((8,25),4,4,False),((12,26),4,4,False)])
        path('hair-right',(36,16),[((40,17),4,4,True),((40,25),4,4,True),((36,26),4,4,True)])
        join('hair-left','head');join('hair-right','head')
        path('ribbon-left',(19,33),[((17,37),4,4,False),((18,40),3,3,True)])
        path('ribbon-right',(29,33),[((31,37),4,4,True),((30,40),3,3,False)])
        join('ribbon-left','head');join('ribbon-right','head')
'''
 module.write_text(s);r.update(run=str(new),module=str(module))
(ROOT/'batch.json').write_text(json.dumps(rows,indent=2))
