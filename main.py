from manim import *

class Kriptografi(Scene):
    def construct(self):
        # === Step 1: Create 25 vertical number-letter pairs ===
        columns = []
        for i in range(26):
            number = Text(str(i + 1), font_size=20)
            if (i + 1) % 2 == 0:
                number.set_color(GREEN) 

            letter = Text(chr(65 + i), font_size=20)  # A–Y
            pair = VGroup(number, letter).arrange(DOWN, buff=0.2)
            columns.append(pair)

        full_group = VGroup(*columns).arrange(RIGHT, buff=0.3).move_to(ORIGIN)

        letter_group = VGroup(*[pair[1] for pair in columns])
        underline = Line(
            start=letter_group.get_left() + DOWN * 0.2,
            end=letter_group.get_right() + DOWN * 0.2,
            color=YELLOW
        )

        number_group = VGroup(*[pair[0] for pair in columns])
        self.play(Write(number_group), run_time=2)
        self.wait(0.5)
        self.play(Write(letter_group), run_time=2)
        self.wait(0.5)
        self.play(Create(underline), run_time=1)

        self.wait(2)
        self.play(
            FadeOut(full_group),
            FadeOut(underline),
            run_time=1
        )

        # === Number 3 in center and move left ===
        number_3 = Text("3", font_size=140)
        self.play(Write(number_3), run_time=1)
        self.wait(0.5)
        self.play(number_3.animate.move_to(LEFT * 5), run_time=1.5)
        self.wait(1)

        # === Message on right ===
        message = Text("berlayar malam\nminggu ya", font_size=50, line_spacing=0.5)
        message.move_to(RIGHT * 3)
        self.play(Write(message), run_time=2)
        self.wait(2)

        # === A–Z alphabet above (y = 2) ===
        alphabet = []
        for i in range(26):
            letter = Text(chr(65 + i), font_size=26)
            alphabet.append(letter)
        alphabet_group = VGroup(*alphabet).arrange(RIGHT, buff=0.3)
        alphabet_group.move_to([0, 2, 0])

        # === Move down number_3 and message while showing alphabet ===
        self.play(
            number_3.animate.move_to([number_3.get_x(), -2, 0]),
            message.animate.move_to([message.get_x(), -2, 0]),
            Write(alphabet_group),
            run_time=1
        )
        self.wait(2)

        # === Color B in alphabet and message ===
        updated_message = Text(
            "berlayar malam\nminggu ya",
    
            font_size=50,
            line_spacing=0.5,
            t2c={"b": BLUE}
        )
        updated_message.move_to(message.get_center())
        b_letter = alphabet_group[1]  # "B"

        self.play(
            Transform(message, updated_message),
            b_letter.animate.set_color(BLUE),
            run_time=1
        )
        self.wait(0.5)

        # === Change number 3 to pink ===
        self.play(number_3.animate.set_color(PINK), run_time=1)

        # === Arrows and numbered labels (B→E) ===
        arrow_items = VGroup()
        for i in range(1, 4):  # B to E (index 1 to 4)
            start = alphabet_group[i].get_center() + DOWN * 0.4
            end = alphabet_group[i + 1].get_center() + DOWN * 0.4

            arrow = CurvedArrow(
                start, end,
                angle=PI,
                color=ORANGE,
                tip_length=0.2
            )

            label = Text(str(i), font_size=24)
            label.next_to(arrow, DOWN, buff=0.1)

            arrow_items.add(arrow, label)
            self.play(Create(arrow), Write(label), run_time=0.8)

        # === Turn E red ===
        e_letter = alphabet_group[4]
        self.play(e_letter.animate.set_color(RED), run_time=0.5)

        # === After a pause, fade out arrows and change b to e ===
        self.wait(2)
        self.play(FadeOut(arrow_items), run_time=0.8)

        final_message = Text(
            "eerlayar malam\nminggu ya",
    
            font_size=50,
            line_spacing=0.5,
        )
        final_message.move_to(message.get_center())

        self.play(
            Transform(message, final_message),
            b_letter.animate.set_color(WHITE),
            e_letter.animate.set_color(WHITE),
            run_time=1
        )

            # === Wait, then highlight the second 'e' ===
        self.wait(1)

        # New updated message where second 'e' is also blue
        second_e_message = Text(
            "eerlayar malam\nminggu ya",
    
            font_size=50,
            line_spacing=0.5
        )

        second_e_message[1].set_color(GREEN)
        
        second_e_message.move_to(message.get_center())

        # Highlight E in the alphabet (again)
        self.play(
            Transform(message, second_e_message),
            alphabet_group[4].animate.set_color(GREEN),
            run_time=1
        )

        # === Caesar cipher arrows from E → F → G → H (index 4 to 7) ===
        second_arrow_items = VGroup()
        for i in range(4, 7):  # E(4) to H(7)
            start = alphabet_group[i].get_center() + DOWN * 0.4
            end = alphabet_group[i + 1].get_center() + DOWN * 0.4

            arrow = CurvedArrow(
                start, end,
                angle=PI,
                color=ORANGE,
                tip_length=0.2
            )
            label = Text(str(i - 3), font_size=24)
            label.next_to(arrow, DOWN, buff=0.1)

            second_arrow_items.add(arrow, label)
            self.play(Create(arrow), Write(label), run_time=0.8)

        self.wait(2)

        # === Turn H (index 7) to ORANGE ===
        h_letter = alphabet_group[7]
        self.play(h_letter.animate.set_color(ORANGE), run_time=0.5)
        self.wait(1)

        # === Remove arrows before transforming letter ===
        self.play(FadeOut(second_arrow_items), run_time=0.6)

        # === Change second 'e' in message to 'h' and reset colors ===
        final_message_2 = Text(
            "ehrlayar malam\nminggu ya",
    
            font_size=50,
            line_spacing=0.5,
        )
        final_message_2.move_to(message.get_center())

        self.play(
            Transform(message, final_message_2),
            h_letter.animate.set_color(WHITE),
            alphabet_group[4].animate.set_color(WHITE),  # reset 'E'
            run_time=1
        )
        self.wait(2)

        # Source and target texts
        source_text = "ehrlayar malam\nminggu ya"
        target_text = "ehuodbdu pdodp\nplqjjx bd"

        final_encrypted = Text(
            target_text,
            font_size=50,
            line_spacing=0.5
        )
        final_encrypted.move_to(message.get_center())

        self.play(TransformMatchingShapes(message, final_encrypted), run_time=2)
        self.wait(2)

        # === Fade out number 3 and alphabet together ===
        self.play(
            FadeOut(number_3),
            FadeOut(alphabet_group),
            run_time=1
        )

        # === Move final message to center ===
        self.play(final_encrypted.animate.move_to(ORIGIN), run_time=1)  

        # last animation
        self.wait(4)

        # === Move final message to X = -2, while re-showing the alphabet ===
        self.play(
            final_encrypted.animate.move_to(DOWN * 1),
            FadeIn(alphabet_group),
            run_time=1
        )

        self.wait(2)

        # Highlight 'e' in final encrypted message and 'E' in alphabet
        self.play(
            final_encrypted[0].animate.set_color(BLUE),  # 'e' in final message (index 0)
            alphabet_group[4].animate.set_color(BLUE),   # 'E' is index 4 in A–Z
            run_time=1
        )

        self.wait(2)

        backward_arrow_items = VGroup()
        for i in range(4, 1, -1):  # E(4) → D(3) → C(2) → B(1)
            start = alphabet_group[i].get_center() + DOWN * 0.4
            end = alphabet_group[i - 1].get_center() + DOWN * 0.4

            arrow = CurvedArrow(
                start, end,
                angle=-PI,  # negative to reverse curve direction
                color=PURPLE,
                tip_length=0.2
            )

            label = Text(str(4 - i + 1), font_size=24)  # 1, 2, 3
            label.next_to(arrow, DOWN, buff=0.1)

            backward_arrow_items.add(arrow, label)
            self.play(Create(arrow), Write(label), run_time=0.8)

        self.wait(2)

        # === Turn B (index 1) ORANGE ===
        self.play(alphabet_group[1].animate.set_color(ORANGE), run_time=0.5)

        # === Remove arrows ===
        self.play(FadeOut(backward_arrow_items), run_time=0.6)

        # === Transform 'e' in message to 'b' ===
        final_message_decrypted = Text(
            "bhuodbdu pdodp\nplqjjx bd",
            font_size=50,
            line_spacing=0.5,
        )
        final_message_decrypted.move_to(final_encrypted.get_center())

        self.play(
            Transform(final_encrypted, final_message_decrypted),
            alphabet_group[1].animate.set_color(WHITE),     # Reset B
            alphabet_group[4].animate.set_color(WHITE),     # Reset E
            run_time=1
        )

        self.wait(2)

        # === Fully transform final encrypted message back to original ===
        final_decrypted_message = Text(
            "berlayar malam\nminggu ya",
            font_size=50,
            line_spacing=0.5
        )
        final_decrypted_message.move_to(final_encrypted.get_center())

        self.play(
            TransformMatchingShapes(final_encrypted, final_decrypted_message),
            run_time=2
        )

        self.wait(3)
