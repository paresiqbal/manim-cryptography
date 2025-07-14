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

        # Step 5: Move both to final vertical positions
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
            FadeOut(result_lines),
            FadeOut(letters)
        )
        self.wait(1)

                # Step 8: Display encrypted ASCII numbers at center
        ascii_result = [str(num) for num in encrypted_ascii]
        ascii_texts = VGroup()
        for num in ascii_result:
            ascii_texts.add(Text(num, font_size=36))
        ascii_texts.arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        self.play(Write(ascii_texts))
        self.wait(2)

        # Step 9: Display encrypted characters above ASCII numbers (parallel)
        encrypted_chars = [chr(num) for num in encrypted_ascii]
        encrypted_texts = VGroup()
        for i, char in enumerate(encrypted_chars):
            t = Text(char, font_size=36)
            t.next_to(ascii_texts[i], UP, buff=0.3)
            encrypted_texts.add(t)

        self.play(Write(encrypted_texts))
        self.wait(2)

         # Step 10: Move encrypted group to the left (X = -4)
        encrypted_group = VGroup(encrypted_texts, ascii_texts).arrange(DOWN, buff=0.3)
        self.play(encrypted_group.animate.move_to(LEFT * 4))
        self.wait(1)

        # Step 11: Decrypt on the right side
        decrypt_lines = VGroup()
        decrypted_ascii = []
        for i in range(len(encrypted_ascii)):
            enc = encrypted_ascii[i]
            key_val = key_ascii_vals[i]
            # Reverse OTP encryption
            raw_val = (enc - key_val - 33) % 94
            orig_ascii = raw_val
            decrypted_ascii.append(orig_ascii)
            line = Text(
                f"{enc} - {key_val} - 33 mod 94 = {orig_ascii}",
                font_size=24
            )
            decrypt_lines.add(line)

        decrypt_lines.arrange(DOWN, buff=0.3)
        decrypt_lines.move_to(RIGHT * 4)

        self.play(Write(decrypt_lines))
        self.wait(2)
