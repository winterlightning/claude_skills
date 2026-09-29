from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).parent
ROWS=json.loads((BATCH/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['source_uuid'] for r in ROWS]
SOURCE_PATH=[r['reference_path'] for r in ROWS]
def circle(x,y,r): return f'M {x-r} {y} A {r} {r} 1 {x+r} {y} A {r} {r} 1 {x-r} {y} Z'
def rect(x,y,w,h,r=2):return f'M {x+r} {y} L {x+w-r} {y} A {r} {r} 1 {x+w} {y+r} L {x+w} {y+h-r} A {r} {r} 1 {x+w-r} {y+h} L {x+r} {y+h} A {r} {r} 1 {x} {y+h-r} L {x} {y+r} A {r} {r} 1 {x+r} {y} Z'
D={}
def add(i,key,wrong,change,paths,ref='truck',flags=None):D[i]=dict(keyshape=key,wrong=wrong,change=change,paths=paths,lucide=ref,flags=flags or [])
add(0,'HRECT_L','The house became the truck body, with a blocked doorway and almost no distinct cab.','Separate a left-facing cab, flatbed and full house with open doorway.',{
 'roof':'M 18 18 L 31 8 L 44 18','house':'M 21 16 L 21 29 L 41 29 L 41 16','door':'M 28 29 L 28 24 A 3 3 1 34 24 L 34 29',
 'cab':'M 9 34 L 4 34 L 4 27 L 8 21 L 16 21 L 16 34','window':'M 4 27 L 10 27', 'bed':'M 16 29 L 44 29 L 44 34 L 39 34','axle':'M 19 35 L 29 35','wheel-front':circle(14,35,5),'wheel-rear':circle(34,35,5)})
add(1,'HRECT_L','The cab lacked a window and the cargo outline did not close, weakening the medical truck silhouette.','Restore a tall medical box, windshield and two round wheels.',{
 'box':'M 4 32 L 4 8 L 27 8 L 27 32','cross-h':'M 11 19 L 20 19','cross-v':'M 15 15 L 15 24','cab':'M 27 16 L 36 16 L 44 26 L 44 33 L 40 33','window':'M 33 17 L 33 25 L 43 25','axle':'M 17 35 L 30 35','rear':circle(12,35,5),'front':circle(35,35,5)})
add(2,'HRECT_L','The house sits on a shallow tray and the disconnected dot wheels do not describe a moving truck.','Restore a box truck with a house symbol above the cargo box and attached outlined wheels.',{
 'house':'M 7 17 L 7 11 L 14 6 L 21 11 L 21 17 Z','door':'M 14 17 L 14 13','box':'M 4 21 L 28 21 L 28 34 L 18 34','back':'M 4 21 L 4 34 L 7 34','cab':'M 28 25 L 36 25 L 44 31 L 44 35 L 40 35','window':'M 34 25 L 34 30 L 42 30','axle':'M 17 36 L 30 36','rear':circle(12,36,4),'front':circle(35,36,4)})
add(3,'SQUARE','The cab was too compressed and the ribbon crowded the box, making the vehicle hard to distinguish.','Open the cab and windshield, keep a clear gift box and two generous bow loops.',{
 'box':'M 18 17 L 42 17 L 42 36 L 39 36','box-left':'M 18 17 L 18 36 L 15 36','ribbon':'M 30 17 L 30 35','lid':'M 18 23 L 42 23',
 'bow-left':'M 30 17 C 25 5 19 4 18 10 C 17 14 22 17 30 17 Z','bow-right':'M 30 17 C 35 5 41 4 42 10 C 43 14 38 17 30 17 Z',
 'cab':'M 18 25 L 11 25 C 8 25 6 29 6 32 L 6 37 L 8 37','window':'M 6 32 L 12 32','base':'M 16 38 L 29 38','front':circle(12,38,4),'rear':circle(34,38,4)},'gift')
add(4,'SQUARE','The receiver was an abstract bent stroke without recognizable earpieces.','Restore a contoured telephone receiver inside the answer speech bubble.',{
 'bubble':'M 14 6 L 34 6 A 8 8 1 42 14 L 42 29 A 8 8 1 34 37 L 21 37 L 12 44 L 12 37 C 8 36 6 33 6 29 L 6 14 A 8 8 1 14 6 Z',
 'receiver':'M 16 14 L 21 19 L 18 22 C 20 26 22 28 26 30 L 29 27 L 34 31 C 31 37 24 34 18 28 C 12 22 11 17 16 14 Z'},'phone')
add(5,'VRECT_L','The front became a box on three sticks; the pair of headlights and front tire were lost.','Restore the tapered roof, wide windshield, two headlights and three visible tires.',{
 'roof':'M 12 15 L 15 6 A 3 3 1 18 4 L 30 4 A 3 3 1 33 6 L 36 15','body':'M 12 15 L 36 15 L 36 33 C 36 36 34 37 29 37 M 19 37 C 14 37 12 36 12 33 L 12 15',
 'windshield':'M 12 23 L 36 23','left-lamp':circle(18,29,2),'right-lamp':circle(30,29,2),'tire':rect(21,35,6,9,3),
 'left-wheel':'M 12 29 L 8 29 L 8 41 A 3 3 0 14 41 L 14 37','right-wheel':'M 36 29 L 40 29 L 40 41 A 3 3 1 34 41 L 34 37'},'truck')
add(6,'SQUARE','The disconnected head and single dangling stroke lost the inverted torso and supporting arms.','Draw an inverted figure with raised split legs, curved torso and two distinct supporting arms; exact head gap 4.',{
 'head':circle(37,30,5),'torso':'M 24 30 C 20 30 18 25 18 22','leg-left':'M 18 22 L 6 7','leg-right':'M 18 22 L 24 6','arm-left':'M 21 29 L 13 34 L 10 42','arm-right':'M 24 30 L 26 41'},'human_ref/full_body_ref.png',[('person','head','torso-1','start')])
add(7,'SQUARE','A tiny square screen and one button made the TV resemble a camera.','Restore a large inset screen, paired tuning knobs, aerial and feet.',{
 'cabinet':rect(6,14,36,24,4),'screen':rect(11,19,20,14,3),'knob-top':circle(36,23,2),'knob-bottom':circle(36,31,2), 'antenna':'M 16 6 L 24 14 L 32 6','foot-left':'M 12 38 L 12 42','foot-right':'M 36 38 L 36 42'},'tv')
add(8,'HRECT_L','A flat-bottomed arch and sharp M replaced the rounded hill and lower curved mountain outline.','Restore the domed emblem, bowl-shaped base and two gently rounded unequal peaks.',{
 'outline':'M 4 32 C 4 24 13 8 24 8 C 35 8 44 24 44 32 C 44 43 4 43 4 32 Z','peaks':'M 6 35 L 14 23 C 16 20 18 23 20 25 C 22 28 23 27 25 24 L 29 19 C 31 17 33 20 35 22 L 42 34'},'none')
add(9,'HRECT_L','The squared vertical prongs and hemispherical bowl missed the nasal device angled inserts and shaped bridge.','Restore two outward-angled soft prongs above a shallow curved bridge and lower shell.',{
 'left-prong':'M 11 24 L 14 10 C 15 7 21 8 21 11 L 18 25','right-prong':'M 30 25 L 27 11 C 27 8 33 7 34 10 L 37 24',
 'shell':'M 4 24 C 4 20 10 23 15 24 C 20 26 28 26 33 24 C 38 23 44 20 44 24 C 44 34 35 40 24 40 C 13 40 4 34 4 24 Z','seam':'M 10 35 C 19 29 29 29 38 35'},'none')
# Append the remaining ten designs below.
add(10,'SQUARE','The rear money bag became a small rectangular tag, and the dollar was an indistinct thick stroke.','Restore two rounded tied bags in depth, scalloped open tops and a clear dollar on the front bag.',{
 'front':'M 23 15 C 18 20 14 28 14 33 C 14 40 20 42 29 42 C 38 42 42 39 42 33 C 42 28 37 20 33 15 L 37 7 C 33 9 32 3 28 7 C 24 3 23 9 19 7 L 23 15 Z',
 'tie':'M 23 15 L 33 15','rear':'M 12 36 C 3 36 4 24 11 17 L 8 11 L 13 12 L 16 9 L 20 12','dollar':'M 33 24 L 27 24 C 22 24 22 29 28 29 C 34 29 34 35 28 35 L 23 35','bar':'M 28 21 L 28 38'},'none')
add(11,'HRECT_L','Two tiny rigid stick bodies and an oversized diagonal line obscured the raised-arm interaction.','Use matched heads and coherent standing bodies, with one arm visibly raised toward the other person.',{
 'head-a':circle(14,12,4),'head-b':circle(36,12,4),'torso-a':'M 14 24 L 14 31','torso-b':'M 36 24 L 36 31','left-arm':'M 14 24 L 8 24 L 4 29','raised-arm':'M 14 24 L 23 24 L 27 12','right-arms':'M 29 29 L 31 24 L 36 24 L 41 24 L 44 29','legs-a':'M 8 40 L 14 31 L 20 40','legs-b':'M 30 40 L 36 31 L 42 40'},'human_ref/full_body_ref.png',[('person-a','head-a','torso-a-1','start'),('person-b','head-b','torso-b-1','start')])
add(12,'SQUARE','Both beans became flat horizontal capsules with no kidney indentation or diagonal arrangement.','Restore two plump asymmetric kidney forms with inward notches and a diagonal upper bean.',{
 'upper':'M 15 14 C 15 9 22 11 25 10 C 31 9 33 4 38 7 C 46 14 39 22 29 25 C 19 28 11 23 15 14 Z','upper-notch':'M 15 14 C 21 15 25 13 25 10',
 'lower':'M 6 31 C 10 25 15 29 20 30 C 26 31 33 27 34 34 C 35 41 23 44 13 41 C 7 40 3 36 6 31 Z','lower-notch':'M 6 31 C 11 35 16 34 20 30'},'bean')
add(13,'VRECT_L','The biscuits were empty rounded bars, losing the characteristic baked grooves.','Restore a pair of broad rounded biscuits with a flowing central groove in each.',{
 'biscuit-a':rect(8,4,12,40,6),'biscuit-b':rect(28,4,12,40,6),'groove-a':'M 14 14 C 11 21 17 27 14 35','groove-b':'M 34 14 C 31 21 37 27 34 35'},'none')
add(14,'HRECT_L','Both bells stood upright with flat bases and stick clappers instead of outward tilt.','Angle two bell bodies away from their shared crown; use slanted rims and curved clappers.',{
 'left':'M 24 15 C 23 7 15 6 11 12 C 8 17 11 22 4 29 L 23 35 C 20 29 20 25 23 19 C 24 17 24 16 24 15 Z',
 'right':'M 24 15 C 25 7 33 6 37 12 C 40 17 37 22 44 29 L 25 35 C 28 29 28 25 25 19 C 24 17 24 16 24 15 Z',
 'clapper-left':'M 10 31 C 8 38 14 42 17 34','clapper-right':'M 38 31 C 40 38 34 42 31 34'},'bell')
add(15,'SQUARE','The rear display was an open bracket with a hanging stub; neither overlap nor its stand was clear.','Restore two offset rounded monitors, a rear stand and front display bezel.',{
 'rear':'M 15 25 L 9 25 A 3 3 1 6 22 L 6 9 A 3 3 1 9 6 L 25 6 A 3 3 1 28 9 L 28 16','rear-stem':'M 12 25 L 12 31','rear-base':'M 6 31 L 15 31',
 'front':rect(18,19,24,17,3),'bezel':'M 18 30 L 42 30','stem':'M 30 36 L 30 42','base':'M 24 42 L 36 42'},'monitor')
add(16,'SQUARE','The flattened circular socket recess was omitted and the ground opening became a solid dot.','Restore the outlet plate, flattened round recess, vertical slots and arch-shaped ground opening.',{
 'plate':rect(6,6,36,36,4),'recess':'M 18 12 L 30 12 C 40 19 40 30 31 37 L 17 37 C 8 30 8 19 18 12 Z','slot-left':'M 19 20 L 19 24','slot-right':'M 29 20 L 29 24','ground':'M 21 33 L 21 31 A 3 3 1 27 31 L 27 33 Z'},'none')
add(17,'HRECT_L','A capsule with a tail and dangling hook omitted the dorsal fin and jointed manipulator.','Restore the submarine-shaped drone with fins, body seam, articulated claw and water surface.',{
 'water':'M 4 8 C 8 12 12 12 16 8 C 20 12 24 12 28 8 C 32 12 36 12 40 8',
 'body':'M 7 23 C 12 19 16 19 22 19 L 31 19 A 6 6 1 31 31 L 22 31 C 15 31 10 28 7 23 Z',
 'tail':'M 7 23 L 7 15 C 10 13 13 17 15 20','fin':'M 23 19 L 25 14 L 31 14 L 31 19','seam':'M 28 19 L 28 31','arm':'M 23 31 L 23 39 L 35 39','claw':'M 44 34 C 33 31 32 43 44 40'},'none')
add(18,'SQUARE','The drawing resembled a comb; both diagonal chopsticks and a gripping hand were missing.','Restore two long diagonal chopsticks crossing a rounded closed grip, thumb and wrist.',{
 'outer-hand':'M 7 42 L 9 33 C 6 23 8 17 15 16 L 26 18 C 29 19 29 23 26 24 C 30 26 28 30 25 31 C 27 35 23 37 21 37 L 22 42',
 'thumb':'M 19 13 C 23 8 29 9 30 13 C 31 16 28 18 26 18','finger':'M 16 25 L 26 26','finger-lower':'M 16 32 L 25 33',
 'stick-upper':'M 8 6 L 42 33','stick-lower-left':'M 6 13 L 15 19','stick-lower-right':'M 29 28 L 40 38'},'hand')
add(19,'VRECT_M','The silhouette read as a rigid cactus with a U-shaped notch rather than a natural raised hand.','Restore the long tapered outer finger, sloped curled-finger edge, thumb crease and open wrist.',{
 'outer':'M 12 44 C 9 35 10 29 15 23 L 23 13 C 26 10 28 15 27 19 L 23 26 C 20 32 25 34 29 29 C 32 25 29 20 30 15 L 31 8 C 32 2 38 2 38 7 L 38 28 C 38 36 29 38 24 44'},'hand')

# Second visual pass: improve UI openings and preserve natural silhouettes.
D[0]['paths']['cab']='M 9 34 L 4 34 L 4 27 L 8 21 L 16 21 L 16 29'
D[0]['paths']['bed']='M 16 29 L 44 29 L 44 34 L 39 34'
D[0]['paths']['door']='M 27 29 L 27 24 A 4 4 1 35 24 L 35 29'
D[0]['paths']['house']='M 20 17 L 20 29 L 42 29 L 42 17'
D[0]['paths']['roof']='M 18 18 L 31 8 L 44 18'
D[2]['paths']['cab']='M 28 22 L 35 22 L 44 30 L 44 35 L 40 35'
D[2]['paths']['window']='M 33 22 L 33 29 L 43 29'
D[2]['paths']['box']='M 4 21 L 27 21 L 27 34 L 18 34'
D[2]['paths']['house']='M 7 17 L 7 11 L 14 6 L 21 11 L 21 17 Z'
D[3]['paths']['cab']='M 18 25 L 11 25 C 8 25 6 29 6 32 L 6 37 L 8 37'
D[4]['paths']['receiver']='M 16 13 L 21 18 L 18 21 C 20 24 23 27 26 28 L 29 25 L 34 29 C 31 34 26 32 20 27 C 14 22 12 17 16 13 Z'
D[5]['paths']['left-lamp']='M 18 29 L 18 29'
D[5]['paths']['right-lamp']='M 30 29 L 30 29'
D[6]['paths']['arm-right']='M 24 30 L 22 41'
D[6]['paths']['arm-left']='M 24 30 L 13 34 L 10 42'
D[7]['paths']['screen']=rect(12,20,18,12,2)
D[7]['paths']['knob-top']='M 36 22 L 36 22'
D[7]['paths']['knob-bottom']='M 36 30 L 36 30'
D[11]['paths']['raised-arm']='M 14 24 L 21 24 L 24 12'
D[12]['paths'].pop('upper-notch');D[12]['paths'].pop('lower-notch')
D[12]['paths']['upper']='M 15 14 C 15 9 22 13 26 11 C 32 8 33 4 38 7 C 46 14 39 22 29 25 C 19 28 11 23 15 14 Z'
D[12]['paths']['lower']='M 6 31 C 10 25 15 32 21 31 C 27 30 33 27 34 34 C 35 41 23 44 13 41 C 7 40 3 36 6 31 Z'
D[16]['paths']['plate']=rect(4,4,40,40,5)
D[16]['paths']['slot-left']='M 19 19 L 19 22'
D[16]['paths']['slot-right']='M 29 19 L 29 22'
D[16]['paths']['ground']='M 20 33 L 20 30 A 4 4 1 28 30 L 28 33 Z'
D[17]['paths']['water']='M 4 6 C 8 10 12 10 16 6 C 20 10 24 10 28 6 C 32 10 36 10 40 6'
D[17]['paths']['tail']='M 7 23 L 7 16 C 10 14 13 18 15 20'
D[17]['paths']['fin']='M 23 19 L 25 14 L 31 14 L 31 19'

# Final native-size pass: separate ground opening; widen biscuits; align both figures.
D[8]['paths']['outline']='M 4 31 C 4 24 13 8 24 8 C 35 8 44 24 44 31 C 44 43 4 43 4 31 Z'
D[11]['paths'].update({'head-a':circle(12,12,4),'head-b':circle(38,12,4),'torso-a':'M 12 24 L 12 31','torso-b':'M 38 24 L 38 31','left-arm':'M 12 24 L 8 24 L 4 29','raised-arm':'M 12 24 L 22 24 L 25 12','right-arms':'M 30 29 L 33 24 L 38 24 L 41 24 L 44 29','legs-a':'M 6 40 L 12 31 L 18 40','legs-b':'M 32 40 L 38 31 L 44 40'})
D[13]['keyshape']='SQUARE'
D[13]['paths']={'biscuit-a':rect(6,6,14,36,7),'biscuit-b':rect(28,6,14,36,7),'groove-a':'M 13 15 C 10 21 16 27 13 34','groove-b':'M 35 15 C 32 21 38 27 35 34'}
D[16]['paths']['slot-left']='M 19 18 L 19 20'
D[16]['paths']['slot-right']='M 29 18 L 29 20'
D[16]['paths']['ground']='M 20 31 L 20 29 A 4 4 1 28 29 L 28 31 Z'
D[19]['paths']['outer']='M 12 44 C 11 40 10 36 10 32 C 10 28 13 25 15 23 L 23 13 C 26 10 28 15 27 19 L 23 26 C 20 32 25 34 29 29 C 32 25 29 20 30 15 L 30 8 A 4 4 1 38 8 L 38 28 C 38 36 29 38 24 44'

D[11]['paths']['left-arm']='M 12 24 L 6 24 L 4 26'

HELPER='''
def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()
'''

def generate(indices):
 for i in indices:
  row=ROWS[i];design=D[i];dest=Path(row['result_dir']);module=dest/(row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
  text='from icon_set.model.icons.solo._base import Solo48\nfrom icon_set.model.keyshapes import Keyshape\n'
  text+=f'SOURCE_ICON_ID = {row["source_uuid"]!r}\nSOURCE_PATH = {row["reference_path"]!r}\nAUTHOR = "gpt-6"\n'
  text+=f'# Plan: {design["change"]}\n# Keyshape: {design["keyshape"]}; preserve reference arrangement.\n# Construction reference: {design["lucide"]}.\n'+HELPER
  text+=f'\nclass Revision(Solo48):\n    icon_id = {row["icon_id"]!r}\n    keyshape = Keyshape.{design["keyshape"]}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects/general"\n    aliases = ()\n    keywords = ()\n\n    def build(self):\n'
  for name,path in design['paths'].items():text+=f'        _draw(self, {name!r}, {path!r})\n'
  # Genuine shared endpoints between contours are contacts; proximity alone is never declared.
  text+='''        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
'''
  for figure,head,torso,junction in design['flags']:text+=f'        self.mark_human_figure({figure!r}, head={head!r}, torso={torso!r}, torso_junction={junction!r})\n'
  module.write_text(text)
  (dest/'comparison.md').write_text(f'# {row["icon_id"]}\n\nOriginal inspected: {row["reference_path"]}\n\nRejected: {design["wrong"]}\n\nFeedback: Does not convey the intended meaning.\n\nRevision: {design["change"]}\n\nConstruction: {design["lucide"]}; native 48px / 4px strokes.\n')
  icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg();(dest/(row['icon_id']+'.svg')).write_text(svg);(dest/'validation.txt').write_text(report.describe());render_previews(svg,row['icon_id'],48,dest)
  print(i,row['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
if __name__=='__main__':generate([int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else range(20))
