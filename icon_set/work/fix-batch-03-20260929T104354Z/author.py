"""Batch 03 standalone primitive-make-ray authoring; metadata stays per input."""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
sys.path.insert(0, str(REPO))
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Per-input values are read from batch.json and emitted below.
SOURCE_PATH = None
ROWS = json.loads((ROOT / 'batch.json').read_text())

HELPERS = '''
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)
'''

SPECS = {}
def spec(name,key,issue,change,body,extra='',reference='No useful subject-specific Lucide match; geometric arcs and smooth coherent contours.'):
    SPECS[name] = dict(key=key,issue=issue,change=change,body=body,extra=extra,reference=reference)

spec('bearded-pirate-with-hook-hand','SQUARE',
     'The rejected hook points downward from an inverted arch, whereas the original has an upright shaft and a lower curled hook; the hat brim is pinched.',
     'Reversed the hook into a lower J-shaped curl and opened the hat brim, keeping the pointed beard and pirate hat.', '''
        bez('hat',(6,18),((6,14),(9,12),(12,12)),((12,8),(14,6),(18,6)),((22,6),(24,8),(24,12)),((27,12),(30,14),(30,18)))
        poly('brim',(30,18),(26,20),(10,20),(6,18));join('hat','brim')
        arc('face',(26,20),(10,20),8);join('face','brim')
        path('beard',(10,20),[('L',(10,32)),('C',(18,42),(10,37),(14,40)),('C',(26,32),(22,40),(26,37)),('L',(26,20))]);join('beard','face');join('beard','brim')
        line('hook-shaft',(34,28),(34,36))
        arc('hook-curl',(34,36),(42,36),4,s=False);join('hook-shaft','hook-curl')
        line('hook-tip',(42,36),(42,32));join('hook-curl','hook-tip')
''',extra="    human_construction = 'bust'\n",reference='human_ref/user.svg for circular face; original supplies hat, beard and asymmetric hook.')

spec('bell-knob-curved-clapper','VRECT_L',
     'The rejected bell dome is squat with very short sides compared with the upright original.',
     'Lengthened the bell sides and used tangent flares, keeping the top knob and curved clapper.', '''
        self.add_dot('knob',(24,4))
        path('bell',(12,20),[('A',(36,20),12,8,True),('L',(36,26)),('C',(40,33),(36,30),(38,31)),('L',(8,33)),('C',(12,26),(10,31),(12,30)),('L',(12,20))],True)
        arc('clapper',(20,42),(28,42),4,2,False)
''',reference='Lucide bell original and atomic-debug: dome, continuous side flares and detached curved clapper.')

spec('bird-in-flight','HRECT_L',
     'The rejected drawing has one wing and a round songbird head; the original is a two-winged soaring bird.',
     'Restored both raised wings and a hooked forward profile, with broad coherent flight contours.', '''
        path('bird',(4,8),[('C',(28,26),(20,9),(23,17)),('C',(44,8),(28,14),(35,10)),('L',(36,26)),('C',(44,34),(42,26),(44,28)),('C',(28,32),(39,31),(33,30)),('L',(30,40)),('C',(20,35),(24,40),(22,38)),('C',(4,40),(11,40),(7,40)),('L',(4,28)),('L',(12,29)),('L',(20,22)),('C',(4,8),(12,18),(7,16))],True)
''',reference='Lucide bird original and atomic-debug: coherent breast contour and beak; supplied reference owns two-wing flight pose.')

spec('body-scanner-gate','HRECT_L',
     'The rejected scanner figure has a tiny head and rigid shoulders; the original has a clear central person between scanning posts.',
     'Enlarged the circular head, set its exact detached gap and spaced the person evenly between paired posts.', '''
        for side,x,sign in [('left',4,1),('right',44,-1)]:
            poly('post-'+side,(x,8),(x,24),(x,40),(x+4*sign,40))
            line('sensor-'+side,(x,24),(x+2*sign,24));join('post-'+side,'sensor-'+side)
        circle('head',24,14,4)
        line('torso',(24,26),(24,33))
        poly('arms',(16,33),(16,26),(24,26),(32,26),(32,33));join('torso','arms')
        poly('legs',(18,40),(24,33),(30,40));join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''',reference='human_ref/full_body_ref.png: circular head, simple limbs; 26-(14+4)=8 centerline gap.')

spec('bowler-hat','HRECT_L',
     'The rejected crown is too tall and narrow compared with the broad low bowler in the original.',
     'Broadened the crown, flattened its dome slightly and retained a regular band and upturned brim.', '''
        path('crown',(8,22),[('A',(40,22),16,14,True),('L',(40,32)),('L',(40,40)),('L',(8,40)),('L',(8,32)),('L',(8,22))],True)
        line('band',(8,32),(40,32));join('band','crown')
        arc('brim-left',(4,36),(8,40),4,s=False);join('brim-left','crown')
        arc('brim-right',(40,40),(44,36),4,s=False);join('brim-right','crown')
''')

