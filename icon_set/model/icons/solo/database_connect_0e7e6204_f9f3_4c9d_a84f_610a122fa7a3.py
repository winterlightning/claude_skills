"""database-connect: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e7e6204-f9f3-4c9d-a84f-610a122fa7a3'
SOURCE_PATH = 'pictographic-primitives/programing/database connect_0e7e6204-f9f3-4c9d-a84f-610a122fa7a3.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DatabaseConnect(Solo48):
    icon_id = 'database-connect'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('database', 'connect', 'programing')

    def build(self):
        # Plan: SQUARE; four identical circles with exact Pythagorean boundary attachments, matched spokes, and no inward hooks.
        # Reference: Lucide node construction principles; original four-node network retained.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry=None):
            ry=rx if ry is None else ry
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        # Radius-five circles have exact integer 3:4 attachment points.
        for i,flipx,flipy in [(0,False,False),(1,True,False),(2,False,True),(3,True,True)]:
         def p(x,y):return (48-x if flipx else x,48-y if flipy else y)
         sweep=not (flipx ^ flipy)
         commands=[('A',p(x,y),5,5,sweep) for x,y in [(14,15),(11,16),(6,11),(11,6),(16,11)]]
         path(f'node-{i}',p(16,11),commands,True)
         self.add_line(f'spoke-{i}',p(14,15),(24,24));self.relate('connect',f'spoke-{i}',f'node-{i}')
        for a in range(4):
         for b in range(a):self.relate('connect',f'spoke-{a}',f'spoke-{b}')
