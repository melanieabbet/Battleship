# class GameSession:

#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2

#     def init_game(self):

#         self.player1.client.send_message(f"Game started! You opponent is {self.player2.name}.")
#         self.player2.client.send_message(f"Game started! You opponent is {self.player1.name}.")

#         print("Game session started!")
#         self.play() 

#     def play(self):
#         while True:
#             # asking for input
#             self.player1.client.send_message("Enter a number:")
#             self.player2.client.send_message("Enter a number:")
#             # wainting for input
#             num1 = self.player1.client.receive_message()
#             num2 = self.player2.client.receive_message()

#             print(f"{self.player1.name} chose: {num1}")  # Debug serveur
#             print(f"{self.player2.name} chose: {num2}")  # Debug serveur

#             #display inputs
#             self.player1.client.send_message(f"Your opponent chose: {num2}")
#             self.player2.client.send_message(f"Your opponent chose: {num1}")

#             #results
#             if num1 == num2:
#                 self.player1.client.send_message("You win! You both chose the same number.")
#                 self.player2.client.send_message("You win! You both chose the same number.")
#                 print("Game Over!")  # Debug serveur
#                 break  # Sortie de la boucle = fin de partie
#             else:
#                 self.player1.client.send_message("You choose different number try again!")
#                 self.player2.client.send_message("You choose different number try again!")