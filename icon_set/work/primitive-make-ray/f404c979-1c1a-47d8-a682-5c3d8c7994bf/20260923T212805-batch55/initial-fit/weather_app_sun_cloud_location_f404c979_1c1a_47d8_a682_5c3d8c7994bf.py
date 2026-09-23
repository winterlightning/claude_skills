"""Weather app sun cloud location, preserving its complete supplied composition.
Symbol plan: coherent contours, nested identifying symbols and parameterized repeats.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f404c979-1c1a-47d8-a682-5c3d8c7994bf'
SOURCE_PATH='icon_set/work/todo-references/weather app sun cloud location_f404c979-1c1a-47d8-a682-5c3d8c7994bf.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='weather-app-sun-cloud-location'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('weather', 'app', 'sun', 'cloud', 'location')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Complete sun/cloud/location composition, retaining all three symbols.
        self.add_arc('sun-upper',(8,16),(24,16),radius_x=8)
        self.add_bezier('sun-lower',(13,23),((10,23),(8,20),(8,16)))
        self.add_contour('sun','sun-lower','sun-upper')
        for n,a,b in [('north',(16,6),(16,7)),('west',(6,16),(7,16)),
                      ('northwest',(8,8),(9,9)),('northeast',(23,8),(24,7)),
                      ('southwest',(8,24),(7,25))]: self.add_line('ray-'+n,a,b)
        self.add_line('cloud-base',(22,34),(12,34))
        self.add_bezier('cloud-left',(12,34),((8,34),(6,31),(6,28)),((6,25),(9,23),(13,23)))
        self.add_bezier('cloud-crown',(13,23),((16,23),(16,16),(24,16)),((30,14),(34,18),(36,22)))
        self.add_bezier('cloud-right',(36,22),((40,22),(42,24),(42,28)),((42,30),(41,32),(40,33)))
        self.add_contour('cloud','cloud-base','cloud-left','cloud-crown','cloud-right')
        self.relate('connect','sun','cloud')
        self.add_arc('pin-top',(28,30),(40,30),radius_x=6)
        self.add_bezier('pin-lower',(40,30),((40,34),(36,40),(34,42)),((32,40),(28,34),(28,30)))
        self.add_contour('pin','pin-top','pin-lower',closed=True)
        self.circle('pin-hole',34,30,2)


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

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # Shared rectangle parameters own radii, symmetry and attachment nodes.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def shoulders(self,n,l,x,r,top,bottom):
        self.add_arc(n+'-left',(l,bottom),(x,top),radius_x=x-l,radius_y=bottom-top)
        self.add_arc(n+'-right',(x,top),(r,bottom),radius_x=r-x,radius_y=bottom-top)
        self.add_contour(n,n+'-left',n+'-right')

