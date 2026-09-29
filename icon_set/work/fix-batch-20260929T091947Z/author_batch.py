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
def add(i,key,wrong,change,paths,ref="none",flags=None,omissions="Minor secondary detail simplified."):
 D[i]=dict(keyshape=key,wrong=wrong,change=change,paths=paths,lucide=ref,flags=flags or [],omissions=omissions)
frame=rect(6,6,36,36,4)
add(0,'SQUARE','The receiver became a squared crescent, with angular steps instead of recognizable earpieces.','Restore a complete curved receiver with two rounded earpieces inside the square.',{
 'frame':frame,'receiver':'M 16 13 C 17 12 18 13 20 15 L 22 18 C 23 19 21 21 19 22 C 21 26 23 28 27 29 L 30 26 C 31 25 33 27 35 29 C 38 32 34 36 31 36 C 24 36 12 24 12 18 C 12 16 14 14 16 13 Z'},'phone',omissions='No defining feature omitted; minute source curvature simplified.')
add(1,'SQUARE','The receiver was identical to the other squared crescent and lost the soft hook and rounded mouthpiece.','Restore the reference’s soft curved handset and broad rounded terminal pieces.',{
 'frame':rect(6,6,36,36,7),'receiver':'M 17 13 C 19 12 19 14 21 18 C 22 20 18 20 19 23 C 21 27 24 29 27 29 C 29 28 29 26 31 27 L 35 29 C 39 32 33 37 29 35 C 20 32 13 25 13 18 C 13 16 15 14 17 13 Z'},'phone',omissions='No hang-up slash added: the source contains a curved receiver only.')
add(2,'SQUARE','The Q was reduced to a tiny ring with a large handle, reading as a search icon.','Enlarge the Q bowl and lighten the proportional tail so it reads as the reference letter.',{
 'frame':frame,'q-bowl':circle(23,22,10),'q-tail':'M 30 29 L 35 35'},'none',omissions='None; bowl and diagonal tail retained.')
add(3,'SQUARE','The arrow was cramped inside a sharply cut tag-shaped frame.','Restore the softly rounded right-pointing frame and a longer arrow with balanced wings.',{
 'frame':'M 11 6 L 28 6 C 30 6 30 7 32 9 L 40 17 C 42 19 42 20 42 24 C 42 28 42 29 40 31 L 32 39 C 30 41 30 42 28 42 L 11 42 A 5 5 1 6 37 L 6 11 A 5 5 1 11 6 Z','arrow':'M 14 24 L 32 24','head':'M 25 17 L 32 24 L 25 31'},'arrow-right')
add(4,'SQUARE','The arrowhead dominated a short shaft, unlike the long balanced arrow in the source.','Rebalance the right arrow with a longer shaft, smaller wings and softer frame corners.',{
 'frame':rect(6,6,36,36,5),'shaft':'M 14 25 L 34 25','head':'M 28 19 L 34 25 L 28 31'},'arrow-right',omissions='None; the source is an arrow despite the square-u catalog name.')
add(5,'SQUARE','The sharp upward arrow was merged into a short, thick hook, losing the source’s separated head and long upright.','Restore a longer rising elbow and separate chevron aligned above it.',{
 'frame':frame,'shaft':'M 14 34 L 25 34 L 25 23','head':'M 18 20 L 25 13 L 32 20'},'corner-right-up',omissions='None; the detached arrowhead is intentional in the source.')
add(6,'SQUARE','The check was squat and unevenly balanced, with its short arm too low and long arm too steep.','Restore the broad descending-then-rising check and rounded-square container.',{
 'frame':rect(6,6,36,36,5),'check':'M 14 25 L 21 32 L 34 16'},'none',omissions='None; kept the check rather than inventing a letter V.')
add(7,'SQUARE','A Y was substituted for the horizontal bar actually present in the reference.','Replace the Y with the centered horizontal bar, preserving the rounded square.',{
 'frame':frame,'bar':'M 14 24 L 34 24'},'none',omissions='Removed the invented Y arms and stem.')
add(8,'SQUARE','A letter Z replaced the source’s horizontal bar and small outlined circle.','Restore a bar above an outlined circle in the square.',{
 'frame':frame,'bar':'M 15 18 L 33 18','ring':circle(24,30,4)},'none',omissions='Removed the invented Z diagonal.')
