class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        lett_list=[]
        rlist=[]
        for i in digits:
            lett_list.append(num_map[i])
        if len(digits)==0:
            return []
        elif len(digits)==1:
            return list(num_map[digits])
        elif len(digits)==2:
            k=lett_list[0]
            m=lett_list[1]
            for i in range(len(k)):
                for j in range(len(m)):
                    rlist.append(f"{k[i]}{m[j]}")
        elif len(digits)==3:
            k=lett_list[0]
            m=lett_list[1]
            l=lett_list[2]
            for i in range(len(k)):
                for j in range(len(m)):
                    for p in range(len(l)):
                        rlist.append(f"{k[i]}{m[j]}{l[p]}")
        elif len(digits)==4:
            k=lett_list[0]
            m=lett_list[1]
            l=lett_list[2]
            f=lett_list[3]
            for i in range(len(k)):
                for j in range(len(m)):
                    for p in range(len(l)):
                        for g in range(len(f)):
                            rlist.append(f"{k[i]}{m[j]}{l[p]}{f[g]}")
        return rlist
