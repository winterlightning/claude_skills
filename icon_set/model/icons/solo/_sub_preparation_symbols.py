"""Direct SOLO48 constructions for user-authorized symbolic sub preparation.
Each enclosure and glyph is authored on integer coordinates for its actual space.
These are not scaled typeface paths. No text/word/number generation is performed.
"""
from ._payments_batch01 import circle, rounded_rect, compact_currency
SOURCE_ICON_ID=None
SOURCE_PATH='work/solo-sub-backlog-20260917/symbol-selection.json'
AUTHOR='gpt-6'

def bubble(i):
    i.add_line('top',(14,4),(34,4))
    i.add_arc('tr',(34,4),(40,10),radius_x=6)
    i.add_line('right',(40,10),(40,34))
    i.add_arc('br',(40,34),(34,40),radius_x=6)
    i.add_line('bottom',(34,40),(18,40))
    i.add_line('tail',(18,40),(8,44))
    i.add_line('left',(8,44),(8,10))
    i.add_arc('tl',(8,10),(14,4),radius_x=6)
    i.add_contour('outline','top','tr','right','br','bottom','tail','left','tl',closed=True)

def document(i):
    i.add_polyline('outline',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)

def wireless_phone(i):
    i.add_bezier('signal',(8,10),((16,2),(32,2),(40,10)))
    i.add_line('left',(8,19),(8,38))
    i.add_arc('bl',(8,38),(14,44),radius_x=6,sweep=False)
    i.add_line('bottom',(14,44),(34,44))
    i.add_arc('br',(34,44),(40,38),radius_x=6,sweep=False)
    i.add_line('right',(40,38),(40,19))
    i.add_contour('phone','left','bl','bottom','br','right')

def banknote(i):
    rounded_rect(i,'outline',4,8,44,40,4)

def moneybag(i):
    i.add_line('neck-a',(14,10),(12,4))
    i.add_line('neck-b',(12,4),(36,4))
    i.add_line('neck-c',(36,4),(34,10))
    i.add_bezier('bag',(34,10),((40,14),(40,18),(40,35)),((40,44),(32,44),(24,44)),((16,44),(8,44),(8,35)),((8,18),(8,14),(14,10)))
    i.add_contour('outline','neck-a','neck-b','neck-c','bag',closed=True)

def house(i):
    i.add_polyline('outline',(6,42),(6,22),(24,6),(42,22),(42,42))

def monitor(i):
    rounded_rect(i,'screen',8,4,40,40,4)
    i.add_line('stand',(24,40),(24,44))
    i.relate('connect','screen','stand')

