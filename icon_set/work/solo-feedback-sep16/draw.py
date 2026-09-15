from pathlib import Path
import json,textwrap
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
R={}
def add(n,k,note,code,reference='Supplied original and local geometric construction references'):
 R[n]=(k,note,textwrap.dedent(code).strip(),reference)
HELPERS='''
        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
'''
add('arched-stone-bridge','HRECT_L','Replace the flattened arc wave with two identical smooth waves, each made from tangent-matched curves. Keep the approved single stone arch.', '''
line('deck',(4,8),(44,8))
path('bridge',(4,8),[('L',(4,27)),('L',(14,27)),('L',(14,26)),('A',(34,26),10,10,True),('L',(34,27)),('L',(44,27)),('L',(44,8))]);join('deck','bridge')
path('water',(4,40),[('C',(14,36),(8,40),(10,36)),('C',(24,40),(18,36),(20,40)),('C',(34,36),(28,40),(30,36)),('C',(44,40),(38,36),(40,40))])
''','Local Lucide waves-horizontal and supplied stone bridge; repeated smooth wave construction')
add('arrange-number','VRECT_L','The 1 and 9 both have a 12-unit centerline height and the same 4-unit stroke. The 9 has a compact loop and straight descending stem.', '''
poly('arrow',(8,36),(14,44),(20,36));line('shaft',(14,4),(14,44));join('shaft','arrow')
poly('one',(32,10),(36,6),(36,18))
path('nine',(40,32),[('A',(32,32),4,4,False),('A',(40,32),4,4,False),('L',(40,40))])
''','Local Lucide arrow-down-0-1; user requested equal numeral size')
add('baby-face-with-bow','SQUARE','Remove both ears. A continuous rounded cheek and jaw outline connects directly to the original bow, retaining the eyes and smile.', '''
path('face',(10,20),[('A',(6,24),4,4,False),('A',(42,24),18,18,False),('A',(38,20),4,4,False)])
poly('bow-left',(24,13),(10,6),(10,20),closed=True);poly('bow-right',(24,13),(38,6),(38,20),closed=True)
join('bow-left','bow-right');join('bow-left','face');join('bow-right','face')
dot('eye-left',(17,26));dot('eye-right',(31,26))
self.add_arc('smile',(21,33),(27,33),radius_x=4,radius_y=2,sweep=False)
''','Existing baby face with bow; shared rounded human face vocabulary')
add('balancing-stick-pose','HRECT_L','A person balances on one leg with the torso and rear leg extended horizontally and the arms reaching forward above the head. A larger head follows the horizontal torso axis.', '''
path('head',(7,21),[('A',(17,21),5,5,True),('A',(7,21),5,5,True)],True)
line('torso',(25,21),(34,21));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
path('arms',(25,21),[('L',(25,13)),('C',(20,8),(25,10),(23,8)),('L',(4,8))]);join('arms','torso')
line('raised-leg',(34,21),(44,21));line('standing-leg',(34,21),(28,40));join('raised-leg','torso');join('standing-leg','torso');join('raised-leg','standing-leg')
''','Shared human_ref/full_body_ref.png; balancing stick / Warrior III action. Head outline to neck: 13 minus radius 5 equals 8 centerline units, leaving 4 units of ink clearance.')
add('artillery-field-gun','HRECT_L','A long horizontal cannon barrel with a clear muzzle band sits on a visible mounting post, wheel and rear carriage. Omit small mechanical details.', '''
path('barrel',(14,8),[('L',(44,8)),('L',(44,18)),('L',(14,18)),('A',(14,8),5,5,True)],True)
line('muzzle-band',(36,8),(36,18));join('muzzle-band','barrel')
circle('wheel',16,33,7)
line('mount',(16,18),(16,26));join('mount','barrel');join('mount','wheel')
line('left-leg',(9,33),(4,40));line('trail',(23,33),(44,40));join('wheel','left-leg');join('wheel','trail')
''','Supplied field-gun silhouette; local Lucide circle construction for the wheel')
add('artillery-gun-outriggers','VRECT_L','A long elevated gun tube terminates in a separate muzzle block. The central wheel and two outward legs make the wheeled artillery silhouette explicit.', '''
circle('wheel',18,36,8)
line('barrel',(18,28),(30,14));join('wheel','barrel')
poly('muzzle',(26,10),(32,4),(40,12),(34,18),closed=True);join('barrel','muzzle')
line('left-outrigger',(10,36),(8,44));line('right-outrigger',(26,36),(40,44));join('wheel','left-outrigger');join('wheel','right-outrigger')
''','Supplied elevated artillery reference; same round wheel and minimal structural strokes')
add('anteater','CIRCLE','A long down-sloping snout leads into a low body, while a broad sweeping tail takes up the rear silhouette. Keep two near legs and one eye; omit the far legs and fur texture.', '''
path('animal',(4,24),[('L',(14,18)),('C',(18,12),(16,16),(16,12)),('L',(26,12)),('C',(32,20),(30,12),(32,16)),('C',(38,22),(34,18),(36,18)),('C',(42,32),(40,24),(42,28)),('C',(30,30),(38,34),(34,32)),('L',(18,30)),('L',(12,26)),('L',(4,24))],True)
dot('eye',(22,21))
line('front-leg',(18,30),(14,38));line('rear-leg',(28,30),(28,38));join('animal','front-leg');join('animal','rear-leg')
''','Naturalist Journeys giant anteater photograph: long snout, low body and large tail; no close Lucide animal match. https://www.naturalistjourneys.com/tours/2026/02/12/guyana-unspoiled-wilderness')

def write():
 rows=json.loads((W/'plan.json').read_text())
 for r in rows:
  key,note,code,ref=R[r['icon_id']];m=r['meta']
  text=f'''"""{note}\nReference: {ref}\nAuthored directly on SOLO48, with prior revision preserved."""\nfrom ...keyshapes import Keyshape\nfrom ._base import Solo48\nSOURCE_ICON_ID = {m.get('SOURCE_ICON_ID')!r}\nSOURCE_PATH = {m.get('SOURCE_PATH')!r}\nAUTHOR = 'gpt-6'\n\nclass {r['class_name']}(Solo48):\n    icon_id = {r['new_id']!r}\n    variant_of = {r['parent']!r}\n    variant_label = 'Revised after specific drawing feedback, 16 September'\n    keyshape = Keyshape.{key}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = {r['category']!r}\n    aliases = ()\n    keywords = {tuple(r['icon_id'].split('-'))!r}\n\n    def build(self):\n        # Symbol plan: {note}\n'''+HELPERS+textwrap.indent(code,'        ')+'\n'
  compile(text,r['new_path'],'exec');Path(r['new_path']).write_text(text);r.update(change=note,reference=ref,keyshape=key)
 (W/'plan.json').write_text(json.dumps(rows,indent=2));print('Seven drawings written')
if __name__=='__main__':write()
