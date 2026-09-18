class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        valid_intervals = []
        
        for char in first:
            start = first[char]
            end = last[char]
            
            i = start
            is_valid = True
            while i <= end:
                c = s[i]
                if first[c] < start:
                    is_valid = False
                    break
                end = max(end, last[c])
                i += 1
                
            if is_valid:
                valid_intervals.append((start, end))
        valid_intervals.sort(key=lambda x: x[1])        
        result = []
        prev_end = -1
        
        for start, end in valid_intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
                
        return result
