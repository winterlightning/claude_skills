from pathlib import Path
import json,sys,datetime,textwrap,shutil
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts import primitive_fix as f,build_gate
B=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
HELPERS = """
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=3):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if a==z:continue
            q=n+str(i);ids.append(q)
            if i%2:self.add_arc(q,a,z,radius_x=k)
            else:self.add_line(q,a,z)
        self.add_contour(n,*ids,closed=True)
"""
def make(index,keyshape,body,problem,change,reference='No useful exact Lucide match; geometric construction from the supplied original.',omit='None',category='objects'):
    dirs=json.loads((B/'fix-dirs.json').read_text()); fix=Path(dirs[index]);item=json.loads((fix/'claim.json').read_text())['item']
    ref=next((fix/'reference').glob('*.svg'));uuid=f.UUID.search(ref.stem).group().replace('_','-');concept=ref.stem[:f.UUID.search(ref.stem).start()].rstrip('_-')
    run=Path('icon_set/work/primitive-make-ray')/uuid/('20260929-b15-1413-'+datetime.datetime.now().strftime('%H%M%S%f'))
    run.mkdir(parents=True);name=item['icon_id'];meta={'concept':concept,'source_uuid':uuid,'reference_path':str(ref)}
    (run/(name+'.metadata.json')).write_text(json.dumps(meta,indent=2))
    for label,source in [('original',ref),('before',next((fix/'before').glob('*.svg')))]:
        import cairosvg
        cairosvg.svg2png(url=str(source),write_to=str(run/(label+'.png')),output_width=384,output_height=384,background_color='white')
    (run/'comparison.md').write_text('Current error: '+problem+'\nFeedback: '+(item.get('feedback') or 'No written feedback; original reference governs.')+'\nRevision: '+change+'\nConstruction: '+reference+'\nOmissions: '+omit)
    source=f'''"""{change}
Symbol plan: {change}
Construction reference: {reference}
Omissions: {omit}
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID={uuid!r}
SOURCE_PATH={str(ref)!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={name!r}
    keyshape=Keyshape.{keyshape}
    semantic_role='MAIN'
    semantic_kind='noun'
    category={category!r}
    aliases=()
    keywords=()
'''+HELPERS+'\n    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
    module=run/(name.replace('-','_')+'_'+uuid.replace('-','_')+'.py');module.write_text(source)
    icon=f.load_icon(module);report=icon.validate_icon();svg=icon.to_svg();(run/(name+'.svg')).write_text(svg);(run/'validation.txt').write_text(report.describe())
    f.render_previews(svg,name,48,run);gate=build_gate.gate(module);(run/'gate.json').write_text(json.dumps(gate,indent=2))
    print(index,name,report.status,gate['status'],run,flush=True)
    for e in list(report.errors)+list(report.warnings)+gate['errors']+gate['warnings']:print(e,flush=True)
    state=json.loads((B/'runs.json').read_text()) if (B/'runs.json').exists() else {}
    state[str(index)]={'run':str(run),'fix':str(fix),'key':item['key'],'module':str(module),'problem':problem,'change':change,'reference':reference,'omissions':omit,'source_uuid':uuid,'reference_path':str(ref),'status':report.status,'gate':gate['status']}
    (B/'runs.json').write_text(json.dumps(state,indent=2))
    return run
