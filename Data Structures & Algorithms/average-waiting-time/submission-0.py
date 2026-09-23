class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = 0
        total_wait = 0

        for arrival, preparation in customers:
            start = max(arrival, finish_time)
            finish_time = start + preparation

            total_wait += finish_time - arrival

        return total_wait / len(customers)