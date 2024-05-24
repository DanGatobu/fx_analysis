def resistance(data,now_p,check_points,start_p):
    i=now_p
    
    right=False
    left=False
    found=False
    nv=i+check_points-start_p
    
    
    while not found :
        if nv>now_p:
            nv=now_p
        else:
            nv=i+check_points-start_p
        mright=data.loc[(i+1)-start_p:nv]['Close'].max()
        mleft=data.loc[((i-start_p)-check_points):i-(start_p+1)]['Close'].max()
        # print(i-check_points)
        # print('i ma mright',mright)
        # print('central',data.loc[i-check_points]['Close'],'time',data.loc[i-check_points]['mtime'])
        # print('i ma mleft',mleft)
        # print('left,right',left,right)
        if data.loc[i-start_p]['Close']>mright:
            right=True
        if data.loc[i-start_p]['Close']>mleft:
            left=True
            
        if left==True and right==True:
            found=True
            break
        else:
            left=False
            right=False
            
            
            
        i-=1
        
        

    return i-start_p
    
    
def moving_resistance(data,now_p,check_points,start_p):
    i=now_p
    
    right=False
    left=False
    found=False
    
    while not found :
        mright=data.loc[(i+1)-start_p:now_p]['Close'].max()
        mleft=data.loc[((i-start_p)-check_points):i-(start_p+1)]['Close'].max()
        # print(i-check_points)
        # print('i ma mright',mright)
        # print('central',data.loc[i-check_points]['Close'],'time',data.loc[i-check_points]['mtime'])
        # print('i ma mleft',mleft)
        # print('left,right',left,right)
        if data.loc[i-start_p]['Close']>mright:
            right=True
        if data.loc[i-start_p]['Close']>mleft:
            left=True
            
        if left==True and right==True:
            found=True
            break
        else:
            left=False
            right=False
            
            
            
        i-=1
        
        

    return i-start_p
    
    
    
def support(data,now_p,check_points,start_p):
    i=now_p
    
    right=False
    left=False
    found=False
    nv=i+check_points-start_p
    
    
    while not found :
        if nv>now_p:
            nv=now_p
        else:
            nv=i+check_points-start_p
        mright=data.loc[(i+1)-start_p:nv]['Low'].min()
        mleft=data.loc[((i-start_p)-check_points):i-(start_p+1)]['Low'].min()
        # print(i-check_points)
        # print('i ma mright',mright)
        # print('central',data.loc[i-check_points]['Close'],'time',data.loc[i-check_points]['mtime'])
        # print('i ma mleft',mleft)
        # print('left,right',left,right)
        if data.loc[i-start_p]['Low']<mright:
            right=True
        if data.loc[i-start_p]['Low']<mleft:
            left=True
            
        if left==True and right==True:
            found=True
            break
        else:
            left=False
            right=False
            
            
            
        i-=1
        
        

    return i-start_p
    
    
def moving_support(data,now_p,check_points,start_p):
    i=now_p
    
    right=False
    left=False
    found=False
    
    while not found :
        mright=data.loc[(i+1)-start_p:now_p]['Low'].min()
        mleft=data.loc[((i-start_p)-check_points):i-(start_p+1)]['Low'].min()
        # print(i-check_points)
        # print('i ma mright',mright)
        # print('central',data.loc[i-check_points]['Close'],'time',data.loc[i-check_points]['mtime'])
        # print('i ma mleft',mleft)
        # print('left,right',left,right)
        if data.loc[i-start_p]['Low']<mright:
            right=True
        if data.loc[i-start_p]['Low']<mleft:
            left=True
            
        if left==True and right==True:
            found=True
            break
        else:
            left=False
            right=False
            
            
            
        i-=1
        
        

    return i-start_p
    