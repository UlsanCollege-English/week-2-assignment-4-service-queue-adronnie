from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    """Return (next_name, remaining_queue)."""
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    """Return a new queue where the first occurrence of `name` is moved to the back."""
    if name not in queue:
        return queue[:]  # return a copy
    idx = queue.index(name)
    return queue[:idx] + queue[idx+1:] + [queue[idx]]


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """Return an interleaved queue: q1[0], q2[0], q1[1], q2[1], ..."""
    result = []
    min_len = min(len(q1), len(q2))
    for i in range(min_len):
        result.append(q1[i])
        result.append(q2[i])
    # Append the remaining part of the longer queue
    result.extend(q1[min_len:])
    result.extend(q2[min_len:])
    return result
