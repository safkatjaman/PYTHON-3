def win_percentage(wins, looses):
      total_games = wins + looses
      wins_percentage = wins / total_games
      looses_percentage = looses / total_games

      if wins_percentage > looses_percentage:
            return wins_percentage * 100
      else:
            return looses_percentage * 100

print(win_percentage(5, 5))
print(win_percentage(10, 0))

