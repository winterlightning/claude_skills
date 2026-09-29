"""Fresh standalone SOLO48 revisions; source identities are preserved per input."""
from pathlib import Path
import json, re, sys, textwrap
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
AUTHOR='gpt-6'
SOURCE_PATH=ROOT/'icon_set/work/primitive-fix-thuan/batch-20260928T165643Z/items.json'
ITEMS=json.loads(SOURCE_PATH.read_text())
SOURCE_ICON_ID=[re.search(r'([0-9a-f-]{36})\.svg$',i['reference']).group(1) for i in ITEMS]
HELPERS='''
    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')
'''
SPECS={}
def add(n,key,problem,change,code,ref,omissions='None.'):
    SPECS[n]=dict(keyshape=key,problem=problem,change=change,code=textwrap.dedent(code).strip(),construction_reference=ref,omissions=omissions)
add(1,'HRECT_M','The current stepped keyboard is vertically stretched relative to the wide reference; feedback says a bit long.','Shortened the vertical body, softened the stepped shoulders and retained both key rows and spacebar.', '''
self.path('case',(4,18),[('A',(8,14),4,4,True),('L',(12,14)),('L',(16,10)),('L',(32,10)),('L',(36,14)),('L',(40,14)),('A',(44,18),4,4,True),('L',(44,30)),('A',(40,34),4,4,True),('L',(36,34)),('L',(32,38)),('L',(16,38)),('L',(12,34)),('L',(8,34)),('A',(4,30),4,4,True),('L',(4,18))],True)
for row,y in enumerate((18,25)):
    for col,x in enumerate((16,24,32)):self.add_dot(f'key-{row}-{col}',(x,y))
self.add_line('spacebar',(17,32),(31,32))
''','Lucide keyboard: regular key series and rounded outer case.','End slots omitted to protect the central keys at 48 px.')
add(2,'HRECT_M','The current keyboard looks nearly square and short across its horizontal axis; feedback says a bit short.','Made the keyboard proportionally wider, with longer key dashes and a centered spacebar.', '''
self.box('case',4,10,44,38,4)
for row,y in enumerate((18,25)):
    for col,x in enumerate((14,24,34)):self.add_line(f'key-{row}-{col}',(x-1,y),(x+1,y))
self.add_line('spacebar',(14,32),(34,32))
''','Lucide keyboard: shared key spacing and quarter-circle case corners.','Four source keys per row reduced to three; two rows preserved.')
fork='''
# Three long, parallel teeth share a smooth U bowl and a diagonal handle.
self.path('fork-head',(6,16),[('L',(12,22)),('C',(20,20),(15,25),(18,22)),('C',(22,12),(22,18),(25,15)),('L',(16,6))])
self.add_line('fork-middle',(11,11),(20,20))
self.add_polyline('fork-handle',(20,20),(25,25),(42,42))
self.relate('connect','fork-head','fork-middle')
self.relate('connect','fork-head','fork-handle')
self.relate('connect','fork-middle','fork-handle')
'''
add(3,'SQUARE','The rejected fork has tiny teeth and reads like a bent trident; feedback specifically names the fork.','Lengthened all three fork teeth and rebuilt the bowl with smooth diagonal joins.',fork+'''
self.add_polyline('knife-handle',(6,42),(25,25),(30,20))
self.path('knife-blade',(30,20),[('L',(42,6)),('C',(36,26),(44,16),(41,21)),('L',(30,20))],True)
self.relate('connect','knife-handle','knife-blade')
self.relate('connect','knife-handle','fork-handle')
''','Lucide utensils-crossed: longer parallel teeth, continuous bowl, diagonal crossing.')
add(4,'SQUARE','The current fork teeth are stubby and hooked, unlike the reference; feedback names the fork.','Extended the three tines and smoothed the bowl; retained the diagonal oval spoon.',fork+'''
self.path('spoon-bowl',(30,19),[('C',(37,6),(26,15),(31,6)),('C',(42,11),(40,6),(42,8)),('C',(30,19),(42,17),(34,23))],True)
self.add_polyline('spoon-handle',(6,42),(25,25),(30,19))
self.relate('connect','spoon-handle','spoon-bowl')
self.relate('connect','spoon-handle','fork-handle')
''','Lucide utensils-crossed: parallel tines and coherent bowl; supplied reference: spoon oval.')
add(5,'HRECT_M','The current eye is too round and its pupil is a dot; the reference has an almond outline and outlined pupil.','Flattened the eye to a natural almond and restored a small circular pupil.', '''
self.path('eye',(4,24),[('C',(24,10),(9,17),(16,10)),('C',(44,24),(32,10),(39,17)),('C',(24,38),(39,31),(32,38)),('C',(4,24),(16,38),(9,31))],True)
self.circle('iris',24,24,8)
self.circle('pupil',24,24,2)
''','Lucide eye: mirrored almond arcs and concentric iris.')
add(6,'SQUARE','The displayed wing merges into the robe near the neck, closing the separation in the reference; feedback asks for wing_spacing.','Separated the open wing from the robe, restored a swept robe, circular head and open halo.', '''
# human_ref full_body_ref: circular head. Head bottom=24, body neck=32: 4 ink gap.
self.circle('head',34,20,4)
self.path('halo',(26,7),[('A',(42,7),8,3,True)])
self.path('robe',(34,32),[('C',(27,42),(34,36),(30,40)),('C',(6,32),(18,42),(9,36)),('C',(34,32),(16,32),(27,27))],True)
self.path('wing',(22,21),[('C',(6,6),(15,18),(9,10)),('C',(15,25),(3,15),(7,23))])
''','human_ref/full_body_ref.png for circular head and robe; supplied reference for wing, pose and halo. No useful local Lucide angel.','Halo uses an open arc to keep its opening clear; face and feather details omitted.')
add(7,'SQUARE','The current heart is narrow and shield-like, and the user head reads as a dot; the reference has a broad heart and outlined head.','Restored broad heart lobes and a circular user head above smooth open shoulders.', '''
self.path('heart',(24,12),[('C',(15,6),(20,8),(18,6)),('C',(6,16),(9,6),(6,10)),('C',(24,42),(6,27),(16,35)),('C',(42,16),(32,35),(42,27)),('C',(33,6),(42,10),(39,6)),('C',(24,12),(30,6),(28,8))],True)
self.circle('head',24,20,3)
# user.svg: circular head bottom 23, shoulder crest31 -> exact 4 ink gap.
self.path('shoulders',(18,34),[('A',(24,31),6,3,True),('A',(30,34),6,3,True)])
''','Lucide heart: broad lobes and tapered point; human_ref/user.svg: circular head and open shoulders.')
add(8,'SQUARE','The rejected hearts overlap and form a dense knot; the source separates a small upper-right heart from a larger broken heart.','Detached the small heart and reopened the large heart on its upper-right edge.', '''
self.path('small',(35,9),[('C',(30,6),(33,6),(31,6)),('C',(28,10),(28,6),(28,8)),('C',(35,20),(28,14),(32,17)),('C',(42,10),(38,17),(42,14)),('C',(40,6),(42,8),(42,6)),('C',(35,9),(39,6),(37,6))],True)
self.path('large',(24,21),[('C',(18,24),(22,20),(20,22)),('C',(12,20),(16,22),(14,20)),('C',(6,27),(8,20),(6,23)),('C',(20,42),(6,33),(14,38)),('C',(33,29),(26,37),(32,34))])
''','Lucide heart: rounded paired lobes; source: separate diagonal hearts and intentional break.','Large heart upper-right edge intentionally open as in source.')
add(9,'HRECT_M','The landscape phone has an oversized side panel and cramped dot; no original exists, so the displayed drawing is the reference.','Reduced the side panel, balanced the screen and replaced uneven corners with equal quarter circles.', '''
self.path('phone',(8,10),[('L',(17,10)),('L',(40,10)),('A',(44,14),4,4,True),('L',(44,34)),('A',(40,38),4,4,True),('L',(17,38)),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,14)),('A',(8,10),4,4,True)],True)
self.add_line('divider',(17,10),(17,38));self.relate('connect','phone','divider')
self.add_dot('button',(10,24))
''','Lucide smartphone: equal quarter-circle corners, one minimal hardware mark.')
add(10,'SQUARE','The big rear heart ends in an abrupt straight diagonal and sharp low point; feedback names the big heart line.','Redrew the rear heart with flowing flanks and a balanced point, retaining the smaller overlapping foreground heart.', '''
self.path('front',(31,22),[('C',(37,18),(33,19),(35,18)),('C',(42,24),(40,18),(42,20)),('C',(31,42),(42,31),(36,37)),('C',(20,24),(26,37),(20,31)),('C',(25,18),(20,20),(22,18)),('C',(31,22),(27,18),(29,19))],True)
self.path('rear',(22,32),[('C',(17,40),(20,35),(18,38)),('C',(6,19),(11,34),(6,26)),('C',(14,6),(6,10),(9,6)),('C',(22,11),(18,6),(20,8)),('C',(29,6),(24,8),(26,6)),('C',(37,18),(34,6),(37,11))])
self.relate('connect','rear','front')
''','Lucide heart: smooth lobe-to-flank curves; original: two overlapping hearts.','Hidden rear-heart edge omitted behind the foreground heart.')
phone_details={
11:"self.add_dot('camera',(24,13))",
12:"self.add_line('speaker',(21,13),(27,13))",
13:"""self.path('bell',(18,27),[('L',(18,22)),('A',(24,16),6,6,True),('A',(30,22),6,6,True),('L',(30,27))])
self.add_line('bell-base',(16,27),(32,27));self.relate('connect','bell','bell-base')
self.add_line('crown',(24,13),(24,16));self.relate('connect','bell','crown')""",
14:"self.add_dot('camera',(24,13))",
15:"self.add_polyline('check',(18,22),(22,26),(30,17))",
16:"for x in (20,28):self.add_line(f'pause-{x}',(x,16),(x,26))",
17:"""self.add_polyline('f',(19,28),(19,21),(19,13),(29,13))
self.add_line('f-middle',(19,21),(27,21));self.relate('connect','f','f-middle')""",
18:"self.add_line('home',(22,36),(26,36))",
19:"self.add_polyline('house',(18,28),(18,20),(24,14),(30,20),(30,28),closed=True)",
20:"self.add_line('home',(22,36),(26,36))"
}
for n,detail in phone_details.items():
    band=n not in (18,20)
    problem='The current handset is too wide relative to the upright reference and its corners are uneven or nearly square.'
    change='Narrowed the handset to VRECT_M, made every corner a tangent 4-unit quarter circle and centered its original screen/hardware marks.'
    if n==13:change+=' Restored the flared horizontal bell rim.'
    add(n,'VRECT_M',problem,change,f'self.phone({band})\n'+detail,'Lucide smartphone: shared rounded frame, balanced interior and minimal hardware marks.')

