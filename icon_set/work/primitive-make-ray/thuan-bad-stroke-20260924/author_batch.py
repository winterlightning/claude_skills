from pathlib import Path
import json, re, importlib.util, cairosvg
from PIL import Image, ImageDraw
import io
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'
ROOT=Path(__file__).resolve().parents[4]
STAMP='20260924-clean-centerlines-thuan'
HELPERS='''
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
'''
DRAWINGS={}
def add(key,shape,plan,body): DRAWINGS[key]=(shape,plan,body)
add('air-pollution-fire','VRECT_L','Flame: rounded bowl, two rising tongues and a smooth inward lick. Lucide flame informs the continuous silhouette. Incomplete reference is completed from its named concept; no extra smoke.', '''
        path('flame',(24,4),[
            ('C',(40,28),(24,16),(40,16)),
            ('A',(8,28),16,16,True),
            ('C',(14,16),(8,22),(11,18)),
            ('C',(20,28),(12,23),(16,28)),
            ('C',(24,4),(28,28),(28,12))],True)
''')
add('conductor-with-raised-baton','SQUARE','Conductor with circular head, coherent curved shoulders and an angled raised baton. Human full_body_ref.png; head(24,12), r6, torso starts(24,26): exact 4 ink gap. Source action retained, outlined torso simplified.', '''
        circle('head',24,12,6)
        line('torso',(24,26),(24,42))
        path('left-arm',(24,26),[('L',(19,26)),('C',(9,32),(14,26),(14,32))])
        path('right-arm',(24,26),[('L',(29,26)),('C',(42,32),(34,26),(36,32))])
        line('baton',(9,32),(6,16))
        join('torso','left-arm');join('torso','right-arm');join('left-arm','right-arm');join('left-arm','baton')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add('craftsman-holding-a-hammer','SQUARE','Craftsman holds an upright hammer. Human full_body_ref.png owns r7 head(15,13) and torso junction(15,28), exact 4 ink gap. Lucide hammer informs square striking face. Smooth arm bends; body cropped as source.', '''
        circle('head',15,13,7)
        line('torso',(15,28),(15,42))
        path('left-arm',(15,28),[('C',(6,37),(10,28),(6,32)),('L',(6,42))])
        path('right-arm',(15,28),[('C',(29,36),(21,28),(23,36)),('L',(36,36))])
        box('hammer',30,14,42,24,2)
        poly('handle',(36,24),(36,36),(36,42))
        for a,b in [('torso','left-arm'),('torso','right-arm'),('left-arm','right-arm'),('hammer','handle'),('right-arm','handle')]:join(a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add('cupped-hands-beneath-a-cross','VRECT_L','Cross above mirrored cupped hand contours. Shared hand dimensions around x24; tangent-continuous rounded finger and palm transitions. Lucide hand informs rounded fingertips; source pose retained with fingers grouped.', '''
        poly('cross-stem',(24,4),(24,12),(24,22));poly('cross-arm',(16,12),(24,12),(32,12));join('cross-stem','cross-arm')
        for j,s in enumerate((-1,1)):
            def p(x,y):return (24+s*x,y)
            path(f'hand-{j}',p(16,44),[('L',p(16,32)),('A',p(8,32),4,4,s==-1),('C',p(4,40),p(8,36),p(4,36)),('L',p(4,44))])
''')
add('cupped-hands-share-component','VRECT_L','Full reference: three linked sharing nodes held above mirrored cupped hands. Lucide hand informs clean curved palms. Restore share symbol missing from rejected drawing; fingers reduced to single coherent strokes.', '''
        circle('share-top',24,7,3);circle('share-left',14,19,3);circle('share-right',34,19,3)
        line('link-left',(22,9),(16,17));line('link-right',(26,9),(32,17))
        for a,b in [('share-top','link-left'),('share-left','link-left'),('share-top','link-right'),('share-right','link-right')]:join(a,b)
        for j,s in enumerate((-1,1)):
            def p(x,y):return (24+s*x,y)
            path(f'hand-{j}',p(16,29),[('L',p(16,32)),('C',p(8,40),p(16,36),p(8,36)),('L',p(8,44))])
            path(f'thumb-{j}',p(8,40),[('C',p(4,32),p(8,36),p(6,34))]);join(f'hand-{j}',f'thumb-{j}')
''')
add('dog-leaping-over-triangular-obstacle','HRECT_L','Right-facing leaping dog over triangular hurdle. Lucide dog informs smooth organic contours; original reference supplies airborne side pose. Open spine and legs replace narrow doubled anatomy; retain head, muzzle, tail and triangle.', '''
        path('back',(4,8),[('C',(14,16),(4,14),(8,16)),('L',(28,16)),('C',(34,8),(32,16),(30,8)),('C',(40,12),(38,8),(37,12)),('L',(44,13)),('L',(44,17))])
        path('hind-leg',(14,16),[('C',(4,26),(12,23),(10,26))])
        path('front-leg',(28,16),[('C',(36,25),(29,21),(30,25)),('L',(44,25))])
        join('back','hind-leg');join('back','front-leg')
        poly('obstacle',(16,40),(24,31),(32,40),closed=True)
''')
add('person-operating-drone','SQUARE','Drone at upper left and operator at lower right. Shared rotor dimensions and horizontal capsule. Human full_body_ref.png: head center(36,26), r4, actual torso(36,38) leaves exact 4 ink gap. Lucide drone informs repeated arms. Cropped operator has curved arms meeting a controller.', '''
        path('drone',(12,14),[('L',(22,14)),('A',(22,22),4,4,True),('L',(12,22)),('A',(12,14),4,4,True)],True)
        for side,x in [('left',12),('right',22)]:
            line(side+'-boom',(x,6),(x,14));join(side+'-boom','drone')
        poly('rotor-left',(6,6),(12,6),(14,6));poly('rotor-right',(22,6),(26,6),(30,6))
        join('rotor-left','left-boom');join('rotor-right','right-boom')
        line('camera',(17,22),(17,25));join('camera','drone')
        circle('head',36,26,4)
        line('torso',(36,38),(36,42))
        path('arms',(28,42),[('C',(36,38),(28,38),(32,38)),('C',(42,42),(40,38),(42,38))])
        join('torso','arms')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add('person-raising-megaphone-with-sound-rays','SQUARE','Person raises curved megaphone with two sound rays. Human full_body_ref.png: head(11,26), r5; torso(11,39) exact 4 ink gap. Lucide megaphone informs curved flared horn. Smooth raised arm replaces angular elbow.', '''
        circle('head',11,26,5)
        line('torso',(11,39),(11,42));line('base',(6,42),(11,42))
        path('arm',(11,39),[('L',(18,39)),('C',(26,24),(25,39),(26,31))])
        path('horn',(26,24),[('C',(22,20),(23,24),(22,23)),('C',(26,14),(22,17),(23,16)),('C',(34,6),(30,12),(32,9)),('L',(34,26)),('C',(26,24),(31,24),(29,24))],True)
        line('ray-top',(42,9),(42,11));line('ray-bottom',(42,23),(42,25))
        join('arm','torso');join('torso','base');join('arm','horn')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
add('two-overlapping-busts-with-oval-heads','SQUARE','Two overlapping busts with equal circular heads and shared baseline. Human user.svg owns round heads and broad shoulders; Lucide users informs overlap. Source oval heads normalized to circular human vocabulary. Head bottoms18 and shoulders26 leave exact4 ink gap.', '''
        for side,x in [('left',14),('right',34)]:circle('head-'+side,x,12,6)
        path('body-left',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('C',(24,36),(20,26),(24,30)),('L',(24,42)),('L',(6,42))],True)
        path('body-right',(24,36),[('C',(34,26),(24,30),(28,26)),('A',(42,34),8,8,True),('L',(42,42)),('L',(24,42))]);join('body-left','body-right')
''')
add('upright-duck-with-long-neck','SQUARE','Left-facing upright duck: round head, long neck, swept breast and broad body. Lucide bird informs coherent curved silhouette and equal legs. Omit tiny eye and wing to keep open negative space. Deliberate directional asymmetry.', '''
        path('duck',(12,14),[('A',(24,14),6,8,True),('L',(24,22)),('A',(28,26),4,4,False),('L',(42,26)),('C',(32,36),(42,33),(38,36)),('L',(22,36)),('C',(12,28),(16,36),(12,33)),('C',(15,20),(12,25),(14,22)),('C',(12,14),(13,19),(12,17))],True)
        line('beak',(6,14),(12,14));join('beak','duck')
        for x in (22,32):line(f'leg-{x}',(x,36),(x,42));join(f'leg-{x}','duck')
''')

def generate(keys=None):
    for claim in sorted((ROOT/'icon_set/work/primitive-fix-thuan').glob('*/20260924T*-thuan-mac/claim.json')):
        data=json.loads(claim.read_text()); item=data['item']; key=item['icon_id']
        if key not in DRAWINGS or keys and key not in keys:continue
        ref=next((claim.parent/'reference').glob('*.svg')); uid=ref.stem[-36:]; concept=ref.stem[:-37]; reference=str(ref.relative_to(ROOT))
        out=ROOT/'icon_set/work/primitive-make-ray'/uid/STAMP;out.mkdir(parents=True,exist_ok=True)
        shape,plan,body=DRAWINGS[key]
        meta=dict(concept=concept,source_uuid=uid,reference_path=reference,icon_id=key,author=AUTHOR)
        (out/f'{key}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
        module=out/(key.replace('-','_')+'_'+uid.replace('-','_')+'.py')
        module.write_text(f'"""{plan}\nKeyshape {shape}; clean centerlines revision. Shared symbol parameters own paired geometry."""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uid!r}\nSOURCE_PATH={reference!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={key!r}\n    keyshape=Keyshape.{shape}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects/reference"\n    aliases=()\n    keywords={tuple(key.split("-"))!r}\n    def build(self):\n'+HELPERS+body)
        spec=importlib.util.spec_from_file_location('drawing',module);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);icon=mod.Drawing();report=icon.validate_icon();svg=icon.to_svg()
        (out/f'{key}.svg').write_text(svg);(out/'validation.txt').write_text(report.describe())
        for theme,ink,bg in [('light','#141413','#ffffff'),('dark','#f5f4ef','#1c1c19')]:
            for size in [48,384]:cairosvg.svg2png(bytestring=svg.replace('currentColor',ink).encode(),write_to=str(out/f'{key}-{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
        cairosvg.svg2png(url=str(ref),write_to=str(out/'reference.png'),output_width=384,output_height=384,background_color='white')
        print(key,report.status,len(report.errors),len(report.warnings));print(report.describe() if report.errors or report.warnings else '')
if __name__=='__main__': generate()
