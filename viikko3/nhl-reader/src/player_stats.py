from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat: str):
        players = self.reader.get_players()
        result = []
        for player in players:
            if player.nationality == nat:
                result.append(player)
        result.sort(key=lambda player: player.goals + player.assists, reverse=True)

        return result
