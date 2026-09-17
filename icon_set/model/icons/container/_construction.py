"""Small native-coordinate constructions for container authoring.

Dimensions belong to each caller; these helpers never scale finished artwork.
"""
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None


def path(icon, name, start, commands, closed=False):
    members = []
    here = start
    for i, (kind, end, *args) in enumerate(commands):
        member = f'{name}-{i}'
        if kind == 'L':
            icon.add_line(member, here, end)
        elif kind == 'A':
            rx, ry, sweep = args[:3]
            icon.add_arc(member, here, end, radius_x=rx, radius_y=ry,
                         sweep=sweep, large_arc=args[3] if len(args) > 3 else False)
        else:
            raise ValueError(kind)
        members.append(member)
        here = end
    icon.add_contour(name, *members, closed=closed)


def rounded_rect(icon, name, left, top, right, bottom, radius=4):
    r = radius
    path(icon, name, (left+r, top), [
        ('L', (right-r, top)), ('A', (right, top+r), r, r, True),
        ('L', (right, bottom-r)), ('A', (right-r, bottom), r, r, True),
        ('L', (left+r, bottom)), ('A', (left, bottom-r), r, r, True),
        ('L', (left, top+r)), ('A', (left+r, top), r, r, True),
    ], True)


def ellipse(icon, name, cx, cy, rx, ry=None):
    ry = rx if ry is None else ry
    path(icon, name, (cx-rx, cy), [
        ('A', (cx+rx, cy), rx, ry, True),
        ('A', (cx-rx, cy), rx, ry, True),
    ], True)
