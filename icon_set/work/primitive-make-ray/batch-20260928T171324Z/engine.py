"""Fresh standalone SOLO48 revisions; source identities are preserved per input."""
from pathlib import Path
import json, re, sys, textwrap
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
AUTHOR='gpt-6'
SOURCE_PATH=ROOT/'icon_set/work/primitive-fix-thuan/batch-20260928T171324Z/items.json'
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
def author(n,attempt='r1'):
    i=ITEMS[n-1];s=SPECS[n];uuid=SOURCE_ICON_ID[n-1]
    out=ROOT/'icon_set/work/primitive-make-ray'/uuid/f'20260928T171324Z-fix-{n:02d}-{attempt}'
    out.mkdir(parents=True,exist_ok=False)
    concept=Path(i['reference']).stem[:-(len(uuid)+1)]
    metadata=dict(concept=concept,source_uuid=uuid,reference_path=i['reference'])
    (out/f"{i['icon_id']}.metadata.json").write_text(json.dumps(metadata,indent=2))
    review={k:v for k,v in s.items() if k!='code'};review.update(feedback=i['feedback'],before_svg=str(Path(i['fix_dir'])/'before'/f"{i['icon_id']}.svg"))
    (out/'review-before-drawing.json').write_text(json.dumps(review,indent=2))
    module=out/(i['icon_id'].replace(uuid,'').strip('-').replace('-','_')+'_'+uuid.replace('-','_')+'.py')
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

