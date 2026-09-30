from pathlib import Path
import json,ast
from remaining_designs import D
ROOT=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
helpers=next(ast.literal_eval(n.value) for n in ast.parse((ROOT/'author.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='helpers' for t in n.targets))
helpers+='''
        def box(name,l,t,r,b,rad=0):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
'''
rs=json.loads((ROOT/'runs.json').read_text())
for claim in json.loads((ROOT/'remaining-claim-responses.json').read_text()):
 i=claim['item'];ident=i['icon_id'];p=Path('icon_set/work/primitive-fix-thuan')/i['key'].replace('/','__')/'20260929T130116Z-thuan-mac';ref=next((p/'reference').glob('*.svg'));uid=ref.stem[-36:];concept=ref.stem[:-37];run=Path('icon_set/work/primitive-make-ray')/uid/'20260929-batch11-attempt01';run.mkdir(parents=True,exist_ok=False)
 key,comparison,body=D[ident]
 r={'concept':concept,'source_uuid':uid,'reference_path':str(ref),'icon_id':ident,'feedback':i.get('feedback'),'comparison':comparison+' No written reviewer feedback.','run':str(run),'claim':str(p),'change':comparison.split('. ',1)[1]}
 (run/(ident+'.metadata.json')).write_text(json.dumps(r,indent=2));(run/'comparison.txt').write_text(r['comparison']+'\n')
 text=f'''"""{comparison}
Plan: {key} envelope; preserve source arrangement with coherent connected contours.
References: original and rejected SVGs visually compared before drawing.
Lucide apple/leaf for fruit and leaves, luggage for rounded case and straps,
scissors for crossing blades and loops, hand for rounded fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={uid!r}
SOURCE_PATH={str(ref)!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={ident!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(concept.split())!r}
    def build(self):
'''+helpers+body
 (run/(ident.replace('-','_')+'_'+uid.replace('-','_')+'.py')).write_text(text);rs.append(r)
(ROOT/'runs.json').write_text(json.dumps(rs,indent=2))
