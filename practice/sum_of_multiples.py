class SumOfMultiples:
    _NUMS = [3, 5]

    def __init__(self, *nums):
        self._nums = nums if nums else SumOfMultiples._NUMS
    
    @classmethod
    def sum_up_to(cls, limit):
        # multiples = []
        # for multiple in range(1, limit):
        #     for num in cls._NUMS:
        #         if multiple % num == 0 and multiple not in multiples:
        #             multiples.append(multiple)
        
        # return sum(multiples)
        return SumOfMultiples().to(limit)

    def to(self, limit):
        multiples = []
        for multiple in range(1, limit):
            for num in self._nums:
                if multiple % num == 0 and multiple not in multiples:
                    multiples.append(multiple)
        
        return sum(multiples)