spec('boxcar-on-rails','HRECT_L',
     'The rejected wagon has stubby dot-like panel marks and protruding chassis bumps absent from the clean original.',
     'Made the freight-door marks longer and rebuilt a clean rounded box above two readable wheel bogies and a rail.', '''
        path('body',(10,8),[('L',(38,8)),('A',(42,12),4),('L',(42,26)),('A',(38,30),4),('L',(36,30)),('L',(12,30)),('L',(10,30)),('A',(6,26),4),('L',(6,12)),('A',(10,8),4)],True)
        for x in (18,30): line('panel-'+str(x),(x,17),(x,21))
        poly('rail',(4,40),(12,40),(36,40),(44,40))
        for x in (12,36):
            n='wheel-'+str(x);circle(n,x,35,5);join(n,'body');join(n,'rail')
''')

spec('boy-figure-with-circular-head','VRECT_L',
     'The rejected head dominates a very short flattened shirt; the original has a balanced circular head and longer tapered body.',
     'Reduced the head slightly and lengthened the shirt body, with smooth shoulders and the required bust contact.', '''
        circle('head',24,11,7)
        path('body',(24,22),[('A',(40,32),16,10,True),('L',(34,32)),('L',(32,44)),('L',(16,44)),('L',(14,32)),('L',(8,32)),('A',(24,22),16,10,True)],True)
        join('head','body')
''',extra="    human_construction = 'bust'\n",reference='human_ref/user.svg and full_body_ref.png: circular head, rounded shoulders; 22-(11+7)=4 centerline/zero ink bust contact.')

spec('braille-cell','VRECT_L',
     'The rejected six circles have pinhole centers and overly wide columns relative to their diameter.',
     'Enlarged all six circles and used a shared regular two-column, three-row construction.', '''
        for x in (12,36):
            for y in (8,24,40): circle(f'dot-{x}-{y}',x,y,4)
''')

spec('bug-beetle','SQUARE',
     'The rejected beetle has crowded shoulder joints and a top divider; the original has a round body crossed at its middle.',
     'Rebuilt a rounded symmetrical body, centered the dividing line and attached three equally balanced leg pairs.', '''
        path('body',(16,14),[('C',(24,10),(18,11),(20,10)),('C',(32,14),(28,10),(30,11)),('C',(36,24),(35,17),(36,20)),('C',(32,34),(36,28),(35,31)),('C',(24,38),(30,37),(28,38)),('C',(16,34),(20,38),(18,37)),('C',(12,24),(13,31),(12,28)),('C',(16,14),(12,20),(13,17))],True)
        line('middle',(12,24),(36,24));join('middle','body')
        for side,s in [('left',-1),('right',1)]:
            for name,a,b in [('upper',(24+s*8,14),(24+s*16,6)),('middle',(24+s*12,24),(24+s*18,24)),('lower',(24+s*8,34),(24+s*16,42))]:
                n=name+'-'+side;line(n,a,b);join(n,'body')
                if name=='middle':join(n,'middle')
''',reference='Lucide bug original and atomic-debug: paired attachments and continuous rounded body; source horizontal body division restored.')

spec('confused-face','CIRCLE',
     'The rejected tiny mouth and uneven brows weaken the worried, confused expression in the original.',
     'Made the inward-raised brows consistent and broadened the shallow frown.', '''
        circle('face',24,24,20)
        line('brow-left',(16,16),(20,14));line('brow-right',(28,14),(32,16))
        for x in (16,32):self.add_dot('eye-'+str(x),(x,24))
        bez('frown',(19,34),((22,31),(26,31),(29,34)))
''')

spec('downhill-skier','VRECT_L',
     'The rejected head floats beside the body and the rear arm bends unnaturally; the source shows a crouching rider with a pole.',
     'Aligned the head above the upper torso, rebuilt a crouch and added the forward pole over a smooth ski.', '''
        circle('head',26,9,5)
        bez('torso',(26,22),((26,26),(23,28),(20,30)))
        poly('leg',(20,30),(28,34),(20,44));join('leg','torso')
        poly('arm',(26,22),(32,28),(40,24));join('arm','torso')
        poly('pole',(40,22),(40,24),(40,36));join('pole','arm')
        path('ski',(8,40),[('C',(20,44),(12,42),(16,44)),('L',(36,44)),('A',(40,40),4,4,False)])
        join('ski','leg')
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
''',reference='human_ref/full_body_ref.png: circular head aligned with vertical upper-torso tangent; 22-(9+5)=8 centerline gap.')

