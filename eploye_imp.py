#time: O(n)
# space: O(n)
"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        q = []
        obj = {}
        totalImp = 0
        # you need to map id with object of that id into a dict
        for e in employees:
            this_id = e.id
            if this_id not in obj:
                obj[this_id] = e
        q.append(obj[id]) # putting entire employee object in the q
        while q:
            curr = q.pop(0) # employee object
            totalImp += curr.importance
            for sid in curr.subordinates:
                q.append(obj[sid])
        return totalImp
