def story_write(phase):
    interrogatives = ("how", "what", "why", "when")
    common = ("hey", "greetings")
    capitalized = phase.capitalize()
    if phase.lower().startswith(interrogatives):
        return "\n{}?".format(capitalized)
    elif phase.lower().startswith(common):
        return "\n{},".format(capitalized)
    else:
        return "\n{}.".format(capitalized)

results = []
while True:
    user_input = input("Story line... ")
    if user_input == "/end":
        break
    else:
        results.append(story_write(user_input))

print(" ".join(results))