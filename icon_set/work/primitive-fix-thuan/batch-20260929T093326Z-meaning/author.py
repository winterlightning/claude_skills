from pathlib import Path
import json,re,textwrap,datetime,sys,hashlib
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).parent
ITEMS=json.loads((BATCH/'items.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID={e['icon_id']:re.search(r'([0-9a-f-]{36})\.svg$',e['reference']).group(1) for e in ITEMS}
SOURCE_PATH={e['icon_id']:e['reference'] for e in ITEMS}
HELPERS='''
        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                eid=f"{name}-{j}"; kind=cmd[0]
                if kind=='L': self.add_line(eid,here,cmd[1]); end=cmd[1]
                elif kind=='B': self.add_bezier(eid,here,(cmd[1],cmd[2],cmd[3])); end=cmd[3]
                elif kind=='A':
                    end,rx,ry,sweep=cmd[1:];self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(eid);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x1,y1,x2,y2,r):
            path(name,(x1+r,y1),[('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True),('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True),('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True),('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)],True)
        def join(*names):
            for i,a in enumerate(names):
                for b in names[i+1:]:self.relate('connect',a,b)
'''
# Reference-first designs: each record contains the comparison and the symbol plan.
DESIGNS={
1:('VRECT_L','The rejected figure was walking on a line and lost the statue pedestal and angled flag. Restore an upright statue, plinth and leaning flag.','Standing figure and trapezoid plinth; angled flag with shared pole attachment.', '''
circle('head',15,8,4)
self.add_line('torso',(15,20),(15,29))
self.add_polyline('arms',(9,28),(9,22),(15,20),(21,23))
self.add_polyline('legs',(10,36),(15,29),(20,36))
self.add_polyline('plinth',(8,36),(25,36),(23,44),(10,44),closed=True)
self.add_line('pole',(26,36),(36,4))
self.add_polyline('flag',(36,4),(40,7),(37,17),(33,14))
join('torso','arms');join('torso','legs');join('legs','plinth');join('pole','flag')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
2:('SQUARE','The rejected icon drew an F, but the original is a speech bubble inside a square. Replace the letter with the source bubble and its downward tail.','Concentric rounded square and speech bubble, with one intentional tail.', '''
rect('frame',6,6,42,42,6)
path('bubble',(18,14),[('L',(30,14)),('A',(34,18),4,4,True),('L',(34,24)),('A',(30,28),4,4,True),('L',(26,28)),('L',(21,34)),('L',(21,28)),('L',(18,28)),('A',(14,24),4,4,True),('L',(14,18)),('A',(18,14),4,4,True)],True)
'''),
3:('SQUARE','The rejected arrow pointed diagonally. The original points straight down. Restore a centered vertical shaft and symmetric downward arrowhead.','Rounded square with centered downward arrow; arrowhead mirrored about x=24.', '''
rect('frame',6,6,42,42,6)
self.add_line('shaft',(24,15),(24,33))
self.add_polyline('arrowhead',(16,25),(24,33),(32,25))
join('shaft','arrowhead')
'''),
4:('SQUARE','The rejected ring was an angular slash cutting through a complete circle. Restore a curved elliptical orbital ring with occluded globe edges.','Two globe arcs and a continuous tilted orbital band; asymmetry follows the source perspective.', '''
path('globe-upper',(10,29),[('B',(4,18),(13,7),(24,7)),('B',(31,7),(36,11),(38,17))])
path('globe-lower',(17,39),[('B',(28,45),(40,34),(39,24))])
path('ring',(10,26),[('B',(6,29),(6,32),(6,35)),('B',(6,42),(26,32),(35,23)),('B',(42,16),(44,10),(40,9)),('B',(38,8),(35,9),(33,10))])
'''),
5:('SQUARE','The rejected airplane looked like a bent arrow. The reviewer specifically requested a plane. Restore an outlined fuselage, swept wings and tail above the food utensils.','Compact horizontal plane silhouette, then separated fork and knife; omit divider to give symbols breathing space.', '''
path('plane',(6,14),[('L',(10,20)),('L',(22,16)),('L',(20,22)),('L',(25,21)),('L',(30,13)),('L',(39,10)),('B',(44,8),(42,4),(38,6)),('L',(29,9)),('L',(19,6)),('L',(15,8)),('L',(22,12)),('L',(12,15)),('L',(9,12)),('L',(6,14))],True)
path('fork',(10,30),[('L',(10,34)),('A',(18,34),4,4,False),('L',(18,30))])
self.add_line('fork-stem',(14,38),(14,42));join('fork','fork-stem')
path('knife',(32,42),[('L',(32,30)),('B',(38,32),(38,35),(38,37)),('L',(32,37))])
'''),
6:('SQUARE','The rejected airplane looked like a bent arrow. The reviewer specifically requested a plane. Restore an outlined airplane above a recognizable stemmed cocktail glass.','Outlined swept-wing plane and wide bowl on a centered stem; omit divider and garnish to protect clarity.', '''
path('plane',(6,14),[('L',(10,20)),('L',(22,16)),('L',(20,22)),('L',(25,21)),('L',(30,13)),('L',(39,10)),('B',(44,8),(42,4),(38,6)),('L',(29,9)),('L',(19,6)),('L',(15,8)),('L',(22,12)),('L',(12,15)),('L',(9,12)),('L',(6,14))],True)
path('glass',(14,30),[('L',(34,30)),('A',(24,38),10,8,True),('A',(14,30),10,8,True)],True)
self.add_line('stem',(24,38),(24,44));self.add_line('foot',(18,44),(30,44));join('glass','stem');join('stem','foot')
'''),
7:('SQUARE','The rejected desk was a heavy low bar and the man had a tiny head. Restore a larger head and broad shoulders behind a complete counter with visible legs.','Centered round head, smooth shoulders and rounded desk; symmetric geometry.', '''
circle('head',24,12,6)
path('shoulders',(13,30),[('B',(13,27),(18,26),(24,26)),('B',(30,26),(35,27),(35,30))])
rect('desk',6,30,42,38,2)
self.add_line('left-leg',(10,38),(10,42));self.add_line('right-leg',(38,38),(38,42))
join('shoulders','desk');join('desk','left-leg');join('desk','right-leg')
'''),
8:('SQUARE','The rejected scene replaced the full sun with a sunrise and omitted the cloud. Restore a centered person beneath a cloud and a complete radiant sun.','Cloud at upper left, sun at upper right, centered round head and open bust; no horizon clutter.', '''
path('cloud',(9,17),[('A',(6,11),4,4,True),('A',(16,9),5,5,True),('A',(19,17),4,4,True),('L',(9,17))],True)
circle('sun',35,12,4)
for name,a,b in [('top',(35,4),(35,5)),('right',(42,12),(44,12)),('lower',(35,19),(35,20)),('upper-right',(41,6),(42,5))]:self.add_line(name,a,b)
circle('head',24,26,5)
path('bust',(12,44),[('B',(12,39),(18,39),(24,39)),('B',(30,39),(36,39),(36,44))])
'''),
9:('SQUARE','The rejected gun faced away from the head and the person was incomplete. Restore a left-facing pistol beside a full bust with headshot reaction marks.','Large round head at left, open shoulders, clearly left-facing pistol at right, two reaction rays.', '''
circle('head',14,17,7)
path('bust',(6,42),[('B',(6,33),(9,32),(14,32)),('B',(19,32),(24,33),(24,42))])
self.add_polyline('pistol',(28,13),(42,13),(42,21),(39,21),(41,31),(34,31),(32,21),(28,21),closed=True)
self.add_line('ray-top',(14,6),(14,7));self.add_line('ray-right',(23,8),(25,6))
'''),
10:('SQUARE','The rejected figure stood upright beside an abstract bowl. Restore a forward-bent torso, head over the bubbler, cupped arm and pedestal fountain.','Leaning person at left and wall-like pedestal fountain at right; head aligned to upper torso with 5-12-13 gap.', '''
circle('head',25,11,5)
path('torso',(13,16),[('B',(8,18),(10,26),(10,31))])
self.add_polyline('legs',(6,42),(10,31),(19,42))
self.add_polyline('arm',(13,16),(17,29),(25,29))
path('basin',(30,31),[('L',(42,31)),('L',(42,39)),('B',(34,39),(30,36),(30,31))],True)
self.add_line('pedestal',(42,39),(42,42))
path('water',(32,25),[('A',(42,25),5,5,True)])
join('torso','legs');self.relate('connect','torso','arm');join('basin','pedestal')
self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
'''),
}

def author(indices,tag='a'):
 out=[]
 for i in indices:
  e=ITEMS[i-1];key,notes,plan,code=DESIGNS[i];uid=SOURCE_ICON_ID[e['icon_id']]
  stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
  run=Path('icon_set/work/primitive-make-ray')/uid/(stamp+'-meaning-'+tag);run.mkdir(parents=True)
  metadata={'concept':Path(e['reference']).stem[:-37],'source_uuid':uid,'reference_path':e['reference']}
  (run/(e['icon_id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
  (run/'comparison.md').write_text(notes+'\nFeedback: '+e['feedback']+'\nPlan: '+plan+'\n')
  module=run/(e['icon_id'].replace('-','_')+'_'+uid.replace('-','_')+'.py')
  header=f'''from icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\nSOURCE_ICON_ID = {uid!r}\nSOURCE_PATH = {e['reference']!r}\nAUTHOR = {AUTHOR!r}\n# Symbol plan: {plan}\n# Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg.\n\nclass Drawing(Solo48):\n    icon_id = {e['icon_id']!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = ()\n\n    def build(self):\n'''
  module.write_text(header+HELPERS+textwrap.indent(textwrap.dedent(code).strip(),'        ')+'\n')
  icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
  (run/(e['icon_id']+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe())
  render_previews(svg,e['icon_id'],48,run)
  g=gate(module);(run/'gate.json').write_text(json.dumps(g,indent=2))
  print(i,e['icon_id'],report.status,g['status'],len(g['errors']),len(g['warnings']),flush=True)
  record={**e,**metadata,'run':str(run),'module':str(module),'notes':notes,'plan':plan,'author':AUTHOR,'gate':g}
  out.append(record)
 (BATCH/f'runs-{tag}.json').write_text(json.dumps(out,indent=2))
 return out
if __name__=='__main__':author([int(s) for s in sys.argv[1:]])
