from pathlib import Path
import json,textwrap
AUTHOR = 'gpt-6'
ROOT=Path(__file__).resolve().parent
ROWS=json.loads((ROOT/'batch.json').read_text())
SOURCE_ICON_ID = tuple(row['source_uuid'] for row in ROWS)
SOURCE_PATH = tuple(row['reference_path'] for row in ROWS)
HELPERS='''
        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
DESIGNS={}
def put(key,shape,reference,plan,code,omissions='None'):
 DESIGNS[key]=(shape,reference,plan,textwrap.dedent(code),omissions)

def write(keys=None):
 for row in ROWS:
  key=row['icon_id']
  if not row['result_dir'] or key not in DESIGNS or keys and key not in keys:continue
  shape,ref,plan,body,omissions=DESIGNS[key]
  run=Path(row['result_dir']);f=run/(key.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
  text=f'''"""{key}: {plan}\nLucide construction: {ref}; original and atomic-debug inspected.\nOmissions: {omissions}\nKeyshape {shape}: exact contract envelope; 4-unit stroke.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {row['source_uuid']!r}\nSOURCE_PATH = {row['reference_path']!r}\nAUTHOR = 'gpt-6'\nclass Drawing(Solo48):\n    icon_id = {key!r}\n    keyshape = Keyshape.{shape}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = 'objects'\n    aliases = ()\n    keywords = {tuple(key.split('-'))!r}\n    def build(self):\n'''+HELPERS+textwrap.indent(body,'        ')
  f.write_text(text)
  (run/'design.json').write_text(json.dumps(dict(keyshape=shape,lucide=ref,plan=plan,omissions=omissions),indent=2))
if __name__=='__main__':write()
