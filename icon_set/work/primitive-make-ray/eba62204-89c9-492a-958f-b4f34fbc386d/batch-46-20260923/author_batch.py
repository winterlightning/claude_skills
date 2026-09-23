"""Ordered standalone SOLO48 authoring for TODO batch 46."""
from pathlib import Path
import json,textwrap,importlib.util,traceback,cairosvg
from PIL import Image,ImageOps
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='eba62204-89c9-492a-958f-b4f34fbc386d'
SOURCE_PATH='icon_set/work/todo-references/square dot top_eba62204-89c9-492a-958f-b4f34fbc386d.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'batch-inputs.json').read_text())
HELPERS='''
    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def magnifier(self):
        # The handle node (30,33) is exactly radius 15 from (21,21).
        pts=[(6,21),(21,6),(36,21),(30,33),(6,21)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'lens-{i}',a,b,radius_x=15)
        self.add_contour('lens',*(f'lens-{i}' for i in range(4)),closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','lens','handle')

    def score(self,y):
        self.add_arc('two-top',(12,y+4),(20,y+4),radius_x=4)
        self.add_polyline('two-bottom',(20,y+4),(12,y+12),(20,y+12));self.relate('connect','two-top','two-bottom')
        for i,cy in enumerate((y+3,y+11)):self.add_dot(f'colon-{i}',(25,cy))
        self.box('zero',31,y,8,12,4)

    def terminal(self):
        self.box('screen',6,6,36,28,3)
        self.add_line('stand',(24,34),(24,42));self.relate('connect','screen','stand')
        self.add_polyline('foot',(16,42),(24,42),(32,42));self.relate('connect','stand','foot')
        for i,y in enumerate((18,26)):self.add_line(f'equals-{i}',(31,y),(35,y))

    def send(self,direction):
        self.box('panel',6,6,36,36,4)
        if direction=='left':
            self.add_polyline('head',(23,17),(16,24),(23,31));self.add_line('shaft',(16,24),(33,24))
        else:
            self.add_polyline('head',(25,17),(32,24),(25,31));self.add_line('shaft',(32,24),(15,24))
        self.relate('connect','head','shaft')
'''
DESIGNS=[('SQUARE', 'Rounded square with a hollow circular tab interrupting its top edge.', 'Source silhouette; circular tab and equal corner arcs.', 'Frame is shortened vertically to accommodate the circular top tab.', "self.add_polyline('top-left',(10,14),(18,14))\nself.add_arc('corner-tl',(6,18),(10,14),radius_x=4)\nself.add_line('left',(6,18),(6,38))\nself.add_arc('corner-bl',(6,38),(10,42),radius_x=4,sweep=False)\nself.add_line('bottom',(10,42),(38,42))\nself.add_arc('corner-br',(38,42),(42,38),radius_x=4,sweep=False)\nself.add_line('right',(42,38),(42,18))\nself.add_arc('corner-tr',(42,18),(38,14),radius_x=4,sweep=False)\nself.add_line('top-right',(38,14),(30,14))\nself.circle('tab',24,12,6)\nself.relate('connect','tab','top-left');self.relate('connect','tab','top-right')\n"), ('SQUARE', 'Rounded square containing the downward arrow actually shown in the source.', 'Lucide arrow-down: shaft and symmetric chevron.', 'Filename direction differs from the picture; preserve the picture.', "self.box('frame',6,6,36,36,4)\nself.add_line('shaft',(24,15),(24,33))\nself.add_polyline('head',(16,25),(24,33),(32,25));self.relate('connect','shaft','head')"), ('SQUARE', 'Rounded square containing the downward arrow actually shown in the source.', 'Lucide arrow-down: shaft and symmetric chevron.', 'Filename direction differs from the picture; preserve the picture.', "self.box('frame',6,6,36,36,4)\nself.add_line('shaft',(24,15),(24,33))\nself.add_polyline('head',(16,25),(24,33),(32,25));self.relate('connect','shaft','head')"), ('SQUARE', 'Square frame containing an envelope with flap and lower folds.', 'Lucide mail: rectangular envelope with centered flap.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('envelope',(15,17),(33,17),(33,31),(15,31),closed=True)\nself.add_polyline('flap',(15,17),(24,24),(33,17));self.relate('connect','envelope','flap')\nfor name,a,b in [('l',(15,31),(20,21)),('r',(33,31),(28,21))]:\n self.add_line(name,a,b);self.relate('connect','envelope',name);self.relate('connect','flap',name)"), ('SQUARE', 'Square frame containing an empty speech bubble with a lower-left tail.', 'Lucide message-square: coherent outline and integrated tail.', 'Rounded inner corners reduced to round joins; source bubble retained despite letter filename.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('bubble',(15,15),(33,15),(33,29),(24,29),(19,34),(19,29),(15,29),closed=True)"), ('SQUARE', 'Square containing a wine glass with rounded bowl, stem and foot.', 'Lucide wine: bowl, centered stem and horizontal foot.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('bowl-top',(16,21),(16,15),(32,15),(32,21))\nself.add_arc('bowl-bottom',(32,21),(16,21),radius_x=8);self.relate('connect','bowl-top','bowl-bottom')\nself.add_line('stem',(24,29),(24,34));self.relate('connect','bowl-bottom','stem')\nself.add_polyline('foot',(19,34),(24,34),(29,34));self.relate('connect','stem','foot')"), ('SQUARE', 'Square grid perimeter with eight inward ticks.', 'Source: mirrored short ticks on four sides.', 'None.', "self.box('frame',6,6,36,36,4)\nfor i,v in enumerate((18,30)):\n for name,a,b in [('top',(v,6),(v,12)),('bottom',(v,42),(v,36)),('left',(6,v),(12,v)),('right',(42,v),(36,v))]:\n  n=f'{name}-{i}';self.add_line(n,a,b);self.relate('connect','frame',n)"), ('SQUARE', 'Square with a symmetrical hollow heart.', 'Lucide heart: paired lobes and pointed base.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_bezier('heart',(24,19),((20,13),(14,15),(14,21)),((14,25),(20,30),(24,34)),((28,30),(34,25),(34,21)),((34,15),(28,13),(24,19)))"), ('SQUARE', 'Square enclosing a single vertical I stroke.', 'Source simple central vertical stroke.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_line('i',(24,15),(24,33))"), ('SQUARE', 'Square enclosing a lower-case information i.', 'Lucide info: detached dot over vertical stem.', 'Hollow source dot and outlined stem reduced to a solid dot and single stroke.', "self.box('frame',6,6,36,36,4)\nself.add_dot('dot',(24,16))\nself.add_line('stem',(24,25),(24,33))"), ('SQUARE', 'Square containing the right arrow shown in the source.', 'Lucide arrow-down construction rotated by authoring coordinates.', 'Source direction preserved despite square j filename.', "self.box('frame',6,6,36,36,4)\nself.add_line('shaft',(15,24),(33,24))\nself.add_polyline('head',(25,16),(33,24),(25,32));self.relate('connect','shaft','head')"), ('SQUARE', 'Broad left-pointing outlined arrow.', 'Source arrow silhouette; deliberate concave corners.', 'Rounded source bends use round joins.', "self.add_polyline('arrow',(6,24),(23,6),(23,16),(42,16),(42,32),(23,32),(23,42),closed=True)"), ('SQUARE', 'Square containing three evenly spaced horizontal lines.', 'Source repeated rules; shared length and 9-unit pitch.', 'None.', "self.box('frame',6,6,36,36,4)\nfor i,y in enumerate((15,24,33)):self.add_line(f'line-{i}',(15,y),(33,y))"), ('SQUARE', 'Square containing a padlock with round shackle and rectangular body.', 'Lucide lock: semicircular shackle and attached body.', 'None.', "self.box('frame',6,6,36,36,4)\nself.box('body',15,24,18,10,2)\nself.add_line('shackle-left',(18,24),(18,20))\nself.add_arc('shackle-top',(18,20),(30,20),radius_x=6)\nself.add_line('shackle-right',(30,20),(30,24))\nself.add_contour('shackle','shackle-left','shackle-top','shackle-right');self.relate('connect','body','shackle')"), ('SQUARE', 'Square portrait containing detached circular head and curved shoulders.', 'Human user.svg and Lucide user: centered head and mirrored shoulders.', 'Shoulders shortened to fit frame; exact head bottom24 to shoulder apex32 gives 4 ink units.', "self.box('frame',6,6,36,36,4)\nself.circle('head',24,19,5)\nself.add_arc('shoulders',(14,36),(34,36),radius_x=10,radius_y=4)"), ('SQUARE', 'Square containing a diagonally raised megaphone and rounded grip.', 'Lucide megaphone: widening cone and lower attached handle.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('cone',(15,28),(28,15),(34,29),(17,33),closed=True)\nself.add_bezier('grip',(19,33),((21,40),(28,38),(26,31)));self.relate('connect','cone','grip')"), ('SQUARE', 'Square containing a centered circular O.', 'Source circle: symmetric semicircular arcs.', 'None.', "self.box('frame',6,6,36,36,4)\nself.circle('o',24,24,9)"), ('SQUARE', 'Square containing a single-stroke uppercase P.', 'Lucide square-parking: upright stem and rounded upper bowl.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('stem',(18,33),(18,24),(18,15),(24,15))\nself.add_arc('bowl',(24,15),(24,25),radius_x=5)\nself.add_line('bar',(24,25),(18,25));self.relate('connect','stem','bowl');self.relate('connect','bowl','bar');self.relate('connect','stem','bar')"), ('SQUARE', 'Square containing a single-stroke R as actually pictured.', 'Lucide square-parking bowl construction plus diagonal R leg.', 'Source R retained despite parking slash filename.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('stem',(18,33),(18,24),(18,15),(24,15))\nself.add_arc('bowl',(24,15),(24,25),radius_x=5)\nself.add_line('bar',(24,25),(18,25));self.relate('connect','stem','bowl');self.relate('connect','bowl','bar');self.relate('connect','stem','bar')\nself.add_line('leg',(24,25),(33,33));self.relate('connect','bowl','leg');self.relate('connect','bar','leg')"), ('SQUARE', 'Square containing an outlined uppercase parking P.', 'Lucide square-parking: P structure; outlined form hand-authored from source.', 'None.', "self.box('frame',6,6,36,36,4)\nself.add_polyline('p-left',(16,34),(16,14),(24,14))\nself.add_arc('p-bowl',(24,14),(24,28),radius_x=7)\nself.add_polyline('p-foot',(24,28),(21,28),(21,34),(16,34))\nself.relate('connect','p-left','p-bowl');self.relate('connect','p-bowl','p-foot');self.relate('connect','p-foot','p-left')\nself.add_polyline('counter-left',(21,19),(24,19))\nself.add_arc('counter-round',(24,19),(24,23),radius_x=2)\nself.add_polyline('counter-bottom',(24,23),(21,23),(21,19))\nself.relate('connect','counter-left','counter-round');self.relate('connect','counter-round','counter-bottom');self.relate('connect','counter-bottom','counter-left')")]

def run():
 for row,(key,plan,refs,omissions,body) in zip(ROWS,DESIGNS):
  d=Path(row['result_dir']);p=d/(row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
  if (d/'result.json').exists():continue
  bounds=Keyshape[key].bounds_for(Profile.SOLO48)
  source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={row['source_uuid']!r}
SOURCE_PATH={row['reference_path']!r}
AUTHOR={AUTHOR!r}
PLAN={plan!r}
CONSTRUCTION_REFERENCES={refs!r}
OMISSIONS={omissions!r}
KEYSHAPE_INK_BOUNDS={bounds!r}

class Drawing(Solo48):
    icon_id={row['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(row['concept'].split())!r}
{HELPERS}
    def build(self):
{textwrap.indent(textwrap.dedent(body).strip(),'        ')}
'''
  p.write_text(source);rec={**row,'author':AUTHOR,'module':p.name,'keyshape':key,'keyshape_ink_bounds':bounds,'subject_and_plan':plan,'construction_references':refs,'omissions':omissions}
  try:
   spec=importlib.util.spec_from_file_location('batch46_'+row['source_uuid'],p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();report=icon.validate_icon();rec['validation_status']=report.status;(d/'validation.txt').write_text(report.describe());svg=icon.to_svg();(d/(row['icon_id']+'.svg')).write_text(svg)
   for size in (48,240):
    out=d/f'light-{size}.png';cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out),output_width=size,output_height=size,background_color='white');ImageOps.invert(Image.open(out).convert('RGB')).save(d/f'dark-{size}.png')
   print(row['concept'],report.describe(),flush=True)
  except Exception:
   rec['validation_status']='error';rec['error']=traceback.format_exc();(d/'validation.txt').write_text(rec['error']);print(row['concept'],rec['error'],flush=True)
  (d/'review-draft.json').write_text(json.dumps(rec,indent=2))

if __name__=='__main__':run()
