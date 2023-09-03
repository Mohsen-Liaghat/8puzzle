from puzzle8 import ENV_8puzzle
from search import *
from sys import setrecursionlimit
import pandas as pd

def main() :
    tmp = []
    res = []
    setrecursionlimit(2500)

    file = open("hardex.text" , "r")
    exs = file.readlines()
    for i in exs :
        print(i)
        l = list( map( int , i.strip().split(',') ) )
        tmp.append(str(l))
        
        env = ENV_8puzzle(l)

        tmp.append(dfs(env , tmp))
        tmp.append(bfs(env , tmp))
        tmp.append(ucs(env , tmp))
        # tmp.append(ids(env , tmp , len( tmp[ len(tmp) - 4]) + 1 ))
        tmp.append(astar(env , tmp))

        res.append(tmp)
        tmp = []
    file = open("res.csv" , "w")
    pd.DataFrame( res , columns=[ "Example" , "DFS_time" , "DFS_memory" , "DFS_res" , "BFS_time" , "BFS_memory" , "BFS_res" , "UCS_time" , "UCS_memory" , "UCS_res" , "A*_time" , "A*_memory" , "A*_res" ] ).to_csv(file)
    file.close()
    
if __name__ == "__main__" :
    main()