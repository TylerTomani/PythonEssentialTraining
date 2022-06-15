secret = "dee"
pw = ""
auth = False
count = 0
max_attempts = 3

while pw != secret:
    count += 1
    pw = input(f"{4 - count} trys left. Enter Password ")
    if count == max_attempts:
        break
else:
    auth = True
print("Authorized" if auth else "Authorized failed")
