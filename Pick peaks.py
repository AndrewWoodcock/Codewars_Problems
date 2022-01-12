from itertools import groupby


class PickPeaks:

    def __init__(self, rng: list):
        self.rng = rng
        self.pos = []
        self.peaks = []
        self.out_dict = {}

    def rng_length(self):
        return len(self.rng)

    def find_peaks(self):
        start = 0
        seq = []
        for key, group in groupby(self.rng):
            seq.append((key, start))
            start += sum(1 for _ in group)

        print(seq)

        curr_peak = 0
        for i in range(1, len(seq)):
            item = seq[i][0]
            if item > curr_peak:
                curr_peak = item
            elif item < curr_peak:
                if seq
                self.peaks.append(curr_peak)
                curr_peak = 0


def pick_peaks(arr: list):
    new_range = PickPeaks(arr)
    print(new_range.rng)
    new_range.find_peaks()
    print(new_range.peaks)
    print(new_range.pos)


print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
