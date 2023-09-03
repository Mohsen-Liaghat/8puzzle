class ENV_8puzzle : 
    def __init__(self , m ) :
        self.__m = [ m[ i : i + 3 ] for i in range( 0 , 9 , 3 ) ]
        for i in range(3) :
            for j in range(3) :
                if self.__m[i][j] == 0 :
                    self.__hole = [ i , j ] 
                    break

    def __swap( self , s , d ) :
        tmp = self.__m[d[0]][d[1]] 
        self.__m[d[0]][d[1]] = self.__m[s[0]][s[1]]
        self.__m[s[0]][s[1]] = tmp
    
    def transition_model( self , dest ) :
        if dest == 'U' and self.__hole[0] != 0 : #up
            self.__swap ( self.__hole , [ self.__hole[0] - 1 , self.__hole[1] ] )
            self.__hole[0] -= 1 
        elif dest == 'D' and self.__hole[0] != 2 : #down
            self.__swap ( self.__hole , [ self.__hole[0] + 1 , self.__hole[1] ] )
            self.__hole[0] += 1 
        elif dest == 'L' and self.__hole[1] != 0 : #left
            self.__swap ( self.__hole , [ self.__hole[0] , self.__hole[1] - 1 ] )
            self.__hole[1] -= 1 
        elif dest == 'R' and self.__hole[1] != 2 : #right
            self.__swap ( self.__hole , [ self.__hole[0] , self.__hole[1] + 1 ] )
            self.__hole[1] += 1
        else :
            raise Exception( "bad destination." )
        
        return dest

    def goal_test ( self ) :
        goal = [ [1 , 2 , 3] , [ 4 , 5 , 6 ] , [ 7 , 8 , 0 ]] 
        if goal == self.__m : 
            return True
        return False
    
    # def up( self ) :
    #     return self.__transition_model('U')
    
    # def down( self ) :
    #     return self.__transition_model('D')
    
    # def left( self ) :
    #     return self.__transition_model('L')

    # def right( self ) :
    #     return self.__transition_model('R')

    # def actions ( self ) :
    #     return ( self.up , self.down , self.left , self.right )
    
    def __goalpos( self , n ) :
        if n == 0 :
            return ( 2 , 2 )
        return ( ( n - 1 ) // 3 , ( n - 1 ) % 3 )
    
    def distance ( self , s , d = None ) :
        if d == None :
            d = self.__goalpos( self.__m[s[0]][s[1]] )
        return abs( s[0] - d[0] ) + abs( s[1] - d[1] )
        
    def hf( self ) :
        t = 0 
        for i in range(3) :
            for j in range(3) :
                t += self.distance( ( i , j ) )
        return t

    def copy ( self ) :
        return ENV_8puzzle( self.__m[0] + self.__m[1] + self.__m[2] )
    
    def __eq__(self, o ) :
        if self.__m == o.__m :
            return True
        return False
    
    def __lt__( self , o ) :
        return self.hf() < o.hf()

    def __hash__(self) :
        return tuple(self.__m[0] + self.__m[1] + self.__m[2]).__hash__()