'''###############################
          
       ^    _   
*         \#     _     
   #        \#    #
* *   #################\\\\
      # ()()()             #
   *  ##################///
 *  #  #    /#    #
          /#    #
        /  #

HTTP Speed:

A check the speed of an HTTP request!

###############################'''

import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000 
        if self.verbose: 
            print 'elapsed time: %f ms' % self.msecs



def main():
    
    import requests
    a = requests.get("http://httpbin.org/delay/9")

if  __name__ == '__main__':
    with Timer() as t:
        main()
     print "=> Execution time of main: %s s" t.secs

