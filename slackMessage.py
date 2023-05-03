import pygame
import slack
import time

client = slack.WebClient(token="xoxb-5185067800342-5204317570273-a77DalTBoNQtdP6fDq4YBQlV")

conversation_id = "C055F1ZQ71C"

def queryMessages():
    result = client.conversations_history(
        channel=conversation_id,
        inclusive=True,
        limit=1
    )
    return result

def PlayMatchFoundSound():
    pygame.mixer.init()
    pygame.mixer.music.load("MatchSound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

result = queryMessages()
lastMessageTime = result["messages"][0]["ts"]

while True:
    time.sleep(2)
    result = queryMessages()
    currentMessageTime = result["messages"][0]["ts"]
    if lastMessageTime != currentMessageTime:
        PlayMatchFoundSound()
        lastMessageTime = currentMessageTime

