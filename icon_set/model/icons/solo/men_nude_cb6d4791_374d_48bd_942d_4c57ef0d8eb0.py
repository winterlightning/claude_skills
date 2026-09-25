from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cb6d4791-374d-48bd-942d-4c57ef0d8eb0'
SOURCE_PATH = 'pictographic-primitives/other/men nude_cb6d4791-374d-48bd-942d-4c57ef0d8eb0.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'A framed pictogram of male genital anatomy.'
CONSTRUCTION_PLAN = 'A diagonal shaft, rounded glans with seam, and curved scrotal outline sit inside a rounded square. Shared endpoint nodes define the glans seam; deliberate anatomical asymmetry. No useful Lucide anatomy match. Human construction guide inspected; detached-head rules do not apply. '
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
    icon_id = 'men-nude'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('men', 'nude')

    def build(self):
        rounded_rect(self,'frame',6,6,42,42)
        self.add_line('shaft-top',(15,21),(26,16))
        self.add_bezier('glans',(26,16),((32,13),(37,22),(30,26)))
        self.add_line('shaft-bottom',(30,26),(24,29))
        self.add_bezier('scrotum',(24,29),((28,34),(18,34),(15,30)))
        self.add_contour('anatomy','shaft-top','glans','shaft-bottom','scrotum')
        # Omit the minor glans seam to keep an open, legible anatomical silhouette.
