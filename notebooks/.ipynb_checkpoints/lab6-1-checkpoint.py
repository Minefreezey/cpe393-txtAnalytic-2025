import re

text = ['The match was thrilling, and the team won.', 'The stock market is experiencing a downturn.', 'The player scored an amazing goal.', 'Investors are concerned about rising inflation.', "The coach praised the team's performance.", 'The economic report predicts slower growth.'];

text_split = [t.split(' ') for t in text]

print(text_split)