add(9,'VRECT_L','The grip became a block grid, without individual curved fingers or a recognizable phone.','Restore a rounded upright phone, four gripping finger segments, side hand and inward squeeze arrows.',{
 'phone':'M 16 44 L 29 44 A 3 3 0 32 41 L 32 7 A 3 3 0 29 4 L 17 4 A 3 3 0 14 7 L 14 16',
 'finger-top':rect(8,17,13,6,3),'finger-mid':rect(8,23,13,6,3),'finger-low':rect(8,29,13,6,3),'finger-last':rect(8,35,13,6,3),
 'thumb':'M 32 17 C 40 15 36 31 42 32','left-arrow':'M 4 10 L 10 10','left-arrowhead':'M 7 7 L 10 10 L 7 13','right-arrow':'M 44 10 L 38 10','right-arrowhead':'M 41 7 L 38 10 L 41 13'},'hand',omissions='Small wrist and phone bezel detail reduced; all four fingers retained.')
add(10,'SQUARE','The scissors were crossed sticks and the curved female-operation mark became a numeral-like 3.','Restore upright closed surgical scissors with two finger loops and the separate curved crossed marker.',{
 'blade':'M 14 30 L 14 20 L 18 6 L 22 20 L 22 30','blade-seam':'M 14 26 L 22 20','left-loop':circle(10,36,6),'right-loop':circle(26,36,6),
 'curve':'M 30 12 C 42 12 43 25 35 30','marker-stem':'M 37 15 L 42 8','cross-a':'M 37 4 L 44 11','cross-b':'M 44 4 L 37 11'},'scissors',omissions='Small blade taper simplified; both loops and the separate marker retained.')
add(11,'SQUARE','The stacked cells merged into stair-step blocks and the arrows lost their long return sweep.','Restore a descending two-two-one column stack and two curved unstack arrows.',{
 'top':rect(6,6,9,14,1),'top-rule':'M 6 13 L 15 13','middle':rect(15,20,9,14,1),'middle-rule':'M 15 27 L 24 27','bottom':rect(24,34,9,8,1),
 'arrow-a':'M 26 8 C 36 8 37 16 34 20 C 33 22 31 24 28 24','head-a':'M 32 20 L 28 24 L 32 27','arrow-b':'M 40 25 C 47 27 43 38 38 38','head-b':'M 41 34 L 37 38 L 41 42'},'none',omissions='Fine cell borders consolidated; all five cells and both arrows preserved.')
add(12,'SQUARE','The rear page was an open line with no left shoulder, and both page silhouettes were angular.','Restore two rounded overlapping file outlines with clipped upper-right corners.',{
 'front':'M 10 14 L 23 14 C 25 14 26 16 28 18 L 32 22 L 32 38 A 4 4 1 28 42 L 10 42 A 4 4 1 6 38 L 6 18 A 4 4 1 10 14 Z',
 'rear':'M 15 14 L 15 10 A 4 4 1 19 6 L 31 6 C 33 6 34 8 36 10 L 42 16 L 42 30 A 4 4 1 38 34 L 32 34'},'files',omissions='No extra content lines added; preserve blank source documents.')
add(13,'SQUARE','The handshake-like strokes lost the three overlapping hands and their finger structure.','Restore a top wrist, left supporting palm and diagonal foreground hand with distinct finger creases.',{
 'top-left':'M 19 4 L 19 10 C 19 14 15 13 15 19','top-right':'M 29 4 L 29 10 C 29 14 33 14 33 20',
 'left-hand':'M 4 35 L 8 30 C 7 27 8 24 10 20 C 11 17 15 18 14 22 L 13 25','left-wrist':'M 10 44 L 16 39 C 20 39 22 37 24 35',
 'front-hand':'M 44 35 L 39 30 C 41 24 36 20 30 15 C 27 12 24 15 27 18 L 33 24','fingers':'M 27 18 L 23 15 C 20 13 17 16 20 19 L 29 28','middle':'M 20 19 C 16 16 13 20 17 23 L 25 31','low':'M 17 23 C 13 22 12 25 16 28 L 26 37 C 29 39 32 37 35 40 L 40 44'},'hand',omissions='Finger creases reduced to three clear diagonal runs; no extra hand ornaments.')
add(14,'VRECT_L','The microphone became a magnifying glass on a short plinth, omitting the long stand and cable.','Restore a tapered angled microphone, tall vertical stand, floor base and trailing cable.',{
 'head':circle(32,12,8),'handle':'M 25 8 L 11 27 C 10 28 12 31 14 30 L 33 18','stand':'M 26 24 L 26 44','base':'M 18 44 L 34 44','cable':'M 11 30 C 5 34 8 37 10 38'},'mic',omissions='Grille texture omitted; cable retained because it distinguishes stage equipment.')
add(15,'VRECT_L','The figure became an angular branching stick with an undersized detached head, losing the backward torso curve.','Restore an arched back, hand on the lower back and upright legs, with a proportionate aligned head.',{
 'head':circle(13,8,4),'torso':'M 25 8 C 22 8 18 14 18 18 C 18 22 22 26 27 29','arm':'M 25 8 L 35 8 C 42 8 41 14 35 14 L 28 14 L 23 19 L 29 25','hip-hand':'M 29 25 L 33 23','legs':'M 27 29 L 23 34 L 23 44','back-leg':'M 27 29 L 30 35 L 30 44'},'human_ref/full_body_ref.png',[('person','head','torso-1','start')],omissions='Outlined body reduced to shared stick-figure construction; bent-back action retained.')
