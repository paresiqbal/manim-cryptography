from manim import *

class OTP(Scene):
    def construct(self):
        # First word
        word = "HELLO"
        text = Text(word, font_size=36)
        letters = VGroup(*text)
        letters.arrange(RIGHT, buff=0.5)

        # ASCII below first word
        ascii_numbers = VGroup()
        for i, letter in enumerate(word):
            ascii_code = ord(letter)
            ascii_text = Text(str(ascii_code), font_size=24)
            ascii_text.next_to(letters[i], DOWN, buff=0.2)
            ascii_numbers.add(ascii_text)

        all_objects = VGroup(letters, ascii_numbers).arrange(DOWN, buff=0.3)
        all_objects.move_to(LEFT * 4)

        self.play(Write(letters))
        self.wait(2)
        self.play(Write(ascii_numbers))
        self.wait(2)

        # Second word: "XMCKL"
        key = "XMCKL"
        key_text = Text(key, font_size=36)
        key_letters = VGroup(*key_text)
        key_letters.arrange(RIGHT, buff=0.5)

        # ASCII below second word
        key_ascii = VGroup()
        for i, letter in enumerate(key):
            ascii_code = ord(letter)
            ascii_text = Text(str(ascii_code), font_size=24)
            ascii_text.next_to(key_letters[i], DOWN, buff=0.2)
            key_ascii.add(ascii_text)

        key_group = VGroup(key_letters, key_ascii).arrange(DOWN, buff=0.3)
        key_group.align_to(all_objects, UP)
        key_group.move_to(RIGHT * 4)

        self.play(Write(key_letters))
        self.wait(2)
        self.play(Write(key_ascii))
        self.wait(2)

        # Move both groups to final positions
        self.play(
            all_objects.animate.move_to([-4, 1, 0]),
            key_group.animate.move_to([-4, -1, 0]),
        )
        self.wait(2)

        # ASCII values
        word_ascii = [ord(c) for c in word]
        key_ascii_vals = [ord(c) for c in key]

        # Step-by-step addition results
        result_lines = VGroup()
        for i in range(len(word)):
            a = word_ascii[i]
            b = key_ascii_vals[i]
            mod_result = (a + b) % 256
            line = Text(f"{a} + {b} mod 256 = {mod_result}", font_size=24)
            result_lines.add(line)

        # Arrange vertically and move to the right
        result_lines.arrange(DOWN, buff=0.3)
        result_lines.move_to([4.5, 0, 0])  # right side

        self.play(Write(result_lines))
        self.wait(3)