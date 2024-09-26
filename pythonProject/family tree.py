class Person:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def gender(self):
        x = self.coordinates[0]
        return "Male" if x >= 0 else "Female"

    def relationship(self, other, description_type):
        x1, y1 = self.coordinates
        x2, y2 = other.coordinates

        # Calculate the differences
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)

        relation_parts = []

        # Determine if the other is a descendant or ancestor
        if y1 < y2:  # other is a descendant
            if x1 == x2:
                relation_parts.append("Child" if y_diff == 1 else f"{y_diff}th Grandchild")
            else:
                if description_type == "cousin":
                    relation_parts.append(f"{x_diff}th Cousin")
                else:
                    relation_parts.append(f"{y_diff}th Great-Grandchild")
                    relation_parts.append("Uncle" if x1 > x2 else "Aunt")

        elif y1 > y2:  # other is an ancestor
            if x1 == x2:
                relation_parts.append("Parent" if y_diff == 1 else f"{y_diff}th Grandparent")
            else:
                relation_parts.append(f"{y_diff}th Great-Grandparent")
                relation_parts.append("Niece" if x1 > x2 else "Nephew")

        else:  # Same generation
            if x1 == x2:
                relation_parts.append("Sibling")
            elif x1 == 0:
                relation_parts.append("Brother")
            elif x1 < 0:
                relation_parts.append("Sister")
            elif abs(x1 - x2) == 1:
                relation_parts.append("Cousin")
            else:
                relation_parts.append(f"{x_diff}th Distant Cousin")

        # Customize description based on user input
        if description_type == "aunt/uncle":
            return f"{self.name} is an {relation_parts[-1]}."
        elif description_type == "parent":
            return f"{self.name} is a {relation_parts[-1]}."
        elif description_type == "great":
            return f"{self.name} is a {relation_parts[-2]}."
        else:  # Default to cousin
            return f"{self.name} is {', '.join(relation_parts)}."


# Example usage
def main():
    person1 = Person("Alice", (0, 0))
    person2 = Person("Bob", (100, 0))
    person3 = Person("Charlie", (0, 100))
    person4 = Person("Diana", (-100, 0))
    person5 = Person("Eve", (57, 42))
    person6 = Person("Frank", (36, 54))

    description_type = input(
        "Enter how to describe the relationship (cousin, aunt/uncle, parent, great): ").strip().lower()

    print(person1.relationship(person2, description_type))  # For example, Alice and Bob
    print(person1.relationship(person3, description_type))  # Alice and Charlie
    print(person1.relationship(person4, description_type))  # Alice and Diana
    print(person5.relationship(person6, description_type))  # Eve and Frank


if __name__ == "__main__":
    main()
