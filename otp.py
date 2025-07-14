from manim import *

class OTP(Scene):
    def construct(self):
        # Step 1: Message
        word = "HALLO"
        word_ascii = [ord(c) for c in word]

        # Step 2: Safe printable key
        key = "M9z$H"
        key_ascii_vals = [ord(c) for c in key]

        # Step 3: Show message letters
        text = Text(word, font_size=36)
        letters = VGroup(*text)
        letters.arrange(RIGHT, buff=0.5)

        # ASCII below message
        ascii_numbers = VGroup()
        for i, val in enumerate(word_ascii):
            ascii_text = Text(str(val), font_size=24)
            ascii_text.next_to(letters[i], DOWN, buff=0.2)
            ascii_numbers.add(ascii_text)

        all_objects = VGroup(letters, ascii_numbers).arrange(DOWN, buff=0.3)
        all_objects.move_to(LEFT * 4)

        self.play(Write(letters))
        self.wait(1)
        self.play(Write(ascii_numbers))
        self.wait(1)

        # Step 4: Show key
        key_text = Text(key, font_size=36)
        key_letters = VGroup(*key_text)
        key_letters.arrange(RIGHT, buff=0.5)

        key_ascii = VGroup()
        for i, val in enumerate(key_ascii_vals):
            ascii_text = Text(str(val), font_size=24)
            ascii_text.next_to(key_letters[i], DOWN, buff=0.2)
            key_ascii.add(ascii_text)

        key_group = VGroup(key_letters, key_ascii).arrange(DOWN, buff=0.3)
        key_group.align_to(all_objects, UP)
        key_group.move_to(RIGHT * 4)

        self.play(Write(key_letters))
        self.wait(1)
        self.play(Write(key_ascii))
        self.wait(1)

        # Step 5: Move to final position
        self.play(
            all_objects.animate.move_to([-4, 1, 0]),
            key_group.animate.move_to([-4, -1, 0]),
        )
        self.wait(1)

        # Step 6: Show ASCII addition
        result_lines = VGroup()
        encrypted_ascii = []
        for i in range(len(word)):
            a = word_ascii[i]
            b = key_ascii_vals[i]
            mod_result = ((a + b) % 94) + 33
            encrypted_ascii.append(mod_result)
            line = Text(f"{a} + {b} mod 94 + 33 = {mod_result}", font_size=24)
            result_lines.add(line)

        result_lines.arrange(DOWN, buff=0.3)
        result_lines.move_to([4.5, 0, 0])

        self.play(Write(result_lines))
        self.wait(2)

        # Step 7: Fade out everything except message letters
        self.play(
            FadeOut(ascii_numbers),
            FadeOut(key_group),
            FadeOut(result_lines)
        )
        self.wait(1)

        # Step 8: Fade out original message letters
        self.play(FadeOut(letters))
        self.wait(0.5)

        # Step 9: Show encrypted result at center
        ascii_result = [str(num) for num in encrypted_ascii]
        spaced_ascii = " ".join(ascii_result)
        result_text = Text(spaced_ascii, font_size=36).move_to(ORIGIN)

        encrypted_chars = [chr(num) for num in encrypted_ascii]
        spaced_chars = " ".join(encrypted_chars)
        encrypted_text = Text(spaced_chars, font_size=36)
        encrypted_text.next_to(result_text, UP, buff=0.4)

        self.play(Write(result_text))
        self.wait(1)
        self.play(Write(encrypted_text))
        self.wait(3)

        # Step 9: Show encrypted result at center
        ascii_result = [str(num) for num in encrypted_ascii]
        spaced_ascii = " ".join(ascii_result)
        result_text = Text(spaced_ascii, font_size=36).move_to(ORIGIN)

        encrypted_chars = [chr(num) for num in encrypted_ascii]
        spaced_chars = " ".join(encrypted_chars)
        encrypted_text = Text(spaced_chars, font_size=36)
        encrypted_text.next_to(result_text, UP, buff=0.4)

        self.play(Write(result_text))
        self.wait(1)
        self.play(Write(encrypted_text))
        self.wait(3)
