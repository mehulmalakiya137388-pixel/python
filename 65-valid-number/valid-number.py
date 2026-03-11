import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile(r"""
            ^                    
            [+-]?                
            (           
                (        
                    (\d+\.\d*) 
                    |             
                    (\.\d+)        
                    |               
                    (\d+\.)        
                )
                |                 
                (\d+)              
            )
            (                       
                [eE][+-]?\d+       
            )?
            $                      
        """, re.VERBOSE)

        return bool(pattern.match(s))