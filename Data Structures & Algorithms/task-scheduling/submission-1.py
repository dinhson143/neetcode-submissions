class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_tasks = Counter(tasks)
        print(count_tasks)

        max_task = max(task for task in count_tasks.values())
        print(max_task)

        count_max_task = sum(1 for count in count_tasks.values() if count == max_task)
        print(count_max_task)

        total_block =  max_task - 1
        oneblock_time = n + 1
        print(total_block)
        total = total_block*oneblock_time + count_max_task

        return max(total, len(tasks))