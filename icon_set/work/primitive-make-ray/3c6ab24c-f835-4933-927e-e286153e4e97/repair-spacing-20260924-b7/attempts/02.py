"""workflow agreement: fresh spacing repair.
Plan: Mirrored busts follow user.svg; head bottom 34, shoulder apex 42 give exactly 8 centerline / 4 ink gap.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Bubble tails removed. Busts reduced to minimal paired head and shoulders.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3c6ab24c-f835-4933-927e-e286153e4e97'
SOURCE_PATH='pictographic-primitives/_uncategorized_40/workflow agreement_3c6ab24c-f835-4933-927e-e286153e4e97.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='workflow-agreement'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('workflow', 'agreement')

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

    def build(self):
        self.path('bubble',(16,4),[('L',(32,4)),('A',(36,8),4),('L',(36,18)),('A',(32,22),4),('L',(16,22)),('A',(12,18),4),('L',(12,8)),('A',(16,4),4)],True)
        self.add_polyline('check',(21,12),(24,14),(27,12))
        for i,x in enumerate((11,37)):
            self.circle(f'head-{i}',x,32,2)
            self.add_arc(f'body-{i}',(x-3,44),(x+3,44),radius_x=3,radius_y=2)
