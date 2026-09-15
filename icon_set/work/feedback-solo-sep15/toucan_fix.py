from edit_batch import revise
revise(136,'Raise the open wing curve into the body and keep it clear of the tail; widen the body to preserve room for the eye.',keyshape='SQUARE',ref='Lucide bird: a coherent body outline with one open wing curve',body="""
path('outline',(6,20),[('A',(20,6),14,14,True),('C',(42,18),(32,6),(42,10)),('L',(28,18)),('L',(30,26)),('A',(20,38),10,12,True),('L',(6,42)),('L',(6,28)),('L',(6,20))],True)
line('bill-root',(20,6),(28,18))
join('bill-root','outline')
dot('eye',(16,18))
path('wing',(6,28),[('C',(18,28),(6,35),(18,36))])
join('wing','outline')
""")