spec('rope-climber','VRECT_L',
     'The rejected head is misaligned with the torso and the rope loops into the waist like a bowl.',
     'Straightened the climbing rope, aligned the head and torso and rebuilt the raised grip and bent climbing legs.', '''
        circle('head',24,10,6)
        bez('torso',(24,24),((24,27),(22,30),(20,32)))
        poly('left-arm',(24,24),(12,24),(8,16));join('left-arm','torso')
        poly('right-arm',(24,24),(32,24),(40,16));join('right-arm','torso');join('right-arm','left-arm')
        poly('rope',(40,4),(40,16),(40,44));join('rope','right-arm')
        line('left-leg',(20,32),(8,44));join('left-leg','torso')
        poly('right-leg',(20,32),(32,36),(32,44));join('right-leg','torso');join('right-leg','left-leg')
        self.mark_human_figure('climber',head='head',torso='torso',torso_junction='start')
''',reference='human_ref/full_body_ref.png: head center on upper torso tangent; 24-(10+6)=8 centerline gap; intentionally asymmetric action.')

spec('thinking-person-with-hand-at-chin','VRECT_L',
     'The rejected arm reads as a thin loop and the shoulder/head junction triggers internal-spacing review.',
     'Rebalanced the head and broad shoulder, enlarged the bent forearm and used explicit bust construction at the chin.', '''
        circle('head',23,13,9)
        path('body',(8,44),[('L',(8,41)),('A',(23,26),15)])
        bez('raised-arm',(23,26),((24,33),(27,41),(30,44)),((38,44),(40,41),(40,36)),((40,31),(38,27),(34,26)))
        join('head','body');join('head','raised-arm');join('body','raised-arm')
''',extra="    human_construction = 'bust'\n",reference='human_ref/user.svg: broad shoulder and circular face; 26-(13+9)=4 centerline/zero ink contact; asymmetric hand-at-chin pose.')

spec('three-people-behind-banner','HRECT_L',
     'The rejected figures have only posts for torsos, losing the visible shoulders of the original demonstrators.',
     'Added equal shoulder spans above the banner, with three circular heads and short visible legs.', '''
        poly('banner',(4,30),(8,30),(24,30),(40,30),(44,30),(44,38),(40,38),(24,38),(8,38),(4,38),closed=True)
        for i,x in enumerate((8,24,40)):
            circle(f'head-{i}',x,11,3)
            line(f'torso-{i}',(x,22),(x,30))
            poly(f'arms-{i}',(x-4,22),(x,22),(x+4,22));join(f'arms-{i}',f'torso-{i}')
            line(f'legs-{i}',(x,38),(x,40));join(f'torso-{i}','banner');join(f'legs-{i}','banner')
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
''',reference='human_ref/full_body_ref.png: repeated heads and shoulder strokes; 22-(11+3)=8 exact detached gap.')

spec('three-people-on-winners-podium','SQUARE',
     'The rejected winners are reduced to head-and-post marks instead of the people visible in the reference.',
     'Restored shoulder spans for all three figures while keeping the raised central podium and symmetric ranking.', '''
        poly('podium',(6,32),(9,32),(18,32),(18,28),(24,28),(30,28),(30,32),(39,32),(42,32),(42,42),(6,42),closed=True)
        for i,(x,y,w) in enumerate(((9,13,3),(24,9,4),(39,13,3))):
            circle(f'head-{i}',x,y,3)
            line(f'torso-{i}',(x,y+11),(x,28 if i==1 else 32))
            poly(f'arms-{i}',(x-w,y+11),(x,y+11),(x+w,y+11));join(f'arms-{i}',f'torso-{i}');join(f'torso-{i}','podium')
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
''',reference='human_ref/full_body_ref.png: same-scale circular heads and shoulder strokes; each torso begins 8 below its head outline.')

for name,rad,width,sy in [('three-people-with-central-foreground-figure',5,10,15),('three-person-team-busts',6,8,16)]:
    spec(name,'HRECT_L',
         'The rejected group uses three equal narrow arches, losing the broad central foreground torso and partly hidden side figures.',
         'Restored a wide central bust with a closed base and two partial outer shoulder silhouettes, preserving three distinct heads.', f'''
        cx,cy,r=24,{8+rad},{rad}
        circle('head-center',cx,cy,r)
        top=cy+r+4; w={width}
        path('body-center',(cx-w,40),[('L',(cx-w,top+w)),('A',(cx,top),w),('A',(cx+w,top+w),w),('L',(cx+w,40)),('L',(cx-w,40))],True)
        join('head-center','body-center')
        for side,x,sign in [('left',7,-1),('right',41,1)]:
            circle('head-'+side,x,{sy},3)
            top={sy}+7
            start=(x+sign*2,36);outer=x+sign*3
            path('body-'+side,start,[('L',(outer,36)),('L',(outer,top+3)),('A',(x,top),3,3,sign<0)])
            join('head-'+side,'body-'+side)
''',extra="    human_construction = 'bust'\n",reference='human_ref/user.svg and Lucide users original/atomic-debug: broad central shoulder contour and partial occluded side busts; each circular jaw has 4 centerline/zero ink shoulder contact.')

