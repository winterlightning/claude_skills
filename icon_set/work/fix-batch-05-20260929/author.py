"""Batch 05 standalone primitive-make-ray authoring; metadata stays per input."""
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
def spec(name,key,issue,change,body,extra='',reference='No useful subject-specific Lucide match; supplied reference defines the subject.'):
    SPECS[name] = dict(key=key,issue=issue,change=change,body=body,extra=extra,reference=reference)

# DRAWINGS
spec('horizontal-bullet-with-separate-base','HRECT_M',
     'The rejected projectile ends in a semicircular D instead of the tapered nose in the original; the separate base has square corners.',
     'Rebuilt a tapered curved nose and rounded the separate rear bracket while retaining its clear gap.', '''
        path('base',(8,10),[('L',(6,10)),('A',(4,12),2,2,False),('L',(4,36)),('A',(6,38),2,2,False),('L',(8,38))])
        path('bullet',(17,10),[('L',(28,10)),('C',(44,24),(36,10),(42,18)),('C',(28,38),(42,30),(36,38)),('L',(17,38)),('L',(17,10))],True)
''')

spec('horizontal-axial-fuse-with-rounded-end-caps','HRECT_M',
     'The rejected fuse looks like a dumbbell, with a very thin central tube and square small-radius end caps.',
     'Thickened the central tube and used consistently rounded mirrored end caps with axial leads.', '''
        for name,cx in [('left',14),('right',34)]:
            path(name,(cx,10),[('A',(cx+4,14),4),('L',(cx+4,16)),('L',(cx+4,24)),('L',(cx+4,32)),('L',(cx+4,34)),('A',(cx,38),4),('A',(cx-4,34),4),('L',(cx-4,32)),('L',(cx-4,24)),('L',(cx-4,16)),('L',(cx-4,14)),('A',(cx,10),4)],True)
        for y in (16,32):
            n='tube-'+str(y);line(n,(18,y),(30,y));join(n,'left');join(n,'right')
        line('lead-left',(4,24),(10,24));join('lead-left','left')
        line('lead-right',(38,24),(44,24));join('lead-right','right')
''',reference='Lucide plug original and atomic-debug: rounded housings and leads attached at explicit wall nodes.')

spec('horizontal-adhesive-bandage','HRECT_M',
     'The rejected capsule has exaggerated semicircular ends and straight pad dividers; the source is a rounded strip with gently bowed dividers.',
     'Reduced the outer corner radius and restored two matched curved pad boundaries.', '''
        path('strip',(8,10),[('L',(18,10)),('L',(32,10)),('L',(40,10)),('A',(44,14),4),('L',(44,34)),('A',(40,38),4),('L',(32,38)),('L',(18,38)),('L',(8,38)),('A',(4,34),4),('L',(4,14)),('A',(8,10),4)],True)
        for x in (18,32):
            n='pad-'+str(x);bez(n,(x,10),((x-4,20),(x-4,28),(x,38)));join(n,'strip')
''',reference='Lucide bandage original and atomic-debug: rounded rectangular strip with structural pad divisions; source supplies curved dividers.')

spec('human-brain-hemispheres-batch-001-r2','SQUARE',
     'The rejected narrow hemispheres resemble two capsules and lose the original scalloped brain outline.',
     'Broadened the paired hemispheres and restored three distinct outer lobes around a centered fissure.', '''
        for side,s in [('left',-1),('right',1)]:
            def p(x,y):return (24+s*x,y)
            bez(side,p(0,14),
                (p(0,8),p(5,6),p(10,6)),
                (p(14,6),p(16,10),p(14,14)),
                (p(18,14),p(18,19),p(18,24)),
                (p(18,29),p(16,32),p(14,32)),
                (p(16,38),p(12,42),p(8,42)),
                (p(4,42),p(0,38),p(0,34)))
        line('fissure',(24,14),(24,34));join('left','right');join('left','fissure');join('right','fissure')
''',reference='Lucide brain original and atomic-debug: mirrored lobes, central fissure and distinct outer scallops. Fine folds omitted for native-size clarity.')

