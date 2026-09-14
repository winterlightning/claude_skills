"""Shared typed geometry for the payment batch, authored directly on SOLO48."""
SOURCE_ICON_ID = None
SOURCE_PATH = 'work/payments-solo/batch-01/briefs'
AUTHOR = 'gpt-6'


def rounded_rect(icon, name, left, top, right, bottom, radius):
    r=radius
    nodes=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,p in enumerate(nodes):
        ident=f'{name}-{i}'; q=nodes[(i+1)%len(nodes)]; members.append(ident)
        if i%2: icon.add_arc(ident,p,q,radius_x=r)
        else: icon.add_line(ident,p,q)
    icon.add_contour(name,*members,closed=True)


def circle(icon,name,x,y,r):
    icon.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
    icon.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)


def dollar(icon,x,y):
    # Two tangent half-ellipses with short terminal stems; no crossing microholes.
    rx,ry=6,4
    icon.add_line('dollar-top',(x+rx,y-2*ry),(x,y-2*ry))
    icon.add_arc('dollar-upper',(x,y-2*ry),(x,y),radius_x=rx,radius_y=ry,sweep=False)
    icon.add_arc('dollar-lower',(x,y),(x,y+2*ry),radius_x=rx,radius_y=ry)
    icon.add_line('dollar-foot',(x,y+2*ry),(x-rx,y+2*ry))
    icon.add_contour('dollar','dollar-top','dollar-upper','dollar-lower','dollar-foot')
    icon.add_line('dollar-stem-top',(x,y-2*ry-3),(x,y-2*ry))
    icon.add_line('dollar-stem-bottom',(x,y+2*ry),(x,y+2*ry+3))
    icon.relate('connect','dollar','dollar-stem-top')
    icon.relate('connect','dollar','dollar-stem-bottom')


def compact_currency(icon, kind, x, y):
    """Currency candidate retaining a readable 12-unit body; no tiny crossings."""
    if kind == 'dollar':
        rx, ry = 4, 3
        icon.add_line('currency-top', (x+rx,y-2*ry),(x,y-2*ry))
        icon.add_arc('currency-upper',(x,y-2*ry),(x,y),radius_x=rx,radius_y=ry,sweep=False)
        icon.add_arc('currency-lower',(x,y),(x,y+2*ry),radius_x=rx,radius_y=ry)
        icon.add_line('currency-foot',(x,y+2*ry),(x-rx,y+2*ry))
        icon.add_contour('currency','currency-top','currency-upper','currency-lower','currency-foot')
        icon.add_line('currency-stem-top',(x,y-2*ry-1),(x,y-2*ry))
        icon.add_line('currency-stem-bottom',(x,y+2*ry),(x,y+2*ry+1))
        icon.relate('connect','currency','currency-stem-top')
        icon.relate('connect','currency','currency-stem-bottom')
    elif kind == 'euro':
        icon.add_arc('currency-upper',(x+3,y-6),(x-4,y),radius_x=7,radius_y=6,sweep=False)
        icon.add_arc('currency-lower',(x-4,y),(x+3,y+6),radius_x=7,radius_y=6,sweep=False)
        icon.add_contour('currency','currency-upper','currency-lower')
        icon.add_line('currency-bar',(x-4,y),(x+2,y))
        icon.relate('connect','currency','currency-bar')
    elif kind == 'pound':
        # Open hook, crossing middle bar, and a distinct lower foot.
        icon.add_arc('currency-hook',(x+5,y-3),(x-3,y-3),radius_x=4,radius_y=3,sweep=False)
        icon.add_line('currency-stem-upper',(x-3,y-3),(x-3,y))
        icon.add_line('currency-stem-lower',(x-3,y),(x-3,y+8))
        icon.add_line('currency-foot',(x-3,y+8),(x+3,y+8))
        icon.add_contour('currency','currency-hook','currency-stem-upper','currency-stem-lower','currency-foot')
        icon.add_polyline('currency-bar',(x-4,y),(x-3,y),(x+1,y))
        icon.relate('connect','currency','currency-bar')
    else:
        icon.add_polyline('currency-fork',(x-5,y-6),(x,y),(x+5,y-6))
        icon.add_polyline('currency-stem',(x,y),(x,y+2),(x,y+6))
        icon.add_polyline('currency-bar',(x-4,y+2),(x,y+2),(x+4,y+2))
        icon.relate('connect','currency-fork','currency-stem')
        icon.relate('connect','currency-stem','currency-bar')


def draw_contactless(icon, kind):
    """An open-corner card, one contactless wave, and an attached right thumb."""
    icon.add_arc('signal-outer',(34,6),(42,14),radius_x=8)
    # Open upper-right corner reserves a contactless signal, while
    # the currency is left of the grasp instead of underneath the thumb.
    icon.add_line('card-right',(38,24),(38,27))
    icon.add_line('card-top-2',(25,6),(10,6))
    icon.add_arc('card-tl',(10,6),(6,10),radius_x=4,sweep=False)
    icon.add_line('card-left',(6,10),(6,34))
    icon.add_arc('card-bl',(6,34),(10,38),radius_x=4,sweep=False)
    icon.add_line('card-bottom',(10,38),(35,38))
    icon.add_contour('card','card-top-2','card-tl','card-left','card-bl','card-bottom')
    icon.add_line('thumb-upper',(42,30),(38,27))
    icon.add_arc('thumb-round',(38,27),(32,35),radius_x=5,sweep=False)
    icon.add_line('thumb-lower-1',(32,35),(35,38))
    icon.add_line('thumb-lower-2',(35,38),(39,42))
    icon.add_line('wrist',(39,42),(42,42))
    icon.add_contour('thumb','thumb-upper','thumb-round','thumb-lower-1','thumb-lower-2','wrist')
    icon.relate('connect','card','thumb')
    icon.relate('connect','card-right','thumb')
    cx,cy = (19,22) if kind=='dollar' else ((20,21) if kind=='yuan' else (19,21))
    compact_currency(icon,kind,cx,cy)
