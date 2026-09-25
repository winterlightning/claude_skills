"""Car Wheel Hubcap.

Plan: Circular hubcap with five spokes around a small central hub.
Reduction / construction: No useful Lucide hubcap match; keep five rays and rim, omit redundant second rim.
Envelope: CIRCLE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8643c72-9de8-4f6f-93e9-f369599363fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hubcap_a8643c72-9de8-4f6f-93e9-f369599363fe.svg'
AUTHOR = 'gpt-6'


class Batch064Icon13(Solo48):
    icon_id = 'five-spoke-wheel-hubcap-batch-064'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('five', 'spoke', 'wheel', 'hubcap')

    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            point=start
            for i,command in enumerate(commands):
                kind,end,*args=command
                member=f"{name}-{i}"
                if kind=='L':
                    self.add_line(member,point,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(member)
                point=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        # Integer points on two concentric circles own every true spoke join.
        vectors=[(0,-10),(8,-6),(6,8),(-6,8),(-8,-6)]
        for name,factor in (('rim',2),('hub',1)):
            nodes=[(24+factor*x,24+factor*y) for x,y in vectors]
            path(name,nodes[0],[('A',p,10*factor,10*factor,True) for p in nodes[1:]+nodes[:1]],True)
        for i,(x,y) in enumerate(vectors):
            self.add_line(f'spoke-{i}',(24+x,24+y),(24+2*x,24+2*y))
            self.relate('connect',f'spoke-{i}','rim')
            self.relate('connect',f'spoke-{i}','hub')
