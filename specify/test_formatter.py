import arrow

class TestFormatter:

    def __init__(self, j_resp):

        self.query_time = self.get_query_time(j_resp)
        self.song_title = j_resp["name"]
        self.artists    = self.get_artists(j_resp)
        self.duration   = self.get_duration(j_resp)

    def get_query_time(self, j):
        return arrow.get(j["timestamp"])

    def get_artists(self, j):

        artist_list = j["item"]["artists"]

        artists = [a["external_urls"]["name"] for a in artist_list]

        return ", ".join(artists)

    def get_duration(self, j):

        ms = j["item"]["duration_ms"]

        return arrow.get(ms).format('mm:ss')

    def build_data(self):

        data: Dict[str, str] =  {
            "Query Time": self.query_time,
            "Song":       self.song_title,
            "Artist":     self.artists,
            "Duration":   self.duration
        }

        return data