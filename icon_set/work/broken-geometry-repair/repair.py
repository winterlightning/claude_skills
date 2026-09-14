from pathlib import Path
import json,re
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/dist/gallery/failures.html#rule=broken'
AUTHOR='gpt-6'
root=Path(__file__).resolve().parents[3]
work=Path(__file__).parent
html=(root/'icon_set/dist/gallery/failures.html').read_text()
data=json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>',html,re.S)[1])
icons=[i for i in data['icons'] if any(x['rule']=='broken' for x in i['issues'])]
assert len(icons)==25
(work/'queue.json').write_text(json.dumps(icons,indent=2))
for item in icons:
 p=root/item['file'];src=p.read_text();before=src;ident=item['id']
 src=re.sub(r'range\(6,\s*(\d+)\)',r'range(1, \1)',src)
 if ident=='hand-saw':src=src.replace('range(1, 6)', 'range(1, 4)')
 if ident=='hatching-dinosaur-egg':src=src.replace('range(1, 6)', 'range(1, 5)')
 if ident=='clogged-air-filter':src=src.replace('for i in (6,6)', 'for i in (1,2)')
 if ident=='fuel-pump-with-display':src=src.replace('in (6,6)', 'in (1,2)')
 if ident=='sun-with-eight-rays':
  src=src.replace('[(6,6),(6,6),(0,-1),(-1,0)]','[(0,1),(1,0),(0,-1),(-1,0)]').replace('[(6,6),(1,-1),(-1,1),(-1,-1)]','[(1,1),(1,-1),(-1,1),(-1,-1)]')
 remove={'anteater':['snout-tip'],'pointed-paintbrush':['handle-tip-b'],'hooded-cobra':['coil-bottom-end','coil-left'],'floppy-disk-v2':['disk-ne','disk-se','disk-sw','disk-nw']}.get(ident,[])
 for name in remove:
  src=re.sub(r'^\s*self\.add_arc\(\''+name+r"'.*\n",'\n',src,flags=re.M)
  src=src.replace("'"+name+"',",'')
 assert src!=before,ident
 compile(src,str(p),'exec')
 backup=work/'before'/p.name;backup.parent.mkdir(exist_ok=True)
 if not backup.exists():backup.write_text(before)
 p.write_text(src)
print('Repaired',len(icons),'existing models; originals backed up in',work/'before')
