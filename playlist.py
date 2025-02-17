songs = {}  
playlists = {}  

def generate_song_id():
    """Generates a unique song ID."""
    return f"song_{len(songs) + 1}"

def generate_playlist_id():
    """Generates a unique playlist ID."""
    return f"playlist_{len(playlists) + 1}"

def binary_search_songs(songs_list, target, key):
    """Performs binary search on a sorted list of songs."""
    left, right = 0, len(songs_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if songs_list[mid][key] == target:
            return songs_list[mid]
        elif songs_list[mid][key] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def merge_sort_songs(songs_list, key):
    """Sorts songs based on a given key (name, artist, genre)."""
    if len(songs_list) <= 1:
        return songs_list

    mid = len(songs_list) // 2
    left = merge_sort_songs(songs_list[:mid], key)
    right = merge_sort_songs(songs_list[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    """Helper function to merge two sorted lists."""
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list