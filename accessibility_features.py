# accessibility_features.py

class AccessibilityFeatures:
    def __init__(self):
        self.difficulty_levels = ['Easy', 'Medium', 'Hard']
        self.current_difficulty = 'Medium'
        self.controls = {
            'move_left': 'left_arrow',
            'move_right': 'right_arrow',
            'fire': 'spacebar'
        }

    def set_difficulty(self, level):
        if level in self.difficulty_levels:
            self.current_difficulty = level
            print(f"Difficulty level set to {self.current_difficulty}")
        else:
            print("Invalid difficulty level")

    def get_difficulty_options(self):
        return self.difficulty_levels

    def set_controls(self, move_left, move_right, fire):
        self.controls['move_left'] = move_left
        self.controls['move_right'] = move_right
        self.controls['fire'] = fire
        print("Controls updated:", self.controls)

    def get_controls(self):
        return self.controls

    def set_novice_options(self):
        self.set_difficulty('Easy')
        self.set_controls('a', 'd', 'w')
        print("Novice options set")

if __name__ == "__main__":
    accessibility = AccessibilityFeatures()

    # Set and display difficulty levels
    print("Available difficulty levels:", accessibility.get_difficulty_options())
    accessibility.set_difficulty('Easy')
    accessibility.set_difficulty('Medium')

    # Set and display custom controls
    print("Current controls:", accessibility.get_controls())
    accessibility.set_controls('a', 'd', 'w')
    print("Updated controls:", accessibility.get_controls())

    # Set novice options
    accessibility.set_novice_options()
    print("Current difficulty:", accessibility.current_difficulty)
    print("Current controls:", accessibility.get_controls())
