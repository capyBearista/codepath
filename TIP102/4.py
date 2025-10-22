"""
Problem 3: Identify Popular Creators

You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.

Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def identify_popular_creators(nft_collection):
    popular_creators = set()
    seen_creators = set()

    for nft in nft_collection:
        creator = nft["creator"]

        if creator in seen_creators:
            popular_creators.add(creator)
        else:
            seen_creators.add(creator)

    return list(popular_creators)

# Time complexity
# O(n)

# Space complexity
# O(n)

# Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))

# Example Output:

# ['ArtByAlex']
# ['SpaceArt']
# []

print()

"""
Problem 6: NFT Queue Processing

NFTs are processed in a queue that follows First-In, First-Out (FIFO). Given a list of NFT names in their initial queue order, return the order in which they are processed.

Write the process_nft_queue() function, which takes a list of NFTs. The function should return a list of NFT names in the order they were processed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

# returns NFTs from FIFO queue (in order)
# nft_queue, already in order, no need to sort

def process_nft_queue(nft_queue):
    list_names = []

    for nft in nft_queue:
        list_names.append(nft["name"])
    
    return list_names

# time complexity
# O(n)

# space complexity
# O(n)

# Example Usage:

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))

# Example Output:

# ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
# ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
# ['Crypto Kitty', 'Galactic Voyage']
