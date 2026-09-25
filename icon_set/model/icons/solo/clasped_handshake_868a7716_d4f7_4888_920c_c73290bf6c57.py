"""Clasped handshake with rounded thumb and flowing lower palm.
Plan: Clasped handshake with rounded thumb and flowing lower palm.
Construction: Lucide hand: coherent curves and rounded fingertips.
Omissions: Individual finger divisions merged into a smooth lower palm."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '868a7716-d4f7-4888-920c-c73290bf6c57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fists crashing conflict_868a7716-d4f7-4888-920c-c73290bf6c57.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='clasped-handshake'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('clasped', 'handshake')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        poly('left-wrist',(4,24),(14,8),(24,14))
        poly('right-wrist',(44,24),(34,8),(24,14));join('left-wrist','right-wrist')
        path('clasp',(24,14),[('L',(16,22)),('C',(22,28),(10,28),(16,34)),('L',(28,22)),('L',(36,30)),('L',(36,33)),('C',(29,40),(36,38),(33,40)),('C',(8,40),(22,40),(16,40)),('L',(4,24))])
        join('clasp','left-wrist');join('clasp','right-wrist')
        line('right-palm',(44,24),(36,30));join('right-palm','clasp');join('right-palm','right-wrist')
