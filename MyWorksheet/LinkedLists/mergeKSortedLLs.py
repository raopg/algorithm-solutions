## Problem: Given a list of linked lists, merge all of them into one sorted linked list

## Solution: Consider a similar approach to merging two lists.
## Obviously, we can call merge_two_LLs in a loop. That would result in a O(kN) algorithm
## Another approach -> Iterate thru all nodes in all LLs, store it in an array, sort it, and build a list from that
## Time-space of that would be O(NlogN) time, O(N) space (brute-force)

## The first approach is actually on the right track. We can optimize this further -> pair up the K lists
## and merge them. This results in K/2 lists that need to be merged further. Repeatedly do this till we have
## one list. Time complexity -> O(N * logK) -> because we pair N nodes every time, logK times.
