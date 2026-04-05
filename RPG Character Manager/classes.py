#BH 2nd classes
import random
import matplotlib.pyplot as plt
from faker import Faker
import pandas as pd

class DataVisualization:
    def __init__(self):
        self.attributes = ["Strength", "Dexterity", "Wisdom", "Charisma", "Intelligence", "Constitution"]
    def display_character_stats(self, character):
        levels = [character["strength"], character["dexterity"], character["wisdom"], character["charisma"], character["intelligence"], character["constitution"]]
        
        plt.bar(self.attributes, levels)
        plt.xlabel("Attributes")
        plt.ylabel("Level")
        plt.title(f"{character['name']}'s Stats")
        plt.show()
    def display_character_progression(self, character):
        # months = np.arange(1, 13)
        # sales_data = {
        #     'California': np.random.randint(50, 150, size=12),
        #     'Texas': np.random.randint(40, 130, size=12),
        #     'New York': np.random.randint(30, 120, size=12)
        # }

        # plt.figure(figsize=(10, 6))
        x_values = range(len(character["level_history"]) + 1)
        y_values = character["level_history"] + [character["level"]]
        plt.plot(x_values, y_values, label="Level")
        for attribute in self.attributes:
            y_values = character[f"{attribute.lower()}_history"] + [character[attribute.lower()]]
            plt.plot(x_values, y_values, label=attribute)
        # for attribute in self.attributes:
        

        plt.title("Character Progression")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.show()

class StatisticalAnalyzer:
    # df = pd.DataFrame(characters)
    def calculate_statistics(self, characters):
        df = pd.DataFrame(characters)
        stats = {}
        for attribute in ["strength", "dexterity", "wisdom", "charisma", "intelligence", "constitution"]:
            stats[attribute] = {
                "mean": df[attribute].mean(),
                "median": df[attribute].median(),
                "max": df[attribute].max(),
                "min": df[attribute].min(),
            }
        return stats

class RandomGenerator:
    def __init__(self):
        self.faker = Faker()
    def create_name(self):
        return self.faker.name()
    def create_backstory(self, name):
        trait = self.create_personality_trait()
        gender = random.choice(["male", "female"])
        age = self.faker.random_int(min=15, max=70)
        profession = self.faker.job()
        hobbies = ["cooking", "hiking", "drawing", "writing", "playing music", "coding"]
        hobby = random.choice(hobbies)
        events = [
            "befriending a whale and traveling the seas together",
            "seeing a social media influencer and deciding to become one themselves",
            "becoming a child prodigy in astronomy",
            "accidentally freezing their cat in a science experiment",
            "building a treehouse with their bare hands at the age of four"
        ]
        event = random.choice(events)
        item = self.create_equipment()
        backstory = (
            f"{name} is a {gender}, {age}-year-old {profession} who enjoys {hobby} and is very {trait}. They were known for {event}. They always have a {item} in their room just in case of emergencies."
        )
        return backstory
    def create_side_quest(self):
        side_quests = [
            "Find a lost artifact in the desert.",
            "Become the champion of a library's arm-wrestling tournament.",
            "Rescue a cow from an evil scientist's lab.",
            "Discover an ancient ruin.",
            "Find a cave painting."
        ]
        side_quest = random.choice(side_quests)
        return side_quest
    def create_personality_trait(self):
        traits = [
            "curtious",
            "outgoing",
            "shy",
            "adventurous",
            "witty",
            "curious",
            "beautiful"
        ]
        trait = random.choice(traits)
        return trait
    def create_equipment(self):
        equipment = [
            "regal spear",
            "double-edged sword",
            "light saber",
            "grenade",
            "laser gun",
            "bow and arrow",
        ]
        item = random.choice(equipment)
        return item