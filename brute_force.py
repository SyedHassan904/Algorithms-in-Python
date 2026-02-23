
points_no=12
points = [(5,1),(4,4),(2,5),(13,3),(11,5),(7,7),(15,7),
          (14,10),(9,10),(4,11),(12,12),(7,13)]

def bruteForce(points_no,points):
    for i in range(points_no):
        maxima=True
        for j in range(points_no):
            if(i!=j and points[i][0]<=points[j][0] and points[i][1]<=points[j][1]):
                maxima=False
                break
        if maxima:
            print(points[i])    
        
bruteForce(points_no,points)
            

    
    
        
            
    
        



