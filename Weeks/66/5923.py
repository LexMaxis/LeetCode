class Solution(object):
    def minimumBuckets(self, street):
        i = 0
        bucket = 0
        if len(street) <= 3:

        else:
            while i + 2 <= len(street):
                if street[i] == 'H':
                    if street[i+1] == 'H' and street[i+2] == 'H':
                        return -1
                    elif street[i+1] == 'H' and street[i+2] == '.':
                        i += 1
                    elif street[i + 1] == '.' and street[i + 2] == 'H':
                        bucket += 1
                        i += 2
                else:
                    if street[i + 1] == 'H' and street[i + 2] == 'H':
                        i += 2
                    elif street[i + 1] == 'H' and street[i + 2] == '.':
                        bucket += 1
                        i += 1
                    elif street[i + 1] == '.' and street[i + 2] == 'H':
                        i += 2
                        bucket += 2
                    elif street[i + 1] == '.' and street[i + 2] == '.':
                        i += 3
        return bucket

if __name__ == '__main__':
    street = ".HHH."
    s = Solution()
    print(s.minimumBuckets(street))
