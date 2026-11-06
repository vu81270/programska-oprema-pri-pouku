from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class KonstrukcijaTangente(Scene):
    def construct(self):
        konstrukcija = Text(
            "KONSTRUKCIJA",
            font_size=48,
            weight=BOLD,
        ).move_to(UP * 4.1)
        tangente = Text(
            "TANGENTE",
            font_size=54,
            weight=BOLD,
        ).move_to(DOWN * 4.0)

        kroznica = Circle(radius=1.25, color=BLUE_C, stroke_width=6)
        dotik = kroznica.get_top()
        premica = Line(
            dotik + LEFT * 2.1,
            dotik + RIGHT * 2.1,
            color=YELLOW,
            stroke_width=6,
        )
        tocka = Dot(dotik, color=YELLOW, radius=0.09)
        oznaka = Text("T", font_size=38, color=YELLOW).next_to(
            tocka, UR, buff=0.15
        )

        self.play(Write(konstrukcija), run_time=1.5)
        self.play(Create(kroznica), run_time=1.5)
        self.play(Create(premica), FadeIn(tocka), run_time=1)
        self.play(Write(oznaka), run_time=0.5)
        self.play(Write(tangente), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(
                konstrukcija,
                kroznica,
                premica,
                tocka,
                oznaka,
                tangente,
            ),
            run_time=0.5,
        )
        self.prvi_del()
        self.play(*[FadeOut(mobject) for mobject in self.mobjects], run_time=0.5)
        self.drugi_del()
        self.play(*[FadeOut(mobject) for mobject in self.mobjects], run_time=0.5)
        self.tretji_del()
        self.play(*[FadeOut(mobject) for mobject in self.mobjects], run_time=0.5)
        self.wait(0.5)
        self.povzetek()

    def prvi_del(self):
        stevilka = VGroup(
            Circle(radius=0.38, color=BLUE_C, stroke_width=5),
            Text("1", font_size=34, color=BLUE_C, weight=BOLD),
        ).move_to(UP * 6.25)
        naslov = Text(
            "Točka T leži v\nkrožnici K",
            font_size=42,
            line_spacing=0.9,
        ).move_to(UP * 4.8)

        kroznica = Circle(radius=2.1, color=BLUE_C, stroke_width=6)
        sredisce = Dot(ORIGIN, color=WHITE, radius=0.08)
        oznaka_k = Text("K", font_size=36).next_to(sredisce, DL, buff=0.12)
        tocka_t = Dot(RIGHT * 0.55 + UP * 0.45, color=YELLOW, radius=0.1)
        oznaka_t = Text("T", font_size=36, color=YELLOW).next_to(
            tocka_t, UR, buff=0.12
        )

        sklep = VGroup(
            Text("Tangente", font_size=36),
            Text("NI", font_size=36, color=RED, weight=BOLD),
            Text("mogoče narisati.", font_size=36),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 4.6)

        self.play(FadeIn(stevilka), Write(naslov), run_time=1.5)
        self.play(Create(kroznica), FadeIn(sredisce, oznaka_k), run_time=1.5)
        self.play(FadeIn(tocka_t, oznaka_t), run_time=0.8)
        self.play(Write(sklep), run_time=1.5)
        self.wait(2)

    def drugi_del(self):
        stevilka = VGroup(
            Circle(radius=0.38, color=BLUE_C, stroke_width=5),
            Text("2", font_size=34, color=BLUE_C, weight=BOLD),
        ).move_to(UP * 6.25)
        naslov = Text(
            "Točka T leži na\nkrožnici K",
            font_size=42,
            line_spacing=0.9,
        ).move_to(UP * 4.8)

        sredisce = UP * 0.65
        kroznica = Circle(
            radius=1.65,
            color=BLUE_C,
            stroke_width=6,
        ).move_to(sredisce)
        koordinata_t = kroznica.get_top()
        srediscna_tocka = Dot(sredisce, color=WHITE, radius=0.08)
        oznaka_k = Text("K", font_size=34).next_to(
            srediscna_tocka, DL, buff=0.12
        )
        tocka_t = Dot(koordinata_t, color=YELLOW, radius=0.1)
        oznaka_t = Text("T", font_size=34, color=YELLOW).next_to(
            tocka_t, UR, buff=0.12
        )
        polmer = Line(sredisce, koordinata_t, color=GREEN_C, stroke_width=7)
        tangenta = Line(
            koordinata_t + LEFT * 2.0,
            koordinata_t + RIGHT * 2.0,
            color=YELLOW,
            stroke_width=7,
        )
        kotnik = VGroup(
            Line(
                koordinata_t + LEFT * 0.28,
                koordinata_t + LEFT * 0.28 + DOWN * 0.28,
                color=WHITE,
                stroke_width=4,
            ),
            Line(
                koordinata_t + LEFT * 0.28 + DOWN * 0.28,
                koordinata_t + DOWN * 0.28,
                color=WHITE,
                stroke_width=4,
            ),
        )

        pravilo_polmer = Text(
            "Narišemo polmer do točke T.",
            font_size=31,
            color=GREEN_C,
        ).move_to(DOWN * 2.25)
        pravilo_tangenta = Text(
            "Skozi T narišemo\npravokotnico na polmer.",
            font_size=29,
            color=YELLOW,
            line_spacing=0.9,
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(stevilka), Write(naslov), run_time=1.5)
        self.play(
            Create(kroznica),
            FadeIn(srediscna_tocka, oznaka_k, tocka_t, oznaka_t),
            run_time=1.5,
        )
        self.play(Write(pravilo_polmer), Create(polmer), run_time=1.5)
        self.play(
            Write(pravilo_tangenta),
            Create(tangenta),
            Create(kotnik),
            run_time=2,
        )
        self.wait(2)

    def tretji_del(self):
        stevilka = VGroup(
            Circle(radius=0.38, color=BLUE_C, stroke_width=5),
            Text("3", font_size=34, color=BLUE_C, weight=BOLD),
        ).move_to(UP * 6.25)
        naslov = Text(
            "Točka T leži izven\nkrožnice K",
            font_size=42,
            line_spacing=0.9,
        ).move_to(UP * 4.8)

        s = LEFT * 1.35 + UP * 0.8
        t = RIGHT * 2.35 + UP * 0.8
        polmer = 1.25
        razdalja_st = np.linalg.norm(t - s)
        sredina_st = (s + t) / 2
        radij_pomozne = razdalja_st / 2
        odmik_presecisca = polmer**2 / razdalja_st
        visina_presecisca = np.sqrt(polmer**2 - odmik_presecisca**2)
        presecisce_a = s + RIGHT * odmik_presecisca + UP * visina_presecisca
        presecisce_b = s + RIGHT * odmik_presecisca + DOWN * visina_presecisca

        kroznica_k = Circle(
            radius=polmer,
            color=BLUE_C,
            stroke_width=6,
        ).move_to(s)
        tocka_s = Dot(s, color=WHITE, radius=0.08)
        oznaka_s = Text("S", font_size=32).next_to(tocka_s, DL, buff=0.1)
        tocka_t = Dot(t, color=YELLOW, radius=0.1)
        oznaka_t = Text("T", font_size=32, color=YELLOW).next_to(
            tocka_t, UR, buff=0.1
        )
        daljica_st = Line(s, t, color=GREEN_C, stroke_width=6)
        tocka_m = Dot(sredina_st, color=WHITE, radius=0.08)
        oznaka_m = Text("M", font_size=30).next_to(tocka_m, DOWN, buff=0.1)
        pomocna_kroznica = Circle(
            radius=radij_pomozne,
            color=PURPLE_B,
            stroke_width=5,
        ).move_to(sredina_st)

        dotik_a = Dot(presecisce_a, color=YELLOW, radius=0.09)
        dotik_b = Dot(presecisce_b, color=YELLOW, radius=0.09)
        oznaka_a = Text("A", font_size=28, color=YELLOW).next_to(
            dotik_a, LEFT, buff=0.12
        )
        oznaka_b = Text("B", font_size=28, color=YELLOW).next_to(
            dotik_b, LEFT, buff=0.12
        )
        podaljsek_tangent = 0.8
        konec_tangente_a = presecisce_a + (
            (presecisce_a - t) / np.linalg.norm(presecisce_a - t)
        ) * podaljsek_tangent
        konec_tangente_b = presecisce_b + (
            (presecisce_b - t) / np.linalg.norm(presecisce_b - t)
        ) * podaljsek_tangent
        tangenta_a = Line(t, konec_tangente_a, color=YELLOW, stroke_width=6)
        tangenta_b = Line(t, konec_tangente_b, color=YELLOW, stroke_width=6)

        pravilo_tales = Text(
            "Pomagamo si s Talesovim izrekom v polkrogu.",
            font_size=26,
            line_spacing=0.9,
        ).move_to(DOWN * 3.0)
        pravilo_daljica = Text(
            "Narišemo daljico ST.",
            font_size=30,
            color=GREEN_C,
        ).move_to(DOWN * 3.0)
        pravilo_sredina = Text(
            "Daljico razpolovimo; dobimo središče M.",
            font_size=27,
            color=GREEN_C,
        ).move_to(DOWN * 3.0)
        pravilo_kroznica = Text(
            "Narišemo krožnico s središčem M.",
            font_size=27,
            color=PURPLE_B,
        ).move_to(DOWN * 3.0)
        pravilo_dotik = Text(
            "Presečišči A in B sta dotikališči tangent.",
            font_size=26,
            color=YELLOW,
        ).move_to(DOWN * 3.0)
        pravilo_tangenti = Text(
            "Skozi T in A ter T in B narišemo tangenti.",
            font_size=26,
            color=YELLOW,
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(stevilka), Write(naslov), run_time=1.5)
        self.play(
            Create(kroznica_k),
            FadeIn(tocka_s, oznaka_s, tocka_t, oznaka_t),
            Write(pravilo_tales),
            run_time=1.5,
        )
        self.wait(1)
        self.play(
            Transform(pravilo_tales, pravilo_daljica),
            Create(daljica_st),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Transform(pravilo_tales, pravilo_sredina),
            FadeIn(tocka_m, oznaka_m),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Transform(pravilo_tales, pravilo_kroznica),
            Create(pomocna_kroznica),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Transform(pravilo_tales, pravilo_dotik),
            FadeIn(dotik_a, dotik_b, oznaka_a, oznaka_b),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Transform(pravilo_tales, pravilo_tangenti),
            Create(tangenta_a),
            Create(tangenta_b),
            run_time=1.5,
        )
        self.wait(2)

    def povzetek(self):
        radij = 0.78
        sredisce_1 = LEFT * 1.35 + UP * 4.5
        sredisce_2 = LEFT * 1.35
        sredisce_3 = LEFT * 1.35 + DOWN * 4.5

        kroznica_1 = Circle(radius=radij, color=BLUE_C, stroke_width=6)
        kroznica_1.move_to(sredisce_1)
        sredina_1 = Dot(sredisce_1, color=WHITE, radius=0.07)
        t_1 = sredisce_1 + RIGHT * 0.35 + DOWN * 0.05
        tocka_1 = Dot(t_1, color=YELLOW, radius=0.09)
        oznaka_t_1 = Text("T", font_size=26, color=YELLOW).next_to(
            tocka_1, UR, buff=0.1
        )

        kroznica_2 = Circle(radius=radij, color=BLUE_C, stroke_width=6)
        kroznica_2.move_to(sredisce_2)
        sredina_2 = Dot(sredisce_2, color=WHITE, radius=0.07)
        t_2 = sredisce_2 + UP * radij
        tocka_2 = Dot(t_2, color=YELLOW, radius=0.09)
        oznaka_t_2 = Text("T", font_size=26, color=YELLOW).next_to(
            tocka_2, UR, buff=0.1
        )
        tangenta_2 = Line(
            t_2 + LEFT * 1.25,
            t_2 + RIGHT * 1.25,
            color=YELLOW,
            stroke_width=6,
        )

        kroznica_3 = Circle(radius=radij, color=BLUE_C, stroke_width=6)
        kroznica_3.move_to(sredisce_3)
        sredina_3 = Dot(sredisce_3, color=WHITE, radius=0.07)
        t_3 = RIGHT * 2.15 + DOWN * 4.5
        tocka_3 = Dot(t_3, color=YELLOW, radius=0.09)
        oznaka_t_3 = Text("T", font_size=26, color=YELLOW).next_to(
            tocka_3, UR, buff=0.1
        )

        vektor = t_3 - sredisce_3
        razdalja = np.linalg.norm(vektor)
        pravokotnik = np.array([-vektor[1], vektor[0], 0])
        nozisce = sredisce_3 + (radij**2 / razdalja**2) * vektor
        odmik = (
            radij
            * np.sqrt(razdalja**2 - radij**2)
            / razdalja**2
            * pravokotnik
        )
        dotik_a = nozisce + odmik
        dotik_b = nozisce - odmik
        tangenti_3 = VGroup()
        for dotik in (dotik_a, dotik_b):
            smer = (dotik - t_3) / np.linalg.norm(dotik - t_3)
            tangenti_3.add(
                Line(
                    t_3,
                    dotik + smer * 0.65,
                    color=YELLOW,
                    stroke_width=6,
                )
            )

        self.play(Create(kroznica_1), run_time=1.2)
        self.play(FadeIn(sredina_1), run_time=0.6)
        self.play(FadeIn(tocka_1, oznaka_t_1), run_time=0.6)
        self.wait(2)

        self.play(Create(kroznica_2), run_time=1.2)
        self.play(FadeIn(sredina_2), run_time=0.6)
        self.play(FadeIn(tocka_2, oznaka_t_2), run_time=0.6)
        self.play(Create(tangenta_2), run_time=1)
        self.wait(2)

        self.play(Create(kroznica_3), run_time=1.2)
        self.play(FadeIn(sredina_3), run_time=0.6)
        self.play(FadeIn(tocka_3, oznaka_t_3), run_time=0.6)
        self.play(Create(tangenti_3), run_time=1.2)
        self.wait(4.8)
