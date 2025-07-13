from manim import *
import random

class Alfabet(Scene):
    def construct(self):
        # === Step 1: Create number-letter pairs ===
        columns = []
        for i in range(26):
            number = Text(str(i + 1), font_size=20)
            if (i + 1) % 2 == 0:
                number.set_color(GREEN)

            letter = Text(chr(65 + i), font_size=20)
            pair = VGroup(number, letter).arrange(DOWN, buff=0.2)
            columns.append(pair)

        # Arrange horizontally
        full_group = VGroup(*columns).arrange(RIGHT, buff=0.3).move_to(ORIGIN)

        # Split into number and letter groups
        number_group = VGroup(*[pair[0] for pair in columns])
        letter_group = VGroup(*[pair[1] for pair in columns])

        # === Step 2: Animate numbers and letters FAST ===
        self.play(Write(number_group), Write(letter_group), run_time=1)
        self.wait(0.5)

        # === Step 3: Create initial arrow pointing to a random number ===
        current_idx = random.randint(0, 25)
        current_number = number_group[current_idx]

        arrow = Arrow(
            start=current_number.get_top() + UP * 0.4,
            end=current_number.get_top(),
            buff=0,
            stroke_width=2,
            color=RED
        )
        self.play(Create(arrow))
        self.wait(0.3)

        # === Step 4: Move the arrow 10 times ===
        for _ in range(10):
            next_idx = random.randint(0, 25)
            while next_idx == current_idx:
                next_idx = random.randint(0, 25)

            current_idx = next_idx
            next_number = number_group[current_idx]

            new_arrow = Arrow(
                start=next_number.get_top() + UP * 0.4,
                end=next_number.get_top(),
                buff=0,
                stroke_width=2,
                color=RED
            )

            self.play(Transform(arrow, new_arrow), run_time=0.5)

        self.wait(2)
