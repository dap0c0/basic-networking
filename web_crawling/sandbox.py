import json
import threading
from cProfile import Profile
from pstats import SortKey, Stats
import re

def dictionary_sandbox():
    dog_registry = {
        1: {"name": "Frieda"}
    }
    print(f"Class of dog_registry: {dog_registry.__class__}")
    dog_json = json.dumps(dog_registry)
    print(f"JSON of dog_registry: {dog_json}")

    dog_registry = json.loads(dog_json)
    print(f"Class of loaded dog_registry {dog_registry.__class__}")

    # Testing with files
    data = {
        "https://website_a.com": {
            "hyperlinks": [
                "www.youtube.com",
                "www.bruh.ca",
                "hey_there.inet"
                ],
            "emails": (
                "you@gmail.com",
                "me@proton.me",
                "foo@outlook.ca"
            ),
            "files": [
            ]
        }, 
        "https://website_b.com": {
            "hyperlinks": [
            ],
            "emails": [
            ],
            "files": [   
            ]
        }
    }
    data_str = json.dumps(data, indent=0)
    print(data)
    with open("test_file.txt", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)

    with open("test_file.txt", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        print(data)

    pattern = re.compile(r"bruh")
    dict = {"bruh": pattern}
    contained = dict["bruh"]
    print(contained.__class__)
    print(contained)

    non_contained = dict["foo"]
    # print(non_contained.__class__)
    print(non_contained)

def profiling_sandbox():
    from cProfile import Profile
    from pstats import SortKey, Stats

    def fibonnaci(n):
        # f(1) = 1
        # f(2) = 1
        # f(n) = f(n-1) + f(n-2), n >= 2
        assert isinstance(n, int)
        
        if n == 1 or n == 2:
            return 1

        else:
            return fibonnaci(n-1) + fibonnaci(n-2)
    
    def wait_interrupt():
        int_caught = False

        def plus_one_mod_5(n):
            return (n + 1) % 5

        n = 1

        while not int_caught:
            try:
                n = plus_one_mod_5(n)
            
            except KeyboardInterrupt:
                print("Keyboard interrupt caught.")
                int_caught = True
    
    with Profile() as profile:
        print(f"{wait_interrupt()}")(
            Stats(profile)
            .strip_dirs()
            .sort_stats(SortKey.CALLS)
            .print_stats()
        )
def profiling_function_sandbox():
    def profile(fx):

        with Profile() as profile:
            print(f"fx is {fx}")
            Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()

    def foo(n, b):
        if n == b:
            return n
        
        print(n)
        return foo(n+1, b)
    
    def bar(loops, n, b):
        total = 0

        for i in range(loops):
            total += foo(n, b)

        return total

    profile(bar(1000, 1, 100))

def thread_result_sandbox():
    def return_n(n):
        assert isinstance(n, int)
        return n
    
    def return_result_array(fx, result_list, index):
        assert isinstance(result_list, list)
        assert isinstance(index, int)
        result_list.insert(index, fx)
    
    result_list = []

    # Start processing
    results = []

    NUM_THREADS = 10
    threads = [None] * 10
    print(f"Len of threads {len(threads)}")

    for i in range(NUM_THREADS):
        # Spawn a thread, get i and place in results[i]
        print("Spawning thread %d" % i)
        thread = threading.Thread(target=return_result_array, args=(return_n(i), results, i)) 
        thread.run()
    
    # Check whether the results are stored before joining threads
    print(results)

    
        

# profiling_sandbox()
# profiling_function_sandbox()
thread_result_sandbox()