for variant in ('r3','r2'):
    spec('human-head-side-profile-scan-batch-001-'+variant,'SQUARE',
         'The rejected face has a cramped forehead and angular chin/nape; the original has smooth anatomical curves within an integrated scan boundary.',
         'Lengthened the forehead curve and rounded the chin and nape, preserving the integrated frame'+(' and ear.' if variant=='r3' else '.'), f'''
        path('profile',({24 if variant=='r3' else 28},15),[('A',(17,22),{7 if variant=='r3' else 11},{7 if variant=='r3' else 7},False),('L',(17,24)),('L',(14,28)),('L',(18,29)),('L',(18,31)),('C',(24,34),(18,33),(20,34)),('L',(24,42)),('L',(10,42)),('A',(6,38),4),('L',(6,10)),('A',(10,6),4),('L',(22,6)),('A',(42,26),20),('C',(38,42),(42,34),(34,34))])
        {"arc('ear',(30,21),(30,27),3)" if variant=='r3' else "# Fine ear detail omitted in this variant to emphasize the profile."}
''',reference='Shared human_ref/user.svg for anatomical vocabulary; original governs continuous profile and integrated boundary. No detached head/body pair.')

spec('heart-set-engagement-ring','VRECT_L',
     'The rejected heart is flat and triangular, whereas the original has a taller rounded jewel above a circular band.',
     'Deepened the heart and smoothed its lower sides, with an open rounded ring band beneath it.', '''
        path('heart',(24,12),[('A',(16,4),8,8,False),('A',(8,12),8,8,False),('C',(24,26),(8,17),(18,23)),('C',(40,12),(30,23),(40,17)),('A',(32,4),8,8,False),('A',(24,12),8,8,False)],True)
        path('band',(10,30),[('A',(24,44),14,14,False),('A',(38,30),14,14,False)])
''',reference='Lucide heart original and atomic-debug: matched lobes and flowing sides; supplied source retains heart above an open band.')

spec('high-column-two-tick-thermometer','VRECT_L',
     'The rejected thermometer reservoir is a solid dot and the bulb has abrupt side flares.',
     'Restored an outlined reservoir, a long high column and smoother bulb shoulders with two detached ticks.', '''
        path('outline',(11,24),[('L',(11,13)),('A',(29,13),9),('L',(29,24)),('C',(32,32),(29,27),(32,28)),('A',(8,32),12),('C',(11,24),(8,28),(11,27))],True)
        circle('reservoir',20,32,3)
        line('column',(20,14),(20,29));join('column','reservoir')
        for j,y in enumerate((14,24)):line(f'tick-{j}',(39,y),(40,y))
''',reference='Lucide thermometer original and atomic-debug: continuous tube and rounded bulb; source high column and two ticks preserved.')

spec('empty-battery-content','HRECT_M',
     'The rejected terminal is a detached bar; the original has a rounded terminal attached to the battery body.',
     'Restored the attached rounded terminal and retained a clean empty body.', '''
        path('body',(8,10),[('L',(30,10)),('A',(34,14),4),('L',(34,18)),('L',(34,30)),('L',(34,34)),('A',(30,38),4),('L',(8,38)),('A',(4,34),4),('L',(4,14)),('A',(8,10),4)],True)
        path('terminal',(34,18),[('L',(40,18)),('A',(44,22),4),('L',(44,26)),('A',(40,30),4),('L',(34,30))]);join('terminal','body')
''',reference='Lucide battery original and atomic-debug for rounded body construction; original specifically requires an attached terminal.')

spec('empty-battery-level-indicator-solo','HRECT_L',
     'The rejected level window is square and small; the original has a wide empty rectangular window.',
     'Replaced the square inset with a wider rectangular level window and regularized the outer corners.', '''
        path('battery',(8,8),[('L',(32,8)),('A',(36,12),4),('L',(36,16)),('L',(36,32)),('L',(36,36)),('A',(32,40),4),('L',(8,40)),('A',(4,36),4),('L',(4,12)),('A',(8,8),4)],True)
        poly('terminal',(36,16),(44,16),(44,32),(36,32));join('terminal','battery')
        poly('level',(13,20),(27,20),(27,28),(13,28),closed=True)
''',reference='Lucide battery original and atomic-debug: shared corner radii and terminal layout; original wide empty inset retained.')

spec('face-blowing-into-tissue','SQUARE',
     'The rejected zigzag tissue looks like a face mask; the original has a soft cloth gathered at the nose and hanging below.',
     'Rebuilt the tissue with a gathered top and draped lower edge, retaining the round face and closed eyes.', '''
        path('face',(10,34),[('A',(6,24),18),('A',(42,24),18),('A',(38,34),18)])
        for j,x in enumerate((18,30)):bez(f'eye-{j}',(x-2,19),((x-1,20),(x+1,20),(x+2,19)))
        path('tissue',(10,34),[('L',(20,28)),('C',(28,28),(22,27),(26,27)),('L',(38,34)),('L',(33,39)),('C',(24,42),(29,39),(29,42)),('C',(15,39),(19,42),(19,39)),('L',(10,34))],True)
        join('face','tissue')
        line('cloth-fold',(24,36),(24,42));join('cloth-fold','tissue')
''',reference='Shared human_ref/user.svg circular face vocabulary; supplied original defines closed eyes and gathered tissue. Fine folds omitted.')

