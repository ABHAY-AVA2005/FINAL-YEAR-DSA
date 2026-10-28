    int:
        # If either low or high is odd, including 
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        # If both low and high are even
        both, the odd count gets rounded up
        return (high - low) // 2
