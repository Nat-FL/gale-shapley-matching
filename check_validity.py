def check_validity(n, matching):
    if len(matching) > n:
        return (False, "INVALID (Not a one to one matching)")
    if len(matching) < n:
        return (False, "INVALID (Not every hospital and student is matched)")
    
    students = set()
    hospitals = set()
    for a,b in matching:
        if a<1 or a>n:
            return (False, f"INVALID (Hospital {a} is out of range)")
        
        if b<1 or b>n:
            return (False, f"INVALID (Student {b} is out of range)")
        
        
        if a in hospitals:
            return (False, f"INVALID (Hospital {a} is matched twice)")
        if b in students:
            return ((False, f"INVALID (Student {b} is matched twice)"))
            
        students.add(b)
        hospitals.add(a)
    return (True, "VALID")
        