spec('three-tower-castle-with-flags','SQUARE',
     'The rejected central flag is just a short bar and the towers have cramped roof-to-wall proportions.',
     'Raised a longer flagstaff with a turned pennant edge, staggered the three roofs and preserved the clear central doorway.', '''
        poly('walls',(6,34),(6,42),(18,42),(18,34),(30,34),(30,42),(42,42),(42,34),(30,34),(30,26),(18,26),(18,34),closed=True)
        poly('roof-left',(6,34),(12,24),(18,34));join('roof-left','walls')
        poly('roof-right',(30,34),(36,24),(42,34));join('roof-right','walls')
        poly('roof-middle',(18,26),(24,16),(30,26));join('roof-middle','walls')
        poly('flag',(24,16),(24,6),(34,6),(34,10));join('flag','roof-middle')
''',reference='Lucide castle original/atomic-debug for coherent wall and doorway construction; original supplies the three pointed towers.')

spec('thumbs-down-hand','SQUARE',
     'The rejected horizontal hand is squat; the original has a longer downward thumb and a clear cuff.',
     'Recomposed on a square envelope with a longer thumb, rounded knuckles, a clear cuff and one readable finger crease.', '''
        path('hand',(16,24),[('L',(22,30)),('L',(24,42)),('L',(28,42)),('A',(32,38),4,4,False),('L',(30,26)),('L',(36,26)),('A',(42,20),6,6,False),('L',(42,16)),('L',(42,12)),('A',(36,6),6,6,False),('L',(16,6))])
        path('cuff',(16,6),[('L',(8,6)),('A',(6,8),2,2,False),('L',(6,22)),('A',(8,24),2,2,False),('L',(16,24)),('L',(16,6))],True);join('hand','cuff')
        line('finger',(34,16),(42,16));join('finger','hand')
''',reference='Lucide thumbs-down original and atomic-debug: coherent thumb/palm outline and separate cuff join; supplied source orientation retained.')

spec('user-avatar','VRECT_L',
     'The rejected generic open-bottom shoulders omit the closed shirt body of the supplied father portrait.',
     'Restored the closed torso and slightly enlarged the circular head, with smooth symmetric shoulders and exact bust contact.', '''
        circle('head',24,13,9)
        path('body',(8,44),[('L',(8,42)),('A',(24,26),16),('A',(40,42),16),('L',(40,44)),('L',(8,44))],True)
        join('head','body')
''',extra="    human_construction = 'bust'\n",reference='human_ref/user.svg: circular head and broad smooth shoulders; original father portrait supplies closed lower torso. 26-(13+9)=4 centerline/zero ink gap.')

def write(names):
    for row in ROWS:
        if names and row['icon_id'] not in names:continue
        s=SPECS[row['icon_id']];run=REPO/row['run']
        if list(run.glob('*.py')):
            previous=run
            attempt=int(re.search(r'attempt(\d+)$',run.name).group(1))+1
            run=run.with_name(re.sub(r'attempt\d+$',f'attempt{attempt}',run.name));run.mkdir(exist_ok=False)
            row['run']=str(run.relative_to(REPO))
            for n in ['reference.png','before.png']:
                if (previous/n).exists():shutil.copyfile(previous/n,run/n)
            (run/(row['icon_id']+'.metadata.json')).write_text(json.dumps(row,indent=2))
        from icon_set.model.keyshapes import Keyshape
        from icon_set.model.profiles import Profile
        bounds=getattr(Keyshape,s['key']).bounds_for(Profile.SOLO48)
        notes={**row,**{k:v for k,v in s.items() if k!='body'},'author':AUTHOR,'feedback':'No reason or written feedback recorded. Revision based on rendered original/current comparison.','bounds':str(bounds)}
        (run/'review-plan.json').write_text(json.dumps(notes,indent=2))
        doc=f"{s['change']}\nOriginal/current comparison: {s['issue']}\nPlan: {s['key']}, bounds {bounds}; shared circles, mirrored pairs and explicit joined nodes.\nReference: {s['reference']}"
        code=f'{doc!r}\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {row["source_uuid"]!r}\nSOURCE_PATH = {row["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {row["icon_id"]!r}\n    keyshape = Keyshape.{s["key"]}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(row["icon_id"].split("-"))!r}\n'+s['extra']+'\n    def build(self):\n'+HELPERS+s['body']
        module=run/(row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
        module.write_text(code)
        print(module.relative_to(REPO))
    (ROOT/'batch.json').write_text(json.dumps(ROWS,indent=2))

if __name__=='__main__':write(sys.argv[1:])
