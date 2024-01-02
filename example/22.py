# Decomposition


def search(query, ranking=lambda r: -r.star):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)


def review_both(restaurant, others):
    return fast_overlap(restaurant.reviewers, others.reviewers)
    return len([r for r in restaurant.reviewers if r in others.reviewers])


def fast_overlap(s, t):
    """Return the overlap between sorted S and sorted T.

    >>> fast_overlap([2, 3, 5, 6, 7], [1, 4, 5, 6, 7, 8])
    3
    """
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i = i + 1
        elif s[i] > t[j]:
            j = j + 1
    return count


class Restaurant:
    """A restaurant."""

    all = []

    def __init__(self, name, stars, reviewers):
        self.name = name
        self.star = stars
        self.reviewers = sorted(reviewers)
        Restaurant.all.append(self)

    def similar(self, k, similarity=review_both):
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r))[:k]

    def __repr__(self):
        return "<" + self.name + ">"


import json

reviewers_by_restaurant = {}
for line in open("reviews.json"):
    r = json.loads(line)
    business_id = r["business_id"]
    if business_id not in reviewers_by_restaurant:
        reviewers_by_restaurant[business_id] = []
    reviewers_by_restaurant[business_id].append(r["user_id"])


for line in open("restaurants.json"):
    b = json.loads(line)
    reviewers = reviewers_by_restaurant.get(b["business_id"], [])
    Restaurant(b["name"], b["stars"], reviewers)

"""
Restaurant("Thai Ha", 5)
Restaurant("Thai Ha", 5)
Restaurant("Thai Ha", 5)
"""

results = search("Thai")
for r in results:
    print(r.name, "is similar to", r.similar(3))
