from queue import Queue
import tracemalloc as tmem
import time  
import heapq
from sys import getrecursionlimit

def iner_dfs ( env , visiteds ) :
    visiteds.add( env )
    if env.goal_test() :
        return ""
    for i in "UDLR" : 
        newenv = env.copy()
        try :
            newenv.transition_model(i)
        except Exception as e :
            if e.__str__() == "bad destination." :
                continue
            else : 
                raise e 
        if newenv not in visiteds :
            res = iner_dfs(newenv, visiteds)
            if type(res) == type( "" ) :
                return i + res
            visiteds = res 
    return visiteds

def dfs ( env , l ) :
    print("DFS")
    t1 = time.time()
    tmem.start()
    try :
        res = iner_dfs(env, set() )
    except RecursionError as re :
        res = str(re)
    l.append( time.time() - t1 )
    l.append( tmem.get_traced_memory()[1] )
    tmem.stop() 
    tmem.reset_peak()
    if type( res ) == type("") :
        return res 
    return "res was not founded."

def bfs ( env , l ) :
    print("BFS")
    tmem.start()
    t1 = time.time()
    waitingq = Queue()
    curpath = ""
    visiteds = set()
    waitingq.put( ( env , curpath ) )
    while not waitingq.empty() :
        curenv , curpath = waitingq.get()
        if curenv.goal_test() :
            l.append( time.time() - t1 )
            l.append( tmem.get_traced_memory()[1] )
            tmem.stop()
            tmem.reset_peak()
            return curpath 
        visiteds.add( curenv )
        for i in "UDLR" :
            try :
                next_env = curenv.copy()
                next_env.transition_model(i)
                if next_env not in visiteds :
                    waitingq.put((next_env , curpath + i) )
            except Exception as e :
                if str(e) == "bad destination." :
                    continue
                else :
                    raise e
    l.append( time.time() - t1 )
    l.append( tmem.get_traced_memory()[1] )
    tmem.stop()
    tmem.reset_peak()
    return "resulat was not founded"


def ucs ( env , l ) :
    print("UCS")
    tmem.start()
    t1 = time.time()
    waitingq = []
    curpath = ""
    visiteds = set()
    heapq.heappush(waitingq, ( 0 , env , curpath ))
    while waitingq != [] :
        cost , curenv , curpath = heapq.heappop(waitingq)
        if curenv.goal_test() :
            l.append( time.time() - t1 )
            l.append( tmem.get_traced_memory()[1] )
            tmem.stop()
            tmem.reset_peak()
            return curpath 
        visiteds.add( curenv )
        for i in "UDLR" :
            try :
                next_env = curenv.copy()
                next_env.transition_model(i)
                if next_env not in visiteds :
                    heapq.heappush(waitingq, (cost + 1 , next_env , curpath + i) )
            except Exception as e :
                if str(e) == "bad destination." :
                    continue
                else :
                    raise e
    l.append( time.time() - t1 )
    l.append( tmem.get_traced_memory()[1] )
    tmem.stop()
    tmem.reset_peak()
    return "resulat was not founded"

def iner_dls ( env , limit , round ) :
    if env.goal_test() :
        return ""
    for i in "UDLR" : 
        newenv = env.copy()
        try :
            newenv.transition_model(i)
        except Exception as e :
            if e.__str__() == "bad destination." :
                continue
            else : 
                raise e 
        if round < limit :
            res = iner_dls(newenv, limit , round + 1 )
            if type(res) == type( "" ) :
                return i + res
            visiteds = res 

def dls ( env , limit ) :
    res = iner_dls(env , limit , 0 )
    if type( res ) == type("") :
        return res 
    return "res was not founded."
 

def ids ( env , l , maxround = 1000 ) :
    print("IDS")
    t1 = time.time()
    tmem.start()
    limit = 0
    while limit < min ( maxround , getrecursionlimit() ):
        res = dls(env, limit)
        if res != "res was not founded." :
            break
        limit += 1 
    l.append( time.time() - t1 )
    l.append( tmem.get_traced_memory()[1] )
    tmem.stop() 
    tmem.reset_peak()
    return res 

def astar ( env , l ) :
    print("A*")
    tmem.start()
    t1 = time.time()
    waitingq = []
    curpath = ""
    visiteds = set()
    heapq.heappush(waitingq, ( env , curpath ))
    while waitingq != [] :
        curenv , curpath = heapq.heappop(waitingq)
        if curenv.goal_test() :
            l.append( time.time() - t1 )
            l.append( tmem.get_traced_memory()[1] )
            tmem.stop()
            tmem.reset_peak()
            return curpath 
        visiteds.add( curenv )
        for i in "UDLR" :
            try :
                next_env = curenv.copy()
                next_env.transition_model(i)
                if next_env not in visiteds :
                    heapq.heappush(waitingq, ( next_env , curpath + i) )
            except Exception as e :
                if str(e) == "bad destination." :
                    continue
                else :
                    raise e
    l.append( time.time() - t1 )
    l.append( tmem.get_traced_memory()[1] )
    tmem.stop()
    tmem.reset_peak()
    return "resulat was not founded"