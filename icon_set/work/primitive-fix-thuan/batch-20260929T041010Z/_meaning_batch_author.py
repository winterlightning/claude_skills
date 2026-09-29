from pathlib import Path
import json,sys,textwrap,re,io
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
B=Path('icon_set/work/primitive-fix-thuan/batch-20260929T041010Z')
claims=json.loads((B/'claims.json').read_text())
helpers='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
'''
specs={}
def add(i,key,why,body,omit='Only insignificant source detail omitted.',ref='No useful subject-specific Lucide match; original reference determines the silhouette.'):
 specs[i]=dict(keyshape=key,comparison=why,body=textwrap.dedent(body).strip(),omissions=omit,construction=ref)
add(0,'SQUARE','Rejected bent strokes no longer show the hanging fabric or recognizable reclined bow pose. Restore triangular suspension and a coherent folded body.', '''
self.circle('head',38,37,4)
self.add_bezier('torso',(26,37),((32,34),(30,28),(23,27)),((17,26),(10,26),(8,32)))
self.path('bent-leg',(8,32),[('L',(8,38)),('A',(16,38),4,4,False),('L',(20,24))])
self.path('sling',(20,24),[('L',(24,6)),('L',(30,27)),('C',(20,32),(31,33),(25,32))])
self.add_line('arm',(26,37),(18,42))
self.relate('connect','torso','bent-leg'); self.relate('connect','torso','arm')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(1,'SQUARE','Rejected diagonal stick and pole omit the lifted arms and fabric. Restore a standing lunge with raised arms and two hanging fabric edges.', '''
self.circle('head',22,14,4)
self.add_bezier('torso',(22,26),((22,29),(21,31),(18,34)))
self.add_polyline('left-leg',(18,34),(8,42),(6,42))
self.add_polyline('right-leg',(18,34),(27,36),(27,42))
self.add_polyline('arms',(22,26),(34,22),(34,6))
self.add_line('fabric',(42,6),(42,28))
self.relate('connect','torso','left-leg','right-leg','arms')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(2,'HRECT_L','Rejected straight bar merges the rifle and arms and looks like pointing. Separate the shoulder stock, barrel and bent supporting arm; retain an aiming stance.', '''
self.circle('head',12,12,4)
self.add_line('torso',(12,24),(12,30))
self.add_polyline('legs',(4,40),(12,30),(22,40))
self.add_polyline('rifle',(12,24),(20,20),(44,20))
self.add_polyline('support-arm',(12,24),(23,30),(31,24))
self.add_line('sight',(40,16),(40,20))
self.relate('connect','torso','legs','rifle','support-arm'); self.relate('connect','rifle','sight')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add(3,'CIRCLE','Reviewer explicitly requests replacing three dot-like wells with circles. Enlarge each well to a clearly open 6-unit centerline diameter.', '''
self.path('palette',(24,44),[('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(36,32),8,8,True),('C',(34,40),(30,32),(38,36)),('C',(24,44),(31,42),(28,44))],True)
for n,(x,y) in enumerate(((17,16),(31,17),(15,30))): self.circle(f'well-{n}',x,y,3)
''','No paint wells omitted.','Lucide palette original and atomic-debug: continuous outer contour and inward thumb turn.')
add(4,'VRECT_L','Rejected tube lacks an eyepiece and objective; the support is a disconnected large hook. Restore eyepiece, tube, objective, curved arm, stage and pedestal.', '''
self.add_polyline('tube',(24,10),(32,14),(23,29),(15,25),closed=True)
self.add_polyline('eyepiece',(26,11),(30,4),(36,8),(32,14))
self.add_line('objective',(19,27),(16,32))
self.path('support',(32,16),[('C',(34,37),(44,21),(43,32)),('C',(24,39),(31,40),(27,40)),('L',(22,44))])
self.add_line('stage',(8,34),(25,34))
self.add_line('base',(14,44),(40,44))
self.relate('connect','tube','eyepiece','objective','support'); self.relate('connect','support','base')
''')
add(5,'SQUARE','Rejected worker is a floating head and hook; the sun lost rays and horizon. Restore rays, horizon, laptop display and a continuous seated back.', '''
self.add_arc('sun',(6,16),(20,16),radius_x=7,sweep=True)
self.add_line('ray-top',(13,6),(13,8))
self.add_line('ray-left',(6,8),(8,10))
self.add_line('horizon',(6,22),(20,22))
self.circle('head',35,15,5)
self.path('back',(35,28),[('C',(42,39),(41,28),(42,34)),('L',(36,39))])
self.add_polyline('laptop',(6,28),(25,28),(30,42),(11,42),closed=True)
self.add_dot('logo',(18,35))
''')
# Mowers share a deck with a sloped top, engine and genuine round wheels; handle direction follows each reference.
for i in (6,16,17):
 right=i==17
 body='''
self.circle('rear-wheel',11,35,7)
self.circle('front-wheel',38,37,5)
self.path('deck',(7,29),[('L',(7,27)),('C',(13,23),(7,24),(9,22)),('L',(37,28)),('C',(43,32),(41,29),(43,29))])
self.add_line('underdeck',(18,37),(33,37))
self.path('engine',(19,24),[('L',(19,19)),('A',(22,16),3,3,True),('L',(28,16)),('A',(31,19),3,3,True),('L',(33,27))])
self.relate('connect','deck','rear-wheel','front-wheel','engine'); self.relate('connect','underdeck','rear-wheel','front-wheel')
'''
 if right:
  body='''
self.circle('wheel-left',10,36,6)
self.circle('wheel-right',34,36,6)
self.path('deck',(4,30),[('A',(10,24),6,6,True),('L',(34,24)),('L',(34,30))])
self.add_line('underdeck',(16,38),(28,38))
self.box('engine',12,16,26,24,3)
self.add_line('handle',(34,24),(44,8))
self.relate('connect','deck','wheel-left','wheel-right','engine','handle'); self.relate('connect','underdeck','wheel-left','wheel-right')
'''
 else: body += "\nself.path('handle',(12,23),[('L',(6,8)),('L',(4,8))])\nself.relate('connect','handle','deck')\n" if i==6 else "\nself.path('handle',(12,23),[('L',(8,12)),('C',(4,8),(7,9),(6,8))])\nself.relate('connect','handle','deck')\n"
 add(i,'HRECT_L','Rejected disconnected wheel struts and engine outline read as a cart. Restore a continuous mower deck, underbody and engine, keeping the reference handle direction.',body,ref='Lucide car original and atomic-debug: coherent chassis and round wheels; mower form from original.')
add(7,'VRECT_L','Rejected angular mark loses the shark body and hammer-shaped head. Restore a broad transverse head, smooth arched body, dorsal fin and forked tail.', '''
self.path('shark',(10,22),[('C',(24,4),(10,13),(16,5)),('L',(30,9)),('L',(24,13)),('C',(33,19),(28,15),(31,17)),('L',(40,15)),('L',(37,26)),('C',(35,38),(39,31),(40,35)),('C',(23,44),(32,42),(27,44)),('L',(26,36)),('L',(17,33)),('C',(28,31),(24,35),(28,34)),('C',(20,22),(28,27),(22,29)),('L',(17,17)),('L',(14,26)),('L',(10,22))],True)
''')
add(8,'HRECT_L','Rejected hand has a tiny thumb bump and merged curled fingers. Restore a raised diagonal thumb, long left index and three clear curled-finger levels.', '''
self.path('hand',(23,18),[('C',(24,8),(17,13),(19,8)),('C',(31,12),(27,8),(29,10)),('L',(39,20)),('C',(44,28),(43,24),(44,25)),('L',(44,31)),('A',(35,40),9,9,True),('L',(20,40)),('A',(20,32),4,4,True),('L',(27,32))])
self.path('index',(23,18),[('L',(8,18)),('A',(8,26),4,4,False),('L',(25,26))])
self.path('middle',(18,26),[('A',(18,33),4,4,False),('L',(24,33))])
self.relate('connect','hand','index');self.relate('connect','index','middle');self.relate('connect','middle','hand')
''',ref='Lucide hand original and atomic-debug: rounded finger ends and continuous palm.')
add(9,'HRECT_M','Rejected silhouette resembles a generic bear and omits feline spots and tail. Add a slender feline body, longer muzzle, bent rear hock, curling tail and spots.', '''
self.path('cat',(8,24),[('C',(15,17),(8,18),(10,17)),('L',(29,17)),('L',(31,10)),('L',(35,13)),('L',(40,14)),('L',(44,19)),('L',(41,24)),('L',(36,23)),('C',(31,28),(33,24),(31,25)),('L',(31,38)),('L',(37,38))])
self.path('belly',(31,28),[('C',(19,28),(27,30),(23,30)),('L',(16,33)),('L',(17,38)),('L',(10,38)),('L',(8,28)),('L',(8,24))])
self.path('tail',(8,24),[('C',(4,15),(3,25),(4,20))])
for n,(x,y) in enumerate(((16,22),(24,23),(32,19))): self.add_dot(f'spot-{n}',(x,y))
self.relate('connect','cat','belly','tail')
''','Three spots retained as species cue; minor coat texture omitted.')
add(10,'SQUARE','Rejected polygon bowl and flat lid do not match a cooking pot. Restore rounded deep pot, dome lid, knob, side handles and curved rising steam.', '''
self.path('pot',(10,26),[('L',(12,36)),('C',(18,42),(13,40),(14,42)),('L',(30,42)),('C',(36,36),(34,42),(35,40)),('L',(38,26))])
self.path('lid',(6,26),[('C',(24,18),(8,21),(15,18)),('C',(42,26),(33,18),(40,21))])
self.add_line('rim',(6,26),(42,26))
self.add_arc('knob',(21,18),(27,18),radius_x=3,sweep=True)
self.add_line('handle-left',(6,30),(10,30));self.add_line('handle-right',(38,30),(42,30))
for x in (19,29): self.path(f'steam-{x}',(x,12),[('C',(x+2,6),(x-3,10),(x+4,9))])
self.relate('connect','pot','rim','lid','handle-left','handle-right');self.relate('connect','lid','knob','rim')
''')
for i in (11,12):
 add(i,'VRECT_M','Rejected broad mushroom-shaped bulb loses the tall rounded glass and tapered neck. Restore a tall globe, smoothly tapered shoulders and rounded base.', '''
self.path('glass',(17,35),[('C',(14,26),(17,31),(16,30)),('C',(10,18),(11,22),(10,20)),('A',(38,18),14,14,True),('C',(34,26),(38,20),(37,22)),('C',(31,35),(32,30),(31,31)),('L',(17,35))],True)
self.path('base',(17,35),[('L',(17,38)),('A',(23,44),6,6,False),('L',(25,44)),('A',(31,38),6,6,False),('L',(31,35))])
self.relate('connect','glass','base')
''','No defining silhouette omitted.')
add(13,'HRECT_M','Rejected short high cabin reads as a normal car. Stretch the cabin, lower the body, reduce wheel dominance and retain the center window divider.', '''
self.circle('wheel-left',11,33,5);self.circle('wheel-right',37,33,5)
self.path('body',(6,33),[('L',(4,33)),('L',(4,25)),('A',(8,21),4,4,True),('L',(11,21)),('L',(19,10)),('L',(30,10)),('L',(39,21)),('L',(40,21)),('A',(44,25),4,4,True),('L',(44,33)),('L',(42,33))])
self.add_line('sill',(16,33),(32,33));self.add_line('windows',(11,21),(39,21));self.add_line('divider',(25,10),(25,21))
self.relate('connect','body','wheel-left','wheel-right','windows','divider');self.relate('connect','windows','divider');self.relate('connect','sill','wheel-left','wheel-right')
''',ref='Lucide car original and atomic-debug: wheels sit in a continuous low chassis.')
add(14,'SQUARE','Rejected two diagonal rings read as a chain link. Restore two hanging circular cuff housings, inset wrist openings, and a top suspension ring.', '''
self.circle('link',24,10,4)
for n,x in [('left',14),('right',34)]:
 self.circle(n+'-cuff',x,32,10);self.circle(n+'-opening',x,32,5)
self.add_line('chain-left',(21,13),(15,22)); self.add_line('chain-right',(27,13),(33,22))
self.relate('connect','link','chain-left','chain-right');self.relate('connect','chain-left','left-cuff');self.relate('connect','chain-right','right-cuff')
''','Double rings and suspension preserved; tiny housing shoulders simplified.')
add(15,'SQUARE','Rejected little hanging zigzag and U shapes do not show pulling a towel. Restore a broad dispenser, hanging sheet with torn edge, and two gripping hands.', '''
self.box('dispenser',6,6,42,23,4)
self.path('sheet',(14,21),[('L',(14,38)),('L',(17,42)),('L',(21,39)),('L',(25,42)),('L',(29,39)),('L',(34,42)),('L',(34,21))])
self.add_line('slot',(14,21),(34,21))
self.path('left-hand',(6,42),[('L',(6,33)),('C',(10,29),(6,31),(8,30)),('L',(14,27)),('L',(14,33)),('L',(19,30))])
self.path('right-hand',(42,42),[('L',(42,33)),('C',(38,29),(42,31),(40,30)),('L',(34,27)),('L',(34,33)),('L',(29,30))])
self.relate('connect','dispenser','sheet','slot'); self.relate('connect','sheet','left-hand','right-hand','slot')
''','Two grips retained; tiny dispenser sensor omitted.', 'Lucide hand: bent fingers and round joints; dispenser and sheet from original.')
add(18,'HRECT_L','Rejected tiny spaced rings read as an abstract triangular symbol. Enlarge the eggs and stack them into a compact mound with visible circular interiors.', '''
r=6
for n,(x,y) in enumerate(((24,14),(16,25),(32,25),(10,36),(24,36),(38,36))): self.circle(f'egg-{n}',x,y,r)
''','All six eggs retained; deliberate close packing preserves a pile of caviar.')
add(19,'HRECT_L','Rejected chassis reads as a simple bicycle/cart. Restore ATV engine body, concave saddle, high steering handle and heavy wheels with hubs.', '''
self.circle('rear-wheel',12,32,8);self.circle('front-wheel',36,32,8)
self.add_dot('rear-hub',(12,32));self.add_dot('front-hub',(36,32))
self.path('body',(4,26),[('L',(4,20)),('L',(17,20)),('C',(26,20),(17,28),(26,28)),('L',(36,20)),('A',(42,26),6,6,True)])
self.add_line('underbody',(20,34),(28,34))
self.add_polyline('handle',(34,20),(29,8),(23,8))
self.relate('connect','body','rear-wheel','front-wheel','handle');self.relate('connect','underbody','rear-wheel','front-wheel')
''',ref='Lucide car original and atomic-debug: independent circular wheels and connected chassis; ATV saddle from original.')

def author(i,version=1):
 x=claims[i]; s=specs[i]; source=Path(x['ref']); uid=re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$',source.stem).group();concept=source.stem[:-(len(uid)+1)]
 run=Path('icon_set/work/primitive-make-ray')/uid/f'20260929T041010Z-fix-{i:02d}-r{version}'
 run.mkdir(parents=True,exist_ok=False)
 metadata=dict(concept=concept,source_uuid=uid,reference_path=x['ref'],icon_id=x['id'],author='gpt-6',feedback=x['feedback'],comparison=s['comparison'])
 (run/(x['id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
 (run/'review-before.txt').write_text(s['comparison']+'\nFeedback: '+x['feedback'])
 module=run/(x['id'].replace('-','_')+'_'+uid.replace('-','_')+'.py')
 header=f'''"""{s['comparison']}"""\nfrom icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.keyshapes import Keyshape\nSOURCE_ICON_ID={uid!r}\nSOURCE_PATH={x['ref']!r}\nAUTHOR='gpt-6'\nPLAN={s['comparison']!r}\nCONSTRUCTION_REFERENCE={s['construction']!r}\nOMISSIONS={s['omissions']!r}\nclass Drawing(Solo48):\n    icon_id={x['id']!r}\n    keyshape=Keyshape.{s['keyshape']}\n    semantic_role='MAIN'\n    semantic_kind='noun'\n    category='objects/general'\n    aliases=()\n    keywords=()\n'''
 module.write_text(header+helpers+'\n    def build(self):\n'+textwrap.indent(s['body'],'        ')+'\n')
 return run,module,metadata

def export(run,module,metadata):
 icon=load_icon(module);r=icon.validate_icon();svg=icon.to_svg();(run/(icon.icon_id+'.svg')).write_text(svg);(run/'validation.txt').write_text(r.describe());render_previews(svg,icon.icon_id,48,run)
 print(metadata['icon_id'],r.status,len(r.errors),len(r.warnings),flush=True)
 for e in list(r.errors)+list(r.warnings): print(' ',e,flush=True)
 return dict(run=str(run),module=str(module),metadata=metadata,status=r.status)
if __name__=='__main__':
 results=[]
 for i in range(20):
  run,module,md=author(i);results.append(export(run,module,md))
 (B/'drafts.json').write_text(json.dumps(results,indent=2))
