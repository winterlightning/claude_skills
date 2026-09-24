from pathlib import Path
import json,re
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
items=json.loads((Path(__file__).parent/'items.json').read_text())
helpers='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')
'''
def author(n,body,key='SQUARE',omissions='',plan=''):
 item=items[n-1];original=Path(item['original']).read_text();ident=re.search(r"icon_id\s*=\s*['\"]([^'\"]+)",original)[1]
 run=Path(item['run']);p=run/Path(item['original']).name
 header=f'''"""{item['concept']}: fresh spacing repair.
Plan: {plan}
Keyshape {key}: extrema derived from the profile's standard envelope.
Omissions: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={item['source_uuid']!r}
SOURCE_PATH={item['reference_path']!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={ident!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(item['concept'].split())!r}
'''
 p.write_text(header+helpers+'\n    def build(self):\n'+''.join('        '+l+'\n' for l in body.strip().splitlines()))
 (run/'design.json').write_text(json.dumps(dict(omissions=omissions,plan=plan,keyshape=key),indent=2))
