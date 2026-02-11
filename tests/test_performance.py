"""Performance validation tests for the Todo CLI application."""

import time
from src.services.task_manager import TaskManager


def test_performance_with_100_tasks(task_manager):
    """Test that the application handles 100+ tasks without performance degradation."""
    # Add 100 tasks
    start_time = time.time()
    task_ids = []

    for i in range(100):
        task = task_manager.add_task(f"Task {i}", f"Description for task {i}")
        task_ids.append(task.id)

    add_time = time.time() - start_time

    # Verify all tasks were added
    assert len(task_manager.get_all_tasks()) == 100

    # Test list performance
    start_time = time.time()
    all_tasks = task_manager.get_all_tasks()
    list_time = time.time() - start_time

    assert len(all_tasks) == 100

    # Test update performance
    start_time = time.time()
    for i in range(10):  # Update 10 tasks
        task_manager.update_task(task_ids[i], title=f"Updated Task {i}")
    update_time = time.time() - start_time

    # Test complete performance
    start_time = time.time()
    for i in range(10):  # Complete 10 tasks
        task_manager.toggle_task_status(task_ids[i])
    complete_time = time.time() - start_time

    # Test delete performance
    start_time = time.time()
    for i in range(10):  # Delete 10 tasks
        task_manager.delete_task(task_ids[i])
    delete_time = time.time() - start_time

    # Verify final count
    assert len(task_manager.get_all_tasks()) == 90

    # Performance assertions (all operations should be sub-second)
    assert add_time < 1.0, f"Adding 100 tasks took {add_time:.3f}s (should be < 1s)"
    assert list_time < 0.1, f"Listing 100 tasks took {list_time:.3f}s (should be < 0.1s)"
    assert update_time < 0.1, f"Updating 10 tasks took {update_time:.3f}s (should be < 0.1s)"
    assert complete_time < 0.1, f"Completing 10 tasks took {complete_time:.3f}s (should be < 0.1s)"
    assert delete_time < 0.1, f"Deleting 10 tasks took {delete_time:.3f}s (should be < 0.1s)"

    print(f"\nPerformance Results:")
    print(f"  Add 100 tasks: {add_time:.3f}s")
    print(f"  List 100 tasks: {list_time:.3f}s")
    print(f"  Update 10 tasks: {update_time:.3f}s")
    print(f"  Complete 10 tasks: {complete_time:.3f}s")
    print(f"  Delete 10 tasks: {delete_time:.3f}s")


def test_memory_efficiency_with_large_dataset(task_manager):
    """Test memory efficiency with a large number of tasks."""
    import sys

    # Add 1000 tasks
    for i in range(1000):
        task_manager.add_task(f"Task {i}", f"Description for task {i}")

    # Get the size of the task manager
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 1000

    # Rough memory check - each task should be relatively small
    # This is a basic check to ensure we're not using excessive memory
    task_size = sys.getsizeof(all_tasks[0])
    total_estimated_size = task_size * 1000

    # Should be well under 50MB for 1000 tasks
    assert total_estimated_size < 50 * 1024 * 1024, f"Memory usage too high: {total_estimated_size / (1024*1024):.2f}MB"

    print(f"\nMemory Efficiency:")
    print(f"  Estimated size per task: {task_size} bytes")
    print(f"  Estimated total for 1000 tasks: {total_estimated_size / 1024:.2f} KB")


def test_lookup_performance(task_manager):
    """Test O(1) lookup performance for task retrieval."""
    # Add 1000 tasks
    task_ids = []
    for i in range(1000):
        task = task_manager.add_task(f"Task {i}", f"Description {i}")
        task_ids.append(task.id)

    # Test lookup time for tasks at different positions
    start_time = time.time()
    for _ in range(100):
        # Lookup first, middle, and last tasks
        task_manager.get_task_by_id(task_ids[0])
        task_manager.get_task_by_id(task_ids[500])
        task_manager.get_task_by_id(task_ids[999])
    lookup_time = time.time() - start_time

    # 300 lookups should be very fast (O(1) dictionary access)
    assert lookup_time < 0.1, f"300 lookups took {lookup_time:.3f}s (should be < 0.1s)"

    print(f"\nLookup Performance:")
    print(f"  300 lookups in 1000 tasks: {lookup_time:.3f}s")
    print(f"  Average per lookup: {(lookup_time / 300) * 1000:.3f}ms")