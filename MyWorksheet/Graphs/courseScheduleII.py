## Problem: Given a list of prerequisites and a total number of courses,
## return the order of courses that will satisfy all pre-requisites for each course.

## Solution: Similar to build project question, we can store a dict of
## inward nodes and outward nodes. For each node that has indegree == 0
## we consider it complete and remove it from the list of dependencies for each node.
## While doing this, we check if any of the nodes we removed the dependencies now has indegree 0
## If so, we add it to the Q.

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_reqs = defaultdict(set)
        dependencies = defaultdict(set)
        
        for c1, c2 in prerequisites:
            pre_reqs[c1].add(c2)
            dependencies[c2].add(c1)
        
        q = []
        ret = []
        for course in range(numCourses):
            if pre_reqs[course] == set():
                q.append(course)
        
        if not q:
            return []
        
        while q:
            course = q.pop(0)
            
            ret.append(course) ## done

            for dep in dependencies[course]:
                pre_reqs[dep].remove(course)
                
                if pre_reqs[dep] == set():
                    q.append(dep)
        
        return ret if len(ret) == numCourses else []