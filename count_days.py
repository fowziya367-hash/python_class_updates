def count_days(a,b,c,d):
    x = int(a[0:2]) * 30 + int(a[3:5])
    y = int(b[0:2])* 30 + int(b[3:5])
    z = int(c[0:2])* 30 + int(c[3:5])
    w = int(d[0:2])* 30 + int(d[3:5])    
    start = max(x,z)
    end = min (y,w)
    
    if start > end:
        return 0
    else:
        return end - start + 1
print(count_days("08-15", "08-18" , "08-16" , "08-19"))