add(16,'SQUARE','The head was flattened, limbs stiff, and weights disproportionate to the standing figure.','Restore a circular head, balanced shoulders, two grounded legs and a straight bar held at waist height.',{
 'head':circle(24,10,4),'torso':'M 24 22 L 24 30 L 24 34','arms':'M 14 30 L 14 22 L 24 22 L 34 22 L 34 30','bar':'M 6 30 L 14 30 L 24 30 L 34 30 L 42 30','weight-left':'M 6 24 L 6 36','weight-right':'M 42 24 L 42 36','legs':'M 17 42 L 24 34 L 31 42'},'human_ref/full_body_ref.png + dumbbell',[('person','head','torso-1','start')],omissions='Filled limbs and fine weight plates reduced to consistent 4px strokes.')
add(17,'SQUARE','The screen looked like a slash, the desk like a box and the person did not reach a keyboard.','Restore a standing operator reaching a desk with an edge-view monitor and open table legs.',{
 'head':circle(36,10,4),'torso':'M 36 22 L 36 33','arm':'M 36 22 L 30 28 L 23 28','legs':'M 31 42 L 36 33 L 41 42','desk':'M 6 31 L 25 31','desk-left':'M 6 31 L 6 42','desk-right':'M 25 31 L 25 42','screen':'M 9 6 L 14 23','monitor-base':'M 12 16 C 7 16 10 26 6 27 L 17 27'},'human_ref/full_body_ref.png + monitor',[('person','head','torso-1','start')],omissions='Keyboard rendered as reaching hand above the desk; preserve side-view screen.')
add(18,'CIRCLE','The short hooked mark had little vertical stem and a cramped dot, weakening the question-mark silhouette.','Restore a clear question mark with a smooth upper hook, longer downward stem and isolated dot.',{
 'circle':circle(24,24,20),'question':'M 17 18 C 17 10 31 10 31 18 C 31 23 24 23 24 28','dot':'M 24 36 L 24 36'},'none',omissions='No question component omitted; use a full 4px dot for UI visibility.')
add(19,'SQUARE','The clock hands merged with its rim and the face was small and heavy inside the document.','Restore a larger round clock with clearly separate hands inside the clipped-corner page.',{
 'page':'M 8 4 L 31 4 L 44 17 L 44 40 A 4 4 1 40 44 L 8 44 A 4 4 1 4 40 L 4 8 A 4 4 1 8 4 Z','clock':circle(24,27,12),'hands':'M 24 20 L 24 27 L 29 31'},'none',omissions='No numerals added; preserve the simple two-hand source clock.')

# Native-size revision: retain source layout while opening safe clearances.
D[3]['paths']['arrow']='M 15 24 L 32 24'
D[4]['paths']['shaft']='M 15 25 L 33 25'
D[4]['paths']['head']='M 27 19 L 33 25 L 27 31'
D[6]['paths']['check']='M 15 25 L 21 32 L 33 16'
D[7]['paths']['bar']='M 15 24 L 33 24'
D[8]['paths']['bar']='M 15 17 L 33 17'
D[8]['paths']['ring']=circle(24,29,4)
D[15]['paths']['torso']='M 25 8 C 30 8 22 13 22 18 C 22 22 25 26 29 29'
D[15]['paths']['legs']='M 29 29 L 23 34 L 23 44'
D[15]['paths']['back-leg']='M 29 29 L 31 35 L 31 44'
D[18]['paths']['question']='M 17 18 C 17 11 31 11 31 18 C 31 23 24 23 24 27'
D[18]['paths']['dot']='M 24 35 L 24 35'

D[15]['paths']['torso']='M 25 8 C 30 8 23 13 23 18 C 23 22 26 26 29 29'
D[15]['paths']['arm']='M 25 8 L 35 8 C 41 8 41 14 35 14 L 30 14 L 37 23 L 29 29'
D[15]['paths'].pop('hip-hand')

D[13]['paths']['front-hand']='M 44 35 L 39 30 C 40 26 38 22 34 19 L 29 14 C 25 10 21 14 24 18 L 30 24'
D[13]['paths']['fingers']='M 24 18 L 19 14 C 15 10 11 15 15 19 L 25 29'
D[13]['paths'].pop('middle')
D[13]['paths']['low']='M 15 19 C 11 17 8 22 12 26 L 25 38 C 29 41 33 37 36 41 L 40 44'
D[13]['omissions']='Reduced the foreground hand to two finger creases to open the palm; retained all three wrist directions.'

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
