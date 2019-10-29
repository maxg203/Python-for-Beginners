 # Concept of constructor in python3
   class point():
    	def __init__(self, x=0, y=0):
    		self.x = x
    		self.y = y
     
    p = point(10,20)  # x = 10, y = 20
    p = point(10)	    # x = 10, y = 0
    p = point()	      # x = 0, y = 0
