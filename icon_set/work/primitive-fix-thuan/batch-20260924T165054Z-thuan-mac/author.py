from pathlib import Path
import json,textwrap
SOURCE_ICON_ID = 'batch-see-per-icon-metadata'
SOURCE_PATH = 'batch.json'
AUTHOR = 'gpt-6'
ROOT=Path(__file__).resolve().parent
ROWS=json.loads((ROOT/'batch.json').read_text())
HELPERS='''
        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
DESIGNS={}
def put(key,shape,reference,plan,code,omissions='None'):
 DESIGNS[key]=(shape,reference,plan,textwrap.dedent(code),omissions)
put('curve-rise-dash-large-head','HRECT_L','move-up-right','Three coherent dashed curves lead to a vertical arrow; intentionally asymmetric winding trajectory.', '''
path('start',(4,12),[('C',(12,14),(7,10),(10,11))])
path('middle',(17,23),[('C',(18,31),(17,25),(17,28))])
path('bend',(25,39),[('C',(38,30),(32,43),(38,38))])
line('shaft',(38,21),(38,8))
poly('head',(32,14),(38,8),(44,14));join('shaft','head')
''','Short dash count reduced to preserve clean visible gaps.')
put('curved-saxophone','VRECT_L','music','U-shaped saxophone tube; nested circular bowls and tangent straight sides; diagonal bell remains asymmetric.', '''
path('sax',(8,4),[('A',(22,18),14,14,True),('L',(22,30)),('A',(32,30),5,5,False),('L',(32,16)),('L',(40,24)),('L',(40,30)),('A',(12,30),14,14,True),('L',(12,12))])
''','Tiny key ticks omitted for tube clearance.')
put('dill','VRECT_L','sprout','A gently leaning herb stem owns four alternating, smoothly swept branch attachments; natural asymmetry retained.', '''
path('stem',(24,44),[('C',(24,34),(24,40),(24,37)),('C',(25,24),(24,30),(24,27)),('C',(28,14),(26,20),(27,17)),('C',(33,4),(29,10),(31,7))])
path('left-low',(24,34),[('C',(12,27),(17,34),(13,31))]);join('left-low','stem')
path('right-low',(24,34),[('C',(40,24),(33,34),(39,30))]);join('right-low','stem');join('left-low','right-low')
path('left-high',(25,24),[('C',(8,12),(16,24),(9,18))]);join('left-high','stem')
path('right-high',(28,14),[('C',(40,7),(35,14),(39,10))]);join('right-high','stem')
''')
put('downward-reflection-diagram','HRECT_L','flip-vertical-2','Mirrored open triangles face a horizontal axis; a semicircular arrow expresses downward reflection.', '''
poly('upper',(4,8),(24,8),(14,16),closed=True)
poly('lower',(4,40),(24,40),(14,32),closed=True)
line('axis',(4,24),(24,24))
path('turn',(34,12),[('A',(44,24),10,12,True),('A',(34,36),10,12,True)])
poly('head',(34,28),(34,36),(42,36));join('head','turn')
''')
for key in ['earth-1','earth-1-maps']:
 put(key,'CIRCLE','earth','Circular rim with smooth west and east continent boundaries, split at exact rim attachments. Geographic asymmetry retained.', '''
path('rim',(24,4),[('A',(36,8),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
path('north',(24,4),[('C',(18,16),(24,11),(23,14)),('C',(4,24),(13,18),(7,18))])
path('south',(4,24),[('C',(20,30),(11,24),(20,24)),('C',(12,40),(20,34),(12,35))])
path('east',(36,8),[('C',(31,20),(32,12),(31,16)),('C',(44,24),(31,25),(38,24))])
for part in ['north','south','east']:join(part,'rim')
join('north','south')
''','Fine coastline detail omitted while keeping the three land boundaries.')
put('educative-toys-music','VRECT_L','music','Two equal circular notes share vertical stems and two precisely parallel beams; equal radii replace traced ovals.', '''
oval('left-note',14,38,6,6);oval('right-note',34,32,6,6)
path('beam',(20,38),[('L',(20,20)),('L',(20,10)),('L',(40,4)),('L',(40,14)),('L',(40,32))])
line('lower-beam',(20,20),(40,14))
join('left-note','beam');join('right-note','beam');join('lower-beam','beam')
''')
put('eggplant','HRECT_L','sprout','One broad curved fruit body joins an asymmetric leaf cap and diagonal stalk with shared nodes.', '''
path('body',(28,14),[('C',(14,22),(24,19),(21,22)),('C',(4,31),(8,22),(4,25)),('C',(15,40),(4,37),(9,40)),('C',(39,25),(24,40),(34,32))])
path('cap',(28,14),[('C',(40,10),(28,8),(36,8)),('C',(40,26),(45,13),(43,20)),('C',(34,16),(36,24),(34,20)),('C',(28,14),(31,17),(29,16))],True)
line('stalk',(40,10),(44,8));join('stalk','cap');join('body','cap')
''')
put('envelope-and-document-letter-batch-008-08','SQUARE','mail','Rounded envelope with an emerging folded-corner letter, one address line, and detached stamp; all contact points explicit.', '''
path('envelope',(12,24),[('L',(36,24)),('L',(39,24)),('A',(42,27),3,3,True),('L',(42,39)),('A',(39,42),3,3,True),('L',(9,42)),('A',(6,39),3,3,True),('L',(6,27)),('A',(9,24),3,3,True),('L',(12,24))],True)
poly('letter',(12,24),(12,6),(28,6),(36,14),(36,24));join('letter','envelope')
line('letter-text',(20,15),(26,15));line('address',(15,33),(22,33))
# A small circular seal keeps the stamp distinct at 48px.
oval('stamp',33,33,3,3)
''','Second address line omitted; stamp reduced to a circular postal seal for legibility.')
put('equalizer-audio','HRECT_L','sliders-vertical','Three equally sized circular controls on perfectly straight columns; same radius and shared cardinal joins.', '''
for name,x,y in [('left',8,22),('middle',24,32),('right',40,16)]:
    oval(name,x,y,4,4)
    line(name+'-top',(x,8),(x,y-4));line(name+'-bottom',(x,y+4),(x,40))
    join(name,name+'-top');join(name,name+'-bottom')
''')

def write(keys=None):
 for row in ROWS:
  key=row['icon_id']
  if key not in DESIGNS or keys and key not in keys:continue
  shape,ref,plan,body,omissions=DESIGNS[key]
  run=Path(row['result_dir']);f=run/(key.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
  text=f'''"""{key}: {plan}\nLucide construction: {ref}; original and atomic-debug inspected.\nOmissions: {omissions}\nKeyshape {shape}: exact contract envelope; 4-unit stroke.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {row['source_uuid']!r}\nSOURCE_PATH = {row['reference_path']!r}\nAUTHOR = 'gpt-6'\nclass Drawing(Solo48):\n    icon_id = {key!r}\n    keyshape = Keyshape.{shape}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'objects'\n    aliases = ()\n    keywords = {tuple(key.split('-'))!r}\n    def build(self):\n'''+HELPERS+textwrap.indent(body,'        ')
  f.write_text(text)
  (run/'design.json').write_text(json.dumps(dict(keyshape=shape,lucide=ref,plan=plan,omissions=omissions),indent=2))
if __name__=='__main__':write()