def author(n,attempt='r1'):
    i=ITEMS[n-1];s=SPECS[n];uuid=SOURCE_ICON_ID[n-1]
    out=ROOT/'icon_set/work/primitive-make-ray'/uuid/f'20260928T165643Z-fix-{n:02d}-{attempt}'
    out.mkdir(parents=True,exist_ok=False)
    concept=Path(i['reference']).stem[:-(len(uuid)+1)]
    metadata=dict(concept=concept,source_uuid=uuid,reference_path=i['reference'])
    (out/f"{i['icon_id']}.metadata.json").write_text(json.dumps(metadata,indent=2))
    review={k:v for k,v in s.items() if k!='code'};review.update(feedback=i['feedback'],before_svg=str(Path(i['fix_dir'])/'before'/f"{i['icon_id']}.svg"))
    (out/'review-before-drawing.json').write_text(json.dumps(review,indent=2))
    module=out/(i['icon_id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
    module.write_text(f'''"""{s['change']}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={uuid!r}
SOURCE_PATH={i['reference']!r}
AUTHOR={AUTHOR!r}
PLAN={s['change']!r}
CONSTRUCTION_REFERENCE={s['construction_reference']!r}
OMISSIONS={s['omissions']!r}
class Drawing(Solo48):
    icon_id={i['icon_id']!r}
    keyshape=Keyshape.{s['keyshape']}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(i['icon_id'].split('-'))!r}
{HELPERS}
    def build(self):
'''+textwrap.indent(s['code'],'        ')+'\n')
    icon=load_icon(module);r=icon.validate_icon();svg=icon.to_svg()
    (out/f"{i['icon_id']}.svg").write_text(svg)
    (out/'validation.txt').write_text(r.describe())
    render_previews(svg,i['icon_id'],48,out)
    import cairosvg
    cairosvg.svg2png(url=str(ROOT/i['reference']),write_to=str(out/'reference.png'),output_width=384,output_height=384)
    g=gate(module);(out/'gate.json').write_text(json.dumps(g,indent=2))
    print(n,i['icon_id'],r.status,'gate',g['status'],str(out.relative_to(ROOT)),flush=True)
    for msg in list(r.errors)+list(r.warnings)+g['errors']+g['warnings']:print(' ',msg,flush=True)
    return dict(n=n,**i,**metadata,run=str(out.relative_to(ROOT)),module=str(module.relative_to(ROOT)),spec=review,validation_status=r.status,gate=g)

if __name__=='__main__':
    records=[]
    for n in range(1,21):records.append(author(n,'r2' if n==1 else 'r1'))
    (Path(__file__).parent/'runs.json').write_text(json.dumps(records,indent=2))
