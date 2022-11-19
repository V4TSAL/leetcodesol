class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        trees = sorted(trees)                                 # [1] make an x-ordered list of points
        #trees = [np.array(t) for t in sorted(trees)]         #     (for a numpy solution, use this)
        U, L = [], []
        
        def cross(A, B, C):                                   # [2] this function computes cross product
            x1, y1, x2, y2, x3, y3 = chain(A, B, C)           #     between vectors A-C and C-B
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
            #return np.cross(A-C,C-B)                         #     (for a numpy solution, use this)
                
        for t in trees:                                       # [3] according to Andrew's algorithm,
            while len(U) >= 2 and cross(t,U[-1],U[-2]) < 0:   #     we add points to upper (lower)
                U.pop()                                       #     convex hulls if they make a
            U.append(t)                                       #     counterclockwise (clockwise) turn
                                                              #     with respect to the last two 
            while len(L) >= 2 and cross(t,L[-1],L[-2]) > 0:   #     points in the convex hull
                L.pop()                                       
            L.append(t)

        return set(tuple(T) for T in (U+L))                   # [4] join convex hulls, with only unique points