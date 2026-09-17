'oval-stadium-with-three-flags: Restore an open oval arena with a curved front wall and 3 triangular flags. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '784daa53-4af1-5316-897f-227157d2a0da'
SOURCE_PATH = 'pictographic-primitives/building/stadium classic_784daa53-4af1-5316-897f-227157d2a0da.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('784daa53-4af1-5316-897f-227157d2a0da', 'pictographic-primitives/building/stadium classic_784daa53-4af1-5316-897f-227157d2a0da.svg'),)

def _circle(icon, name, cx, cy, radius):
    left, right = (cx-radius, cy), (cx+radius, cy)
    icon.add_arc(name+'-upper', left, right, radius_x=radius)
    icon.add_arc(name+'-lower', right, left, radius_x=radius)
    icon.add_contour(name, name+'-upper', name+'-lower', closed=True)


def _box(icon, name, left, top, right, bottom, radius, attachments=()):
    # One rounded rectangle owns all corners and cardinal attachment nodes.
    cx, cy = (left+right)//2, (top+bottom)//2
    points = [(cx,top),(right-radius,top),(right,top+radius),
              (right,cy),(right,bottom-radius),(right-radius,bottom),
              (cx,bottom),(left+radius,bottom),(left,bottom-radius),
              (left,cy),(left,top+radius),(left+radius,top),(cx,top)]
    members = []
    for index, (start,end) in enumerate(zip(points,points[1:])):
        if start == end:
            continue
        member = f'{name}-{index}'
        if index in (1,4,7,10):
            icon.add_arc(member, start, end, radius_x=radius)
        else:
            dx,dy=end[0]-start[0],end[1]-start[1]
            inside=[p for p in attachments if (p[0]-start[0])*dy == (p[1]-start[1])*dx
                    and 0 < (p[0]-start[0])*dx+(p[1]-start[1])*dy < dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-start[0])*dx+(p[1]-start[1])*dy)
            nodes=[start]+inside+[end]
            for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
                part=member+f'-split-{j}'
                icon.add_line(part,a,b)
                members.append(part)
            continue
        members.append(member)
    icon.add_contour(name, *members, closed=True)


class OvalStadiumWithThreeFlags(Solo48):
    icon_id = 'oval-stadium-with-three-flags'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('oval', 'stadium', 'with', 'three', 'flags')

    def build(self):
        # Symbol plan: Restore an open oval arena with a curved front wall and 3 triangular flags.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        ellipse('rim',24,27,20,7)
        path('wall',(4,27),[('L',(6,36)),('C',(24,44),(8,42),(16,44)),('C',(42,36),(32,44),(40,42)),('L',(44,27))]);join('rim','wall')
        for i,x in enumerate((6, 22, 38)):
         poly('flag-'+str(i),(x,20),(x,4),(x+6,8))
         join('flag-'+str(i),'rim')
