print("Welcome to Quiz Game!")

playing = input("Do you interest to play? ")

# lower() = converts into lowercase letters
# upper() = converts into uppercase letters

if playing.lower() != "y":
    quit()

print ("Okay! Let's play :)")

score = 0
answer = input("What does AZ stand for? ")
if answer.lower() == "availability zone":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the command to check running docker containers? ")
if answer.lower() == "docker ps":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is storage mechanism using by kubernetes volume? ")
if answer.lower() == "pv":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is purpose of EFS ? ")
if answer.lower() == "file share":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Total score of this quiz is: " + str(score))
print("You got " + str((score/4) * 100) + "%.")