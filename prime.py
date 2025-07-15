from manim import *

# Helper to check primes
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class NumbersWithCustomFont(Scene):
    def construct(self):
        # Create Text objects with custom font and color
        numbers = []
        for i in range(1, 51):
            color = PINK if is_prime(i) else WHITE
            text = Text(str(i), font_size=36, color=color, font="KH Interference Trial")
            numbers.append(text)

        # Arrange in 5 rows of 10
        rows = VGroup(
            VGroup(*numbers[0:10]).arrange(RIGHT, buff=0.5),
            VGroup(*numbers[10:20]).arrange(RIGHT, buff=0.5),
            VGroup(*numbers[20:30]).arrange(RIGHT, buff=0.5),
            VGroup(*numbers[30:40]).arrange(RIGHT, buff=0.5),
            VGroup(*numbers[40:50]).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, buff=0.5)

        # Center the group
        rows.move_to(ORIGIN)

        # Animate each number
        for row in rows:
            for number in row:
                self.play(Write(number), run_time=0.2)
