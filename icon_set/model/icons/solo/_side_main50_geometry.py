"""Shared typed shapes for the September 19 SOLO48 source batch; no scaling."""
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'


def circle(icon, name, cx, cy, radius):
    icon.add_arc(name+'-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
    icon.add_arc(name+'-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
    icon.add_contour(name, name+'-top', name+'-bottom', closed=True)


def path(icon, name, start, segments, closed=False):
    """A coherent line/arc contour with explicit integer nodes."""
    point = start
    members = []
    for index, segment in enumerate(segments):
        ident = f'{name}-{index}'
        end = segment[1]
        if segment[0] == 'L':
            icon.add_line(ident, point, end)
        else:
            icon.add_arc(ident, point, end, radius_x=segment[2],
                         radius_y=segment[3], sweep=segment[4],
                         large_arc=segment[5] if len(segment)>5 else False)
        members.append(ident)
        point = end
    icon.add_contour(name, *members, closed=closed)


def box(icon, name, left, top, right, bottom, radius=4, nodes=()):
    """Rounded rectangle with split straight sides at real attachment nodes."""
    points=[(left+radius,top),(right-radius,top),(right,top+radius),
            (right,bottom-radius),(right-radius,bottom),(left+radius,bottom),
            (left,bottom-radius),(left,top+radius),(left+radius,top)]
    segments=[]
    for i,(a,b) in enumerate(zip(points,points[1:])):
        if i%2:
            segments.append(('A',b,radius,radius,True))
        else:
            on=[p for p in nodes if p!=a and p!=b and
                min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and
                min(a[1],b[1])<=p[1]<=max(a[1],b[1])]
            on.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
            segments.extend(('L',p) for p in [*on,b] if p!=a)
    path(icon,name,points[0],segments,True)
