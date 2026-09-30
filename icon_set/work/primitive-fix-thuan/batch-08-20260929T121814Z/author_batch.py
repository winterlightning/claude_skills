from pathlib import Path
import json, re, datetime, sys
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
BASE=Path(__file__).parent
rows=json.loads((BASE/'claims.json').read_text())
HELPERS='''
    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
'''
from draw_specs import SPECS
def author(indices):
    manifest=json.loads((BASE/'runs.json').read_text()) if (BASE/'runs.json').exists() else {}
    for idx in indices:
        r=rows[idx]; key=r['key'].split('/')[1]; ref=Path(r['ref']);uuid=re.search(r'[0-9a-f-]{36}$',ref.stem).group();concept=ref.stem[:-37]
        shape,finding,construction,body=SPECS[idx]
        stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-batch08')
        out=ROOT/'icon_set/work/primitive-make-ray'/uuid/stamp;out.mkdir(parents=True)
        metadata=dict(concept=concept,source_uuid=uuid,reference_path=r['ref'])
        (out/f'{key}.metadata.json').write_text(json.dumps(metadata,indent=2))
        (out/'review-before.txt').write_text(finding+'\n'+construction+'\n')
        import shutil
        shutil.copy(BASE/f'{idx+1}-ref.png',out/'reference.png');shutil.copy(BASE/f'{idx+1}-before.png',out/'before.png')
        human="    human_construction='bust'\n" if idx in (11,) else ''
        source=f'''"""{finding}\nSymbol plan: {construction}\nKeyshape {shape}, authored on the SOLO48 integer grid with 4-unit strokes.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={r['ref']!r}\nAUTHOR='gpt-6'\nclass Drawing(Solo48):\n    icon_id={key!r}\n    keyshape=Keyshape.{shape}\n    semantic_role='MAIN'\n    semantic_kind='noun'\n    category='primitives-generate'\n    aliases=()\n    keywords={tuple(key.split('-'))!r}\n'''+human+HELPERS+'\n    def build(self):\n'+body
        module=out/(key.replace('-','_')+'_'+uuid.replace('-','_')+'.py');module.write_text(source)
        icon=load_icon(module);report=icon.validate_icon();(out/'validation.txt').write_text(report.describe())
        svg=icon.to_svg();(out/f'{key}.svg').write_text(svg);render_previews(svg,key,48,out)
        g=gate(module,out/'gate');(out/'gate.json').write_text(json.dumps(g,indent=2))
        print(idx+1,key,report.describe(),g,flush=True)
        manifest[str(idx)]=str(out.relative_to(ROOT));(BASE/'runs.json').write_text(json.dumps(manifest,indent=2))
if __name__=='__main__':author([int(a)-1 for a in sys.argv[1:]] or list(range(20)))
