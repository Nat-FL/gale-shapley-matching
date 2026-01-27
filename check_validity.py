def check_validity(n, matching):
    if len(matching) > n:
        return (False, "INVALID (Not a one to one matching)")
    if len(matching) < n:
        return (False, "INVALID (Not every hospital and student is matched)")
    
    students = set()
    hospitals = set()
    for h,s in matching:
        if h<1 or s>n:
            return (False, f"INVALID (Hospital {h} is out of range)")
        
        if s<1 or s>n:
            return (False, f"INVALID (Student {s} is out of range)")
        
        
        if h in hospitals:
            return (False, f"INVALID (Hospital {h} is matched twice)")
        if s in students:
            return ((False, f"INVALID (Student {s} is matched twice)"))
            
        students.add(s)
        hospitals.add(h)
    return (True, "VALID")

#now check stability 

def check_stability(n, matchings, hospital_prefs, student_prefs):
    #matching is list of tuples
    #hospital prefs is dictionary of hospital: preference list
    #stucent prefs is vice versa

    bl, msg = check_validity(n, matchings)    
    if bl == False:
        return False, msg

    match_h = {}
    match_s = {}
   
    for h, s in matchings:
        match_h[h] = s
        match_s[s] = h

        """This allows lookups in O(1) time, which is better than iterating through the list in every iteration"""

    """
    I will do this algorithm later


    Iterate over hospitals
    which ever the hospital is matched to, check students to the left.
    check students to the left, do they prefer this hospital over their current? 

    If yes, Return False for unstable match,
    if not, continue

    once all hospitals have been iterated over, and if there is no unstable match, 
    then the matching is stable, and return True.

    """

    return (True, "VALID STABLE")