spec('fairy-with-narrow-wings','SQUARE',
     'The rejected rigid triangular wings look like a bow tie and the head is undersized relative to the wings.',
     'Rebuilt the fairy as a full figure with a flared dress, two short legs and mirrored narrow curved wings.', '''
        circle('head',24,10,4)
        path('dress',(20,26),[('A',(28,26),4),('L',(28,30)),('L',(32,36)),('L',(28,36)),('L',(20,36)),('L',(16,36)),('L',(20,30)),('L',(20,26))],True)
        for x in (20,28):line('leg-'+str(x),(x,36),(x,42));join('leg-'+str(x),'dress')
        for side,s in [('left',-1),('right',1)]:
            def p(x,y):return (24+s*x,y)
            path('wing-'+side,p(18,18),[('C',p(13,23),p(17,21),p(14,22)),('C',p(18,28),p(15,25),p(17,26)),('C',p(14,29),p(17,29),p(16,29))])
''',reference='human_ref/full_body_ref.png: circular head above an outlined garment; actual gap 22-(10+4)=8 centerline/4 ink. Source narrow wings and short legs restored; this is an outlined figure, not a stick torso.')

spec('figure-broad-rain-poncho','SQUARE',
     'The rejected poncho has a rigid diamond hem and angular shoulders compared with the flowing garment in the original.',
     'Smoothed both shoulders and the broad curved hem while preserving the hood and circular lower face.', '''
        bez('hood',(16,20),((16,12),(18,6),(24,6)),((30,6),(32,12),(32,20)))
        bez('poncho',(16,20),((12,21),(9,28),(6,34)),((12,38),(19,42),(24,42)),((29,42),(36,38),(42,34)),((39,28),(36,21),(32,20)))
        arc('face',(16,20),(32,20),8,s=False)
        join('hood','poncho');join('hood','face');join('poncho','face')
''',reference='human_ref/user.svg circular face vocabulary; original broad hooded garment supplies silhouette and natural curved hem.')

spec('figure-wearing-headscarf-7530ebed','VRECT_L',
     'The rejected scarf is an open arch that runs into the shoulders, losing the wrapped lower edge around the face.',
     'Closed the headscarf around the circular face and attached distinct broad shoulders at shared cloth endpoints.', '''
        circle('face',24,18,5)
        path('scarf',(24,4),[('A',(38,18),14),('L',(38,22)),('C',(32,32),(38,27),(36,30)),('C',(24,34),(30,34),(26,34)),('C',(16,32),(22,34),(18,34)),('C',(10,22),(12,30),(10,27)),('L',(10,18)),('A',(24,4),14)],True)
        bez('shoulder-left',(8,44),((8,38),(12,34),(16,32)))
        bez('shoulder-right',(32,32),((36,34),(40,38),(40,44)))
        join('shoulder-left','scarf');join('shoulder-right','scarf')
''',reference='human_ref/user.svg for a circular blank face and broad shoulders; source headscarf is one continuous clothing outline. No detached head/body pair.')

spec('inverted-freestyle-skier-batch-051','SQUARE',
     'The rejected skis are tiny disconnected bars and read like a ladder beside the bent legs.',
     'Lengthened the two skis, attached the bent legs explicitly and retained the upside-down head and extended pole arm.', '''
        circle('head',28,38,4)
        line('torso',(28,26),(28,22))
        poly('leg-one',(28,22),(20,12),(14,12),(6,12))
        poly('leg-two',(28,22),(20,24),(14,24))
        poly('ski-one',(6,6),(6,12),(6,30))
        poly('ski-two',(14,6),(14,12),(14,24),(14,30))
        poly('arm',(28,26),(42,22),(42,6))
        for n in ('leg-one','leg-two','arm'):join('torso',n)
        join('leg-one','leg-two');join('ski-one','leg-one');join('ski-two','leg-one');join('ski-two','leg-two')
        self.mark_human_figure('skier',head='head',torso='torso',torso_junction='start')
''',reference='human_ref/full_body_ref.png: circular head and coherent limbs; inverted exact gap (38-4)-26=8 centerline/4 ink, aligned with actual upper torso.')

