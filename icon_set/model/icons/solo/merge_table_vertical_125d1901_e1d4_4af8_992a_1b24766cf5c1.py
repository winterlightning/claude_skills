from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '125d1901-e1d4-4af8-992a-1b24766cf5c1'
SOURCE_PATH = 'icon_set/work/todo-references/merge table vertical_125d1901-e1d4-4af8-992a-1b24766cf5c1.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'Two inward vertical arrows within an open four-corner table boundary.'
CONSTRUCTION_PLAN = 'One rounded corner definition is mirrored about x=24 and y=24. Equal arrows point toward the central gap. '
KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def rounded_rect(icon,name,left,top,right,bottom,r=4,split_y=None):
    points=[(left+r,top),(right-r,top),(right,top+r)]
    if split_y is not None: points.append((right,split_y))
    points += [(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r)]
    if split_y is not None: points.append((left,split_y))
    points += [(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%len(points)];n=f'{name}-{i}';members.append(n)
        if start[0]!=end[0] and start[1]!=end[1]: icon.add_arc(n,start,end,radius_x=r)
        else:icon.add_line(n,start,end)
    icon.add_contour(name,*members,closed=True)

class Drawing(Solo48):
    icon_id = 'merge-table-vertical'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('merge', 'table', 'vertical')

    def build(self):
        for sx in [-1,1]:
            for sy in [-1,1]:
                transform=lambda x,y:(24+sx*(x-24),24+sy*(y-24))
                n=f'corner-{sx}-{sy}'
                self.add_line(n+'-v',transform(6,18),transform(6,10))
                self.add_arc(n+'-a',transform(6,10),transform(10,6),radius_x=4,sweep=sx*sy>0)
                self.add_line(n+'-h',transform(10,6),transform(14,6))
                self.add_contour(n,n+'-v',n+'-a',n+'-h')
        for sy in [-1,1]:
            y=lambda v:24+sy*(v-24)
            n=f'arrow-{sy}'
            self.add_line(n+'-shaft',(24,y(6)),(24,y(18)))
            self.add_polyline(n+'-head',(20,y(14)),(24,y(18)),(28,y(14)))
            self.relate('connect',n+'-shaft',n+'-head')
