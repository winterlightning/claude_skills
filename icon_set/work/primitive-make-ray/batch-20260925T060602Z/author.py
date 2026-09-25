from pathlib import Path
import json,re,textwrap,hashlib
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"
BATCH = Path(__file__).parent
items = json.loads((BATCH/'items.json').read_text())
HELPERS = """
        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
"""
DESIGNS={}
def design(i,key,plan,body,ref): DESIGNS[i]=(key,plan,textwrap.dedent(body),ref)
from designs import populate
populate(design)

def write_all():
    for i,(key,plan,body,ref) in DESIGNS.items():
        item=items[i]; source=Path(item['reference']); uuid=source.stem[-36:]
        run=Path('icon_set/work/primitive-make-ray')/uuid/'20260925T060602Z-thuan-mac-redraw'
        run.mkdir(parents=True,exist_ok=True)
        metadata={'concept':source.stem[:-37],'source_uuid':uuid,'reference_path':str(source)}
        (run/(item['id']+'.metadata.json')).write_text(json.dumps(metadata,indent=2))
        module=run/(item['id'].replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        header=f'''"""{plan}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {str(source)!r}
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = {item['id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ({metadata['concept']!r},)

    def build(self):
        # Symbol plan: {plan}
        # Construction reference: Lucide {ref}; original supplied subject controls meaning.
'''
        module.write_text(header+HELPERS+textwrap.indent(body.strip(),'        ')+'\n')
        item.update(run=str(run),module=str(module),plan=plan,lucide=ref,keyshape=key)
    (BATCH/'items.json').write_text(json.dumps(items,indent=2))

if __name__=='__main__':write_all()
