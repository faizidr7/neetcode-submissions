class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + '#' + s 
        return new_str


    def decode(self, s: str) -> List[str]:
        new_str = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            new_str.append(s[j+1 : j+1+length])
            i = j+1+length
        return new_str
