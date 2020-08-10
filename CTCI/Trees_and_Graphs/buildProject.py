## Problem: There is a list of projects that needs to be built. Each project has zero to many dependencies.
## Each project's dependencies must be built before the project can be built
## Design an algorithm to find a build order that will build all projects.

## Solution: This is a graph problem. We should find the in-degree and out-degree of each project.
## There must exist a project whose in-degree is 0. Else return an error
## Then, keep finding a project that can be built.

from collections import defaultdict

def build_projects(projects, dependencies):
    dependency_map = defaultdict(set)
    dependant_map = defaultdict(set)
    build_order = []
    for p1, p2 in dependencies:
        dependency_map[p2].add(p1)
        dependant_map[p1].add(p2)

    # print(dependant_map)
    # print()
    # print(dependency_map)

    q = []
    for p in projects:
        if dependency_map[p] == set():
            q.append(p)
    if not q:
        raise Exception("no possible solution")

    
    while q:
        project = q.pop()
        build_order.append(project)
        for dep in dependant_map[project]:
            dependency_map[dep].remove(project)

            if dependency_map[dep] == set():
                q.append(dep)

    if len(build_order) != len(projects):
        raise Exception("cannot build all projects")
    return build_order


if __name__ == "__main__":
    projects = ['a','b', 'c', 'd', 'e', 'f']
    dependencies = [
        ('a', 'd'),
        ('f', 'b'),
        ('b', 'd'),
        ('f', 'a'),
        ('d', 'c'),
        ('a', 'f')
    ]

    print(build_projects(projects, dependencies))
    

