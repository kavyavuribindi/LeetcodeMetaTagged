class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for folder in path.split('/'):
            if folder=='..':
                if stack:
                    stack.pop()
            elif folder in ('','.'):
                continue
            else:
                stack.append(folder)
        return '/'+'/'.join(stack)