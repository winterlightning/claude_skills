from repair_geometry import *
from icon_set.scripts.create_variant import prepare_variant
import ast,importlib,inspect
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
HUMANS={'baby-figure-v2':(6,8),'figure-with-outstretched-limbs':(4,8),'fortune-teller-reading':(5,8),'geisha-bust':(9,8),'two-stick-figures':(4,8)}
if (W/'results.json').exists():raise SystemExit('Results already exist; edit existing variants instead of allocating duplicates.')
results=[]
for f in sorted((W/'candidates').glob('*.json')):
 if f.stem=='figured-ceremonial-urn':continue
 x=json.loads(f.read_text());r=x['record'];q=x['report']['validation']
 assert q['status']=='pass' and q['internal_spacing']['status']=='pass',(f.stem,q['status'])
 original=create(f.stem);module=importlib.import_module(type(original).__module__);source_id=getattr(module,'SOURCE_ICON_ID',None);source_path=getattr(module,'SOURCE_PATH',None) or str(Path(inspect.getsourcefile(type(original))).relative_to(ROOT))
 destination,newid,scaffold=prepare_variant(f.stem,'solo','Exact keyshape envelope and clear internal spacing')
 tree=ast.parse(scaffold);cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and any(isinstance(a,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='icon_id' for t in a.targets) and getattr(a.value,'value',None)==newid for a in n.body))
 if source_id:destination=destination.with_name(destination.stem+'_'+source_id.replace('-','_')+'.py')
 note=x.get('manual_note','Rebalanced the existing shared geometry on the selected keyshape while retaining its construction and features.').strip()
 doc=f"{f.stem.replace('-v2','').replace('-',' ').capitalize()}.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The {r['keyshape']} visible envelope is {tuple(model(f.stem,r).keyshape_bounds())}.\nThe parent remains available for comparison."
 if f.stem in HUMANS:doc+='\nHuman construction: icon_set/references/human_ref/full_body_ref.png and\nicon_set/references/human_ref/user.svg. Circular head radius '+str(HUMANS[f.stem][0])+',\nwith exactly 8 units of centerline head-to-body separation (4 visible units).'
 parts=[repr(doc),'from ...keyshapes import Keyshape','from ._base import Solo48','',f'SOURCE_ICON_ID = {source_id!r}',f'SOURCE_PATH = {source_path!r}',"AUTHOR = 'gpt-6'",'',f'class {cls.name}(Solo48):',f'    icon_id = {newid!r}',f'    variant_of = {f.stem!r}',"    variant_label = 'Exact keyshape envelope and clear internal spacing'",f"    keyshape = Keyshape.{r['keyshape']}","    semantic_role = 'MAIN'","    semantic_kind = 'noun'",f'    category = {original.category!r}',f'    aliases = {tuple(original.aliases)!r}',f'    keywords = {tuple(original.keywords)!r}','','    def build(self) -> None:','        # Shared nodes are reused by every touching member.']
 nodes={}
 for p in r['primitives']:
  for key in ['start','end']:
   v=tuple(p[key])
   if v not in nodes:nodes[v]='p_'+str(v[0]).replace('-','m')+'_'+str(v[1]).replace('-','m')
 for point,name in nodes.items():parts.append(f'        {name} = {point!r}')
 for p in r['primitives']:
  a=nodes[tuple(p['start'])];b=nodes[tuple(p['end'])];n=p['element_id']
  if p['kind']=='line':parts.append(f'        self.add_line({n!r}, {a}, {b})')
  elif p['kind']=='arc':parts.append(f"        self.add_arc({n!r}, {a}, {b}, radius_x={p['radius_x']}, radius_y={p['radius_y']}, sweep={p['sweep']}, large_arc={p['large_arc']})")
  else:raise ValueError(p)
 for c in r['contours']:parts.append(f"        self.add_contour({c['contour_id']!r}, "+', '.join(repr(n) for n in c['members'])+f", closed={c['closed']})")
 for rel in r['relationships']:parts.append(f"        self.relate({rel['kind']!r}, "+', '.join(repr(n) for n in rel['members'])+')')
 text='\n'.join(parts)+'\n';compile(text,str(destination),'exec')
 with destination.open('x') as out:out.write(text)
 originals=[f.stem]
 if f.stem=='baby-figure-v2':originals=['baby-figure','baby-figure-v2']
 if f.stem=='pair-of-teardrop-earrings-v2':originals=['pair-of-teardrop-earrings','pair-of-teardrop-earrings-v2']
 results.append({'original':f.stem,'originals':originals,'id':newid,'file':str(destination.relative_to(ROOT)),'keyshape':r['keyshape'],'bounds':list(model(f.stem,r).keyshape_bounds()),'note':note,'reused':False})
for old,newid in [('scorpio-zodiac-symbol','scorpio-zodiac-symbol-v3'),('cd-rom-drive','cd-rom-drive-v3')]:
 o=create(newid);results.append({'original':old,'originals':[old],'id':newid,'file':str(Path(inspect.getsourcefile(type(o))).relative_to(ROOT)),'keyshape':o.keyshape.name,'bounds':list(o.keyshape_bounds()),'note':'Reused the validated repair from the preceding batch.','reused':True})
(W/'results.json').write_text(json.dumps(results,indent=2));print(f'{len(results)} variants covering {sum(len(r["originals"]) for r in results)} standalone entries')
