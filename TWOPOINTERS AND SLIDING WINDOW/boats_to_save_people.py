class Solution:
    def boats_to_save_people(self,people,limit):
        people.sort()
        n=len(people)
        right=n-1
        left=0
        boats=0
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
            right-=1
            boats+=1
        return boats
# Example usage:
if __name__=="__main__":
    sol=Solution()
    people=[1,2]
    limit=3
    print(sol.boats_to_save_people(people,limit))  # Output: 1
    people=[3,2,2,1]
    limit=3
    print(sol.boats_to_save_people(people,limit))  # Output: 3
    # time complexity: O(nlogn) due to sorting the array
    # space complexity: O(1) since we are using only a constant amount of extra
