# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hmap = defaultdict(list)
#         count =[0]*26 # 26 chars of alphabet
        
#         for string in strs:
#             for char in string:
#                 count[ord(char)-ord("a")] += 1
            
#             # ans[tuple(count)].append(string)
#             hmap[tuple(count)].append(string)

#         return hmap.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res = {} #hashmap -- map character counts to the strings
        ans = defaultdict(list) #default value is a list
        # 1e, 1a, 1t ---> eat, ate, tea
        #hat = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] 
       
        for string in strs:
            count=[0]*26 #count array of len of 26 -- a to z [0,0,0,0,0,0,0....]

            for char in string:
                count[ord(char)- ord("a")] += 1 # ascii any char - Ascii A == 80-80 = 0
            
            #ans[count].append but list cannot be keys. Tuples - non mutable 
           # {[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] : hat}
            ans[tuple(count)].append(string)
        
        return ans.values()
