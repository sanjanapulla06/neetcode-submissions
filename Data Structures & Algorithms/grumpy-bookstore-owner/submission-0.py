class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return base + max_extra  