def currency(i,kind,x,y):
    if kind=='dollar':
        i.add_line('currency-top',(x+6,y-8),(x,y-8))
        i.add_arc('currency-upper',(x,y-8),(x,y),radius_x=6,radius_y=4,sweep=False)
        i.add_arc('currency-lower',(x,y),(x,y+8),radius_x=6,radius_y=4)
        i.add_line('currency-bottom',(x,y+8),(x-6,y+8))
        i.add_contour('currency','currency-top','currency-upper','currency-lower','currency-bottom')
        i.add_line('stem-top',(x,y-10),(x,y-8))
        i.add_line('stem-bottom',(x,y+8),(x,y+10))
        i.relate('connect','currency','stem-top')
        i.relate('connect','currency','stem-bottom')
    elif kind=='euro':
        i.add_arc('currency-upper',(x+6,y-8),(x-6,y),radius_x=12,radius_y=8,sweep=False)
        i.add_arc('currency-lower',(x-6,y),(x+6,y+8),radius_x=12,radius_y=8,sweep=False)
        i.add_contour('currency','currency-upper','currency-lower')
        i.add_line('bar',(x-6,y),(x+3,y))
        i.relate('connect','currency','bar')
    elif kind=='pound':
        i.add_arc('hook',(x+5,y-4),(x-3,y-4),radius_x=4,sweep=False)
        i.add_line('stem',(x-3,y-4),(x-3,y+8))
        i.add_contour('currency','hook','stem')
        i.add_line('foot',(x-6,y+8),(x+6,y+8))
        i.add_line('bar',(x-6,y),(x-1,y))
        i.relate('connect','currency','bar')
        i.relate('connect','currency','foot')
    elif kind=='yen':
        i.add_polyline('fork',(x-6,y-8),(x,y),(x+6,y-8))
        i.add_line('stem',(x,y),(x,y+8))
        i.add_line('bar',(x-6,y),(x+6,y))
        i.relate('connect','fork','stem','bar')
    elif kind=='bitcoin':
        i.add_line('coin-top',(x-6,y-8),(x+2,y-8))
        i.add_arc('upper',(x+2,y-8),(x+2,y),radius_x=6,radius_y=4)
        i.add_arc('lower',(x+2,y),(x+2,y+8),radius_x=6,radius_y=4)
        i.add_line('coin-bottom',(x+2,y+8),(x-6,y+8))
        i.add_line('spine',(x-6,y+8),(x-6,y-8))
        i.add_contour('currency','coin-top','upper','lower','coin-bottom','spine',closed=True)
        i.add_line('middle',(x-6,y),(x+2,y))
        i.relate('connect','currency','middle')
        for dx in (-6,2):
            for end in (-1,1):
                name=f'tick-{dx}-{end}';i.add_line(name,(x+dx,y+end*8),(x+dx,y+end*9));i.relate('connect','currency',name)
    elif kind=='question':
        i.add_arc('hook',(x-5,y-3),(x+5,y-3),radius_x=5,sweep=True)
        i.add_bezier('turn',(x+5,y-3),((x+5,y),(x,y),(x,y+1)))
        i.add_contour('question','hook','turn')
        i.add_dot('dot',(x,y+10))
    elif kind=='info':
        i.add_dot('dot',(x,y-8))
        i.add_line('stem',(x,y),(x,y+8))
        i.add_line('foot',(x-5,y+8),(x+5,y+8))
        i.relate('connect','stem','foot')

def baht(i):
    i.add_line('top',(8,8),(28,8))
    i.add_arc('upper',(28,8),(28,24),radius_x=12,radius_y=8)
    i.add_arc('lower',(28,24),(28,40),radius_x=12,radius_y=8)
    i.add_line('bottom',(28,40),(8,40))
    i.add_line('spine',(8,40),(8,8))
    i.add_contour('outline','top','upper','lower','bottom','spine',closed=True)
    i.add_line('middle',(8,24),(28,24))
    i.add_line('stem',(20,4),(20,44))
    i.relate('connect','outline','middle','stem')

def compact(i,kind,x,y):
    if kind!='dollar':
        compact_currency(i,kind,x,y)
        return
    i.add_line('currency-top',(x+6,y-8),(x,y-8))
    i.add_arc('currency-upper',(x,y-8),(x,y),radius_x=6,radius_y=4,sweep=False)
    i.add_arc('currency-lower',(x,y),(x,y+8),radius_x=6,radius_y=4)
    i.add_line('currency-foot',(x,y+8),(x-6,y+8))
    i.add_contour('currency','currency-top','currency-upper','currency-lower','currency-foot')
    i.add_line('stem-top',(x,y-9),(x,y-8))
    i.add_line('stem-bottom',(x,y+8),(x,y+9))
    i.relate('connect','currency','stem-top')
    i.relate('connect','currency','stem-bottom')

def diagonal_dollar(i,x,y):
    # Direct integer-grid diagonal currency, retaining both S lobes and stems.
    i.add_line('top',(x+10,y-1),(x+6,y-6))
    i.add_bezier('upper',(x+6,y-6),((x+1,y-11),(x-5,y-5),(x,y)))
    i.add_bezier('lower',(x,y),((x+5,y+5),(x-1,y+11),(x-6,y+6)))
    i.add_line('foot',(x-6,y+6),(x-10,y+1))
    i.add_contour('currency','top','upper','lower','foot')
    i.add_line('stem-top',(x+7,y-7),(x+6,y-6))
    i.add_line('stem-bottom',(x-6,y+6),(x-7,y+7))
    i.relate('connect','currency','stem-top')
    i.relate('connect','currency','stem-bottom')
