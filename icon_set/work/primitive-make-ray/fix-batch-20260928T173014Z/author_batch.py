from pathlib import Path
import json
root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[m['source_uuid'] for m in rows]
SOURCE_PATH=[m['reference_path'] for m in rows]
from specs import drawings
helpers='''
    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)
'''
for i,m in enumerate(rows,1):
    key,ref,note,body=drawings[i];rd=Path(m['result_dir']);m.update(comparison=note,lucide=ref,keyshape=key,author=AUTHOR)
    (rd/'comparison.md').write_text(f'# Reference/current comparison\n\n{note}\n\nReviewer feedback: {m["feedback"]}\n\nConstruction reference: {ref}. Inspected original and atomic-debug where present. Preserve semantic silhouette and arrangement.\n')
    mod=rd/(m['icon_id'].replace('-','_')+'_'+m['source_uuid'].replace('-','_')+'.py')
    mod.write_text(f'''"""{note}
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: {ref}.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={m['source_uuid']!r}
SOURCE_PATH={m['reference_path']!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={m['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(m['concept'].split())!r}
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
{body}
{helpers}
''')
    m['module']=str(mod)
(root/'batch.json').write_text(json.dumps(rows,indent=2))
