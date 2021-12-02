class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def win_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            score = self.scores_equal()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.score_4_or_more()
        else:
            score = self.score_other()
        return score

    def scores_equal(self):
        score_strings = ["Love-All", "Fifteen-All", "Thirty-All", "Forty-All", "Deuce"]
        return score_strings[self.player1_score]

    def score_4_or_more(self):
        point_difference = self.player1_score - self.player2_score

        if point_difference == 1:
            return "Advantage player1"
        if point_difference == -1:
            return "Advantage player2"
        if point_difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def score_other(self):
        score_strings = ["Love", "Fifteen", "Thirty", "Forty"]
        return (
            f"{score_strings[self.player1_score]}-{score_strings[self.player2_score]}"
        )
