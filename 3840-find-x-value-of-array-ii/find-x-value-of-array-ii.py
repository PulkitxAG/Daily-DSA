class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)        
        sz = 1
        while sz < n:
            sz *= 2            
        tree_prod = [1] * (2 * sz)        
        tree_cnt = [[0] * k for _ in range(2 * sz)]        
        for i in range(n):
            idx = sz + i
            val = nums[i] % k
            tree_prod[idx] = val
            tree_cnt[idx][val] = 1            
        for i in range(sz - 1, 0, -1):
            L = 2 * i
            R = 2 * i + 1
            L_p = tree_prod[L]
            tree_prod[i] = (L_p * tree_prod[R]) % k
            c = [tree_cnt[L][j] for j in range(k)]
            for p in range(k):
                if tree_cnt[R][p] > 0:
                    c[(L_p * p) % k] += tree_cnt[R][p]
            tree_cnt[i] = c
        res = []        
        for idx, val, start, x in queries:            
            p_idx = sz + idx
            v = val % k
            tree_prod[p_idx] = v
            new_cnt = [0] * k
            new_cnt[v] = 1
            tree_cnt[p_idx] = new_cnt
            curr = p_idx // 2
            while curr > 0:
                L = 2 * curr
                R = 2 * curr + 1     
                L_p = tree_prod[L]
                tree_prod[curr] = (L_p * tree_prod[R]) % k                
                c = [tree_cnt[L][j] for j in range(k)]
                for p in range(k):
                    if tree_cnt[R][p] > 0:
                        c[(L_p * p) % k] += tree_cnt[R][p]
                tree_cnt[curr] = c
                curr //= 2                
            l = start + sz
            r = n - 1 + sz
            left_nodes = []
            right_nodes = []
            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2
            curr_prod = 1
            curr_cnt = [0] * k            
            for node in left_nodes:
                n_prod = tree_prod[node]
                n_cnt = tree_cnt[node]
                next_cnt = [curr_cnt[j] for j in range(k)]
                for p in range(k):
                    if n_cnt[p] > 0:
                        next_cnt[(curr_prod * p) % k] += n_cnt[p]
                curr_prod = (curr_prod * n_prod) % k
                curr_cnt = next_cnt
            for i in range(len(right_nodes) - 1, -1, -1):
                node = right_nodes[i]
                n_prod = tree_prod[node]
                n_cnt = tree_cnt[node]
                next_cnt = [curr_cnt[j] for j in range(k)]
                for p in range(k):
                    if n_cnt[p] > 0:
                        next_cnt[(curr_prod * p) % k] += n_cnt[p]
                curr_prod = (curr_prod * n_prod) % k
                curr_cnt = next_cnt
            res.append(curr_cnt[x])
        return res