class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
        print(f"Fun fact about me: {self.fun_fact}")

    def show_stack(self):
        print("My Tech Stack includes:")
        for tool in self.tech_stack:
            print(f"- {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


if __name__ == "__main__":
    my_profile = Profile(
        name="Joan Kyokusiima",
        favorite_language="Python",
        hobby="Reading novels",
        tech_stack=["Python", "Django", "Git", "MySQL"],
        github_username="JoanKyokusiima",
        fun_fact="I’m the quiet observer in the room,so yes, I probably noticed your new things before you mentioned them.!"
    )

    my_profile.introduce()
    my_profile.show_stack()
    print("My GitHub Profile:", my_profile.github_link("https://github.com/JoanJojoJojo/oop-lab1"))