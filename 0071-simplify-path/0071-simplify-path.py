class Solution:
    def simplifyPath(self, path: str) -> str:
      #  [home, user, documents, '..',Pictures]
      #stack=[home,user,pictures]
        pathlst=path.split('/')
        stack=[]
        for folder in pathlst:
            if folder=='..':
                if stack:
                    stack.pop()
                else:
                    continue
            elif folder=='' or folder=='.':
                continue
            else:
                stack.append(folder)
        return '/'+'/'.join(stack)















    #   stack=[]

    #   for token in path.split('/'):
    #     if token in ('' ,'.'):
    #       pass
    #     elif token=='..':
    #       if(stack):
    #         stack.pop()
    #     else:
    #       stack.append(token)

    #   return '/'+'/'.join(stack)



    # # stack = []
    # # for token in path.split('/'):
    # #     if token in ('', '.'):
    # #         pass
    # #     elif token == '..':
    # #         if stack: stack.pop()
    # #     else:
    # #         stack.append(token)
    # # return '/' + '/'.join(stack)