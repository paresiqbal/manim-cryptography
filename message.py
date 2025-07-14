from manim import *

class Message(Scene):
    def construct(self):
        # Step 1: Display "Informasi" in center
        informasi = Text("Informasi")
        self.play(Write(informasi))
        self.wait(1)

        # Step 2: Move "Informasi" to the left
        self.play(informasi.animate.move_to(LEFT * 4))
        self.wait(0.5)

        # Step 3: Display "=" in center
        equal = Text("=")
        self.play(Write(equal))
        self.wait(0.5)

        # Step 4: Display "Senjata" on the right
        senjata = Text("Senjata").move_to(RIGHT * 4)
        self.play(Write(senjata))
        self.wait(1)

        # Step 5: Create a smaller pink square with "Musuh" inside it
        square = Square(side_length=2).scale(0.8).set_color(PINK)
        musuh_text = Text("Musuh", font_size=24).set_color(PINK)
        group = VGroup(square, musuh_text).move_to(RIGHT * 2 + DOWN * 2)
        self.play(FadeIn(group))
        
        # Step 6: Move square+text toward "Informasi"
        self.play(group.animate.move_to(LEFT * 2 + DOWN * 0.5))
        self.wait(2)

        # Step 7: Change "Senjata" to "Kelemahan"
        kelemahan = Text("Kelemahan").move_to(senjata.get_center())
        self.play(Transform(senjata, kelemahan))
        self.wait(2)
