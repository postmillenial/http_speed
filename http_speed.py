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

import cProfile

def main():
    
    import requests
    a = requests.get("http://httpbin.org/delay/9")

if  __name__ == '__main__':
    cProfile.run('main()')
