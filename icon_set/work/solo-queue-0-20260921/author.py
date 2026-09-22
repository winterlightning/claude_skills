import json,re,sys
from pathlib import Path
w=Path(__file__).resolve().parent
COMMON="""        def path(name,start,steps,closed=False):
            point=start; members=[]
            for i,step in enumerate(steps):
                pid=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(pid,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(pid,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(pid)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True),((x,y-r),r,r,True)],True)
"""
def author(i,name,keyshape,plan,body):
 u=json.loads((w/'worklist.json').read_text())['uuids'][i]
 brief=json.loads((w/(u+'-briefs.json')).read_text())['brief']
 source=re.search(r'- source: `([^`]+)`',brief).group(1)
 tags=re.search(r'- tags: (.+)',brief).group(1).split(', ')
 title=brief.splitlines()[0][2:]
 p=Path('icon_set/model/icons/solo')/(name.replace('-','_')+'_'+u.replace('-','_')+'.py')
 p.write_text(repr(plan)+'\nfrom ...keyshapes import Keyshape\nfrom ._base import Solo48\n'+f'SOURCE_ICON_ID = {u!r}\nSOURCE_PATH = {source!r}\nAUTHOR = "gpt-6-astra"\nclass Drawing(Solo48):\n    icon_id = {name!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "Uncategorized"\n    aliases = {[title]!r}\n    keywords = {tags!r}\n    def build(self):\n'+COMMON+body+'\n')
 print(p)
 return p