spec('isometric-room-grid-with-central-corner','VRECT_L',
     'The rejected centerline extends to the bottom vertex, making the room look like a fishbone instead of two walls and a floor.',
     'Terminated the central wall corner at the floor junction and rebuilt the separate floor plane under the wall grid.', '''
        nodes={'T':(24,4),'L':(8,14),'R':(40,14),'BL':(8,34),'BR':(40,34),'B':(24,44),'C':(24,28),'M':(24,14),'LM':(8,24),'RM':(40,24)}
        edges=[('T','L'),('T','R'),('L','LM'),('LM','BL'),('R','RM'),('RM','BR'),('BL','B'),('B','BR'),('T','M'),('M','C'),('BL','C'),('C','BR'),('LM','M'),('M','RM')]
        for i,(a,b) in enumerate(edges):line('edge-'+str(i),nodes[a],nodes[b])
        for i,(a,b) in enumerate(edges):
            for j,(c,d) in enumerate(edges[:i]):
                if {a,b}&{c,d}:join('edge-'+str(i),'edge-'+str(j))
''',reference='Lucide box original and atomic-debug: coherent isometric edge graph and shared junctions. Source room interpretation reverses the box depth and preserves the floor.')

spec('jaguar','HRECT_L',
     'The rejected jaguar has block-like legs, a triangular ear and an angular tail, unlike the rounded cat in the source.',
     'Rounded the ear, chest, feet and tail corner while keeping a clear feline silhouette and body spot.', '''
        path('cat',(4,20),[('C',(10,12),(8,17),(10,16)),('A',(16,12),3,4,True),('L',(20,12)),('L',(28,12)),('A',(36,20),8),('L',(36,38)),('A',(34,40),2),('L',(30,40)),('A',(28,38),2),('L',(28,30)),('L',(20,30)),('L',(20,38)),('A',(18,40),2),('L',(14,40)),('A',(12,38),2),('L',(12,27)),('C',(8,24),(12,25),(10,24)),('L',(4,24)),('L',(4,20))],True)
        path('tail',(36,20),[('L',(40,20)),('A',(44,24),4),('L',(44,34))]);join('tail','cat')
        self.add_dot('spot',(26,21))
''')

spec('jumbo-jet','SQUARE',
     'The rejected jet has a boxy tail and an abrupt small nose compared with the rounded, swept silhouette in the source.',
     'Enlarged the rounded nose and recomposed the swept wings and tail around the diagonal fuselage.', '''
        path('plane',(34,6),[('A',(42,14),8),('L',(32,24)),('L',(38,40)),('L',(30,42)),('L',(24,32)),('L',(16,40)),('L',(8,42)),('L',(6,34)),('L',(16,24)),('L',(6,16)),('L',(8,8)),('L',(24,16)),('L',(34,6))],True)
''',reference='Lucide plane original and atomic-debug: coherent diagonal fuselage with integrated swept wings and tail; supplied passenger-jet orientation retained.')

spec('kendo-practitioner','VRECT_L',
     'The rejected oversized head and short triangular robe make the practitioner look like a bust rather than the full martial artist in the reference.',
     'Reduced the head and lengthened the robe, retaining the two-handed sword junction and split lower garment.', '''
        circle('head',18,10,6)
        bez('torso',(18,24),((18,28),(21,30),(24,30)))
        poly('robe',(24,30),(30,30),(34,44),(22,44),(8,44),(10,30),(18,24));join('torso','robe')
        line('robe-split',(22,44),(22,36));join('robe-split','robe')
        line('sword',(24,30),(40,14));join('sword','torso');join('sword','robe')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''',reference='human_ref/full_body_ref.png: circular head and coherent body; actual detached gap 24-(10+6)=8 centerline/4 ink. Fine helmet band omitted to restore full-body proportions.')

spec('kazoo','SQUARE',
     'The rejected kazoo omits the circular membrane opening and reads like a wrench or bent tube.',
     'Restored the round membrane housing and inner opening, with tapered diagonal tube ends joined at exact nodes.', '''
        circle('membrane-housing',24,24,12)
        circle('opening',24,24,3)
        poly('mouthpiece',(12,24),(6,36),(12,42),(24,36));join('mouthpiece','membrane-housing')
        poly('bell',(24,12),(36,6),(42,12),(36,24));join('bell','membrane-housing')
''')

def write(names):
    for row in ROWS:
        if (names and row['icon_id'] not in names) or row['icon_id'] not in SPECS:continue
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
