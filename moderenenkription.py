from manim import *

class SecurityTerms(Scene):
    def construct(self):
        # 1. Write "HTTPS" in big letters
        https = Text("HTTPS", font_size=72, font="KH Interference Trial")
        https.move_to(UP * 2)
        self.play(Write(https))
        self.wait(2)

        # 2. Write "END TO END ENCRYPTION" under it
        encryption = Text("END TO END ENCRYPTION", font_size=72, font="KH Interference Trial")
        encryption.next_to(https, DOWN, buff=0.5)
        self.play(Write(encryption))
        self.wait(1)

        # 3. Write "VPN"
        vpn = Text("VPN", font_size=72, font="KH Interference Trial")
        vpn.next_to(encryption, DOWN, buff=1.2)
        self.play(Write(vpn))

        # 4. Write "SSH"
        ssh = Text("SSH", font_size=72, font="KH Interference Trial")
        ssh.next_to(vpn, DOWN, buff=0.7)
        self.play(Write(ssh))

        self.wait(1)
