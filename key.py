from manim import *

class OTP(Scene):
    def construct(self):
        word = "HALLO"
        key = "M9z$H"
        custom_font = "KH Interference Trial"  # 👈 Custom font name

        # Create letter-by-letter Text objects
        top_letters = VGroup(*[Text(c, font_size=48, font=custom_font) for c in word])
        bottom_letters = VGroup(*[Text(c, font_size=48, font=custom_font) for c in key])

        # Arrange them horizontally
        top_letters.arrange(RIGHT, buff=0.5)
        bottom_letters.arrange(RIGHT, buff=0.5)

        # Move bottom letters below corresponding top letters
        for top, bottom in zip(top_letters, bottom_letters):
            bottom.move_to(top).shift(DOWN * 1.0)

        # Group all letters together and scale down
        all_letters = VGroup(top_letters, bottom_letters).scale(0.6)

        # Move to the left (x = -4)
        all_letters.move_to(LEFT * 4)

        # Create a circle around the word and key
        left_circle = Circle(
            radius=all_letters.width / 2 + 0.5,
            color=YELLOW
        )
        left_circle.move_to(all_letters.get_center())

        # Display the word + key with the circle
        self.play(Write(top_letters), Write(bottom_letters))
        self.wait()
        self.play(Create(left_circle))
        self.wait()

        # Create cipher names on the right in pink using the custom font
        caesar = Text("Caesar", font_size=48, color=PINK, font=custom_font)
        vigenere = Text("Vigenère", font_size=48, color=PINK, font=custom_font)
        aes = Text("AES", font_size=48, color=PINK, font=custom_font)

        # Arrange vertically
        right_group = VGroup(caesar, vigenere, aes).arrange(DOWN, buff=0.5)

        # Move to the right (x = 4)
        right_group.move_to(RIGHT * 4)

        # Create a circle around the cipher names
        right_circle = Circle(
            radius=right_group.width / 2 + 0.7,
            color=YELLOW
        )
        right_circle.move_to(right_group.get_center())

        # Display the cipher names and circle
        self.play(Write(right_group))
        self.wait()
        self.play(Create(right_circle))
        self.wait()
