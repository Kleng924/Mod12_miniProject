from flask import Flask, request, jsonify
from playlist import songs, playlists, generate_song_id, generate_playlist_id, merge_sort_songs

app = Flask(__name__)

@app.route("/song", methods=["POST"])
def create_song():
    """Creates a new song."""
    data = request.json
    song_id = generate_song_id()
    songs[song_id] = {
        "name": data["name"],
        "artist": data["artist"],
        "genre": data["genre"],
    }
    return jsonify({"message": "Song added", "song_id": song_id}), 201

@app.route("/song/<song_id>", methods=["GET"])
def get_song(song_id):
    """Fetches a song by ID."""
    return jsonify(songs.get(song_id, {"error": "Song not found"}))

@app.route("/song/<song_id>", methods=["PUT"])
def update_song(song_id):
    """Updates an existing song."""
    if song_id not in songs:
        return jsonify({"error": "Song not found"}), 404
    data = request.json
    songs[song_id].update(data)
    return jsonify({"message": "Song updated", "song": songs[song_id]})

@app.route("/song/<song_id>", methods=["DELETE"])
def delete_song(song_id):
    """Deletes a song."""
    if song_id in songs:
        del songs[song_id]
        return jsonify({"message": "Song deleted"})
    return jsonify({"error": "Song not found"}), 404

@app.route("/playlist", methods=["POST"])
def create_playlist():
    """Creates a new playlist."""
    data = request.json
    playlist_id = generate_playlist_id()
    playlists[playlist_id] = {"name": data["name"], "songs": []}
    return jsonify({"message": "Playlist created", "playlist_id": playlist_id}), 201

@app.route("/playlist/<playlist_id>", methods=["GET"])
def get_playlist(playlist_id):
    """Fetches a playlist by ID."""
    return jsonify(playlists.get(playlist_id, {"error": "Playlist not found"}))

@app.route("/playlist/<playlist_id>", methods=["PUT"])
def update_playlist(playlist_id):
    """Updates a playlist's name."""
    if playlist_id not in playlists:
        return jsonify({"error": "Playlist not found"}), 404
    data = request.json
    playlists[playlist_id]["name"] = data["name"]
    return jsonify({"message": "Playlist updated"})

@app.route("/playlist/<playlist_id>", methods=["DELETE"])
def delete_playlist(playlist_id):
    """Deletes a playlist."""
    if playlist_id in playlists:
        del playlists[playlist_id]
        return jsonify({"message": "Playlist deleted"})
    return jsonify({"error": "Playlist not found"}), 404

@app.route("/playlist/<playlist_id>/add_song", methods=["POST"])
def add_song_to_playlist(playlist_id):
    """Adds a song to a playlist."""
    data = request.json
    song_id = data["song_id"]
    if playlist_id in playlists and song_id in songs:
        playlists[playlist_id]["songs"].append(song_id)
        return jsonify({"message": "Song added to playlist"})
    return jsonify({"error": "Playlist or Song not found"}), 404

@app.route("/playlist/<playlist_id>/remove_song", methods=["POST"])
def remove_song_from_playlist(playlist_id):
    """Removes a song from a playlist."""
    data = request.json
    song_id = data["song_id"]
    if playlist_id in playlists and song_id in playlists[playlist_id]["songs"]:
        playlists[playlist_id]["songs"].remove(song_id)
        return jsonify({"message": "Song removed from playlist"})
    return jsonify({"error": "Playlist or Song not found"}), 404

