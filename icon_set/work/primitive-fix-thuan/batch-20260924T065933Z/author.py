from pathlib import Path
import json,re,textwrap,sys,importlib.util,io
import cairosvg
from PIL import Image,ImageDraw
ROOT=Path.cwd(); BATCH=Path(__file__).parent
AUTHOR='gpt-6'
RUN='20260924T071000Z-thuan-mac'
HELPERS='''
    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
'''
D={}
def add(name,key,brief,body,refs='',omit='None'):
 D[name]=(key,brief,textwrap.dedent(body),refs,omit)
add('microphone-b72da6ab','VRECT_L','Microphone capsule with a smooth semicircular cradle and short stem.', '''
self.path('capsule',(18,10),[('A',(30,10),6,6,True),('L',(30,20)),('A',(18,20),6,6,True),('L',(18,10))],True)
self.path('cradle',(8,22),[('L',(8,24)),('A',(24,40),16,16,False),('A',(40,24),16,16,False),('L',(40,22))])
self.add_line('stem',(24,40),(24,44));self.relate('connect','stem','cradle')
''','mic: capsule and concentric cradle','Small grille notch removed because it crowds the capsule opening.')
for n in ['shield-9d1518e9','shield-ba7b0c51']:
 add(n,'VRECT_L','Symmetric pointed shield with concave top edges and long smooth sides.', '''
# Shared axis x=24, mirrored circular sides; extremes (8,4)-(40,44).
self.path('shield',(24,4),[('A',(40,12),40,40,False),('A',(24,44),40,40,True),('A',(8,12),40,40,True),('A',(24,4),40,40,False)],True)
''','shield: coherent symmetric outline')
add('peace-symbol','CIRCLE','Circular peace emblem with a vertical stem and two downward diagonal branches.', '''
# All ring nodes lie on radius20 about (24,24), using 12/16/20 triangles.
nodes=[(24,4),(44,24),(36,40),(24,44),(12,40),(4,24),(24,4)]
self.path('rim',nodes[0],[('A',p,20,20,True) for p in nodes[1:]],True)
for n,p in [('top',(24,4)),('bottom',(24,44)),('left',(12,40)),('right',(36,40))]:
    self.add_line(n,(24,24),p);self.relate('connect',n,'rim')
for i,a in enumerate(['top','bottom','left','right']):
    for b in ['top','bottom','left','right'][i+1:]:self.relate('connect',a,b)
''','No useful exact Lucide match; exact circle and shared junction')
add('shottkey-diode','SQUARE','Diagonal electronic component with a clean rectangular body and two aligned leads.', '''
# Body and leads share the diagonal axis; deliberate 45-degree orientation.
self.add_polyline('body',(14,26),(26,14),(30,18),(34,22),(22,34),(18,30),closed=True)
self.add_line('lead-top',(30,18),(42,6));self.add_line('lead-bottom',(18,30),(6,42))
self.relate('connect','lead-top','body');self.relate('connect','lead-bottom','body')
''','No useful exact Lucide match; single joined rectangle','Tiny corner bevels simplified to round stroke joins.')
add('sauna-heat-stone','SQUARE','Three coherent heat waves rise over a smooth stone bowl.', '''
# Identical two-arc waves own spacing; opposing sweeps meet tangentially.
for i,x in enumerate([12,24,36]):
    self.path('heat-'+str(i),(x+2,6),[('A',(x,15),7,7,False),('A',(x-2,24),7,7,True)])
self.path('stone',(6,32),[('A',(24,42),18,10,False),('A',(42,32),18,10,False)])
''','No useful exact Lucide match; repeated smooth arcs')
add('smart-glasses-with-raised-temple-arms','HRECT_L','Broad smart-glasses frame with mirrored smooth raised temples.', '''
self.path('frame',(4,24),[('L',(44,24)),('L',(44,36)),('A',(40,40),4,4,True),('L',(32,40)),('A',(28,36),4,4,True),('A',(20,36),4,4,False),('A',(16,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,24))],True)
# The long elliptical shoulder ends with a horizontal tangent at each tip.
for i in range(2):
    def q(x,y):return (x if i==0 else 48-x,y)
    self.path('temple-'+str(i),q(4,24),[('A',q(14,8),10,16,i==0),('L',q(16,8))])
    self.relate('connect','temple-'+str(i),'frame')
''','glasses: mirrored temples and nose bridge')
add('girl-pigtails','VRECT_L','Girl with circular head, paired pigtails and a smooth flared body.', '''
# Shared human user.svg proportions, head radius8; body apex28 minus head bottom20 =8.
self.oval('head',24,12,8)
for i,s in enumerate([-1,1]):
    self.path('hair-'+str(i),(24+s*8,12),[('A',(24+s*15,22),12,12,s<0)])
    self.relate('connect','hair-'+str(i),'head')
# Smooth elliptical arch reaches exact bottom and width without shoulder kinks.
self.path('body',(8,44),[('A',(40,44),16,16,True)])
''','human_ref/user.svg: circular head and broad open body; user-round: coherent shoulder arc')
add('person-with-angular-heart-torso','SQUARE','A round head above a heart-shaped torso with smooth paired lobes.', '''
# Circular head and paired lobes: center separation20, radii6+6 gives exact gap8.
self.oval('head',24,12,6)
self.path('heart',(24,34),[('L',(18,28)),('A',(6,28),6,6,False),('A',(10,34),10,10,False),('L',(24,42)),('L',(38,34)),('A',(42,28),10,10,False),('A',(30,28),6,6,False),('L',(24,34))],True)
''','heart: smooth lobes and a pointed tip; human_ref/user.svg: round detached head')
add('skull-85266d86','VRECT_L','Skull with a round cranium, narrowing cheekbones and three open lower teeth.', '''
self.path('cranium',(15,44),[('L',(15,38)),('L',(12,32)),('A',(8,20),20,20,True),('A',(40,20),16,16,True),('A',(36,32),20,20,True),('L',(33,38)),('L',(33,44))])
self.add_line('tooth',(24,38),(24,44))
for x in [18,30]:self.add_dot('eye-'+str(x),(x,23))
''','skull: coherent rounded cranium','Eye dots retained as the meaningful completion of the faint source eyes.')

