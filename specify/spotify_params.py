"""
Transcription of Spotify Recommendation query parameters and their attributes, as found in:
https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/
"""

REC_PARAM_FIELDS = ["name", "type", "descr", "min", "max", "default"]


# a) max_*, min_*, and target_* exist as fields for tuneable attributes e.g. danceability, max_danceability.
# --> low/high caps on sliders, as well as target value?

# b) seed_* (artists, genres, tracks) have a cumulative total of 5
# --> will need at least 1, though... how to find? can you run seedless? random?
REC_PARAMS       = {

                    ("limit",            int, "target size of recommendation list",
                     1, 100, 20),

                    ("seed_artists",     list,  "comma-separated list of IDs for seed artists (max 5 overall)"),
                    ("seed_genres",      list,  "comma-separated list of IDs for seed genres  (max 5 overall)"),
                    ("seed_tracks",      list,  "comma-separated list of IDs for seed tracks  (max 5 overall)"),

                    ("duration_ms",      int,   "duration of result track, in milliseconds",),
                    ("loudness",         float, "average volume of a track in dB"),

                    ("key",              int,   "musical key of track, as per integer pitch class notation",
                     0, 11, None),
                    ("time_signature",   int,   "estimated time signature"), # how is this parametrised?
                                                                             # e.g. 4... go look at Rush or something
                    ("tempo",            float, "estimated tempo of track, in bpm"),
                    ("mode",             int,   "major (1) or minor (0) modality",
                     0, 1, None),

                    ("acousticness",     float, "confidence measure that track result is acoustic",
                     0.0, 1.0, None),
                    ("danceability",     float, "degree measure that track is danceable (beat, tempo, regularity)",
                     0.0, 1.0, None),
                    ("instrumentalness", float, "degree measure of vocal content in track (>0.5 likely instrumental)",
                     0.0, 1.0, None),
                    ("speechiness",      float, "degree measure of spoken word vocals (higher is more speech-like)",
                     0.0, 1.0, None),           # >0.66 spoken word, 0.33-0.66 music+speech, <0.33 music/non-speech
                    ("liveness",         float, "confidence measure that track is live recording",
                     0.0, 1.0, None),

                    ("energy",           float, "degree measure that track has intensity, speed, entropy, and activity",
                     0.0, 1.0, None),
                    ("valence",          float, "degree measure of emotional positivity (higher is cheerier",
                     0.0, 1.0, None),

                    ("popularity",       int,   "least (0) to most (100) popular; recency of track plays matters",
                     0,   100, None)
                   }

"""
EXAMPLE ANALYSIS RESPONSE:
{
  "duration_ms" : 255349,
  "key" : 5,
  "mode" : 0,
  "time_signature" : 4,
  "acousticness" : 0.514,
  "danceability" : 0.735,
  "energy" : 0.578,
  "instrumentalness" : 0.0902,
  "liveness" : 0.159,
  "loudness" : -11.840,
  "speechiness" : 0.0461,
  "valence" : 0.624,
  "tempo" : 98.002,
  "id" : "06AKEBrKUckW0KREUWRnvT",
  "uri" : "spotify:track:06AKEBrKUckW0KREUWRnvT",
  "track_href" : "https://api.spotify.com/v1/tracks/06AKEBrKUckW0KREUWRnvT",
  "analysis_url" : "https://api.spotify.com/v1/audio-analysis/06AKEBrKUckW0KREUWRnvT",
  "type" : "audio_features"
}
"""