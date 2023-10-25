from mrjob.job import MRJob
from mrjob.step import MRStep

"""
map reduce using MRJob
"""

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapperGetRatings, reducer=self.reducerCountRatings)
        ]

    def mapperGetRatings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split("\t")
        yield rating, 1

    def reducerCountRatings(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    RatingsBreakdown.run()
