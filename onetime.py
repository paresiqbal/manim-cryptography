from manim import *

class RepeatingKeyWarning(Scene):
    def construct(self):
        message = "HELLOFROMTHEOTHERSIDE"
        key = "KEY"
        repeated_key = (key * ((len(message) // len(key)) + 1))[:len(message)]

        font = "KH Interference Trial"  # Or your preferred font

        # Create message text
        message_text = VGroup(*[
            Text(c, font_size=40, font=font) for c in message
        ]).arrange(RIGHT, buff=0.2).move_to(UP * 1.5)

        # Create repeated key text
        key_text = VGroup(*[
            Text(c, font_size=40, font=font, color=BLUE) for c in repeated_key
        ]).arrange(RIGHT, buff=0.2)

        # Align key text below message
        for m, k in zip(message_text, key_text):
            k.move_to(m).shift(DOWN * 1.0)

        # Group both lines
        both_lines = VGroup(message_text, key_text).move_to(ORIGIN)

        self.play(Write(message_text), Write(key_text))
        self.wait()

        # Highlight the repeated pattern (every full 'KEY')
        pattern_groups = []
        for i in range(0, len(message) - 2, 3):
            pattern = VGroup(key_text[i], key_text[i+1], key_text[i+2])
            pattern_groups.append(pattern)

        for group in pattern_groups:
            rect = SurroundingRectangle(group, color=RED, buff=0.1)
            self.play(Create(rect), run_time=0.3)
            self.wait(0.1)

        # Warning message
        warning = Text(
            "Mengulang tombol akan menciptakan sebuah pola!",
            font_size=23,
            color=YELLOW,
            font=font
        ).next_to(key_text, DOWN, buff=1)

        self.play(Write(warning))
        self.wait()
