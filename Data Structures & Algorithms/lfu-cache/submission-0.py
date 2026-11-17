from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        self.key_to_val_freq = {}

        self.freq_to_keys = defaultdict(OrderedDict)

    def update_freq(self, key):
        value, freq = self.key_to_val_freq[key]


        del self.freq_to_keys[freq][key]

        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]

            if self.min_freq == freq:
                self.min_freq += 1

        new_freq = freq + 1
        self.key_to_val_freq[key] = [value, new_freq]

        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        value, freq = self.key_to_val_freq[key]

        self.update_freq(key)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self.update_freq(key)
            return

        if len(self.key_to_val_freq) == self.capacity:
            lru_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)

            del self.key_to_val_freq[lru_key]

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert new key with frequency 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1