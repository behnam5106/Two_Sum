class Solution:
    def twoSum(self, nums: list[int], target: list[int] ) ->list[int]:
        a=[] # <= target/2 
        b=[] # <  target/2
        c=[] # >  target/2
        d=[] # =  target/2

        for i in range (0,len(nums)):
            if nums[i] <= target:
                a.append([i,nums[i]])
        for i in range (0, len(a)):
            if a[i][1] < target/2:
                b.append(a[i])
            elif a[i][1] > target/2:
                c.append(a[i])
            else:
                d.append(a[i])
        if len(d)==2:
            result=[d[0][0],d[1][0]]
            return result
        else:
            # a[i][j] : i = raw , j = col
            for i in range(0,len(b)):           
                for j in range(0,len(c)):
                    if b[i][1]+c[j][1]==target:
                        result=[b[i][0],c[j][0]]
                        return result

        # print("b",b)
        # print("c",c)
        # print("d",d)             

        

#main
                
nums=[2,7,3,11,4,1,15]
target=15
solution=Solution()
result=solution.twoSum(nums,target)
print(result)
# print(result[0])
# print(result[1][0])
# print(result[1][1])
# print(result[4][1])