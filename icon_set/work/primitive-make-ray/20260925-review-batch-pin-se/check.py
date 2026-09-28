from pathlib import Path
import importlib.util,json,sys,cairosvg
from PIL import Image,ImageDraw
from icon_set.validation.library_qa import inspect_icon
B=Path(__file__).parent;rows=json.loads((B/'inputs.json').read_text());sheet=Image.new('RGB',(700,160*len(rows)),'white');d=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
 spec=importlib.util.spec_from_file_location('repair'+str(i),row['module']);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);ic=m.Drawing();r=ic.validate_icon();q=inspect_icon(ic,validation=r);out=Path(row['run']);svg=ic.to_svg();(out/(ic.icon_id+'.svg')).write_text(svg);(out/'validation.txt').write_text(r.describe()+'\nFull QA: '+q['status']+'\n'+'\n'.join(q['errors']+q['warnings']));print(i+1,(out/'validation.txt').read_text(),flush=True)
 (out/'qa.json').write_text(json.dumps({k:v for k,v in q.items() if k!='_svg'},indent=2))
 for theme,bg,ink in [('light','#ffffff','#000000'),('dark','#161b22','#ffffff')]:
  for sz in (48,144):
   cairosvg.svg2png(bytestring=svg.replace('currentColor',ink).encode(),write_to=str(out/f'{theme}-{sz}.png'),output_width=sz,output_height=sz,background_color=bg)
 for name,x in [('reference',0),('light-144',160),('dark-144',320),('light-48',490),('dark-48',550)]:
  im=Image.open(out/(name+'.png'));sheet.paste(im,(x,i*160),im if im.mode=='RGBA' else None)
 d.text((490,i*160+70),str(i+1)+' '+q['status'],fill='black')
 row['status']=r.status;row['qa_status']=q['status'];row['icon_id']=ic.icon_id;row['keyshape']=str(ic.keyshape)
(B/'inputs.json').write_text(json.dumps(rows,indent=2));sheet.save(B/'after-sheet.png')
