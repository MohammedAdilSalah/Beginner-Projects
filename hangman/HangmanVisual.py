def visual(lives):
    if lives == 0:
        print( """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """)
    elif lives == 1:   
       print ("""
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """)
    elif lives == 2: 
        print( """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """)
    elif lives == 3:      
        print( """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """)
    elif lives == 4: 
        print ("""
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """)
    elif lives == 5: 
        print("""
                ___________
               | /        
               |/        
               |          
               |          
               |
            """)
    elif lives== 6: 
        print("""
               |
               |
               |
               |
               |
            """)
    else: 
        print("")
    