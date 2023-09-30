class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        final_path = ['/']

        for dir in split_path:
            if dir == '..':
                final_path.pop() if len(final_path) > 1 else ''
            elif dir == '.':
                continue
            elif dir != '':
                final_path.append(dir)

        return '/'.join(final_path)[1:] if len(final_path) > 1 else '/'

        