def write(name):
 key,brief,body,refs,omit=D[name]
 claim=next(Path('icon_set/work/primitive-fix-thuan').glob('solo__'+name+'/20260924T065933Z-thuan-mac/claim.json'))
 source=next((claim.parent/'reference').glob('*.svg'))
 SOURCE_ICON_ID=re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',source.stem).group();SOURCE_PATH=str(source)
 concept=source.stem[:-(len(SOURCE_ICON_ID)+1)]
 out=Path('icon_set/work/primitive-make-ray')/SOURCE_ICON_ID/RUN;out.mkdir(parents=True,exist_ok=True)
 meta=dict(concept=concept,source_uuid=SOURCE_ICON_ID,reference_path=SOURCE_PATH,icon_id=name,author=AUTHOR)
 (out/(name+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
 file=out/(name.replace('-','_')+'_'+SOURCE_ICON_ID.replace('-','_')+'.py')
 file.write_text(f'"""{brief}\nSymbol plan: shared parameters and coherent contours.\nConstruction: {refs}.\nOmissions: {omit}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={SOURCE_ICON_ID!r}\nSOURCE_PATH={SOURCE_PATH!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={name!r}\n    keyshape=Keyshape.{key}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="objects/general"\n    aliases=()\n    keywords={tuple(name.split("-"))!r}\n'+HELPERS+'\n    def build(self):\n'+textwrap.indent(body.strip(),'        ')+'\n')
 cairosvg.svg2png(url=str(source),write_to=str(out/'reference.png'),output_width=240,output_height=240,background_color='white')
 return out

def export(out):
 file=next(out.glob('*.py'));spec=importlib.util.spec_from_file_location('candidate_'+out.parent.name.replace('-','_'),file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);icon=m.Drawing();r=icon.validate_icon()
 (out/'validation.txt').write_text(r.describe()+'\n');svg=icon.to_svg();(out/(icon.icon_id+'.svg')).write_text(svg)
 for theme,bg,fg in [('light','white','black'),('dark','#171717','white')]:
  for size in [48,240]:
   cairosvg.svg2png(bytestring=svg.replace('currentColor',fg).replace('#000000',fg).encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
 print(icon.icon_id,r.status,len(r.errors),len(r.warnings),flush=True)
 if r.errors or r.warnings:print(r.describe(),flush=True)
 return r
if __name__=='__main__':
 for name in sys.argv[1:] or D:
  export(write(name))
